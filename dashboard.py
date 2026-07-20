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
    .dc-row span:first-child { color: white; font-weight: bold; }
    .dc-row-manja { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; text-align: center; margin-bottom: 5px; }
    .dc-row-manja span:first-child { text-align: left; color: white; font-weight: bold; }
    .dc-row-kendala { display: grid; grid-template-columns: 2fr 1.5fr 1.5fr; text-align: center; margin-bottom: 5px; }
    .dc-row-kendala span:first-child { text-align: left; color: white; font-weight: bold; }

    /* Section Titles */
    .section-title-wrap { display: flex; align-items: center; justify-content: space-between; margin-bottom: 15px; border-bottom: 1px solid #1e293b; padding-bottom: 8px; }
    .section-title { font-size: 1rem; font-weight: bold; color: #e2e8f0; text-transform: uppercase; display: flex; align-items: center; gap: 8px; }
    
    /* Table Styling overrides */
    div[data-testid="stDataFrame"] { border: 1px solid #1e293b; border-radius: 8px; overflow: hidden; }
    
    /* Custom Pivot */
    .cp-container { background-color: #0f172a; border-radius: 8px; border: 1px solid #1e293b; overflow: hidden; }
    .cp-header { display: grid; grid-template-columns: 2fr 3fr 1fr 1fr 1fr 1fr 1fr; background-color: #172554; font-size: 0.85rem; font-weight: 700; color: white; text-transform: uppercase; border-bottom: 2px solid #3b82f6; text-align: center; }
    .cp-header > div { padding: 12px 15px; border-right: 1px solid #64748b; display: flex; align-items: center; justify-content: center; }
    .cp-header > div:last-child { border-right: none; }
    .cp-header div:nth-child(1), .cp-header div:nth-child(2) { justify-content: flex-start; text-align: left; }
    .cp-row { border-bottom: 1px solid #1e293b; }
    .cp-row:last-child { border-bottom: none; }
    .cp-summary { display: grid; grid-template-columns: 2fr 3fr 1fr 1fr 1fr 1fr 1fr; padding: 12px 15px; cursor: pointer; text-align: center; align-items: center; font-size: 0.8rem; color: #cbd5e1; }
    .cp-summary:hover { background-color: #1e293b; }
    .cp-summary div:nth-child(1), .cp-summary div:nth-child(2) { text-align: left; }
    .cp-details { background-color: #0b1121; padding: 0; }
    .cp-body-grid { display: grid; grid-template-columns: 2fr 3fr 1fr 1fr 1fr 1fr 1fr; font-size: 0.8rem; color: white; }
    .cp-cell { border-top: 1px solid #64748b; border-right: 1px solid #64748b; padding: 8px 15px; display: flex; align-items: center; justify-content: center; text-align: center; }
    .cp-cell-left { border-top: 1px solid #64748b; border-right: 1px solid #64748b; padding: 8px 15px; display: flex; align-items: center; justify-content: flex-start; text-align: left; }
    .cp-badge { background-color: #10b981; color: #022c22; padding: 2px 8px; border-radius: 12px; font-weight: 800; font-size: 0.7rem; margin-left: 8px; }
    .cp-arrow { display: inline-block; width: 20px; color: #475569; font-weight: bold; transition: 0.2s; }
    details[open] summary .cp-arrow { transform: rotate(90deg); }
    details summary { list-style: none; }
    details summary::-webkit-details-marker { display: none; }
    .cp-grand { background-color: #172554; display: grid; grid-template-columns: 5fr 1fr 1fr 1fr 1fr 1fr; text-align: center; font-weight: bold; color: white; font-size: 0.85rem; border-top: 2px solid #3b82f6; }
    .cp-grand > div { padding: 12px 15px; border-right: 1px solid #64748b; display: flex; align-items: center; justify-content: center; }
    .cp-grand > div:last-child { border-right: none; }
    
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
        
    st.sidebar.markdown('<p style="color: #94a3b8; font-size: 0.8rem; font-weight: bold; letter-spacing: 1px; margin-bottom: 5px; margin-top: 20px;">DASHBOARD FULFILLMENT</p>', unsafe_allow_html=True)
    
    from streamlit_option_menu import option_menu
    with st.sidebar:
        menu = option_menu(
            menu_title=None,
            options=["PS/RE", "KENDALA", "Detail RE HI (HARIAN)", "Detail MANJA"],
            icons=["trophy", "exclamation-triangle", "card-list", "hourglass-split"],
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent", "border": "none"},
                "icon": {"color": "#94a3b8", "font-size": "18px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"2px 0px", "color": "#cbd5e1", "--hover-color": "#1e293b", "border-radius": "8px"},
                "nav-link-selected": {"background-color": "#3f2b34", "border-left": "4px solid #ef4444", "color": "white", "border-radius": "8px", "border-top-left-radius": "8px", "border-bottom-left-radius": "8px"},
            }
        )
    
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
    ps_re_val = (ps_hi_ao / re_hi_ao * 100) if re_hi_ao > 0 else 0
    ps_re_pct = f"{ps_re_val:.2f}%".replace('.', ',')
    ps_re_color = "#34d399" if ps_re_val >= 85.0 else "#ef4444"
    
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
    if menu == "PS/RE":
        
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
            manja_html += '<div class="dc-row-manja" style="color:white; font-weight:bold; font-size:0.65rem;"><span></span><span>H-</span><span>HI</span><span>H+</span></div>'
            for prod in PROD_COLS:
                sub = manja_df[manja_df[order_col].astype(str).str.upper().str.contains(prod.split()[0], na=False)]
                h_min = len(sub[sub[flag_manja_col].astype(str).str.contains("H-", regex=False, na=False)])
                h_i = len(sub[sub[flag_manja_col].astype(str).str.contains("HI", regex=False, na=False)])
                h_plus = len(sub[sub[flag_manja_col].astype(str).str.contains("H+", regex=False, na=False)])
                manja_html += f'<div class="dc-row-manja"><span>{prod}</span><span style="color:white">{h_min if h_min>0 else "-"}</span><span style="color:white">{h_i if h_i>0 else "-"}</span><span style="color:white">{h_plus if h_plus>0 else "-"}</span></div>'
        else:
            manja_html = "<div style='text-align:center; padding-top:20px'>NO DATA</div>"
            
        kendala_html = ""
        if order_col:
            kendala_html += '<div class="dc-row-kendala" style="color:white; font-size:0.75rem; font-weight:bold; margin-bottom:8px;"><span></span><span>WFM</span><span>UNSC</span></div>'
            for prod in PROD_COLS:
                sub = kendala_df[kendala_df[order_col].astype(str).str.upper().str.contains(prod.split()[0], na=False)]
                wfm = len(sub[sub['Status_Upper'] == 'WORKFAIL'])
                unsc = len(sub[sub['Status_Upper'] == 'CANCLWORK'])
                kendala_html += f'<div class="dc-row-kendala"><span>{prod}</span><span style="color:white">{wfm if wfm>0 else "-"}</span><span style="color:white">{unsc if unsc>0 else "-"}</span></div>'
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
                <div class="dc-breakdown">{bd_html(brk_re).strip()}<div class="dc-row" style="border-top: 1px dashed #334155; margin-top: 8px; padding-top: 8px; font-size: 1.05rem; font-weight: bold;"><span style="color: #cbd5e1;">PS/RE</span><span></span><span style="color:{ps_re_color}; font-size: 1.15rem;">{ps_re_pct}</span></div></div>
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
            if tim_col and len(df_ps_today) > 0:
                top_tech = df_ps_today[tim_col].value_counts().nlargest(5).reset_index()
                top_tech.columns = [tim_col, 'Jumlah']
                
                total_done_ps = len(df_ps_today)
                total_tek_aktif = df_ps_today[tim_col].nunique()
                max_val = top_tech['Jumlah'].max() if len(top_tech) > 0 else 1
                
                # Colors for the 1-5 rank badges
                badge_colors = ["#059669", "#10b981", "#0891b2", "#2563eb", "#7c3aed"]
                
                html_str = '<div style="background-color: #0b1120; border: 2px solid #334155; border-radius: 12px; padding: 20px; font-family: sans-serif; height: 40rem; display: flex; flex-direction: column; justify-content: space-between;">'
                
                # Header
                html_str += '''
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 15px;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="font-size: 2.2rem;">🏆</div>
                        <div>
                            <div style="color: white; font-size: 1.1rem; font-weight: 800; letter-spacing: 0.5px;">TOP 5 TEKNISI</div>
                            <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 2px;">(DONE PS HARI INI)</div>
                        </div>
                    </div>
                    <div style="border: 1px solid #334155; padding: 4px 10px; border-radius: 6px; color: #cbd5e1; font-size: 0.75rem; display: flex; align-items: center; gap: 6px;">
                        📅 Periode Hari Ini
                    </div>
                </div>
                '''
                
                # List
                html_str += '<div style="display: flex; flex-direction: column; gap: 8px;">'
                for i, row in top_tech.iterrows():
                    rank = i + 1
                    name = row[tim_col]
                    count = row['Jumlah']
                    bg_col = badge_colors[i] if i < len(badge_colors) else "#475569"
                    bar_width = (count / max_val) * 100
                    
                    html_str += f'''
                    <div style="background-color: #0f172a; border-radius: 8px; padding: 10px; display: flex; align-items: center; gap: 15px;">
                        <div style="background: {bg_col}; min-width: 38px; height: 38px; border-radius: 8px; display: flex; justify-content: center; align-items: center; color: white; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                            {rank}
                        </div>
                        <div style="flex-grow: 1;">
                            <div style="color: #cbd5e1; font-size: 0.85rem; font-weight: 700; margin-bottom: 6px;">{str(name).upper()}</div>
                            <div style="display: flex; align-items: center; gap: 12px;">
                                <div style="flex-grow: 1; height: 18px; background-color: #1e293b; border-radius: 4px; overflow: hidden;">
                                    <div style="width: {bar_width}%; height: 100%; background: linear-gradient(90deg, #059669, #10b981); border-radius: 4px;"></div>
                                </div>
                                <div style="color: #10b981; font-weight: 800; font-size: 1.1rem; min-width: 20px; text-align: right;">
                                    {count}
                                </div>
                            </div>
                        </div>
                    </div>
                    '''
                html_str += '</div>'
                
                # Divider
                html_str += '<hr style="border: 0; border-top: 1px dashed #334155; margin: 15px 0;">'
                
                # Footer Stats
                html_str += f'''
                <div style="display: flex; gap: 15px;">
                    <!-- Stat 1 -->
                    <div style="flex: 1; background-color: #0f172a; border-radius: 8px; padding: 15px; display: flex; align-items: center; gap: 15px;">
                        <div style="background-color: #064e3b; color: #10b981; width: 45px; height: 45px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 1.5rem; flex-shrink: 0;">
                            👥
                        </div>
                        <div>
                            <div style="color: #cbd5e1; font-size: 0.75rem; margin-bottom: 4px; line-height: 1.2;">Total Done PS<br>hari ini</div>
                            <div style="color: #10b981; font-size: 1.4rem; font-weight: bold;">{total_done_ps}</div>
                        </div>
                    </div>
                    <!-- Stat 2 -->
                    <div style="flex: 1; background-color: #0f172a; border-radius: 8px; padding: 15px; display: flex; align-items: center; gap: 15px;">
                        <div style="background-color: #1e3a8a; color: #3b82f6; width: 45px; height: 45px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 1.5rem; flex-shrink: 0;">
                            🛠️
                        </div>
                        <div>
                            <div style="color: #cbd5e1; font-size: 0.75rem; margin-bottom: 4px; line-height: 1.2;">Total Teknisi<br>Aktif</div>
                            <div style="color: #3b82f6; font-size: 1.4rem; font-weight: bold;">{total_tek_aktif}</div>
                        </div>
                    </div>
                </div>
                '''
                
                html_str += '</div>'
                
                st.markdown(html_str.replace('\n', ''), unsafe_allow_html=True)
            else:
                st.markdown('<div class="section-title-wrap"><div class="section-title">🏆 TOP 5 TEKNISI (DONE PS HARI INI)</div></div>', unsafe_allow_html=True)
                st.info("Belum ada pencapaian PS hari ini.")
                
        with c_right:
            if order_col:
                month, year = selected_date.month, selected_date.year
                
                # Convert dates to datetime to extract month/year safely
                re_dt = pd.to_datetime(df['Parsed_Date_RE'], errors='coerce')
                ps_dt = pd.to_datetime(df['Parsed_Date_PS'], errors='coerce')
                
                re_mask = (re_dt.dt.month == month) & (re_dt.dt.year == year)
                ps_mask = (ps_dt.dt.month == month) & (ps_dt.dt.year == year)
                
                # Filter specific for AO TSEL
                ao_mask = df[order_col].astype(str).str.upper().isin(['AO TSEL', 'AO'])
                
                # RE excludes COMPLETE status (same as RE MASUK HI)
                no_complete_mask = ~df['Status_Upper'].str.contains('COMPLETE', na=False)
                
                df_re_month = df[re_mask & ao_mask & no_complete_mask]
                df_ps_month = df[ps_mask & ao_mask & (df['Status_Upper'].str.contains('COMPWORK', na=False))]
                
                re_counts = df_re_month.groupby('Parsed_Date_RE').size().rename('RE')
                ps_counts = df_ps_month.groupby('Parsed_Date_PS').size().rename('PS')
                
                summary = pd.merge(re_counts, ps_counts, left_index=True, right_index=True, how='outer').fillna(0).astype(int)
                
                if not summary.empty:
                    summary.index.name = 'TANGGAL'
                    # Sort ascending (oldest date first)
                    summary = summary.sort_index(ascending=True)
                    
                    # Calculate grand totals
                    tot_re = summary['RE'].sum()
                    tot_ps = summary['PS'].sum()
                    tot_pct_val = (tot_ps / tot_re * 100) if tot_re > 0 else 0
                    tot_pct = f"{tot_pct_val:.2f}%".replace('.', ',')
                    
                    def format_pct(ps, re):
                        if re == 0: return "0,00%"
                        pct = (ps / re) * 100
                        return f"{pct:.2f}%".replace('.', ',')
                        
                    summary['% PS/RE'] = summary.apply(lambda row: format_pct(row['PS'], row['RE']), axis=1)
                    summary.reset_index(inplace=True)
                    
                    # Convert date to string for cleaner display
                    summary['TANGGAL'] = summary['TANGGAL'].astype(str)
                    
                    # Wrap table in a premium card matching the left side
                    html_table = '<div style="background-color: #0b1120; border: 2px solid #334155; border-radius: 12px; padding: 20px; font-family: sans-serif; height: 40rem; display: flex; flex-direction: column;">'
                    
                    # Custom Header exactly like the left side
                    html_table += '''
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px;">
                        <div style="font-size: 2.2rem; color: #6366f1;">📈</div>
                        <div style="color: white; font-size: 1.1rem; font-weight: 800; letter-spacing: 0.5px;">PS/RE HARIAN (AO TSEL)</div>
                    </div>
                    '''
                    
                    # Manual HTML Table with Scroll and Sticky Headers/Footers
                    html_table += '<div style="flex-grow: 1; overflow-y: auto; border: 1px solid #1e293b; border-radius: 8px;">'
                    html_table += '<table style="width: 100%; border-collapse: collapse; text-align: center; font-family: sans-serif; background-color: #0f172a;">'
                    html_table += '<thead style="background-color: #1e293b; position: sticky; top: 0; z-index: 2;"><tr>'
                    
                    headers = [
                        ('📅 TANGGAL', 'white'), 
                        ('👤 RE', '#38bdf8'), 
                        ('✅ PS', '#34d399'), 
                        ('📊 % PS/RE', '#a855f7')
                    ]
                    for title, color in headers:
                        html_table += f'<th style="padding: 15px 12px; border-bottom: 2px solid #334155; color: {color}; font-size: 0.95rem; text-align: center;">{title}</th>'
                    html_table += '</tr></thead><tbody>'
                    
                    for _, row in summary.iterrows():
                        pct_val = (row["PS"] / row["RE"] * 100) if row["RE"] > 0 else 0
                        pct_color = "#34d399" if pct_val >= 85.0 else "#ef4444"
                        
                        html_table += '<tr style="border-bottom: 1px solid #1e293b;">'
                        html_table += f'<td style="padding: 12px 10px; font-weight: bold; color: white; font-size: 0.85rem; text-align: center;">{row["TANGGAL"]}</td>'
                        html_table += f'<td style="padding: 12px 10px; color: #38bdf8; font-weight: bold; font-size: 0.9rem; text-align: center;">{row["RE"]}</td>'
                        html_table += f'<td style="padding: 12px 10px; color: #34d399; font-weight: bold; font-size: 0.9rem; text-align: center;">{row["PS"]}</td>'
                        html_table += f'<td style="padding: 12px 10px; font-weight: bold; color: {pct_color}; font-size: 0.85rem; text-align: center;">'
                        html_table += f'<div style="display:flex; align-items:center; justify-content:center; gap:10px;">'
                        html_table += f'<span style="width: 60px; text-align:right;">{row["% PS/RE"]}</span>'
                        html_table += f'<div style="width: 60px; height: 6px; background: #1e293b; border-radius: 4px; overflow: hidden;">'
                        html_table += f'<div style="width: {min(pct_val, 100)}%; height: 100%; background: {pct_color};"></div>'
                        html_table += f'</div></div></td>'
                        html_table += '</tr>'
                        
                    html_table += '</tbody>'
                    
                    # Sticky Footer for Totals
                    html_table += '<tfoot style="background-color: #1e293b; position: sticky; bottom: -1px; z-index: 2;">'
                    html_table += '<tr>'
                    html_table += '<th style="padding: 12px; text-align: center; color: white; font-size: 0.95rem; border-top: 2px solid #334155;">'
                    html_table += '<div style="display:flex; align-items:center; justify-content:center; gap:10px;">'
                    html_table += '<div style="background: rgba(139, 92, 246, 0.2); color:#a855f7; padding: 6px 10px; border-radius: 6px; font-weight:900; font-size:1.1rem;">∑</div>'
                    html_table += 'TOTAL'
                    html_table += '</div></th>'
                    html_table += f'<th style="padding: 12px; text-align: center; border-top: 2px solid #334155;"><div style="color: #38bdf8; font-size: 1.1rem;">{tot_re}</div><div style="font-size: 0.65rem; color: #94a3b8; font-weight: normal; margin-top: 4px;">Total RE</div></th>'
                    html_table += f'<th style="padding: 12px; text-align: center; border-top: 2px solid #334155;"><div style="color: #34d399; font-size: 1.1rem;">{tot_ps}</div><div style="font-size: 0.65rem; color: #94a3b8; font-weight: normal; margin-top: 4px;">Total PS</div></th>'
                    html_table += f'<th style="padding: 12px; text-align: center; border-top: 2px solid #334155;"><div style="color: white; font-size: 1.1rem;">{tot_pct}</div><div style="font-size: 0.65rem; color: #94a3b8; font-weight: normal; margin-top: 4px;">Rata-rata % PS/RE</div></th>'
                    html_table += '</tr></tfoot>'
                    
                    html_table += '</table></div>'
                    html_table += '</div>'
                    
                    st.markdown(html_table.replace('\n', ''), unsafe_allow_html=True)
                else:
                    st.info(f"Belum ada data AO TSEL untuk bulan {selected_date.strftime('%B %Y')}.")
            else:
                st.info("Kolom Jenis Order tidak ditemukan.")

        # --- PIVOT TABLE ---
        st.markdown('<div class="section-title-wrap" style="margin-top: 40px;"><div class="section-title">📑 <b>DONE COMPWORK / PS HI</b></div></div>', unsafe_allow_html=True)
        st.markdown("<p style='font-size:0.85rem; color:#94a3b8; margin-top:-10px; margin-bottom:15px;'>Detail seluruh pesanan yang sudah Closing (PS) hari ini, dikelompokkan berdasarkan Teknisi dan Jenis Order.</p>", unsafe_allow_html=True)
        
        if tim_col and order_col and len(df_ps_today) > 0:
            pivot_ps = pd.pivot_table(df_ps_today, index=[tim_col, 'INFO ORDER'], columns=[order_col], values=status_col, aggfunc='count', fill_value=0)
            
            ot_cols = ['AO TSEL', 'PDA TSEL', 'INDIBIZ', 'ISP VULA']
            
            html = '<div class="cp-container">'
            html += f'<div class="cp-header"><div>MORNING TIM</div><div>INFO ORDER (NO WONUM & AO)</div><div>{ot_cols[0]}</div><div>{ot_cols[1]}</div><div>{ot_cols[2]}</div><div>{ot_cols[3]}</div><div>GRAND TOTAL</div></div>'
            
            techs = pivot_ps.index.get_level_values(0).unique()
            total_grand = 0
            total_by_type = [0, 0, 0, 0]
            
            html += '<div class="cp-body-grid">'
            for tech in techs:
                tech_data = pivot_ps.xs(tech, level=0)
                tech_total_orders = int(tech_data.sum().sum())
                total_grand += tech_total_orders
                row_span = len(tech_data)
                
                # Merged tech column (grid-row: span N)
                col1 = f'{tech} <span class="cp-badge">{tech_total_orders} WO</span>'
                html += f'<div class="cp-cell-left" style="grid-row: span {row_span};">{col1}</div>'
                
                for i, (order, row) in enumerate(tech_data.iterrows()):
                    html += f'<div class="cp-cell-left">{order}</div>'
                    
                    row_tot = 0
                    for j, ot in enumerate(ot_cols):
                        if ot in row.index:
                            val = int(row[ot])
                            row_tot += val
                            total_by_type[j] += val
                            html += f'<div class="cp-cell">{val if val > 0 else ""}</div>'
                        else:
                            html += '<div class="cp-cell"></div>'
                            
                    html += f'<div class="cp-cell" style="font-weight:bold;">{row_tot}</div>'
            html += '</div>'

            html += f'<div class="cp-grand"><div style="text-align:center;">GRAND TOTAL KESELURUHAN</div><div>{total_by_type[0]}</div><div>{total_by_type[1]}</div><div>{total_by_type[2]}</div><div>{total_by_type[3]}</div><div>{total_grand}</div></div>'
            html += '</div>'
            
            st.markdown(html, unsafe_allow_html=True)
            
    # =====================================================================
    # HALAMAN LAINNYA
    # =====================================================================
    elif menu == "KENDALA":
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

    elif menu == "Detail RE HI (HARIAN)":
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

    elif menu == "Detail MANJA":
        st.markdown('<div class="section-title-wrap"><div class="section-title">⏳ <b>DETAIL PESANAN MANJA</b></div></div>', unsafe_allow_html=True)
        st.info("Halaman Detail MANJA sedang dalam tahap pengembangan (Under Construction).")

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
