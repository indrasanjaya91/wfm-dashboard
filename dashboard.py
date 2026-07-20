import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import time
import subprocess
import os
import plotly.graph_objects as go
from datetime import datetime, timedelta
import subprocess
import time

# --- PENGATURAN HALAMAN ---
st.set_page_config(page_title="OPERATION DASHBOARD", page_icon="🏢", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS (PREMIUM DARK THEME) ---
st.markdown("""
<style>
    .stApp { background-color: #0b1121; color: #f8fafc; }
    
    /* Top Header Styling */
    .header-container { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 15px; margin-bottom: 20px; }
    .header-left { display: flex; flex-direction: column; }
    .dash-title { font-size: 1.8rem; font-weight: 800; color: #f8fafc; margin: 0; letter-spacing: 1px; text-transform: uppercase; }
    .dash-subtitle { font-size: 0.9rem; color: #94a3b8; margin: 0; }
    .header-right { display: flex; align-items: center; gap: 20px; }
    .update-time { font-size: 0.85rem; color: #94a3b8; text-align: right; line-height: 1.2; }
    .export-btn { background-color: #1e293b; border: 1px solid #334155; padding: 8px 16px; border-radius: 6px; color: white; font-size: 0.9rem; display: flex; align-items: center; gap: 8px; cursor: pointer; }

    /* 5 Grid Cards */
    .grid-5 { display: grid; grid-template-columns: repeat(5, 1fr); gap: 15px; margin-bottom: 20px; }
    .d-card { background-color: #0f172a; border-radius: 10px; padding: 15px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3); border: 1px solid #1e293b; }
    .c-blue { border-top: 4px solid #3b82f6; }
    .c-green { border-top: 4px solid #10b981; }
    .c-purple { border-top: 4px solid #8b5cf6; }
    .c-orange { border-top: 4px solid #f59e0b; }
    .c-teal { border-top: 4px solid #0d9488; }
    
    .dc-header { display: flex; align-items: center; gap: 12px; margin-bottom: 15px; }
    .dc-icon { width: 42px; height: 42px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }
    .ic-blue { background-color: rgba(59,130,246,0.2); color: #3b82f6; }
    .ic-green { background-color: rgba(16,185,129,0.2); color: #10b981; }
    .ic-purple { background-color: rgba(139,92,246,0.2); color: #8b5cf6; }
    .ic-orange { background-color: rgba(245,158,11,0.2); color: #f59e0b; }
    .ic-teal { background-color: rgba(13,148,136,0.2); color: #0d9488; }
    
    .dc-title { font-size: 0.75rem; font-weight: 700; color: #cbd5e1; text-transform: uppercase; margin-bottom: 2px; }
    .dc-value { font-size: 2rem; font-weight: 800; color: white; line-height: 1; }
    
    .dc-breakdown { font-size: 0.75rem; color: #94a3b8; }
    .dc-row { display: flex; justify-content: space-between; margin-bottom: 5px; }
    .dc-row-val { font-weight: bold; color: white; }
    .dc-row-manja { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; text-align: center; margin-bottom: 5px; }
    .dc-row-manja span:first-child { text-align: left; }

    /* Section Titles */
    .section-title-wrap { display: flex; align-items: center; justify-content: space-between; margin-bottom: 15px; border-bottom: 1px solid #1e293b; padding-bottom: 8px; }
    .section-title { font-size: 1rem; font-weight: bold; color: #e2e8f0; text-transform: uppercase; display: flex; align-items: center; gap: 8px; }
    
    /* Table Styling overrides */
    div[data-testid="stDataFrame"] { border: 1px solid #1e293b; border-radius: 8px; overflow: hidden; }
    
    /* Custom Pivot */
    .cp-container { background-color: #0f172a; border-radius: 8px; border: 1px solid #1e293b; padding: 1px; }
    .cp-header { display: grid; grid-template-columns: 2fr 3fr 1fr 1fr 1fr 1fr 1fr; background-color: #0b1121; padding: 12px 15px; font-size: 0.75rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; border-bottom: 1px solid #1e293b; text-align: center; }
    .cp-header div:nth-child(1), .cp-header div:nth-child(2) { text-align: left; }
    .cp-row { border-bottom: 1px solid #1e293b; }
    .cp-row:last-child { border-bottom: none; }
    .cp-summary { display: grid; grid-template-columns: 2fr 3fr 1fr 1fr 1fr 1fr 1fr; padding: 12px 15px; cursor: pointer; text-align: center; align-items: center; font-size: 0.8rem; color: #cbd5e1; }
    .cp-summary:hover { background-color: #1e293b; }
    .cp-summary div:nth-child(1), .cp-summary div:nth-child(2) { text-align: left; }
    .cp-details { background-color: #0b1121; padding: 0; }
    .cp-subrow { display: grid; grid-template-columns: 2fr 3fr 1fr 1fr 1fr 1fr 1fr; padding: 8px 15px; text-align: center; font-size: 0.75rem; color: #94a3b8; border-top: 1px solid #1e293b; align-items: center; }
    .cp-subrow div:nth-child(1) { text-align: left; padding-left: 20px; }
    .cp-subrow div:nth-child(2) { text-align: left; }
    .cp-badge { background-color: #10b981; color: #022c22; padding: 2px 8px; border-radius: 12px; font-weight: 800; font-size: 0.7rem; margin-left: 8px; }
    .cp-arrow { display: inline-block; width: 20px; color: #475569; font-weight: bold; transition: 0.2s; }
    details[open] summary .cp-arrow { transform: rotate(90deg); }
    details summary { list-style: none; }
    details summary::-webkit-details-marker { display: none; }
    .cp-grand { background-color: #172554; display: grid; grid-template-columns: 5fr 1fr 1fr 1fr 1fr 1fr; padding: 12px 15px; text-align: center; font-weight: bold; color: white; font-size: 0.85rem; border-top: 2px solid #3b82f6; }
    .cp-grand div:nth-child(1) { text-align: center; }
    
</style>
""", unsafe_allow_html=True)

# --- PENGATURAN DATA ---
SHEET_ID = "1zA5ucYxE9gOSnKZIhEKQyV2rEdV5je__knsS9neA5iA"
SHEET_NAME = "GABUNGAN"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

@st.cache_data(ttl=60)
def load_data():
    try:
        return pd.read_csv(CSV_URL)
    except Exception as e:
        st.error(f"Gagal mengambil data dari Google Sheet: {e}")
        return pd.DataFrame()

# --- HEADER BERSAMA ---
now_str = datetime.now().strftime("%d %B %Y %H:%M WIB")
st.markdown(f'''
<div class="header-container">
    <div class="header-left">
        <h1 class="dash-title">SERVICE AREA ULIN</h1>
        <p class="dash-subtitle">OPERATION DASHBOARD &ndash; Telkom Akses Provisioning & Monitoring</p>
    </div>
    <div class="header-right">
        <div class="update-time">Update Terakhir<br><span style="color:white;font-weight:bold;">{now_str}</span></div>
        <div class="export-btn">📥 Export ⌄</div>
    </div>
</div>
''', unsafe_allow_html=True)

with st.spinner("Membaca data dari satelit..."):
    df = load_data()

if not df.empty:
    # --- PENCARI KOLOM OTOMATIS ---
    def find_col(possible_names):
        for name in possible_names:
            if name in df.columns: return name
            for col in df.columns:
                if str(col).strip().upper() == name.upper(): return col
        return None

    date_col = find_col(['TANGGAL PS', 'PS', 'Booking Date', 'Date Modified'])
    re_col = find_col(['TANGGAL RE', 'Date Created', 'RE'])
    order_col = find_col(['CECK BY ORDER', 'CEK INDIBIZ', 'PRODUCT TYPE'])
    status_col = find_col(['Status', 'STATUS BIMA', 'STATUS WO'])
    tim_col = find_col(['MORNING TIM', 'TIM MORNING', 'TIM MORNING"2', 'AO'])
    wonum_col = find_col(['NO WONUM', 'WONUM', 'WONUM"2', 'Workorder'])
    ao_col = find_col(['AO', 'NO SC/AO', 'SC Order No/Track ID/CSRM No'])
    morning_status_col = find_col(['MORNING STATUS WO', 'MORNING STATUS', 'STATUS DETAIL'])
    flag_manja_col = find_col(['FLAG MANJA', 'MANJA', 'KATEGORI MANJA'])

    # --- SIDEBAR: KONTROL & NAVIGASI ---
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
    if os.path.exists(logo_path):
        # Tambahkan sedikit CSS untuk memastikan letaknya presisi di tengah dan lebih ke atas
        st.sidebar.markdown("""
        <style>
        [data-testid="stSidebar"] img {
            margin: -40px auto 0 auto;
            display: block;
        }
        </style>
        """, unsafe_allow_html=True)
        st.sidebar.image(logo_path, width=200)
    else:
        st.sidebar.markdown("<h2 style='text-align: center;'>👑<br>SA ULIN</h2>", unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    st.sidebar.header("📅 KONTROL WAKTU")
    
    today_default = datetime.now().date()
    selected_date = st.sidebar.date_input("Pilih Tanggal Pantauan:", today_default)
        
    st.sidebar.markdown("---")
    st.sidebar.header("📂 MENU DASHBOARD")
    menu = st.sidebar.radio("Silakan Pilih Halaman:", [
        "🟢 1. Ringkasan PS & Progres (Startwork)",
        "🔴 2. Pantauan Kendala Harian",
        "📑 3. Master Detail RE (Pesanan Masuk)"
    ])
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Sinkronisasi Data:**")
    
    if "is_admin" not in st.session_state:
        st.session_state.is_admin = False

    is_cloud = os.environ.get("STREAMLIT_CLOUD") == "true"

    if is_cloud:
        st.sidebar.info("☁️ **Mode Cloud Aktif**\n\nUntuk penarikan data (Sync WFM), silakan gunakan **Bot Telegram BIMA** Anda. Data di layar pantau ini akan otomatis terupdate setelah bot selesai.")
    else:
        if not st.session_state.is_admin:
            admin_pin = st.sidebar.text_input("🔑 PIN Admin (Untuk Tarik Data):", type="password")
            if admin_pin == "888888":
                st.session_state.is_admin = True
                st.rerun()
            elif admin_pin != "":
                st.sidebar.error("❌ PIN Salah! Akses View-Only.")
        else:
            st.sidebar.success("✅ Mode Admin Aktif")
            if st.sidebar.button("🚀 Tarik Data WFM Terbaru"):
                with st.spinner("🤖 Robot sedang bekerja... (Tunggu 1-2 menit)"):
                    try:
                        subprocess.run(["python", "main.py", "DASHBOARD"], capture_output=True, text=True, check=True)
                        st.cache_data.clear()
                        st.success("✅ Berhasil menarik data! Halaman akan dimuat ulang...")
                        time.sleep(2)
                        st.rerun()
                    except Exception as e:
                        st.sidebar.error("❌ Robot Gagal menarik data.")
            
            if st.sidebar.button("🔒 Keluar Admin"):
                st.session_state.is_admin = False
                st.rerun()

    # --- PERSIAPAN DATA BERDASARKAN TANGGAL ---
    df['Parsed_Date_PS'] = pd.to_datetime(df[date_col], dayfirst=True, errors='coerce').dt.date if date_col else None
    df['Parsed_Date_RE'] = pd.to_datetime(df[re_col], dayfirst=True, errors='coerce').dt.date if re_col else None
    
    jam_re_col = find_col(['JAM RE MASUK REAL', 'JAM RE MASUK', 'JAM RE'])
    if jam_re_col:
        df['Jam_RE'] = df[jam_re_col].astype(str).str.replace('nan', 'Unknown')
    elif re_col:
        temp_dt = pd.to_datetime(df[re_col], dayfirst=True, errors='coerce')
        df['Jam_RE'] = temp_dt.dt.strftime('%H:%M:%S').fillna('Unknown')
    else:
        df['Jam_RE'] = 'Unknown'
    
    df['Status_Upper'] = df[status_col].astype(str).str.upper().str.strip() if status_col else "UNKNOWN"
    
    info_order_col = find_col(['NO WONUM & AO', 'WONUM & AO'])
    if info_order_col:
        df['INFO ORDER'] = df[info_order_col]
    elif wonum_col and ao_col:
        df['INFO ORDER'] = df[wonum_col].astype(str) + " - " + df[ao_col].astype(str)
    elif wonum_col:
        df['INFO ORDER'] = df[wonum_col]
    else:
        df['INFO ORDER'] = "Unknown WO"

    # --- KATEGORI PRODUK ---
    PROD_COLS = ['AO TSEL', 'PDA TSEL', 'INDIBIZ', 'ISP VULA']
    def get_breakdown(df_subset):
        if not order_col: return {k:0 for k in PROD_COLS}
        counts = df_subset[order_col].astype(str).str.upper().value_counts()
        return {
            'AO TSEL': counts.get('AO TSEL', 0) + counts.get('AO', 0),
            'PDA TSEL': counts.get('PDA TSEL', 0) + counts.get('PDA', 0),
            'INDIBIZ': counts.get('INDIBIZ', 0),
            'ISP VULA': counts.get('ISP VULA', 0) + counts.get('VULA', 0)
        }

    # --- DATA & METRICS ---
    df_re_today = df[(df['Parsed_Date_RE'] == selected_date) & (~df['Status_Upper'].str.contains('COMPLETE', na=False))].copy()
    brk_re = get_breakdown(df_re_today)
    
    df_ps_today = df[(df['Parsed_Date_PS'] == selected_date) & (df['Status_Upper'].str.contains("COMPWORK", na=False))].copy()
    brk_ps = get_breakdown(df_ps_today)
    
    re_hi_ao = brk_re.get('AO TSEL', 0)
    ps_hi_ao = brk_ps.get('AO TSEL', 0)
    ps_re_pct = f"{(ps_hi_ao / re_hi_ao * 100):.2f}%".replace('.', ',') if re_hi_ao > 0 else "0,00%"
    
    potensi_statuses = ['CONTWORK', 'INSTCOMP', 'ACTCOMP', 'VALCOMP', 'VALSTART']
    potensi_df = df[df['Status_Upper'].isin(potensi_statuses)].copy()
    brk_pot = get_breakdown(potensi_df)
    
    kendala_df = df[(df['Status_Upper'].isin(['WORKFAIL', 'CANCLWORK'])) & (df['Parsed_Date_RE'] == selected_date)].copy()
    brk_ken = get_breakdown(kendala_df)
    
    startwork_df = df[df['Status_Upper'] == "STARTWORK"].copy()
    
    # Manja (H-, HI, H+)
    manja_df = df[(df[flag_manja_col].notna()) & (df['Status_Upper'] == 'STARTWORK')].copy() if flag_manja_col else pd.DataFrame()
    
    # =====================================================================
    # HALAMAN 1: DASHBOARD UTAMA
    # =====================================================================
    if menu == "🟢 1. Ringkasan PS & Progres (Startwork)":
        
        # --- 5 GRID CARDS ---
        def bd_html(brk):
            return f'''
                <div class="dc-row"><span>AO TSEL</span><span style="color:#475569">:</span><span class="dc-row-val">{brk['AO TSEL']}</span></div>
                <div class="dc-row"><span>PDA TSEL</span><span style="color:#475569">:</span><span class="dc-row-val">{brk['PDA TSEL']}</span></div>
                <div class="dc-row"><span>INDIBIZ</span><span style="color:#475569">:</span><span class="dc-row-val">{brk['INDIBIZ']}</span></div>
                <div class="dc-row"><span>ISP VULA</span><span style="color:#475569">:</span><span class="dc-row-val">{brk['ISP VULA']}</span></div>
            '''
            
        manja_total = len(manja_df)
        manja_html = ""
        if flag_manja_col and order_col:
            manja_html += '<div class="dc-row-manja" style="color:#64748b; font-size:0.65rem;"><span></span><span>H-</span><span>HI</span><span>H+</span></div>'
            for prod in PROD_COLS:
                sub = manja_df[manja_df[order_col].astype(str).str.upper().str.contains(prod.split()[0], na=False)]
                h_min = len(sub[sub[flag_manja_col].astype(str).str.contains("H-", na=False)])
                h_i = len(sub[sub[flag_manja_col].astype(str).str.contains("HI", na=False)])
                h_plus = len(sub[sub[flag_manja_col].astype(str).str.contains("H+", na=False)])
                manja_html += f'<div class="dc-row-manja"><span>{prod}</span><span style="color:white">{h_min if h_min>0 else "-"}</span><span style="color:white">{h_i if h_i>0 else "-"}</span><span style="color:white">{h_plus if h_plus>0 else "-"}</span></div>'
        else:
            manja_html = "<div style='text-align:center; padding-top:20px'>NO DATA</div>"
            
        kendala_html = ""
        if order_col:
            kendala_html += '<div class="dc-row-manja" style="color:#cbd5e1; font-size:0.75rem; font-weight:bold; margin-bottom:8px;"><span></span><span style="text-align:center">WFM</span><span style="text-align:center">UNSC</span><span></span></div>'
            for prod in PROD_COLS:
                sub = kendala_df[kendala_df[order_col].astype(str).str.upper().str.contains(prod.split()[0], na=False)]
                wfm = len(sub[sub['Status_Upper'] == 'WORKFAIL'])
                unsc = len(sub[sub['Status_Upper'] == 'CANCLWORK'])
                kendala_html += f'<div class="dc-row-manja"><span>{prod}</span><span style="color:white; text-align:center">{wfm if wfm>0 else "-"}</span><span style="color:white; text-align:center">{unsc if unsc>0 else "-"}</span><span></span></div>'
        else:
            kendala_html = "<div style='text-align:center; padding-top:20px'>NO DATA</div>"
            
        grid_html = f'''
        <div class="grid-5">
            <!-- CARD 1 -->
            <div class="d-card c-blue">
                <div class="dc-header">
                    <div class="dc-icon ic-blue">📥</div>
                    <div><div class="dc-title">RE MASUK HI</div><div class="dc-value">{len(df_re_today)}</div></div>
                </div>
                <div class="dc-breakdown">{bd_html(brk_re).strip()}<div class="dc-row" style="border-top: 1px dashed #334155; margin-top: 8px; padding-top: 8px; font-size: 1.05rem; font-weight: bold;"><span style="color: #cbd5e1;">PS/RE</span><span></span><span style="color:#38bdf8; font-size: 1.15rem;">{ps_re_pct}</span></div></div>
            </div>
            <!-- CARD 2 -->
            <div class="d-card c-green">
                <div class="dc-header">
                    <div class="dc-icon ic-green">✓</div>
                    <div><div class="dc-title">DONE PS</div><div class="dc-value">{len(df_ps_today)}</div></div>
                </div>
                <div class="dc-breakdown">{bd_html(brk_ps)}</div>
            </div>
            <!-- CARD 3 -->
            <div class="d-card c-purple">
                <div class="dc-header">
                    <div class="dc-icon ic-purple">◎</div>
                    <div><div class="dc-title">PONTENSI PS</div><div class="dc-value">{len(potensi_df)}</div></div>
                </div>
                <div class="dc-breakdown">{bd_html(brk_pot)}</div>
            </div>
            <!-- CARD 4 -->
            <div class="d-card c-orange">
                <div class="dc-header">
                    <div class="dc-icon ic-orange">⚠️</div>
                    <div><div class="dc-title">KENDALA HI</div><div class="dc-value">{len(kendala_df)}</div></div>
                </div>
                <div class="dc-breakdown">{kendala_html}</div>
            </div>
            <!-- CARD 5 -->
            <div class="d-card c-teal">
                <div class="dc-header">
                    <div class="dc-icon ic-teal">👤</div>
                    <div><div class="dc-title">MANJA</div><div class="dc-value">{manja_total}</div></div>
                </div>
                <div class="dc-breakdown">{manja_html}</div>
            </div>
        </div>
        '''
        st.markdown(grid_html, unsafe_allow_html=True)
        
        # --- MIDDLE SECTION (CHART & TABLE) ---
        c_left, c_right = st.columns([1, 2.5])
        
        with c_left:
            st.markdown('<div class="section-title-wrap"><div class="section-title">🏆 TOP 5 TEKNISI (DONE PS HARI INI)</div></div>', unsafe_allow_html=True)
            if tim_col and len(df_ps_today) > 0:
                top_tech = df_ps_today[tim_col].value_counts().nlargest(5).reset_index()
                top_tech.columns = [tim_col, 'Jumlah']
                fig_bar = px.bar(top_tech.sort_values('Jumlah', ascending=True), x='Jumlah', y=tim_col, orientation='h', text='Jumlah')
                fig_bar.update_traces(marker_color='#10b981', textfont=dict(color='white', size=14), textposition='outside')
                fig_bar.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
                    font=dict(color='#cbd5e1', size=11), 
                    xaxis=dict(showgrid=False, showticklabels=False, title=""), 
                    yaxis=dict(showgrid=False, title=""),
                    margin=dict(t=0, b=0, l=0, r=20),
                    height=280
                )
                st.plotly_chart(fig_bar, use_container_width=True)
            else:
                st.info("Belum ada pencapaian PS hari ini.")
                
        with c_right:
            st.markdown('<div class="section-title-wrap"><div class="section-title">📈 DETAIL LIVE STARTWORK (SINKRONISASI TEKNISI)</div><div style="font-size:0.8rem;color:#3b82f6;cursor:pointer">Lihat Semua →</div></div>', unsafe_allow_html=True)
            if not startwork_df.empty and tim_col:
                # Custom Styling for DataFrame
                def style_badges(val):
                    val_str = str(val).upper()
                    if 'BELUM PS' in val_str: return 'background-color: #1e293b; color: #94a3b8; border-radius: 4px; padding: 2px 8px; text-align:center; font-size:0.75rem;'
                    if 'SEDANG PS' in val_str: return 'background-color: #065f46; color: #34d399; border-radius: 4px; padding: 2px 8px; text-align:center; font-size:0.75rem;'
                    if 'PENDING' in val_str: return 'background-color: #7c2d12; color: #fb923c; border-radius: 4px; padding: 2px 8px; text-align:center; font-size:0.75rem;'
                    if 'ODP' in val_str: return 'background-color: #3f3f46; color: #a1a1aa; border-radius: 4px; padding: 2px 8px; text-align:center; font-size:0.75rem;'
                    if 'MANJA H++' in val_str or 'MANJA HI' in val_str: return 'background-color: #312e81; color: #818cf8; border-radius: 4px; padding: 2px 8px; text-align:center; font-size:0.75rem;'
                    if 'STARTWORK' in val_str: return 'background-color: #1e3a8a; color: #93c5fd; border-radius: 4px; padding: 2px 8px; text-align:center; font-size:0.75rem;'
                    return ''

                cols = [tim_col]
                if re_col: cols.append(re_col)
                cols.append('INFO ORDER')
                cols.append(status_col)
                if flag_manja_col: cols.append(flag_manja_col)
                if morning_status_col: cols.append(morning_status_col)
                
                disp_df = startwork_df[cols].copy()
                disp_df.insert(0, 'NO', range(1, len(disp_df) + 1))
                
                rename_dict = {
                    tim_col: 'NAMA TEKNISI', 
                    re_col: 'TANGGAL MASUK (RE)',
                    status_col: 'STATUS BIMA',
                    flag_manja_col: 'KATEGORI MANJA',
                    morning_status_col: 'MONITOR'
                }
                disp_df.rename(columns={k:v for k,v in rename_dict.items() if k in disp_df.columns}, inplace=True)
                
                styled_df = disp_df.style.set_properties(**{
                    'background-color': '#0f172a',
                    'color': '#cbd5e1',
                    'border-color': '#1e293b',
                    'font-size': '0.8rem',
                    'text-align': 'center'
                })
                
                # Apply map only to columns that actually exist in the dataframe
                badge_cols = [c for c in ['STATUS BIMA', 'KATEGORI MANJA', 'MONITOR'] if c in disp_df.columns]
                if badge_cols:
                    styled_df = styled_df.map(style_badges, subset=badge_cols)
                
                # Align left for specific columns
                styled_df = styled_df.set_properties(subset=['NAMA TEKNISI', 'INFO ORDER'], **{'text-align': 'left'})
                
                st.dataframe(styled_df, use_container_width=True, hide_index=True, height=320)
            else:
                st.info("Tidak ada WO yang sedang berstatus STARTWORK saat ini.")

        # --- PIVOT TABLE ---
        st.markdown('<div class="section-title-wrap"><div class="section-title">📑 RINCIAN PENCAPAIAN PS (PIVOT TABLE)</div><div style="font-size:0.8rem;color:#94a3b8;border:1px solid #334155;padding:4px 8px;border-radius:4px;cursor:pointer">≡ Tampilkan Semua ⌄</div></div>', unsafe_allow_html=True)
        st.markdown("<p style='font-size:0.85rem; color:#94a3b8; margin-top:-10px; margin-bottom:15px;'>Detail seluruh pesanan yang sudah Closing (PS) hari ini, dikelompokkan berdasarkan Teknisi dan Jenis Order.</p>", unsafe_allow_html=True)
        
        if tim_col and order_col and len(df_ps_today) > 0:
            pivot_ps = pd.pivot_table(df_ps_today, index=[tim_col, 'INFO ORDER'], columns=[order_col], values=status_col, aggfunc='count', fill_value=0)
            order_types = list(pivot_ps.columns)
            
            # Ensure we have exactly 4 order types for the grid to look perfect, or adjust grid
            ot_cols = order_types + [''] * (4 - len(order_types)) if len(order_types) < 4 else order_types[:4]
            
            html = '<div class="cp-container">'
            html += f'<div class="cp-header"><div>MORNING TIM</div><div>TEKNISI / PROV</div><div>{ot_cols[0]}</div><div>{ot_cols[1]}</div><div>{ot_cols[2]}</div><div>{ot_cols[3]}</div><div>GRAND TOTAL</div></div>'
            
            techs = pivot_ps.index.get_level_values(0).unique()
            total_grand = 0
            total_by_type = [0, 0, 0, 0]
            
            for tech in techs:
                tech_data = pivot_ps.xs(tech, level=0)
                tech_total_orders = int(tech_data.sum().sum())
                total_grand += tech_total_orders
                
                # Calculate tech totals for the summary row
                tech_totals = []
                for i, ot in enumerate(ot_cols):
                    if ot in tech_data.columns:
                        t_sum = int(tech_data[ot].sum())
                        tech_totals.append(t_sum)
                        total_by_type[i] += t_sum
                    else:
                        tech_totals.append(0)
                        
                html += f'''
                <details class="cp-row">
                    <summary class="cp-summary">
                        <div><span class="cp-arrow">›</span> {tech}</div>
                        <div><span class="cp-badge">{tech_total_orders} WO</span></div>
                        <div>{tech_totals[0]}</div><div>{tech_totals[1]}</div><div>{tech_totals[2]}</div><div>{tech_totals[3]}</div>
                        <div style="font-weight:bold; color:white;">{tech_total_orders}</div>
                    </summary>
                    <div class="cp-details">
                '''
                for order, row in tech_data.iterrows():
                    html += f'<div class="cp-subrow"><div></div><div>{order}</div>'
                    row_tot = 0
                    for ot in ot_cols:
                        if ot in row.index:
                            val = int(row[ot])
                            row_tot += val
                            html += f'<div>{val}</div>'
                        else:
                            html += '<div>0</div>'
                    html += f'<div style="font-weight:bold; color:white;">{row_tot}</div></div>'
                html += '</div></details>'
                
            html += f'<div class="cp-grand"><div style="text-align:center;">GRAND TOTAL KESELURUHAN</div><div>{total_by_type[0]}</div><div>{total_by_type[1]}</div><div>{total_by_type[2]}</div><div>{total_by_type[3]}</div><div>{total_grand}</div></div>'
            html += '</div>'
            
            st.markdown(html, unsafe_allow_html=True)
            
    # =====================================================================
    # HALAMAN LAINNYA
    # =====================================================================
    elif menu == "🔴 2. Pantauan Kendala Harian":
        st.markdown(f'<div class="metric-container mc-red" style="width: 300px; margin-bottom: 20px;"><div class="mc-title">⚠️ TOTAL LIVE KENDALA</div><div class="mc-value">{len(kendala_df)} <span style="font-size:1rem; color:#94a3b8">WO</span></div><div class="mc-sub">Seluruh status WORKFAIL/CANCL aktif</div></div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-title-wrap"><div class="section-title">🚨 DAFTAR LENGKAP WO KENDALA (REAL-TIME)</div></div>', unsafe_allow_html=True)
        st.markdown("Berikut adalah daftar seluruh pesanan yang SAAT INI berstatus Fail/Cancel di sistem.")
        
        if len(kendala_df) > 0 and tim_col:
            cols_to_show = [tim_col, 'INFO ORDER', status_col]
            if morning_status_col: cols_to_show.append(morning_status_col)
            
            disp_fail = kendala_df[cols_to_show].rename(columns={
                tim_col: 'NAMA TEKNISI (YANG MENGERJAKAN)',
                status_col: 'STATUS BIMA UTAMA'
            })
            st.dataframe(disp_fail.style.set_properties(**{'background-color': '#450a0a', 'color': '#fca5a5', 'border-color': '#333333'}), use_container_width=True, hide_index=True, height=500)
        else:
            st.success("🎉 Luar Biasa! Bersih, tidak ada satupun pesanan yang mengalami kendala.")

    elif menu == "📑 3. Master Detail RE (Pesanan Masuk)":
        st.markdown(f'<div class="metric-container mc-blue" style="margin-bottom: 20px;"><div class="mc-title">📥 TOTAL JUMLAH RE HARI INI</div><div class="mc-value">{len(df_re_today)} <span style="font-size:1rem; color:#94a3b8">WO</span></div></div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-title-wrap"><div class="section-title">📈 DISTRIBUSI JAM MASUK RE & PROGRESS</div></div>', unsafe_allow_html=True)
        if len(df_re_today) > 0 and 'Jam_RE' in df_re_today.columns:
            jam_df = df_re_today[df_re_today['Jam_RE'] != 'Unknown'].copy()
            if not jam_df.empty:
                # Menyiapkan data 24 Jam dengan format 00:00
                all_hours = pd.DataFrame({'Jam': [f"{i:02d}:00" for i in range(24)]})
                
                # Tambahkan :00 ke Jam untuk formatting sumbu X
                jam_df['Jam'] = jam_df['Jam_RE'].astype(str).str[:2] + ":00"
                
                # Split RE MASUK berdasarkan JAM KERJA
                if 'JAM KERJA' in jam_df.columns:
                    re_jk = jam_df[jam_df['JAM KERJA'].astype(str).str.upper() == 'JAM KERJA']
                    re_djk = jam_df[jam_df['JAM KERJA'].astype(str).str.upper() != 'JAM KERJA']
                    
                    re_counts_jk = pd.merge(all_hours, re_jk.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                    re_counts_jk['Kategori'] = 'RE JAM KERJA'
                    
                    re_counts_djk = pd.merge(all_hours, re_djk.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                    re_counts_djk['Kategori'] = 'RE DILUAR JAM KERJA'
                else:
                    re_counts_jk = pd.merge(all_hours, jam_df.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                    re_counts_jk['Kategori'] = 'RE MASUK'
                    re_counts_djk = pd.DataFrame()
                
                comp_counts = pd.merge(all_hours, jam_df[jam_df['Status_Upper'].str.contains('COMPWORK', na=False)].groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                comp_counts['Kategori'] = 'DONE PS'
                
                kendala_counts = pd.merge(all_hours, jam_df[jam_df['Status_Upper'] == 'WORKFAIL'].groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                kendala_counts['Kategori'] = 'KENDALA'
                
                unsc_counts = pd.merge(all_hours, jam_df[jam_df['Status_Upper'] == 'CANCLWORK'].groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                unsc_counts['Kategori'] = 'UNSC'
                
                frames = [re_counts_jk]
                if not re_counts_djk.empty: frames.append(re_counts_djk)
                frames.extend([comp_counts, kendala_counts, unsc_counts])
                
                chart_df = pd.concat(frames, ignore_index=True)
                chart_df['Text'] = chart_df['Jumlah'].apply(lambda x: str(int(x)) if x > 0 else '')
                
                # Splitting layout for chart and summary
                ch_col1, ch_col2 = st.columns([3, 1])
                
                with ch_col1:
                    fig_jam = px.line(chart_df, x='Jam', y='Jumlah', color='Kategori', text='Text', markers=True,
                                     color_discrete_map={
                                         'RE MASUK': '#3b82f6', 
                                         'RE JAM KERJA': '#3b82f6', 
                                         'RE DILUAR JAM KERJA': '#8b5cf6', 
                                         'DONE PS': '#22c55e', 
                                         'KENDALA': '#f59e0b',
                                         'UNSC': '#ef4444'
                                     })
                    fig_jam.update_traces(line=dict(width=3, shape='spline'), fill='tozeroy', marker=dict(size=8), textposition='top center')
                    
                    fill_colors = {
                        'RE MASUK': 'rgba(59, 130, 246, 0.15)',
                        'RE JAM KERJA': 'rgba(59, 130, 246, 0.15)',
                        'RE DILUAR JAM KERJA': 'rgba(139, 92, 246, 0.15)',
                        'DONE PS': 'rgba(34, 197, 94, 0.15)',
                        'KENDALA': 'rgba(245, 158, 11, 0.15)',
                        'UNSC': 'rgba(239, 68, 68, 0.15)'
                    }
                    for trace in fig_jam.data:
                        if trace.name in fill_colors:
                            trace.fillcolor = fill_colors[trace.name]
                            
                    fig_jam.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
                                         font=dict(color='#cbd5e1'), xaxis_title="Waktu (Jam)", yaxis_title="Jumlah WO", 
                                         margin=dict(t=10, b=10, l=10, r=10),
                                         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title=""),
                                         hovermode="x unified",
                                         xaxis=dict(fixedrange=True, dtick=2),
                                         yaxis=dict(fixedrange=True, dtick=1))
                    st.plotly_chart(fig_jam, use_container_width=True, config={'displayModeBar': False})
                    
                with ch_col2:
                    tot_re = len(df_re_today)
                    tot_ps = len(df_ps_today)
                    tot_ken = len(kendala_df)
                    
                    if 'JAM KERJA' in df_re_today.columns:
                        tot_jk = len(df_re_today[df_re_today['JAM KERJA'].astype(str).str.upper() == 'JAM KERJA'])
                        tot_djk = len(df_re_today[df_re_today['JAM KERJA'].astype(str).str.upper() != 'JAM KERJA'])
                    else:
                        tot_jk = tot_re
                        tot_djk = 0
                        
                    pct_jk = f"{(tot_jk/tot_re)*100:.1f}".rstrip('0').rstrip('.') if tot_re > 0 else "0"
                    pct_djk = f"{(tot_djk/tot_re)*100:.1f}".rstrip('0').rstrip('.') if tot_re > 0 else "0"
                    
                    ps_re_pct = f"{(tot_ps/tot_re)*100:.2f}" if tot_re > 0 else "0.00"
                    
                    html_str = (
                        '<div style="border: 1px solid #334155; border-radius: 8px; padding: 20px; text-align: center; background-color: #0f172a; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">'
                        '<div style="font-size: 0.9rem; font-weight: bold; color: #cbd5e1; margin-bottom: 20px;">TOTAL WO (GRAND TOTALS)</div>'
                        '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px 10px; margin-bottom: 20px;">'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #3b82f6; line-height: 1;">{tot_re}</div><div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; margin-top:8px;">RE Masuk</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #22c55e; line-height: 1;">{tot_ps}</div><div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; margin-top:8px;">Done PS</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #f59e0b; line-height: 1;">{tot_ken}</div><div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; margin-top:8px;">Kendala</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #a855f7; line-height: 1;">{ps_re_pct}%</div><div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; margin-top:8px;">PS/RE</div></div>'
                        '</div>'
                        f'<div style="border-top: 1px dashed #334155; padding-top: 20px; margin-top: auto; font-size: 1.05rem; font-weight: bold; color: #94a3b8; text-align: left;">'
                        f'<div style="display:flex; justify-content:space-between; margin-bottom:10px;"><span>RE JAM KERJA</span> <span style="color:white;">{tot_jk} ({pct_jk}%)</span></div>'
                        f'<div style="display:flex; justify-content:space-between;"><span>RE DILUAR JAM KERJA</span> <span style="color:white;">{tot_djk} ({pct_djk}%)</span></div>'
                        f'</div>'
                        '</div>'
                    )
                    st.markdown(html_str, unsafe_allow_html=True)
                    
                st.markdown("<br>", unsafe_allow_html=True)
                
                # --- SPARKLINE CHARTS (SMALL MULTIPLES) ---
                mini_cols = st.columns(5)
                
                categories = [
                    ('RE JAM KERJA', '#3b82f6', 'rgba(59, 130, 246, 0.15)'),
                    ('RE DILUAR JAM KERJA', '#8b5cf6', 'rgba(139, 92, 246, 0.15)'),
                    ('DONE PS', '#22c55e', 'rgba(34, 197, 94, 0.15)'),
                    ('KENDALA', '#f59e0b', 'rgba(245, 158, 11, 0.15)'),
                    ('UNSC', '#ef4444', 'rgba(239, 68, 68, 0.15)')
                ]
                
                for i, (cat, color, fill_color) in enumerate(categories):
                    df_cat = chart_df[chart_df['Kategori'] == cat]
                    
                    fig_mini = px.line(df_cat, x='Jam', y='Jumlah', text='Text', markers=True)
                    fig_mini.update_traces(line=dict(width=2, color=color, shape='spline'), 
                                           fill='tozeroy', fillcolor=fill_color, 
                                           marker=dict(size=4, color=color), textposition='top center')
                    
                    fig_mini.update_layout(
                        title=dict(text=cat, font=dict(color=color, size=13), x=0.5, xanchor='center'),
                        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='#0f172a',
                        margin=dict(t=40, b=20, l=10, r=10),
                        xaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, dtick=8, title="Waktu (Jam)"),
                        yaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, showticklabels=True, title="Jumlah WO", dtick=1),
                        hovermode="x unified",
                        height=280
                    )
                    # Create a border around the plot area
                    fig_mini.update_xaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_mini.update_yaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    
                    with mini_cols[i]:
                        st.plotly_chart(fig_mini, use_container_width=True, config={'displayModeBar': False})
            else:
                st.info("Format jam tidak valid.")
        else:
            st.info("Belum ada RE masuk hari ini.")
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-title-wrap"><div class="section-title">📑 Rekap RE Masuk Harian</div></div>', unsafe_allow_html=True)
        if len(df_re_today) > 0:
            try:
                rekap_df = df_re_today.copy()
                if 'Jam_RE' in rekap_df.columns:
                    rekap_df = rekap_df.sort_values('Jam_RE', ascending=True)
                
                cols_to_show = []
                cols_rename = {}
                
                if 'Jam_RE' in rekap_df.columns:
                    cols_to_show.append('Jam_RE')
                    cols_rename['Jam_RE'] = 'JAM RE MASUK REAL'
                    
                if 'INFO ORDER' in rekap_df.columns:
                    cols_to_show.append('INFO ORDER')
                    cols_rename['INFO ORDER'] = 'NO WONUM & AO'
                    
                if 'Status_Upper' in rekap_df.columns:
                    cols_to_show.append('Status_Upper')
                    cols_rename['Status_Upper'] = 'Status'
                    
                if tim_col and tim_col in rekap_df.columns:
                    cols_to_show.append(tim_col)
                    cols_rename[tim_col] = 'MORNING TIM'
                    
                if morning_status_col and morning_status_col in rekap_df.columns:
                    cols_to_show.append(morning_status_col)
                    cols_rename[morning_status_col] = 'MORNING STATUS WO'
                
                final_df = rekap_df[cols_to_show].copy()
                final_df = final_df.rename(columns=cols_rename)
                final_df.insert(0, 'NO', range(1, len(final_df) + 1))
                final_df = final_df.fillna('-')
                
                html_table = '<div style="height: 600px; overflow-y: auto; border: 1px solid #1e293b; border-radius: 8px;">'
                html_table += '<table style="width: 100%; border-collapse: collapse; text-align: center; color: white; font-size: 0.85rem; font-family: sans-serif;">'
                html_table += '<thead style="position: sticky; top: 0; background-color: #1e293b; z-index: 1;"><tr>'
                for col in final_df.columns:
                    html_table += f'<th style="padding: 12px; border-bottom: 2px solid #334155;">{col}</th>'
                html_table += '</tr></thead><tbody>'
                
                for _, row in final_df.iterrows():
                    html_table += '<tr style="border-bottom: 1px solid #1e293b; background-color: #0f172a;">'
                    for col in final_df.columns:
                        val = row[col]
                        
                        if col == 'Status':
                            val_str = str(val).upper().strip()
                            bg_color = 'transparent'
                            text_color = 'white'
                            if val_str == 'STARTWORK':
                                bg_color = '#64748b'
                                text_color = 'white'
                            elif val_str == 'VALSTART':
                                bg_color = '#39ff14'
                                text_color = 'black'
                            elif val_str == 'COMPWORK':
                                bg_color = '#22c55e'
                                text_color = 'white'
                            elif val_str == 'WORKFAIL':
                                bg_color = '#facc15'
                                text_color = 'black'
                            elif val_str == 'CANCLWORK':
                                bg_color = '#ef4444'
                                text_color = 'white'
                            
                            pill = f'<div style="background-color: {bg_color}; color: {text_color}; border-radius: 12px; padding: 4px 10px; display: inline-block; font-weight: bold; font-size: 0.75rem;">{val}</div>'
                            html_table += f'<td style="padding: 10px;">{pill}</td>'
                        else:
                            html_table += f'<td style="padding: 10px;">{val}</td>'
                    html_table += '</tr>'
                
                html_table += '</tbody></table></div>'
                
                st.markdown(html_table, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Gagal memproses Rekap RE: {e}")
        else:
            st.warning("Belum ada data RE masuk untuk hari ini.")

else:
    st.warning("Belum ada data di Google Sheet GABUNGAN. Pastikan Robot telah men-download file CSV terbaru.")

# --- FLOATING LAST UPDATE WIDGET ---
import os
sync_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "last_sync.txt")
last_sync_text = "Belum Ditarik"
last_sync_source = ""
if os.path.exists(sync_file):
    try:
        with open(sync_file, "r") as f:
            content = f.read().strip()
            if " | VIA " in content:
                parts = content.split(" | VIA ")
                last_sync_text = parts[0]
                last_sync_source = parts[1]
            else:
                last_sync_text = content
    except:
        pass

source_badge = f'<div class="source-badge">VIA {last_sync_source}</div>' if last_sync_source else ''

floating_html = f"""
<style>
.floating-update {{
    position: fixed;
    top: 10px;
    right: 350px;
    background-color: #0f172a;
    border: 1px solid #fbbf24;
    border-radius: 20px;
    padding: 6px 15px;
    color: #f8fafc;
    font-size: 0.8rem;
    font-weight: bold;
    z-index: 999999;
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.5);
}}
.floating-update span {{
    color: #fde68a;
    font-weight: 800;
    font-size: 0.75rem;
}}
.source-badge {{
    background-color: rgba(34, 197, 94, 0.2);
    border: 1px solid #22c55e;
    color: #4ade80;
    font-size: 0.65rem;
    padding: 2px 8px;
    border-radius: 12px;
    letter-spacing: 0.5px;
}}
</style>
<div class="floating-update">
    <span>🔄 UPDATE:</span> {last_sync_text} {source_badge}
</div>
"""
st.markdown(floating_html, unsafe_allow_html=True)
