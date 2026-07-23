import streamlit as st
import pandas as pd
import re
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
    @import url('https://fonts.cdnfonts.com/css/superstar-m54');
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
    .cp-container { background-color: #0f172a; border-radius: 8px; border: 1px solid #1e293b; overflow-y: auto; overflow-x: hidden; max-height: 800px; }
    .cp-header { display: grid; grid-template-columns: 2fr 3fr 1fr 1fr 1fr 1fr 1fr; background-color: #172554; font-size: 0.85rem; font-weight: 700; color: white; text-transform: uppercase; border-bottom: 2px solid #3b82f6; text-align: center; position: sticky; top: 0; z-index: 10; }
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
    .cp-grand { background-color: #172554; display: grid; grid-template-columns: 5fr 1fr 1fr 1fr 1fr 1fr; text-align: center; font-weight: bold; color: white; font-size: 0.85rem; border-top: 2px solid #3b82f6; position: sticky; bottom: 0; z-index: 10; }
    .cp-grand > div { padding: 12px 15px; border-right: 1px solid #64748b; display: flex; align-items: center; justify-content: center; }
    .cp-grand > div:last-child { border-right: none; }
    
    /* Custom Pivot Detail MANJA */
    .manja-header { display: grid; grid-template-columns: 4fr 1fr 1fr 1fr 1fr 1fr; background-color: #172554; font-size: 0.95rem; font-weight: 700; color: white; text-transform: uppercase; border-bottom: 2px solid #3b82f6; text-align: center; position: sticky; top: 0; z-index: 10; }
    .manja-header > div { padding: 12px 15px; border-right: 1px solid #64748b; display: flex; align-items: center; justify-content: center; }
    .manja-header > div:last-child { border-right: none; }
    .manja-header div:nth-child(1) { justify-content: flex-start; text-align: left; }
    .manja-row { display: grid; grid-template-columns: 4fr 1fr 1fr 1fr 1fr 1fr; padding: 10px 15px; border-bottom: 1px solid #1e293b; color: #f8fafc; font-size: 0.9rem; align-items: center; text-align: center; }
    .manja-row > div:nth-child(1) { text-align: left; justify-content: flex-start; }
    .manja-grand { background-color: #172554; display: grid; grid-template-columns: 4fr 1fr 1fr 1fr 1fr 1fr; text-align: center; font-weight: bold; color: white; font-size: 0.95rem; border-top: 2px solid #3b82f6; position: sticky; bottom: 0; z-index: 10; padding: 12px 15px; }
    
    /* MANJA WIDGETS */
    .widget-card { background-color: #0b1121; border-radius: 10px; padding: 15px; border: 3px solid #475569; height: 330px; box-sizing: border-box; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    .widget-title { color: #f8fafc; font-size: 1rem; font-weight: bold; margin-bottom: 5px; display: flex; align-items: center; gap: 8px; }
    .widget-subtitle { color: #3b82f6; font-size: 0.75rem; font-weight: bold; margin-bottom: 15px; text-transform: uppercase; }
    
    .hm-table { width: 100%; border-collapse: collapse; font-size: 0.8rem; text-align: center; }
    .hm-table th, .hm-table td { border: 1px solid #1e293b; padding: 8px; }
    .hm-table th { background-color: #0f172a; color: #cbd5e1; font-weight: bold; font-size: 0.75rem; }
    .hm-cell-h2 { background-color: #854d0e; color: white; font-weight: bold; font-size: 1.1rem; }
    .hm-cell-h1 { background-color: #7f1d1d; color: white; font-weight: bold; font-size: 1.1rem; }
    .hm-cell-hi { background-color: #b45309; color: white; font-weight: bold; font-size: 1.1rem; }
    .hm-cell-non { background-color: #14532d; color: white; font-weight: bold; font-size: 1.1rem; }
    
    .sc-box { background-color: #0f172a; border-radius: 8px; padding: 15px; margin-bottom: 10px; border: 1px solid #1e293b; flex: 1; min-width: 0; }
    .sc-title { font-size: 1.3rem; font-weight: bold; color: #3b82f6; margin-bottom: 5px; }
    .sc-title.pda { color: #10b981; }
    .sc-total { font-size: 2.2rem; font-weight: bold; color: white; margin-bottom: 15px; line-height: 1; }
    .sc-total span { font-size: 1.0rem; color: #94a3b8; font-weight: normal; }
    .sc-item { display: flex; justify-content: space-between; font-size: 0.95rem; margin-bottom: 5px; align-items: center; }
    .sc-item-left { display: flex; align-items: center; gap: 5px; color: #cbd5e1; font-weight: bold; }
    .sc-dot-h2 { width: 8px; height: 8px; border-radius: 50%; background-color: #eab308; }
    .sc-dot-h1 { width: 8px; height: 8px; border-radius: 50%; background-color: #ef4444; }
    .sc-dot-hi { width: 8px; height: 8px; border-radius: 50%; background-color: #f97316; }
    .sc-dot-non { width: 8px; height: 8px; border-radius: 50%; background-color: #22c55e; }
</style>
""", unsafe_allow_html=True)

# --- PENGATURAN DATA ---
SHEET_ID = "1zA5ucYxE9gOSnKZIhEKQyV2rEdV5je__knsS9neA5iA"
SHEET_NAME = "GABUNGAN"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

@st.cache_data(ttl=600)
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
        <p class="dash-subtitle" style="display: flex; align-items: center; font-size: 1.45rem; letter-spacing: 1px; margin-top: -8px;">OPERATION DASHBOARD &ndash;&nbsp;<span style="font-family: 'Superstar M54', sans-serif; color: #dc2626; font-size: 1.5rem; letter-spacing: 2px; text-transform: uppercase; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); padding-top: 2px;">YOU'LL NEVER WALK ALONE</span></p>
    </div>
    <div class="header-right">
        <div class="update-time" id="live-clock" style="color: #60a5fa; font-weight: bold; font-size: 1.1rem; text-align: right;">Memuat waktu...</div>
        <div class="export-btn">📥 Export ⌄</div>
    </div>
</div>
''', unsafe_allow_html=True)

# Inject JS untuk Live Clock Real-time
js_clock = """
<script>
    function updateClock() {
        const days = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'];
        const months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
        
        const now = new Date();
        const dayName = days[now.getDay()];
        const day = now.getDate();
        const monthName = months[now.getMonth()];
        const year = now.getFullYear();
        
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        
        const timeString = `${dayName}, ${day} ${monthName} ${year} | ${hours}:${minutes}:${seconds}`;
        
        try {
            const el = window.parent.document.getElementById('live-clock');
            if(el) {
                el.innerText = timeString;
            }
        } catch(e) {}
    }
    
    setInterval(updateClock, 1000);
    updateClock();
</script>
"""
import streamlit.components.v1 as components
components.html(js_clock, width=0, height=0)

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
    st.sidebar.markdown('<p style="font-size:0.9rem; margin-bottom:5px;">Pilih Periode Pantauan:</p>', unsafe_allow_html=True)
    c1, c2, c3 = st.sidebar.columns([10, 1, 10])
    with c1:
        start_date = st.date_input("Dari", today_default)
    with c2:
        st.markdown("<div style='margin-top: 32px; text-align: center;'>-</div>", unsafe_allow_html=True)
    with c3:
        end_date = st.date_input("Sampai", today_default)
    
    # Keep selected_date for backwards compatibility where used
    selected_date = start_date
        
    st.sidebar.markdown('<p style="color: #94a3b8; font-size: 0.8rem; font-weight: bold; letter-spacing: 1px; margin-bottom: 5px; margin-top: 20px;">DASHBOARD FULFILLMENT</p>', unsafe_allow_html=True)
    
    from streamlit_option_menu import option_menu
    with st.sidebar:
        menu = option_menu(
            menu_title=None,
            options=["PS/RE", "KENDALA", "DETAIL RE PERIODE", "DETAIL MANJA", "WO ODS PERIODE", "TRIAL"],
            icons=["trophy", "exclamation-triangle", "card-list", "hourglass-split", "clipboard-data", "pie-chart"],
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
        
    jam_mod_col = find_col(['DATE MODIFIED REAL', 'Date Modified', 'Status Date'])
    if jam_mod_col:
        temp_dt_mod = pd.to_datetime(df[jam_mod_col], dayfirst=True, errors='coerce')
        df['Jam_Update'] = temp_dt_mod.dt.strftime('%H:%M:%S').fillna('Unknown')
    else:
        df['Jam_Update'] = 'Unknown'
    
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
    df_re_today = df[(df['Parsed_Date_RE'] >= start_date) & (df['Parsed_Date_RE'] <= end_date) & (~df['Status_Upper'].str.contains('COMPLETE', na=False))].copy()
    brk_re = get_breakdown(df_re_today)
    
    df_ps_today = df[(df['Parsed_Date_PS'] >= start_date) & (df['Parsed_Date_PS'] <= end_date) & (df['Status_Upper'].str.contains('COMPWORK', na=False))].copy()
    brk_ps = get_breakdown(df_ps_today)
    
    re_hi_ao = brk_re.get('AO TSEL', 0)
    ps_hi_ao = brk_ps.get('AO TSEL', 0)
    ps_re_val = (ps_hi_ao / re_hi_ao * 100) if re_hi_ao > 0 else 0
    ps_re_pct = f"{ps_re_val:.2f}%".replace('.', ',')
    ps_re_color = "#34d399" if ps_re_val >= 85.0 else "#ef4444"
    
    potensi_statuses = ['CONTWORK', 'INSTCOMP', 'ACTCOMP', 'VALCOMP', 'VALSTART']
    potensi_df = df[df['Status_Upper'].isin(potensi_statuses)].copy()
    brk_pot = get_breakdown(potensi_df)
    
    kendala_df = df[(df['Status_Upper'].isin(['WORKFAIL', 'CANCLWORK'])) & (df['Parsed_Date_PS'] >= start_date) & (df['Parsed_Date_PS'] <= end_date)].copy()
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
                
                html_str = '<div style="background-color: #0b1120; border: 2px solid #334155; border-radius: 12px; padding: 20px; font-family: sans-serif; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">'
                
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
        # 1. Hitung Metrik
        total_kendala = len(kendala_df)
        wfm_count = len(kendala_df[kendala_df['Status_Upper'] == 'WORKFAIL'])
        cancl_count = len(kendala_df[kendala_df['Status_Upper'] == 'CANCLWORK'])
        
        wfm_pct = f"{(wfm_count/total_kendala*100):.2f}%".replace('.', ',') if total_kendala > 0 else "0,00%"
        cancl_pct = f"{(cancl_count/total_kendala*100):.2f}%".replace('.', ',') if total_kendala > 0 else "0,00%"
        
        # 2. Render Metric Cards
        cards_html = f'''
        <div style="margin-bottom: 25px;">
            <!-- Title Block -->
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                <div style="width: 45px; height: 45px; display: flex; align-items: center; justify-content: center;">
                    <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12.8659 3.00017C12.4812 2.3335 11.5187 2.3335 11.134 3.00017L2.13401 18.6002C1.74934 19.2668 2.23059 20.1002 2.99991 20.1002H20.9999C21.7692 20.1002 22.2505 19.2668 21.8658 18.6002L12.8659 3.00017Z" fill="#ef4444"/>
                        <path d="M12 9V14" stroke="#0b1121" stroke-width="2.5" stroke-linecap="round"/>
                        <circle cx="12" cy="17.5" r="1.5" fill="#0b1121"/>
                    </svg>
                </div>
                <div>
                    <div style="color: white; font-weight: 900; font-size: 1.3rem; letter-spacing: 0.5px;">MONITORING KENDALA</div>
                    <div style="color: #94a3b8; font-size: 0.9rem;">Real-time Overview</div>
                </div>
            </div>

            <!-- Cards Row -->
            <div style="display: flex; gap: 20px; align-items: stretch;">
                
                <!-- WORKFAIL Card -->
                <div style="flex: 1; background-color: #0f172a; border-radius: 12px; border: 1px solid #1e293b; display: flex; flex-direction: column; position: relative; overflow: hidden;">
                    <div style="padding: 15px 20px; display: flex; gap: 15px; flex-grow: 1;">
                        <div style="background-color: #ef4444; width: 60px; height: 60px; border-radius: 12px; display: flex; justify-content: center; align-items: center; flex-shrink: 0;">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 2L1 21H23L12 2ZM11 16H13V18H11V16ZM11 10H13V14H11V10Z"/>
                            </svg>
                        </div>
                        <div style="display: flex; flex-direction: column; justify-content: center;">
                            <div style="color: #cbd5e1; font-size: 0.75rem; font-weight: bold; letter-spacing: 0.5px; margin-bottom: 2px;">WORKFAIL</div>
                            <div style="color: #ef4444; font-size: 1.8rem; font-weight: bold; line-height: 1;">{wfm_count}</div>
                            <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 4px;">({wfm_pct})</div>
                        </div>
                    </div>
                    <div style="height: 3px; background-color: #ef4444; margin: 0 15px 15px 15px; border-radius: 2px;"></div>
                </div>

                <!-- CANCEL Card -->
                <div style="flex: 1; background-color: #0f172a; border-radius: 12px; border: 1px solid #1e293b; display: flex; flex-direction: column; position: relative; overflow: hidden;">
                    <div style="padding: 15px 20px; display: flex; gap: 15px; flex-grow: 1;">
                        <div style="background-color: #f97316; width: 60px; height: 60px; border-radius: 12px; display: flex; justify-content: center; align-items: center; flex-shrink: 0;">
                            <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="12" r="10"></circle>
                                <line x1="15" y1="9" x2="9" y2="15"></line>
                                <line x1="9" y1="9" x2="15" y2="15"></line>
                            </svg>
                        </div>
                        <div style="display: flex; flex-direction: column; justify-content: center;">
                            <div style="color: #cbd5e1; font-size: 0.75rem; font-weight: bold; letter-spacing: 0.5px; margin-bottom: 2px;">CANCEL (WORK)</div>
                            <div style="color: #f97316; font-size: 1.8rem; font-weight: bold; line-height: 1;">{cancl_count}</div>
                            <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 4px;">({cancl_pct})</div>
                        </div>
                    </div>
                    <div style="height: 3px; background-color: #f97316; margin: 0 15px 15px 15px; border-radius: 2px;"></div>
                </div>

                <!-- TOTAL Card -->
                <div style="flex: 1; background-color: #0f172a; border-radius: 12px; border: 1px solid #1e293b; display: flex; flex-direction: column; position: relative; overflow: hidden;">
                    <div style="padding: 15px 20px; display: flex; gap: 15px; flex-grow: 1;">
                        <div style="background-color: #3b82f6; width: 60px; height: 60px; border-radius: 12px; display: flex; justify-content: center; align-items: center; flex-shrink: 0;">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                <polyline points="14 2 14 8 20 8"></polyline>
                                <line x1="16" y1="13" x2="8" y2="13"></line>
                                <line x1="16" y1="17" x2="8" y2="17"></line>
                                <polyline points="10 9 9 9 8 9"></polyline>
                            </svg>
                        </div>
                        <div style="display: flex; flex-direction: column; justify-content: center;">
                            <div style="color: #cbd5e1; font-size: 0.75rem; font-weight: bold; letter-spacing: 0.5px; margin-bottom: 2px;">TOTAL WO</div>
                            <div style="color: #3b82f6; font-size: 1.8rem; font-weight: bold; line-height: 1;">{total_kendala}</div>
                            <div style="color: #3b82f6; font-size: 0.8rem; margin-top: 4px;">(100%)</div>
                        </div>
                    </div>
                    <div style="height: 3px; background-color: #3b82f6; margin: 0 15px 15px 15px; border-radius: 2px;"></div>
                </div>
                
            </div>
        </div>
        '''
        st.markdown(cards_html.replace('\n', ''), unsafe_allow_html=True)
        
        # 3. Render Plotly Charts
        st.markdown('<br>', unsafe_allow_html=True)
        if total_kendala > 0:
            col1, col2, col3 = st.columns([1, 1.3, 1.3])
            
            # --- Chart 1: Donut ---
            with col1:
                with st.container(border=True):
                    st.markdown('<div style="color: #cbd5e1; font-size: 0.9rem; font-weight: bold; margin-bottom: 10px;">DISTRIBUSI STATUS WO</div>', unsafe_allow_html=True)
                    
                    donut_df = pd.DataFrame({
                        'Status': ['WORKFAIL', 'CANCEL (WORK)'],
                        'Jumlah': [wfm_count, cancl_count],
                        'Color': ['#ef4444', '#f97316'],
                        'Label': [f'WORKFAIL<br><b>{wfm_count}</b> ({wfm_pct})', f'CANCEL (WORK)<br><b>{cancl_count}</b> ({cancl_pct})']
                    })
                    donut_df = donut_df[donut_df['Jumlah'] > 0]
                    if not donut_df.empty:
                        fig1 = go.Figure(data=[go.Pie(
                            labels=donut_df['Label'], 
                            values=donut_df['Jumlah'], 
                            hole=.6,
                            marker_colors=donut_df['Color'],
                            textinfo='none',
                            hoverinfo='label'
                        )])
                        fig1.update_layout(
                            showlegend=True,
                            legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=0.9, font=dict(color="#cbd5e1", size=11)),
                            annotations=[dict(text=f"TOTAL<br><b>{total_kendala}</b><br>WO", x=0.45, y=0.5, font_size=13, font_color="white", showarrow=False)],
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            margin=dict(t=0, b=0, l=0, r=0),
                            height=250
                        )
                        # Shift the pie center to the left slightly so legend fits better on the right
                        fig1.update_traces(domain=dict(x=[0, 0.9]))
                        st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False}, theme=None)
                    else:
                        st.info("No Data")
            
            # --- Chart 2: Top 5 Kendala ---
            with col2:
                with st.container(border=True):
                    st.markdown('<div style="color: #cbd5e1; font-size: 0.9rem; font-weight: bold; margin-bottom: 10px;">TOP 5 KENDALA</div>', unsafe_allow_html=True)
                    if morning_status_col:
                        top_reasons = kendala_df[morning_status_col].dropna().astype(str).str.upper().value_counts().nlargest(5).reset_index()
                        top_reasons.columns = ['Alasan', 'Jumlah']
                        if not top_reasons.empty:
                            html_bars2 = '<div style="display: flex; flex-direction: column; justify-content: space-evenly; height: 250px; padding: 5px 0;">'
                            max_val2 = top_reasons['Jumlah'].max()
                            rank_colors2 = ['#ef4444', '#f97316', '#f59e0b', '#eab308', '#facc15']
                            
                            for i, row in enumerate(top_reasons.itertuples()):
                                name2 = row.Alasan
                                val2 = row.Jumlah
                                color2 = rank_colors2[i] if i < len(rank_colors2) else rank_colors2[-1]
                                width_pct2 = (val2 / max_val2) * 100 if max_val2 > 0 else 0
                                
                                html_bars2 += f'<div style="display: flex; align-items: center; width: 100%;">'
                                html_bars2 += f'<div style="color: #cbd5e1; width: 170px; white-space: normal; word-wrap: break-word; line-height: 1.2; font-size: 0.8rem; margin-right: 10px; flex-shrink: 0;" title="{name2}">{name2}</div>'
                                html_bars2 += f'<div style="flex-grow: 1; display: flex; align-items: center; padding-right: 10px;">'
                                html_bars2 += f'<div style="background-color: {color2}; height: 14px; width: {width_pct2}%;"></div>'
                                html_bars2 += f'<div style="color: #ffffff; font-weight: bold; font-size: 0.8rem; margin-left: 8px;">{val2}</div>'
                                html_bars2 += f'</div></div>'
                                
                            html_bars2 += '</div>'
                            st.markdown(html_bars2, unsafe_allow_html=True)
                        else:
                            st.info("No Morning Status Data")
                    else:
                        st.info("Column Not Found")
                    
            # --- Chart 3: Top 5 Teknisi ---
            with col3:
                with st.container(border=True):
                    st.markdown('<div style="color: #cbd5e1; font-size: 0.9rem; font-weight: bold; margin-bottom: 10px;">TOP 5 TEKNISI DENGAN KENDALA</div>', unsafe_allow_html=True)
                    if tim_col:
                        top_tek = kendala_df[tim_col].dropna().astype(str).str.upper().value_counts().nlargest(5).reset_index()
                        top_tek.columns = ['Teknisi', 'Jumlah']
                        if not top_tek.empty:
                            html_bars = '<div style="display: flex; flex-direction: column; justify-content: space-evenly; height: 250px; padding: 5px 0;">'
                            max_val = top_tek['Jumlah'].max()
                            rank_colors = ['#ef4444', '#f97316', '#f59e0b', '#eab308', '#facc15']
                            
                            for i, row in enumerate(top_tek.itertuples()):
                                rank = i + 1
                                name = row.Teknisi
                                val = row.Jumlah
                                color = rank_colors[i] if i < len(rank_colors) else rank_colors[-1]
                                width_pct = (val / max_val) * 100 if max_val > 0 else 0
                                
                                html_bars += f'<div style="display: flex; align-items: center; width: 100%;">'
                                html_bars += f'<div style="background-color: #1e293b; color: #94a3b8; border-radius: 4px; width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: bold; margin-right: 12px; flex-shrink: 0;">{rank}</div>'
                                html_bars += f'<div style="color: #cbd5e1; width: 140px; white-space: normal; word-wrap: break-word; line-height: 1.2; font-size: 0.8rem; margin-right: 10px; flex-shrink: 0;" title="{name}">{name}</div>'
                                html_bars += f'<div style="flex-grow: 1; display: flex; align-items: center; padding-right: 10px;">'
                                html_bars += f'<div style="background-color: {color}; height: 14px; width: {width_pct}%;"></div>'
                                html_bars += f'<div style="color: #ffffff; font-weight: bold; font-size: 0.8rem; margin-left: 8px;">{val}</div>'
                                html_bars += f'</div></div>'
                                
                            html_bars += '</div>'
                            st.markdown(html_bars, unsafe_allow_html=True)
                        else:
                            st.info("No Technician Data")
                    else:
                        st.info("Column Not Found")
        
        st.markdown('<br>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-title-wrap"><div class="section-title">🚨 DAFTAR LENGKAP WO KENDALA (REAL-TIME)</div></div>', unsafe_allow_html=True)
        st.markdown("Berikut adalah daftar seluruh pesanan yang SAAT INI berstatus Fail/Cancel di sistem.")
        
        if len(kendala_df) > 0 and tim_col:
            cols_to_show = [tim_col, 'INFO ORDER', status_col]
            if morning_status_col: cols_to_show.append(morning_status_col)
            
            disp_fail = kendala_df[cols_to_show].rename(columns={
                tim_col: 'MORNING TIM',
                'INFO ORDER': 'NO WONUM & AO',
                status_col: 'STATUS'
            })
            html_table = '<table style="width:100%; border-collapse: collapse; margin-top: 15px; font-size: 0.85rem; font-family: sans-serif;">'
            html_table += '<thead><tr style="background-color: #7f1d1d; color: white; text-align: center;">'
            for col in disp_fail.columns:
                html_table += f'<th style="border: 1px solid #cbd5e1; padding: 12px 8px;">{col}</th>'
            html_table += '</tr></thead><tbody>'
            
            for _, row in disp_fail.iterrows():
                html_table += '<tr style="background-color: #450a0a; color: #fca5a5; text-align: center;">'
                for val in row:
                    html_table += f'<td style="border: 1px solid #cbd5e1; padding: 10px 8px;">{val if pd.notna(val) and str(val).strip() != "" else "-"}</td>'
                html_table += '</tr>'
            html_table += '</tbody></table>'
            
            st.markdown(html_table, unsafe_allow_html=True)
        else:
            st.success("🎉 Luar Biasa! Bersih, tidak ada satupun pesanan yang mengalami kendala.")

    elif menu == "DETAIL RE PERIODE":
        if order_col:
            df_re_today = df_re_today[df_re_today[order_col].astype(str).str.upper().str.contains('AO', na=False)]
            df_ps_today = df_ps_today[df_ps_today[order_col].astype(str).str.upper().str.contains('AO', na=False)]
            kendala_df = kendala_df[kendala_df[order_col].astype(str).str.upper().str.contains('AO', na=False)]
            
        st.markdown(f'<div class="metric-container mc-blue" style="margin-bottom: 20px;"><div class="mc-title">📥 TOTAL JUMLAH RE HARI INI (AO TSEL)</div><div class="mc-value">{len(df_re_today)} <span style="font-size:1rem; color:#94a3b8">WO</span></div></div>', unsafe_allow_html=True)
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
                
                if 'Jam_Update' in df_ps_today.columns and not df_ps_today.empty:
                    jam_ps = df_ps_today[df_ps_today['Jam_Update'] != 'Unknown'].copy()
                    jam_ps['Jam'] = jam_ps['Jam_Update'].astype(str).str[:2] + ":00"
                    comp_counts = pd.merge(all_hours, jam_ps.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                else:
                    comp_counts = pd.merge(all_hours, pd.DataFrame(columns=['Jam', 'Jumlah']), on='Jam', how='left').fillna(0)
                comp_counts['Kategori'] = 'DONE PS'
                
                if 'Jam_Update' in kendala_df.columns and not kendala_df.empty:
                    jam_ken = kendala_df[kendala_df['Jam_Update'] != 'Unknown'].copy()
                    jam_ken['Jam'] = jam_ken['Jam_Update'].astype(str).str[:2] + ":00"
                    ken_wfm = jam_ken[jam_ken['Status_Upper'] == 'WORKFAIL']
                    kendala_counts = pd.merge(all_hours, ken_wfm.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                    ken_unsc = jam_ken[jam_ken['Status_Upper'] == 'CANCLWORK']
                    unsc_counts = pd.merge(all_hours, ken_unsc.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                else:
                    kendala_counts = pd.merge(all_hours, pd.DataFrame(columns=['Jam', 'Jumlah']), on='Jam', how='left').fillna(0)
                    unsc_counts = pd.merge(all_hours, pd.DataFrame(columns=['Jam', 'Jumlah']), on='Jam', how='left').fillna(0)
                kendala_counts['Kategori'] = 'KENDALA'
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
                                         margin=dict(t=10, b=40, l=10, r=10),
                                         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title=""),
                                         hovermode="x unified",
                                         xaxis=dict(fixedrange=True, dtick=2, showgrid=True, gridwidth=1, gridcolor='#334155'),
                                         yaxis=dict(fixedrange=True, dtick=1, showgrid=True, gridwidth=1, gridcolor='#334155'))
                    st.plotly_chart(fig_jam, use_container_width=True, config={'displayModeBar': False}, theme=None)
                    
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
                        margin=dict(t=40, b=45, l=10, r=10),
                        xaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, dtick=8, title="Waktu (Jam)"),
                        yaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, showticklabels=True, title="Jumlah WO", dtick=1),
                        hovermode="x unified",
                        height=280
                    )
                    # Create a border around the plot area
                    fig_mini.update_xaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_mini.update_yaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    
                    with mini_cols[i]:
                        st.plotly_chart(fig_mini, use_container_width=True, config={'displayModeBar': False}, theme=None)
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

    elif menu == "DETAIL MANJA":
        st.markdown("""
        <style>
        .cp-container { color: #f1f5f9; font-size: 1.25rem; max-height: 800px; }
        .manja-header { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr 1fr; background: #4c1d95; padding: 3px 10px; font-weight: bold; color: #ffffff; font-size: 1.05rem; }
        .manja-row { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr 1fr; padding: 12px 10px; border-bottom: 1px solid #334155; align-items: center; }
        .manja-grand { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr 1fr; padding: 15px 10px; background: #4c1d95; font-weight: bold; border-top: 2px solid #334155; color: #ffffff; font-size: 1.15rem; }
        .cp-arrow { display: inline-block; transition: transform 0.2s; margin-right: 5px; }
        details[open] > summary .cp-arrow { transform: rotate(90deg); }
        </style>
        <div class="section-title">⏳ DETAIL PESANAN MANJA</div>
        """, unsafe_allow_html=True)
        
        # 1. Filter Data
        df['Status_Upper'] = df['Status'].astype(str).str.upper().str.strip()
        df_manja = df[df['Status_Upper'].isin(['STARTWORK', 'CONTWORK'])].copy()
        
        if 'FLAG MANJA' in df_manja.columns:
            df_manja['FLAG MANJA'] = df_manja['FLAG MANJA'].fillna('NON MANJA').replace('', 'NON MANJA')
        else:
            df_manja['FLAG MANJA'] = 'NON MANJA'
            
        if len(df_manja) == 0:
            st.info("Tidak ada data pesanan MANJA (STARTWORK / CONTWORK) saat ini.")
        else:
            st.markdown("<br>", unsafe_allow_html=True)
            col_top1, col_top2 = st.columns(2)
            
            hm_agg = df_manja.groupby(['CECK BY ORDER', 'FLAG MANJA']).size().reset_index(name='count')
            cbos = df_manja['CECK BY ORDER'].dropna().unique()
            cbo_totals = df_manja['CECK BY ORDER'].value_counts().to_dict()
            flags = ['MANJA H-1', 'MANJA HI', 'MANJA H++', 'NON MANJA']
            
            # WIDGET 1: HEATMAP
            with col_top1:
                hm_html = '''
                <div class="widget-card">
                    <div class="widget-title"><span style="font-size: 1.2rem;">🎛️</span> HEATMAP MATRIX</div>
                    <table class="hm-table">
                        <tr>
                            <th rowspan="2" style="width: 30%;">CHECK BY<br>ORDER</th>
                            <th colspan="4">FLAG MANJA</th>
                        </tr>
                        <tr>
                            <th>MANJA H-1</th><th>MANJA HI</th><th>MANJA H++</th><th>NON MANJA</th>
                        </tr>
                '''
                
                hm_colors = ['hm-cell-h1', 'hm-cell-hi', 'hm-cell-h2', 'hm-cell-non']
                
                for cbo in cbos:
                    hm_html += f'<tr><td style="font-weight: bold; text-align: left; color: #f8fafc;">{cbo}</td>'
                    cbo_data = hm_agg[hm_agg['CECK BY ORDER'] == cbo]
                    for i, flag in enumerate(flags):
                        val = cbo_data[cbo_data['FLAG MANJA'] == flag]['count'].sum() if flag in cbo_data['FLAG MANJA'].values else 0
                        cls = hm_colors[i] if val > 0 else ''
                        val_str = str(val) if val > 0 else '0'
                        hm_html += f'<td class="{cls}">{val_str}</td>'
                    hm_html += '</tr>'
                
                hm_html += '''
                    </table>
                    <div style="display: flex; justify-content: space-between; margin-top: 15px; font-size: 0.65rem; color: #cbd5e1; font-weight: bold;">
                        <div style="display: flex; align-items: center; gap: 4px;"><div class="sc-dot-h1" style="border-radius: 2px;"></div> MANJA H-1</div>
                        <div style="display: flex; align-items: center; gap: 4px;"><div class="sc-dot-hi" style="border-radius: 2px;"></div> MANJA HI</div>
                        <div style="display: flex; align-items: center; gap: 4px;"><div class="sc-dot-h2" style="border-radius: 2px;"></div> MANJA H++</div>
                        <div style="display: flex; align-items: center; gap: 4px;"><div class="sc-dot-non" style="border-radius: 2px;"></div> NON MANJA</div>
                    </div>
                </div>
                '''
                st.markdown(hm_html, unsafe_allow_html=True)
            

            with col_top2:
                # Custom SVG Flow Diagram (Sankey Alternative)
                total_wo = len(df_manja)
                cbo_list = list(cbo_totals.keys())
                
                cbo_html = ""
                script_lines = []
                
                flag_colors = {
                    'MANJA H-1': ('#ef4444', 'red'), 
                    'MANJA HI': ('#f97316', 'orange'), 
                    'MANJA H++': ('#eab308', 'yellow'), 
                    'NON MANJA': ('#22c55e', 'green')
                }
                
                for i, cbo in enumerate(cbo_list):
                    cbo_id = f"cbo-{i}"
                    cbo_data = hm_agg[hm_agg['CECK BY ORDER'] == cbo]
                    
                    flags_html = ""
                    for j, flag in enumerate(flags):
                        count = cbo_data[cbo_data['FLAG MANJA'] == flag]['count'].sum() if flag in cbo_data['FLAG MANJA'].values else 0
                        flag_id = f"flag-{i}-{j}"
                        color_hex, color_class = flag_colors.get(flag, ('#ffffff', ''))
                        flags_html += f'''
                        <div class="node-flag" id="{flag_id}">
                            <div class="flag-box {color_class}"></div>
                            <div style="color: #f8fafc; font-size: 0.75rem; font-weight: bold; font-family: sans-serif;">{flag} ({count})</div>
                        </div>
                        '''
                        # Draw line from CBO to Flag (Gradient from CBO blue to Flag color)
                        script_lines.append(f"drawLine('{cbo_id}', '{flag_id}', '#2563eb', '{color_hex}', 0.4, 15, 6);")
                    
                    # Draw line from Root to CBO (Solid/Gradient blue)
                    script_lines.append(f"drawLine('root', '{cbo_id}', '#1e3a8a', '#2563eb', 0.6, 20, 12);")
                    
                    cbo_html += f'''
                    <div class="cbo-row">
                        <div class="node" id="{cbo_id}">
                            <div>{cbo}</div>
                            <div class="node-total">{cbo_totals.get(cbo, 0)} WO</div>
                        </div>
                        <div class="flags-container">
                            {flags_html}
                        </div>
                    </div>
                    '''

                sankey_card = f'''
                <style>
                    body {{ margin: 0; padding: 0; background-color: transparent; font-family: sans-serif; overflow: hidden; }}
                    .widget-card {{ background-color: #0b1121; border-radius: 10px; padding: 15px; border: 3px solid #475569; height: 330px; box-sizing: border-box; box-shadow: 0 4px 6px rgba(0,0,0,0.3); overflow: hidden; }}
                    .widget-title {{ color: #f8fafc; font-size: 1rem; font-weight: bold; margin-bottom: 5px; display: flex; align-items: center; gap: 8px; font-family: sans-serif; text-transform: uppercase; }}
                    .flow-container {{ display: flex; width: 100%; height: 265px; position: relative; align-items: center; }}
                    .svg-layer {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; }}
                    .col-left {{ width: 28%; z-index: 2; display: flex; justify-content: flex-start; }}
                    .col-right {{ width: 72%; z-index: 2; display: flex; flex-direction: column; justify-content: space-around; height: 100%; padding-left: 25px; }}
                    .node {{ background: #0f172a; border: 1px solid #3b82f6; border-radius: 8px; padding: 12px 8px; color: #f8fafc; font-size: 0.85rem; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.3); z-index: 3; position: relative; }}
                    .node-total {{ color: #60a5fa; font-size: 1.1rem; font-weight: bold; margin-top: 5px; }}
                    .cbo-row {{ display: flex; justify-content: space-between; align-items: center; width: 100%; }}
                    .flags-container {{ display: flex; flex-direction: column; gap: 6px; align-items: flex-start; z-index: 3; position: relative; }}
                    .node-flag {{ display: flex; align-items: center; gap: 8px; background: transparent; padding: 2px 0; }}
                    .flag-box {{ width: 14px; height: 14px; border-radius: 3px; box-shadow: 0 0 5px rgba(0,0,0,0.5); }}
                    .red {{ background: #ef4444; }} .orange {{ background: #f97316; }} .yellow {{ background: #eab308; }} .green {{ background: #22c55e; }}
                </style>
                <div class="widget-card">
                    <div class="widget-title"><span style="font-size: 1.2rem;">🌊</span> SANKY FLOW (ALIRAN DATA)</div>
                    <div class="flow-container">
                        <svg class="svg-layer" id="svg"></svg>
                        <div class="col-left">
                            <div class="node" id="root" style="border-color: #60a5fa;">
                                <div>STARTWORK<br>TOTAL</div>
                                <div class="node-total">{total_wo} WO</div>
                            </div>
                        </div>
                        <div class="col-right">
                            {cbo_html}
                        </div>
                    </div>
                </div>
                <script>
                    function drawLine(id1, id2, color1, color2, opacity, strokeWidth, offsetRight) {{
                        const el1 = document.getElementById(id1);
                        const el2 = document.getElementById(id2);
                        const svg = document.getElementById('svg');
                        const container = document.querySelector('.flow-container');
                        
                        if(!el1 || !el2) return;
                        
                        const rect1 = el1.getBoundingClientRect();
                        const rect2 = el2.getBoundingClientRect();
                        const contRect = container.getBoundingClientRect();
                        
                        let x1 = rect1.right - contRect.left;
                        let y1 = rect1.top + rect1.height/2 - contRect.top;
                        
                        let x2 = rect2.left - contRect.left;
                        let y2 = rect2.top + rect2.height/2 - contRect.top;
                        
                        if (id2.startsWith("flag")) {{
                            x2 = x2 + offsetRight; // Adjust to point to the middle of the small box
                        }}
                        
                        const offset = Math.max(30, Math.abs(x2 - x1) * 0.4);
                        const d = `M ${{x1}} ${{y1}} C ${{x1 + offset}} ${{y1}}, ${{x2 - offset}} ${{y2}}, ${{x2}} ${{y2}}`;
                        
                        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                        path.setAttribute('d', d);
                        
                        const gradId = 'grad-' + id1 + '-' + id2;
                        const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
                        const linearGradient = document.createElementNS('http://www.w3.org/2000/svg', 'linearGradient');
                        linearGradient.setAttribute('id', gradId);
                        linearGradient.setAttribute('x1', '0%');
                        linearGradient.setAttribute('y1', '0%');
                        linearGradient.setAttribute('x2', '100%');
                        linearGradient.setAttribute('y2', '0%');
                        
                        const stop1 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
                        stop1.setAttribute('offset', '0%');
                        stop1.setAttribute('stop-color', color1);
                        
                        const stop2 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
                        stop2.setAttribute('offset', '100%');
                        stop2.setAttribute('stop-color', color2);
                        
                        linearGradient.appendChild(stop1);
                        linearGradient.appendChild(stop2);
                        defs.appendChild(linearGradient);
                        svg.appendChild(defs);
                        
                        path.setAttribute('stroke', `url(#${{gradId}})`);
                        path.setAttribute('stroke-width', strokeWidth);
                        path.setAttribute('fill', 'none');
                        path.setAttribute('opacity', opacity);
                        
                        svg.appendChild(path);
                    }}
                    
                    function renderLines() {{
                        document.getElementById('svg').innerHTML = '';
                        {' '.join(script_lines)}
                    }}
                    
                    // Render lines initially and on resize
                    setTimeout(renderLines, 100);
                    window.addEventListener('resize', () => setTimeout(renderLines, 100));
                </script>
                '''
                st.components.v1.html(sankey_card, height=330, scrolling=False)
            
            st.markdown("<br>", unsafe_allow_html=True)
            col_bot1, col_bot2 = st.columns(2)
            
            # WIDGET 4: DONUT CHART
            with col_bot1:
                count_h2 = len(df_manja[df_manja['FLAG MANJA'] == 'MANJA H++'])
                count_h1 = len(df_manja[df_manja['FLAG MANJA'] == 'MANJA H-1'])
                count_hi = len(df_manja[df_manja['FLAG MANJA'] == 'MANJA HI'])
                count_non = len(df_manja[df_manja['FLAG MANJA'] == 'NON MANJA'])
                
                pct_h2 = (count_h2 / total_wo * 100) if total_wo else 0
                pct_h1 = (count_h1 / total_wo * 100) if total_wo else 0
                pct_hi = (count_hi / total_wo * 100) if total_wo else 0
                pct_non = (count_non / total_wo * 100) if total_wo else 0
                
                p1 = pct_h1
                p2 = p1 + pct_hi
                p3 = p2 + pct_h2
                
                donut_html = f'''
                <div class="widget-card">
                    <div class="widget-title" style="margin-bottom: 20px;"><span style="font-size: 1.2rem;">🍩</span> DONUT CHART</div>
                    <div style="display: flex; align-items: center; justify-content: space-around; height: 240px; padding: 0 10px;">
                        <!-- Donut -->
                        <div style="position: relative; width: 200px; height: 200px; border-radius: 50%; background: conic-gradient(#ef4444 0% {p1}%, #f97316 {p1}% {p2}%, #eab308 {p2}% {p3}%, #22c55e {p3}% 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 0 15px rgba(0,0,0,0.5);">
                            <!-- Inner hole -->
                            <div style="width: 140px; height: 140px; background-color: #0b1121; border-radius: 50%; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: inset 0 0 10px rgba(0,0,0,0.5);">
                                <span style="color: #cbd5e1; font-size: 0.95rem; font-weight: bold; margin-bottom: 2px;">TOTAL</span>
                                <span style="color: white; font-size: 2.5rem; font-weight: bold; line-height: 1;">{total_wo}</span>
                                <span style="color: #cbd5e1; font-size: 0.95rem; margin-top: 2px;">WO</span>
                            </div>
                        </div>
                        
                        <!-- Legend -->
                        <div style="display: flex; flex-direction: column; gap: 18px;">
                            <div style="display: flex; align-items: center; gap: 10px; color: #f8fafc; font-weight: bold; font-size: 0.9rem;">
                                <div style="width: 14px; height: 14px; border-radius: 50%; background-color: #ef4444; box-shadow: 0 0 5px #ef4444;"></div>
                                <div style="width: 85px;">MANJA H-1</div>
                                <div style="color: white; font-weight: bold;">{count_h1} &nbsp;&nbsp; ({int(round(pct_h1))}%)</div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 10px; color: #f8fafc; font-weight: bold; font-size: 0.9rem;">
                                <div style="width: 14px; height: 14px; border-radius: 50%; background-color: #f97316; box-shadow: 0 0 5px #f97316;"></div>
                                <div style="width: 85px;">MANJA HI</div>
                                <div style="color: white; font-weight: bold;">{count_hi} &nbsp;&nbsp; ({int(round(pct_hi))}%)</div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 10px; color: #f8fafc; font-weight: bold; font-size: 0.9rem;">
                                <div style="width: 14px; height: 14px; border-radius: 50%; background-color: #eab308; box-shadow: 0 0 5px #eab308;"></div>
                                <div style="width: 85px;">MANJA H++</div>
                                <div style="color: white; font-weight: bold;">{count_h2} &nbsp;&nbsp; ({int(round(pct_h2))}%)</div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 10px; color: #f8fafc; font-weight: bold; font-size: 0.9rem;">
                                <div style="width: 14px; height: 14px; border-radius: 50%; background-color: #22c55e; box-shadow: 0 0 5px #22c55e;"></div>
                                <div style="width: 85px;">NON MANJA</div>
                                <div style="color: white; font-weight: bold;">{count_non} &nbsp;&nbsp; ({int(round(pct_non))}%)</div>
                            </div>
                        </div>
                    </div>
                </div>
                '''
                st.markdown(donut_html.replace('\n', ''), unsafe_allow_html=True)

            # WIDGET 3: STATUS CARD
            with col_bot2:
                sc_html = '''
                <div class="widget-card">
                    <div class="widget-title"><span style="font-size: 1.2rem;">📋</span> STATUS CARD PER AREA</div>
                    <div style="display: flex; gap: 10px;">
                '''
                
                dots = ['sc-dot-h1', 'sc-dot-hi', 'sc-dot-h2', 'sc-dot-non']
                
                for i, cbo in enumerate(cbos):
                    total_cbo = cbo_totals.get(cbo, 0)
                    t_class = "sc-title pda" if "PDA" in str(cbo).upper() else "sc-title"
                    
                    sc_html += f'<div class="sc-box">'
                    sc_html += f'<div class="{t_class}">{cbo}</div>'
                    sc_html += f'<div class="sc-total">{total_cbo} <span>WO</span></div>'
                    
                    cbo_data = hm_agg[hm_agg['CECK BY ORDER'] == cbo]
                    for j, flag in enumerate(flags):
                        count = cbo_data[cbo_data['FLAG MANJA'] == flag]['count'].sum() if flag in cbo_data['FLAG MANJA'].values else 0
                        pct = int(round((count / total_cbo * 100) if total_cbo > 0 else 0))
                        sc_html += f'<div class="sc-item">'
                        sc_html += f'<div class="sc-item-left"><div class="{dots[j]}"></div> {flag}</div>'
                        sc_html += f'<div style="color: white; font-weight: bold;">{count} &nbsp;&nbsp; ({pct}%)</div>'
                        sc_html += f'</div>'
                    
                    sc_html += '</div>'
                
                sc_html += '</div></div>'
                st.markdown(sc_html, unsafe_allow_html=True)
                
            st.markdown("<br>", unsafe_allow_html=True)
            # 2. Pivot Data
            pivot = pd.pivot_table(
                df_manja, 
                values='Workorder', 
                index=['CECK BY ORDER', 'Workzone', 'NO WONUM & AO'], 
                columns='FLAG MANJA', 
                aggfunc='count', 
                fill_value=0
            )
            
            # Ensure columns exist
            cols = ['MANJA H-1', 'MANJA HI', 'MANJA H++', 'NON MANJA']
            for c in cols:
                if c not in pivot.columns:
                    pivot[c] = 0
            
            pivot = pivot[cols]
            pivot['Grand Total'] = pivot.sum(axis=1)
            
            # 3. Build HTML
            html = '<div class="cp-container">'
            html += f'<div class="manja-header"><div>CECK BY ORDER / WORKZONE / WONUM</div><div>MANJA H-1</div><div>MANJA HI</div><div>MANJA H++</div><div>NON MANJA</div><div>GRAND TOTAL</div></div>'
            
            html += '<div style="background-color: #0b1121;">'
            
            grand_totals = [0, 0, 0, 0, 0] # H++, H-1, HI, NON, Grand
            
            def fmt_num(val):
                v = int(val)
                return str(v) if v > 0 else ""
            
            for cbo, df_cbo in pivot.groupby(level=0):
                cbo_sum = df_cbo.sum()
                html += f'<div class="manja-row" style="background-color: #1e293b; font-weight: bold;">'
                html += f'<div style="font-weight: bold; color: #fbbf24; font-size: 1.25rem;">{cbo}</div>'
                html += f'<div>{fmt_num(cbo_sum["MANJA H-1"])}</div><div>{fmt_num(cbo_sum["MANJA HI"])}</div><div>{fmt_num(cbo_sum["MANJA H++"])}</div><div>{fmt_num(cbo_sum["NON MANJA"])}</div><div>{fmt_num(cbo_sum["Grand Total"])}</div>'
                html += f'</div>'
                
                for wz, df_wz in df_cbo.groupby(level=1):
                    wz_sum = df_wz.sum()
                    html += f'<div class="manja-row" style="background-color: #0f172a; border-left: 4px solid #3b82f6;">'
                    html += f'<div style="padding-left: 20px; font-weight: bold; color: #38bdf8; font-size: 1.15rem;">{wz}</div>'
                    html += f'<div>{fmt_num(wz_sum["MANJA H-1"])}</div><div>{fmt_num(wz_sum["MANJA HI"])}</div><div>{fmt_num(wz_sum["MANJA H++"])}</div><div>{fmt_num(wz_sum["NON MANJA"])}</div><div>{fmt_num(wz_sum["Grand Total"])}</div>'
                    html += f'</div>'
                    
                    for wonum, df_wonum in df_wz.groupby(level=2):
                        wonum_sum = df_wonum.sum()
                        html += f'<div class="manja-row" style="border-left: 4px solid #10b981;">'
                        html += f'<div style="padding-left: 45px; font-size: 1.05rem; color: white; font-weight: bold;">{wonum}</div>'
                        html += f'<div>{fmt_num(wonum_sum["MANJA H-1"])}</div><div>{fmt_num(wonum_sum["MANJA HI"])}</div><div>{fmt_num(wonum_sum["MANJA H++"])}</div><div>{fmt_num(wonum_sum["NON MANJA"])}</div><div>{fmt_num(wonum_sum["Grand Total"])}</div>'
                        html += f'</div>'
                
                grand_totals[0] += int(cbo_sum["MANJA H-1"])
                grand_totals[1] += int(cbo_sum["MANJA HI"])
                grand_totals[2] += int(cbo_sum["MANJA H++"])
                grand_totals[3] += int(cbo_sum["NON MANJA"])
                grand_totals[4] += int(cbo_sum["Grand Total"])

            html += '</div>'
            
            # Grand Total Row
            html += f'<div class="manja-grand"><div>GRAND TOTAL KESELURUHAN</div><div>{int(grand_totals[0])}</div><div>{int(grand_totals[1])}</div><div>{int(grand_totals[2])}</div><div>{int(grand_totals[3])}</div><div>{int(grand_totals[4])}</div></div>'
            
            html += '</div>'
            
            st.markdown(html, unsafe_allow_html=True)

    elif menu == "WO ODS PERIODE":

        st.markdown("""
        <style>
        .cp-container { color: #f1f5f9; font-size: 0.85rem; max-height: 800px; }
        .manja-header { display: grid; grid-template-columns: 0.5fr 3fr 1.5fr 1fr 2fr 1fr 1.5fr; background: #facc15; padding: 9px 15px; font-weight: bold; color: #020617; font-size: 1.0rem; text-align: center; border-radius: 4px 4px 0 0;}
        .manja-row { display: grid; grid-template-columns: 0.5fr 3fr 1.5fr 1fr 2fr 1fr 1.5fr; padding: 8px 15px; border-bottom: 1px solid #334155; align-items: center; text-align: center; color: #cbd5e1; font-size: 0.9rem;}
        .pill-compwork { background-color: #10b981; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold; font-size: 0.75rem; display: inline-block; }
        .pill-startwork { background-color: #475569; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold; font-size: 0.75rem; display: inline-block; }
        .pill-other { background-color: #3b82f6; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold; font-size: 0.75rem; display: inline-block; }
        </style>
        <div class="section-title">📊 WO ODS HI</div>
        """, unsafe_allow_html=True)
        
        ods_col = find_col(['WO ODS', 'WO_ODS', 'ODS'])
        tgl_ods_col = find_col(['TANGGAL WO ODS', 'TGL ODS', 'TGL WO ODS'])
        
        if ods_col and tgl_ods_col:
            df['Parsed_Date_ODS'] = pd.to_datetime(df[tgl_ods_col], errors='coerce').dt.date
            df_ods = df[(df[ods_col].astype(str).str.strip().str.upper() == 'ONE DAY SERVICE') & 
                        (df['Parsed_Date_ODS'] >= start_date) & 
                        (df['Parsed_Date_ODS'] <= end_date) & 
                        (~df['Status_Upper'].str.contains('COMPLETE', na=False))].copy()
        else:
            df_ods = df[(df['Parsed_Date_RE'] >= start_date) & 
                        (df['Parsed_Date_RE'] <= end_date) & 
                        (~df['Status_Upper'].str.contains('COMPLETE', na=False))].copy()
        
        if len(df_ods) == 0:
            st.info("Tidak ada data WO ODS untuk periode ini.")
        else:
            html = '<div class="cp-container">'
            html += """
<div class="manja-header">
    <div>NO</div>
    <div>NO WONUM & AO</div>
    <div>DATE RE</div>
    <div>WORZONE</div>
    <div>MORNING TIM</div>
    <div>STATUS</div>
    <div>MORNING STATUS WO</div>
</div>
"""
            nowonum_col = find_col(['NO WONUM & AO', 'NO WONUM'])
            date_cr_col = find_col(['DATE CREATE REAL', 'Date Created', 'DATE CREATED'])
            wz_col = find_col(['WORZONE', 'WORKZONE', 'Workzone', 'ZONE', 'Zone'])
            
            for i, (_, row) in enumerate(df_ods.iterrows(), 1):
                no_wonum = str(row[nowonum_col]) if nowonum_col and pd.notna(row[nowonum_col]) else ""
                if no_wonum.lower() == 'nan': no_wonum = ""
                
                date_cr = str(row[date_cr_col]) if date_cr_col and pd.notna(row[date_cr_col]) else ""
                if date_cr.lower() == 'nan': date_cr = ""
                if '.' in date_cr: date_cr = date_cr.split('.')[0]
                
                wz = str(row[wz_col]) if wz_col and pd.notna(row[wz_col]) else ""
                if wz.lower() == 'nan': wz = ""
                
                tim = str(row['MORNING TIM']) if 'MORNING TIM' in row and pd.notna(row['MORNING TIM']) else ""
                if tim.lower() == 'nan': tim = ""
                
                status = str(row['Status_Upper']) if 'Status_Upper' in row else ""
                if status == 'COMPWORK':
                    status_html = f'<div class="pill-compwork">{status}</div>'
                elif status == 'STARTWORK':
                    status_html = f'<div class="pill-startwork">{status}</div>'
                else:
                    status_html = f'<div class="pill-other">{status}</div>'
                    
                morning_st = str(row['MORNING STATUS WO']) if 'MORNING STATUS WO' in row and pd.notna(row['MORNING STATUS WO']) else ""
                if morning_st.lower() == 'nan': morning_st = ""
                
                html += f"""
<div class="manja-row">
    <div style="color: white; font-weight: bold;">{i}</div>
    <div style="font-size: 0.8rem; color: white; font-weight: bold;">{no_wonum}</div>
    <div>{date_cr}</div>
    <div>{wz}</div>
    <div style="font-size: 0.8rem;">{tim}</div>
    <div>{status_html}</div>
    <div>{morning_st}</div>
</div>
"""
            html += '</div>'
            st.markdown(html, unsafe_allow_html=True)
            
    elif menu == "TRIAL":
        st.markdown(f"""
<div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:20px;">
    <div>
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:5px;">
            <h4 style="margin:0; color:#cbd5e1; font-weight:700; letter-spacing: 0.5px;">
                <i class="bi bi-diagram-3" style="color: #60a5fa; margin-right: 8px;"></i> SANKY FLOW - TOTAL ALL PS HI
            </h4>
        </div>
        <div style="color:#64748b; font-size:0.75rem; font-weight:600; text-transform:uppercase; margin-left:32px;">STARTWORK TOTAL {len(df[(df['Parsed_Date_PS'] >= start_date) & (df['Parsed_Date_PS'] <= end_date) & (df['Status_Upper'].str.contains('COMPWORK', na=False))])} WO COMPWORK</div>
    </div>
    <div style="background:#1e293b; padding:6px 15px; border-radius:6px; font-size:0.8rem; color:#94a3b8; border: 1px solid #334155;">
        <i class="bi bi-calendar-event" style="color: #60a5fa; margin-right: 5px;"></i> Periode: {start_date.strftime('%d %b %Y')} - {end_date.strftime('%d %b %Y')}
    </div>
</div>
""", unsafe_allow_html=True)
        
        ai_col = find_col(['CECK BY ORDER'])
        au_col = find_col(['DETAIL PS KAPAN'])
        
        if ai_col and au_col:
            valid_orders = ['AO TSEL', 'PDA TSEL', 'INDIBIZ', 'VULA BITSTREAM']
            df_sankey = df[(df['Parsed_Date_PS'] >= start_date) & (df['Parsed_Date_PS'] <= end_date) & (df['Status_Upper'].str.contains('COMPWORK', na=False))].copy()
            df_sankey['Order_Type'] = df_sankey[ai_col].astype(str).str.strip().str.upper()
            df_sankey = df_sankey[df_sankey['Order_Type'].isin([v.upper() for v in valid_orders])]
            df_sankey['PS_Kapan'] = df_sankey[au_col].astype(str).str.strip()
            total_wo = len(df_sankey)
            
            if total_wo > 0:
                width = 850
                height = 500
                
                color_map = {
                    'PS H-': '#dc2626', 'PS H-²': '#2563eb', 'PS HI': '#eab308', 
                    'PS H -': '#dc2626', 'PS H -²': '#2563eb',
                    'AO TSEL': '#ef4444', 'PDA TSEL': '#f97316', 'INDIBIZ': '#eab308', 'VULA BITSTREAM': '#22c55e'
                }
                
                l1_counts = df_sankey['PS_Kapan'].value_counts().to_dict()
                l2_counts = df_sankey['Order_Type'].value_counts().to_dict()
                l1_keys = list(l1_counts.keys())
                l2_keys = list(l2_counts.keys())
                
                col0_x = 20
                col1_x = 350
                col2_x = 650
                root_y = height / 2
                
                l1_nodes = {}
                spacing1 = height / (len(l1_keys) + 1)
                for i, k in enumerate(l1_keys): l1_nodes[k] = {'y': spacing1 * (i + 1), 'val': l1_counts[k]}
                    
                l2_nodes = {}
                spacing2 = height / (len(l2_keys) + 1)
                for i, k in enumerate(l2_keys): l2_nodes[k] = {'y': spacing2 * (i + 1), 'val': l2_counts[k]}
                
                svg_paths = ""
                html_cards = f"""
                <div style="position:absolute; left:{col0_x}px; top:10px; width:120px; text-align:center; background:#1e293b; padding:8px 0; border-radius:6px; color:#cbd5e1; font-size:0.7rem; font-weight:700;">TOTAL ALL PS HI</div>
                <div style="position:absolute; left:{col1_x}px; top:10px; width:160px; text-align:center; background:#1e293b; padding:8px 0; border-radius:6px; color:#cbd5e1; font-size:0.7rem; font-weight:700;">PS BY DATE RE</div>
                <div style="position:absolute; left:{col2_x}px; top:10px; width:160px; text-align:center; background:#1e293b; padding:8px 0; border-radius:6px; color:#cbd5e1; font-size:0.7rem; font-weight:700;">JENIS ORDER</div>
                <div style="position:absolute; left:{col0_x}px; top:{root_y - 70}px; width:120px; height:140px; background:#0f172a; border:1px solid #334155; border-radius:12px; display:flex; flex-direction:column; justify-content:center; align-items:center; box-shadow: 0 4px 10px rgba(0,0,0,0.5); z-index:10;">
                    <i class="bi bi-file-earmark-text" style="color:#60a5fa; font-size:1.8rem; margin-bottom:8px;"></i>
                    <div style="color:#f8fafc; font-size:0.8rem; font-weight:700; margin-bottom:5px;">TOTAL</div>
                    <div style="color:#f8fafc; font-size:2.5rem; font-weight:700; line-height:1; margin-bottom:5px;">{total_wo}</div>
                    <div style="color:#94a3b8; font-size:0.8rem; font-weight:700;">WO</div>
                </div>
                """
                
                for k, node in l1_nodes.items():
                    val = node['val']
                    w = max(2, (val / total_wo) * 80)
                    col = color_map.get(k, '#3b82f6')
                    if '²' in k: col = '#2563eb' 
                    x0 = col0_x + 120
                    y0 = root_y
                    x2 = col1_x
                    y2 = node['y']
                    x1 = x0 + (x2 - x0) / 2
                    svg_paths += f'<path d="M {x0} {y0} C {x1} {y0}, {x1} {y2}, {x2} {y2}" fill="none" stroke="{col}" stroke-width="{w}" stroke-opacity="0.6" />'
                
                for k, node in l1_nodes.items():
                    y = node['y']
                    val = node['val']
                    pct = (val / total_wo * 100) if total_wo > 0 else 0
                    col = color_map.get(k, '#3b82f6')
                    if '²' in k: col = '#2563eb'
                    html_cards += f"""
                    <div style="position:absolute; left:{col1_x}px; top:{y - 40}px; width:160px; height:80px; background:#0f172a; border:1px solid #1e293b; border-left: 4px solid {col}; border-radius:8px; display:flex; flex-direction:column; justify-content:center; padding-left:15px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); z-index:10;">
                        <div style="color:#cbd5e1; font-size:0.8rem; font-weight:700; margin-bottom:3px;">{k}</div>
                        <div style="display:flex; align-items:baseline; gap:5px;">
                            <div style="color:#f8fafc; font-size:1.2rem; font-weight:700;">{val}</div><div style="color:#94a3b8; font-size:0.7rem; font-weight:700;">WO</div>
                        </div>
                        <div style="color:{col}; font-size:0.75rem; font-weight:700; margin-top:2px;">({pct:.0f}%)</div>
                    </div>
                    """
                    
                l1_l2 = df_sankey.groupby(['PS_Kapan', 'Order_Type']).size().reset_index(name='count')
                for _, row in l1_l2.iterrows():
                    k1 = row['PS_Kapan']
                    k2 = row['Order_Type']
                    val = row['count']
                    if val == 0: continue
                    w = max(2, (val / total_wo) * 80)
                    col = color_map.get(k2, '#ef4444')
                    x0 = col1_x + 160
                    y0 = l1_nodes[k1]['y']
                    x2 = col2_x
                    y2 = l2_nodes[k2]['y']
                    x1 = x0 + (x2 - x0) / 2
                    svg_paths += f'<path d="M {x0} {y0} C {x1} {y0}, {x1} {y2}, {x2} {y2}" fill="none" stroke="{col}" stroke-width="{w}" stroke-opacity="0.6" />'
                
                for k, node in l2_nodes.items():
                    y = node['y']
                    val = node['val']
                    pct = (val / total_wo * 100) if total_wo > 0 else 0
                    col = color_map.get(k, '#ef4444')
                    html_cards += f"""
                    <div style="position:absolute; left:{col2_x}px; top:{y - 40}px; width:160px; height:80px; background:#0f172a; border:1px solid #1e293b; border-left: 4px solid {col}; border-radius:8px; display:flex; flex-direction:column; justify-content:center; padding-left:15px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); z-index:10;">
                        <div style="color:#cbd5e1; font-size:0.8rem; font-weight:700; margin-bottom:3px;">{k}</div>
                        <div style="display:flex; align-items:baseline; gap:5px;">
                            <div style="color:#f8fafc; font-size:1.2rem; font-weight:700;">{val}</div><div style="color:#94a3b8; font-size:0.7rem; font-weight:700;">WO</div>
                        </div>
                        <div style="color:{col}; font-size:0.75rem; font-weight:700; margin-top:2px;">({pct:.0f}%)</div>
                    </div>
                    """
                
                final_html = f"""
                <div style="position:relative; width:100%; height:{height}px; background:#0b1120; border-radius:12px; border:1px solid #1e293b; overflow:hidden; margin-bottom:20px;">
                    <svg width="100%" height="100%" style="position:absolute; top:0; left:0; pointer-events:none;">
                        {svg_paths}
                    </svg>
                    {html_cards}
                </div>
                """
                
                card1_inner = ""
                for k,v in l1_counts.items():
                    pct = (v / total_wo * 100) if total_wo > 0 else 0
                    col = color_map.get(k, '#3b82f6')
                    if '²' in k: col = '#2563eb'
                    card1_inner += f"""
                    <div style="display:flex; flex-direction:column; align-items:center; padding:0 15px;">
                        <div style="display:flex; align-items:center; gap:5px; margin-bottom:10px;">
                            <div style="width:10px; height:10px; border-radius:50%; background:{col};"></div>
                            <div style="color:#cbd5e1; font-size:0.7rem; font-weight:700;">{k}</div>
                        </div>
                        <div style="color:#f8fafc; font-size:1.5rem; font-weight:700; line-height:1;">{v}</div>
                        <div style="color:#64748b; font-size:0.7rem; margin-bottom:10px;">WO</div>
                        <div style="color:{col}; font-size:0.9rem; font-weight:700;">{pct:.0f}%</div>
                    </div>
                    """
                    
                card2_inner = ""
                for k,v in list(l2_counts.items())[:2]: 
                    pct = (v / total_wo * 100) if total_wo > 0 else 0
                    col = color_map.get(k, '#ef4444')
                    card2_inner += f"""
                    <div style="display:flex; flex-direction:column; align-items:center; padding:0 15px;">
                        <div style="color:#cbd5e1; font-size:0.7rem; font-weight:700; margin-bottom:10px;">{k}</div>
                        <div style="color:#f8fafc; font-size:1.5rem; font-weight:700; line-height:1;">{v}</div>
                        <div style="color:#64748b; font-size:0.7rem; margin-bottom:10px;">WO</div>
                        <div style="color:#10b981; font-size:0.9rem; font-weight:700;">{pct:.0f}%</div>
                    </div>
                    """
                
                cards_html = f"""
                <div style="display:flex; gap:15px; margin-top:10px;">
                    <div style="flex:1; background:#0f172a; padding:15px; border-radius:8px; border: 1px solid #1e293b;">
                        <div style="color:#cbd5e1; font-size:0.75rem; font-weight:700; margin-bottom:15px;">RINGKASAN PS BY DATE RE</div>
                        <div style="display:flex; justify-content:space-around; text-align:center;">{card1_inner}</div>
                    </div>
                    <div style="flex:1; background:#0f172a; padding:15px; border-radius:8px; border: 1px solid #1e293b;">
                        <div style="color:#cbd5e1; font-size:0.75rem; font-weight:700; margin-bottom:15px;">RINGKASAN JENIS ORDER</div>
                        <div style="display:flex; justify-content:space-around; text-align:center;">{card2_inner}</div>
                    </div>
                    <div style="flex:1; background:#0f172a; padding:15px; border-radius:8px; border: 1px solid #1e293b; display:flex; flex-direction:column; justify-content:center; align-items:center;">
                        <div style="color:#cbd5e1; font-size:0.75rem; font-weight:700; margin-bottom:15px;">TOTAL KESELURUHAN</div>
                        <div style="display:flex; align-items:center; gap:15px;">
                            <i class="bi bi-clipboard-data" style="color:#60a5fa; font-size:2.5rem;"></i>
                            <div style="display:flex; flex-direction:column;">
                                <div style="display:flex; align-items:baseline; gap:5px;">
                                    <span style="color:#f8fafc; font-size:2rem; font-weight:700; line-height:1;">{total_wo}</span>
                                    <span style="color:#64748b; font-size:0.8rem; font-weight:700;">WO</span>
                                </div>
                                <div style="color:#10b981; font-size:1.1rem; font-weight:700; margin-top:5px;">100%</div>
                            </div>
                        </div>
                    </div>
                </div>
                """
                
                final_html = re.sub(r'^\s+', '', final_html, flags=re.MULTILINE).replace('\n', '')
                cards_html = re.sub(r'^\s+', '', cards_html, flags=re.MULTILINE).replace('\n', '')
                
                st.markdown(final_html, unsafe_allow_html=True)
                st.markdown(cards_html, unsafe_allow_html=True)
                
            else:
                st.info("Tidak ada data PS (COMPWORK) untuk periode ini.")
                
        else:
            st.error("Kolom 'CECK BY ORDER' atau 'DETAIL PS KAPAN' tidak ditemukan.")
