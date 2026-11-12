import streamlit as st
import pandas as pd
import numpy as np
import psutil
import textwrap
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

@st.cache_resource
def get_auto_puller():
    import threading
    import random
    import time
    import subprocess
    import sys
    import os
    
    class AutoPuller:
        def __init__(self):
            self.running = False
            self.thread = None
            self.next_run_time = None
            
        def _loop(self):
            while self.running:
                # Tidur bervariasi antara 20:00 hingga 21:00 menit untuk menghindari deteksi anti-bot
                sleep_time = random.randint(1200, 1260)
                self.next_run_time = time.time() + sleep_time
                
                # Tidur dalam interval 1 detik agar bisa dihentikan kapan saja secara instan, dan mendukung reset waktu
                while self.running and self.next_run_time and time.time() < self.next_run_time:
                    time.sleep(1)
                    
                if not self.running:
                    self.next_run_time = None
                    return
                    
                # Menjalankan perintah penarikan data (dengan timeout 600 detik agar thread tidak pernah macet selamanya)
                try:
                    py_exec = sys.executable or "python"
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    script_path = os.path.join(base_dir, "main.py")
                    subprocess.run([py_exec, script_path, "DASHBOARD", "Admin Web", "WFM_MORNING", "Otomatis"], cwd=base_dir, capture_output=True, text=True, timeout=600)
                except Exception:
                    pass
                    
        def start(self):
            if not self.running or self.thread is None or not self.thread.is_alive():
                import time, random
                self.next_run_time = time.time() + random.randint(1200, 1260)
                self.running = True
                self.thread = threading.Thread(target=self._loop, daemon=True)
                self.thread.start()
                
        def stop(self):
            self.running = False
            self.thread = None
            
        def reset_timer(self):
            if self.running:
                sleep_time = random.randint(1200, 1260)
                self.next_run_time = time.time() + sleep_time
            
    return AutoPuller()

auto_puller = get_auto_puller()

@st.cache_resource
def get_ibooster_auto_puller():
    import threading
    import random
    import time
    import subprocess
    import sys
    import os
    
    class IboosterAutoPuller:
        def __init__(self):
            self.running = False
            self.thread = None
            self.next_run_time = None
            
        def _loop(self):
            while self.running:
                # 02:55:30 to 02:56:30
                sleep_time = random.randint(8700, 9000)
                self.next_run_time = time.time() + sleep_time
                
                while self.running and self.next_run_time and time.time() < self.next_run_time:
                    time.sleep(1)
                    
                if not self.running:
                    self.next_run_time = None
                    return
                    
                try:
                    py_exec = sys.executable or "python"
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    script_path = os.path.join(base_dir, "main.py")
                    subprocess.run([py_exec, script_path, "DASHBOARD", "Admin Web", "IBOOSTER", "Otomatis"], cwd=base_dir, capture_output=True, text=True, timeout=3600)
                except Exception:
                    pass
                    
        def start(self):
            if not self.running or self.thread is None or not self.thread.is_alive():
                import time, random
                self.next_run_time = time.time() + random.randint(8700, 9000)
                self.running = True
                self.thread = threading.Thread(target=self._loop, daemon=True)
                self.thread.start()
                
        def stop(self):
            self.running = False
            self.thread = None
            
        def reset_timer(self):
            if self.running:
                sleep_time = random.randint(8700, 9000)
                self.next_run_time = time.time() + sleep_time
            
    return IboosterAutoPuller()

ibooster_auto_puller = get_ibooster_auto_puller()

@st.cache_resource
def get_insera_auto_puller():
    import threading
    import random
    import time
    import subprocess
    import sys
    import os
    
    class InseraAutoPuller:
        def __init__(self):
            self.running = False
            self.thread = None
            self.next_run_time = None
            
        def _loop(self):
            while self.running:
                # Durasi penarikan sama seperti WFM & ADING (1200-1260 detik / ~20-21 menit)
                sleep_time = random.randint(870, 900)
                self.next_run_time = time.time() + sleep_time
                
                while self.running and self.next_run_time and time.time() < self.next_run_time:
                    time.sleep(1)
                    
                if not self.running:
                    self.next_run_time = None
                    return
                    
                # Menjalankan penarikan data INSERA ASR secara otomatis
                try:
                    py_exec = sys.executable or "python"
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    script_path = os.path.join(base_dir, "main_assurance.py")
                    subprocess.run([py_exec, script_path, "DASHBOARD", "Admin Web", "Otomatis"], cwd=base_dir, capture_output=True, text=True)
                except Exception:
                    pass
                    
        def start(self):
            if not self.running:
                import time, random
                self.next_run_time = time.time() + random.randint(870, 900)
                self.running = True
                self.thread = threading.Thread(target=self._loop, daemon=True)
                self.thread.start()
                
        def stop(self):
            self.running = False
            self.thread = None
            
        def reset_timer(self):
            if self.running:
                sleep_time = random.randint(870, 900)
                self.next_run_time = time.time() + sleep_time
            
    return InseraAutoPuller()

insera_auto_puller = get_insera_auto_puller()

@st.cache_resource
def get_ibooster_asgar_auto_puller():
    import threading
    import random
    import time
    import subprocess
    import sys
    import os
    
    class IboosterAsgarAutoPuller:
        def __init__(self):
            self.running = False
            self.thread = None
            self.next_run_time = None
            
        def _loop(self):
            while self.running:
                # Interval 2.5 jam (8700 - 9000 detik)
                sleep_time = random.randint(8700, 9000)
                self.next_run_time = time.time() + sleep_time
                
                while self.running and self.next_run_time and time.time() < self.next_run_time:
                    time.sleep(1)
                    
                if not self.running:
                    self.next_run_time = None
                    return
                    
                try:
                    py_exec = sys.executable or "python"
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    script_path = os.path.join(base_dir, "main.py")
                    subprocess.run([py_exec, script_path, "DASHBOARD", "Admin Web", "IBOOSTER_ASR", "Otomatis"], cwd=base_dir, capture_output=True, text=True, timeout=3600)
                except Exception:
                    pass
                    
        def start(self):
            if not self.running or self.thread is None or not self.thread.is_alive():
                import time, random
                self.next_run_time = time.time() + random.randint(8700, 9000)
                self.running = True
                self.thread = threading.Thread(target=self._loop, daemon=True)
                self.thread.start()
                
        def stop(self):
            self.running = False
            self.thread = None
            
        def reset_timer(self):
            if self.running:
                sleep_time = random.randint(8700, 9000)
                self.next_run_time = time.time() + sleep_time
            
    return IboosterAsgarAutoPuller()

ibooster_asgar_auto_puller = get_ibooster_asgar_auto_puller()


# --- CUSTOM CSS (PREMIUM DARK THEME) ---
st.markdown("""
<style>
    @import url('https://fonts.cdnfonts.com/css/superstar-m54');
    .stApp { background-color: #0b1121 !important; color: #f8fafc !important; }
    
    /* Enforce Consistent Dark Theme on Sidebar */
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
        background-color: #0e1626 !important;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
        color: #f8fafc !important;
    }
    
    /* Global Container Border Override */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 2.5px solid #94a3b8 !important;
        border-radius: 12px !important;
    }
    
    /* Custom Border for Kendala Charts (Innermost Block) */
    div[data-testid="stVerticalBlock"]:has(.custom-border-target):not(:has(div[data-testid="stVerticalBlock"]:has(.custom-border-target))) {
        border: 2.5px solid #94a3b8 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        background-color: #0f172a !important;
    }
    
    /* Top Header Styling */
    .header-container { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 15px; margin-bottom: 20px; }
    .header-left { display: flex; flex-direction: column; }
    .dash-title { font-size: 1.8rem; font-weight: 800; color: #f8fafc; margin: 0; letter-spacing: 1px; text-transform: uppercase; }
    .dash-subtitle { font-size: 0.9rem; color: #94a3b8; margin: 0; }
    .header-right { display: flex; align-items: center; gap: 20px; }
    .update-time { font-size: 1.05rem; color: #94a3b8; text-align: right; line-height: 1.2; }
    .export-btn { background-color: #1e293b; border: 1px solid #334155; padding: 8px 16px; border-radius: 6px; color: white; font-size: 0.9rem; display: flex; align-items: center; gap: 8px; cursor: pointer; }
    
    /* Sync Status Badge & Modal Styling */
    @keyframes syncPulse {
        0% { transform: scale(0.95); opacity: 0.8; }
        50% { transform: scale(1.2); opacity: 1; box-shadow: 0 0 10px #10b981; }
        100% { transform: scale(0.95); opacity: 0.8; }
    }
    .sync-pulse-dot {
        animation: syncPulse 2s infinite ease-in-out;
    }
    .sync-status-pill:hover {
        transform: translateY(-2px);
        border-color: #facc15 !important;
        box-shadow: 0 6px 20px rgba(234, 179, 8, 0.45) !important;
    }
    #btn-close-sync-modal:hover, #btn-close-sync-modal-bottom:hover {
        background: rgba(239, 68, 68, 0.2) !important;
        border-color: #ef4444 !important;
        color: #fca5a5 !important;
    }

    /* 6 Grid Cards (Changed to 4 columns) */
    .grid-6 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-bottom: 20px; }
    .d-card { background-color: #0f172a; border-radius: 10px; padding: 15px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3); border: 2.5px solid #334155; }
    .c-blue { border-top: 4px solid #3b82f6; }
    .c-green { border-top: 4px solid #10b981; }
    .c-purple { border-top: 4px solid #8b5cf6; }
    .c-indigo { border-top: 4px solid #6366f1; }
    .c-cyan { border-top: 4px solid #06b6d4; }
    .c-slate { border-top: 4px solid #94a3b8; }
    .c-orange { border-top: 4px solid #f59e0b; }
    .c-teal { border-top: 4px solid #0d9488; }
    
    .dc-header { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 15px; }
    .dc-header-left { display: flex; align-items: center; gap: 12px; }
    .dc-icon { width: 42px; height: 42px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }
    .ic-blue { background-color: rgba(59,130,246,0.2); color: #3b82f6; }
    .ic-green { background-color: rgba(16,185,129,0.2); color: #10b981; }
    .ic-purple { background-color: rgba(139,92,246,0.15); color: #8b5cf6; }
    .ic-indigo { background-color: rgba(99,102,241,0.15); color: #6366f1; }
    .ic-cyan { background-color: rgba(6,182,212,0.15); color: #06b6d4; }
    .ic-slate { background-color: rgba(148,163,184,0.15); color: #94a3b8; }
    .ic-orange { background-color: rgba(245,158,11,0.2); color: #f59e0b; }
    .ic-teal { background-color: rgba(13,148,136,0.2); color: #0d9488; }
    
    .dc-title { font-size: 1.3rem; font-weight: 700; color: white; text-transform: uppercase; margin: 0; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5); }
    
    /* Custom Toggle Switch (ON/OFF) */
    [data-testid="stSidebar"] [data-testid="stCheckbox"] label > div:nth-child(2) {
        background-color: #ef4444 !important; /* Red for OFF */
        width: 60px !important;
        height: 30px !important;
        border-radius: 15px !important;
        position: relative;
        transition: background-color 0.2s ease;
        display: flex !important;
        align-items: center !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stCheckbox"] label:not([data-selected="true"]) > div:nth-child(2)::after {
        content: "OFF";
        position: absolute;
        right: 10px;
        top: 50%;
        transform: translateY(-50%);
        color: white;
        font-size: 13px;
        font-weight: 900;
        z-index: 0;
    }
    
    [data-testid="stSidebar"] [data-testid="stCheckbox"] label[data-selected="true"] > div:nth-child(2) {
        background-color: #10b981 !important; /* Green for ON */
    }
    
    [data-testid="stSidebar"] [data-testid="stCheckbox"] label[data-selected="true"] > div:nth-child(2)::after {
        content: "ON";
        position: absolute;
        left: 10px;
        right: auto;
        top: 50%;
        transform: translateY(-50%);
        color: white;
        font-size: 13px;
        font-weight: 900;
        z-index: 0;
    }
    
    [data-testid="stSidebar"] [data-testid="stCheckbox"] label > div:nth-child(2) > div {
        z-index: 1;
        position: absolute !important;
        left: 3px !important;
        top: 3px !important;
        height: 24px !important;
        width: 24px !important;
        border-radius: 50% !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.5) !important;
        transition: transform 0.2s ease !important;
        background-color: white !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stCheckbox"] label[data-selected="true"] > div:nth-child(2) > div {
        transform: translateX(30px) !important;
    }

    /* Custom Pivot */
    .dc-value { font-size: 2.7rem; font-weight: 800; color: white; line-height: 1; text-align: right; margin-top: 2px; }
    
    .dc-breakdown { font-size: 1.05rem; color: #94a3b8; margin-top: 10px; }
    .dc-row { display: grid; grid-template-columns: 4.8rem 15px 1fr; align-items: center; margin-bottom: 5px; }
    .dc-row-val { font-weight: bold; color: white; text-align: right; }
    .dc-row > span:first-child { color: white; font-weight: bold; text-align: left; }
    .dc-row > span:nth-child(2) { text-align: center; }
    .dc-row > span:last-child, .dc-row > div:last-child { text-align: right; }
    .dc-row-manja { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; text-align: center; margin-bottom: 5px; font-weight: bold; }
    .dc-row-manja span:first-child { text-align: left; color: white; }
    .dc-row-kendala { display: grid; grid-template-columns: 2fr 1.5fr 1.5fr; text-align: center; margin-bottom: 5px; font-weight: bold; }
    .dc-row-kendala span:first-child { text-align: left; color: white; }
    
    .header-badge-text { font-size: 0.95rem; font-weight: 800; text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5); }

    /* Section Titles */
    .section-title-wrap { display: flex; align-items: center; justify-content: space-between; margin-bottom: 15px; border-bottom: 1px solid #1e293b; padding-bottom: 8px; }
    .section-title { font-size: 1rem; font-weight: bold; color: #e2e8f0; text-transform: uppercase; display: flex; align-items: center; gap: 8px; }
    
    /* Table Styling overrides */
    div[data-testid="stDataFrame"] { border: 1px solid #1e293b; border-radius: 8px; overflow: hidden; }
    
    /* Custom Pivot */
    .cp-container { background-color: #0f172a; border-radius: 8px; border: 1px solid #1e293b; overflow-y: auto; overflow-x: hidden; max-height: 800px; }
    .cp-header { display: grid; grid-template-columns: 2fr 3fr 1fr 1fr 1fr 1fr 1fr; background-color: #172554; font-size: 1.05rem; font-weight: 700; color: white; text-transform: uppercase; border-bottom: 2px solid #3b82f6; text-align: center; position: sticky; top: 0; z-index: 10; }
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
    .cp-grand { background-color: #172554; display: grid; grid-template-columns: 5fr 1fr 1fr 1fr 1fr 1fr; text-align: center; font-weight: bold; color: white; font-size: 1.05rem; border-top: 2px solid #3b82f6; position: sticky; bottom: 0; z-index: 10; }
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
    .widget-subtitle { color: #3b82f6; font-size: 14px; font-weight: bold; margin-bottom: 15px; text-transform: uppercase; }
    
    .hm-table { width: 100%; border-collapse: collapse; font-size: 0.8rem; text-align: center; }
    .hm-table th, .hm-table td { border: 1px solid #1e293b; padding: 8px; }
    .hm-table th { background-color: #0f172a; color: #cbd5e1; font-weight: bold; font-size: 14px; }
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

ASSURANCE_SHEET_ID = "1bUXmomLo6DJYdk0CHGW9KCnoRgG8EqsUdOtALJ0_r7o"
ASSURANCE_SHEET_NAME = "GABUNGAN ALL & CLOSE TIKET"

@st.cache_data(ttl=60)
def load_assurance_data(sync_time_val):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Prioritaskan baca cache Parquet lokal super cepat (0.01 detik)
    try:
        parquet_cache = os.path.join(base_dir, "last_insera_gabungan.parquet")
        if os.path.exists(parquet_cache) and os.path.getsize(parquet_cache) > 1000:
            df_pq = pd.read_parquet(parquet_cache)
            if not df_pq.empty:
                # Merge ADING Teknisi jika belum ada di parquet
                if 'NAMA TEKNISI' not in df_pq.columns:
                    try:
                        ading_p = os.path.join(base_dir, "last_ading_assr.parquet")
                        if os.path.exists(ading_p):
                            df_ad = pd.read_parquet(ading_p)
                            if 'NO TIKET' in df_ad.columns and 'NAMA TIM' in df_ad.columns:
                                ad_map = {}
                                for _, r_ad in df_ad.iterrows():
                                    t_no = str(r_ad.get('NO TIKET', '')).strip()
                                    t_nm = str(r_ad.get('NAMA TIM', '')).strip()
                                    if t_no and t_nm and t_no != 'nan':
                                        clean_nm = t_nm.split('/')[0].strip().upper() if '/' in t_nm else t_nm.strip().upper()
                                        ad_map[t_no] = clean_nm
                                df_pq['NAMA TEKNISI'] = df_pq['INCIDENT'].map(ad_map).fillna('-')
                    except Exception:
                        pass
                return df_pq, "LOCAL_CACHE"
    except Exception:
        pass

    # 2. Coba baca dari Google Sheets (hanya jika cache parquet belum ada, misal di Streamlit Cloud)
    try:
        import urllib.parse
        import urllib.request
        import io
        import time as time_lib
        encoded_name = urllib.parse.quote(ASSURANCE_SHEET_NAME)
        cb = int(time_lib.time() // 60)
        url = f"https://docs.google.com/spreadsheets/d/{ASSURANCE_SHEET_ID}/gviz/tq?tqx=out:csv&sheet={encoded_name}&_cb={cb}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            content = resp.read().decode('utf-8')
            df_sheet = pd.read_csv(io.StringIO(content)) if (content and not content.strip().startswith("<!DOCTYPE")) else pd.DataFrame()
        if not df_sheet.empty and len(df_sheet.columns) > 5:
            cloud_insera_sync = None
            for inc_col in ['INCIDENT', 'incident', 'ID TICKET', 'TICKET ID', 'NO TIKET']:
                if inc_col in df_sheet.columns:
                    meta = df_sheet[df_sheet[inc_col] == 'METADATA_SYNC']
                    if not meta.empty:
                        for sum_col in ['SUMMARY', 'summary', 'DESCRIPTION']:
                            if sum_col in meta.columns:
                                cloud_insera_sync = str(meta.iloc[0][sum_col])
                                break
                    df_sheet = df_sheet[df_sheet[inc_col] != 'METADATA_SYNC']
                    break
            if cloud_insera_sync:
                try:
                    st.session_state['cloud_insera_sync'] = cloud_insera_sync
                except Exception:
                    pass
                return df_sheet, cloud_insera_sync
            return df_sheet, "GOOGLE_SHEETS"
    except Exception:
        pass
        
    # 3. Fallback: Baca dari file unduhan excel terbaru di folder downloads
    try:
        import glob
        dl_dir = os.path.join(base_dir, "downloads")
        all_files = sorted(glob.glob(os.path.join(dl_dir, "insera_all_ticket_*.xlsx")), reverse=True)
        closed_files = sorted(glob.glob(os.path.join(dl_dir, "insera_closed_ticket_*.xlsx")), reverse=True)
        if all_files or closed_files:
            df_a = pd.read_excel(all_files[0]) if all_files else pd.DataFrame()
            df_c = pd.read_excel(closed_files[0]) if closed_files else pd.DataFrame()
            df_m = pd.concat([df_a, df_c], ignore_index=True)
            return df_m, "LOCAL_EXCEL"
    except Exception:
        pass
        
    return pd.DataFrame(), None

@st.cache_data(ttl=60)
def load_proactive_data(sync_time_val):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Coba baca dari Google Sheets tab 'PROACTIVE TICKET' (membawa kolom rumus ARRAYFORMULA)
    try:
        import urllib.parse, urllib.request, io
        import time as time_lib
        encoded_name = urllib.parse.quote("PROACTIVE TICKET")
        cb = int(time_lib.time() // 60)
        url = f"https://docs.google.com/spreadsheets/d/{ASSURANCE_SHEET_ID}/gviz/tq?tqx=out:csv&sheet={encoded_name}&_cb={cb}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=4) as resp:
            content = resp.read().decode('utf-8')
            df_sheet = pd.read_csv(io.StringIO(content)) if (content and not content.strip().startswith("<!DOCTYPE")) else pd.DataFrame()
        if not df_sheet.empty and len(df_sheet.columns) > 5:
            try:
                pq_cache = os.path.join(base_dir, "last_insera_proactive.parquet")
                df_sheet.astype(str).to_parquet(pq_cache, index=False)
            except Exception:
                pass
            return df_sheet, "GOOGLE_SHEETS"
    except Exception:
        pass

    # 2. Prioritaskan baca cache Parquet lokal jika ada
    try:
        pq_cache = os.path.join(base_dir, "last_insera_proactive.parquet")
        if os.path.exists(pq_cache) and os.path.getsize(pq_cache) > 1000:
            df_pq = pd.read_parquet(pq_cache)
            if not df_pq.empty:
                return df_pq, "LOCAL_CACHE"
    except Exception:
        pass

    # 3. Fallback: Baca dari file unduhan excel terbaru di folder downloads
    try:
        import glob
        dl_dir = os.path.join(base_dir, "downloads")
        pro_files = sorted(glob.glob(os.path.join(dl_dir, "insera_proactive_ticket_*.xlsx")), reverse=True)
        if pro_files:
            df_excel = pd.read_excel(pro_files[0])
            return df_excel, "LOCAL_EXCEL"
    except Exception:
        pass

    return pd.DataFrame(), None

@st.cache_data(ttl=600)
def load_data(sync_time_val):
    try:
        df = pd.read_csv(CSV_URL)
        if 'Workorder' not in df.columns:
            err_detail = ""
            for col in df.columns:
                if any(k in str(col).lower() for k in ['message', '429', 'export']):
                    err_detail = str(col)
                    break
            if err_detail:
                raise ValueError(f"Respon Google Sheets: {err_detail}")
            else:
                raise ValueError("Kolom 'Workorder' tidak ditemukan pada sumber data.")

        cloud_sync = None
        if 'Workorder' in df.columns and 'Description' in df.columns:
            meta = df[df['Workorder'] == 'METADATA_SYNC']
            if not meta.empty:
                cloud_sync = str(meta.iloc[0]['Description'])
                df = df[df['Workorder'] != 'METADATA_SYNC']
        return df, cloud_sync
    except Exception as e:
        try:
            dl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")
            if os.path.exists(dl_dir):
                wfm_files = [os.path.join(dl_dir, f) for f in os.listdir(dl_dir) if f.startswith("wfm_data_") and f.endswith(".xlsx")]
                if wfm_files:
                    latest_wfm = max(wfm_files, key=os.path.getmtime)
                    df_fb = pd.read_excel(latest_wfm)
                    if 'Workorder' in df_fb.columns:
                        return df_fb, None
        except Exception:
            pass
        st.error(f"⚠️ Gagal memuat data dari Google Sheet: {e}")
        return pd.DataFrame(), None

# Read last_sync.txt to get the actual last pulled time and source
import os
sync_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "last_sync.txt")
last_sync_time = "Belum Ada Data"
sync_source = "VIA DASHBOARD"

if os.path.exists(sync_file):
    try:
        with open(sync_file, "r") as f:
            content = f.read().strip()
            parts = content.split(" | VIA ")
            if len(parts) == 2:
                last_sync_time = parts[0].replace(" WIB", "")
                sync_source = "VIA " + parts[1]
            else:
                last_sync_time = content.replace(" WIB", "")
    except:
        pass
else:
    last_sync_time = "Belum Ada Data"

with st.spinner("Membaca data dari satelit..."):
    df, cloud_sync = load_data(last_sync_time)
    
if last_sync_time == "Belum Ada Data" and cloud_sync:
    parts = cloud_sync.split(" | VIA ")
    if len(parts) == 2:
        last_sync_time = parts[0].replace(" WIB", "")
        sync_source = "VIA " + parts[1]
    else:
        last_sync_time = cloud_sync.replace(" WIB", "")

# 2. Segmentasi Penarikan IBOOSTER FFG (Target AO TSEL & INDIBIZ)
base_dir = os.path.dirname(os.path.abspath(__file__))
ibooster_ao_file = os.path.join(base_dir, "last_ibooster_AO_TSEL.txt")
ibooster_ind_file = os.path.join(base_dir, "last_ibooster_INDIBIZ.txt")
ibooster_ao_time = "Belum Ada Data"
ibooster_ao_source = "VIA DASHBOARD"
ibooster_ind_time = "Belum Ada Data"
ibooster_ind_source = "VIA DASHBOARD"

if os.path.exists(ibooster_ao_file):
    try:
        with open(ibooster_ao_file, "r") as f:
            c = f.read().strip().replace(" WIB", "")
            p = c.split(" | VIA ")
            ibooster_ao_time = p[0]
            if len(p) > 1: ibooster_ao_source = "VIA " + p[1]
    except:
        pass

if os.path.exists(ibooster_ind_file):
    try:
        with open(ibooster_ind_file, "r") as f:
            c = f.read().strip().replace(" WIB", "")
            p = c.split(" | VIA ")
            ibooster_ind_time = p[0]
            if len(p) > 1: ibooster_ind_source = "VIA " + p[1]
    except:
        pass

# 3. Segmentasi Penarikan INSERA ASR (Assurance Incident)
import json
insera_file = os.path.join(base_dir, "last_insera_sync.txt")
insera_summary_file = os.path.join(base_dir, "last_insera_summary.json")
insera_time = "Belum Ada Data"
insera_source = "VIA DASHBOARD"
insera_all_cnt = 2716
insera_closed_cnt = 591
insera_proactive_cnt = 0
insera_total_cnt = 3307
insera_ading_cnt = 0

if os.path.exists(insera_file):
    try:
        with open(insera_file, "r") as f:
            c = f.read().strip().replace(" WIB", "")
            p = c.split(" | VIA ")
            insera_time = p[0]
            if len(p) > 1: insera_source = "VIA " + p[1]
    except:
        pass

if os.path.exists(insera_summary_file):
    try:
        with open(insera_summary_file, "r", encoding="utf-8") as f:
            js = json.load(f)
            insera_all_cnt = js.get("all_count", insera_all_cnt)
            insera_closed_cnt = js.get("closed_count", insera_closed_cnt)
            insera_proactive_cnt = js.get("proactive_count", 0)
            insera_ading_cnt = js.get("ading_count", 0)
            insera_total_cnt = js.get("total_count", insera_total_cnt)
            if (insera_time == "Belum Ada Data" or not insera_time) and "last_sync" in js:
                insera_time = js["last_sync"]
                insera_source = js.get("source", "VIA DASHBOARD")
    except:
        pass

# Fallback cerdas: Cek jika file parquet lokal memiliki waktu yang lebih baru dari file sync
parquet_cache_file = os.path.join(base_dir, "last_insera_gabungan.parquet")
if os.path.exists(parquet_cache_file):
    try:
        pq_mtime = os.path.getmtime(parquet_cache_file)
        pq_dt = datetime.fromtimestamp(pq_mtime)
        is_newer = False
        if insera_time != "Belum Ada Data":
            try:
                curr_dt = datetime.strptime(insera_time, "%d %b %Y | %H:%M:%S")
                if pq_dt > curr_dt + timedelta(seconds=30):
                    is_newer = True
            except Exception:
                pass
        else:
            is_newer = True
            
        if is_newer:
            insera_time = pq_dt.strftime("%d %b %Y | %H:%M:%S")
    except Exception:
        pass

ading_cache_file = os.path.join(base_dir, "last_ading_assr.parquet")
if os.path.exists(ading_cache_file) and insera_ading_cnt == 0:
    try:
        df_ad_pq = pd.read_parquet(ading_cache_file)
        insera_ading_cnt = len(df_ad_pq)
    except Exception:
        pass

if st.session_state.get('cloud_insera_sync') and not os.path.exists(os.path.join(base_dir, "last_insera_gabungan.parquet")):
    p = str(st.session_state['cloud_insera_sync']).split(" | VIA ")
    insera_time = p[0].replace(" WIB", "")
    if len(p) > 1:
        insera_source = "VIA " + p[1]

if insera_time == "Belum Ada Data":
    try:
        df_asr_probe, asr_probe_src = load_assurance_data("probe")
        if not df_asr_probe.empty:
            insera_total_cnt = len(df_asr_probe)
            if asr_probe_src and " | VIA " in str(asr_probe_src):
                p = str(asr_probe_src).split(" | VIA ")
                insera_time = p[0].replace(" WIB", "")
                if len(p) > 1:
                    insera_source = "VIA " + p[1]
            else:
                insera_source = "GOOGLE SHEETS LIVE" if asr_probe_src == "GOOGLE_SHEETS" else "CACHE"
                for col_chk in ['REPORTED DATE', 'REPORTED_DATE', 'STATUS DATE']:
                    if col_chk in df_asr_probe.columns:
                        valid_dates = pd.to_datetime(df_asr_probe[col_chk], errors='coerce').dropna()
                        if not valid_dates.empty:
                            insera_time = valid_dates.max().strftime("%d %b %Y | %H:%M:%S")
                            break
            if insera_time == "Belum Ada Data":
                insera_time = "LIVE SATELLITE"
    except Exception:
        pass

# Helper ekstraksi jam ringkas (lengkap dengan detik HH:MM:SS) untuk pill di navbar
def extract_time_short(t_str):
    if not t_str or "Belum Ada" in t_str: return "-"
    clean = t_str.replace("WIB", "").strip()
    if "|" in clean:
        clean = clean.split("|")[-1].strip()
    parts = clean.split(":")
    if len(parts) >= 3:
        sec = parts[2].strip().split()[0]
        return f"{parts[0].strip()}:{parts[1].strip()}:{sec}"
    elif len(parts) == 2:
        sec = parts[1].strip().split()[0]
        return f"{parts[0].strip()}:{sec}:00"
    return clean

# 4. Segmentasi Penarikan IBOOSTER ASGAR (Assurance Gangguan Ulang)
ibooster_asgar_file = os.path.join(base_dir, "last_ibooster_ASR.txt")
ibooster_asgar_parquet = os.path.join(base_dir, "last_ibooster_asr.parquet")
ibooster_asgar_time = "Belum Ada Data"
ibooster_asgar_source = "VIA DASHBOARD"
ibooster_asgar_cnt = 0

if os.path.exists(ibooster_asgar_file):
    try:
        with open(ibooster_asgar_file, "r", encoding="utf-8") as f:
            c = f.read().strip().replace(" WIB", "")
            p = c.split(" | VIA ")
            ibooster_asgar_time = p[0]
            if len(p) > 1: ibooster_asgar_source = "VIA " + p[1]
    except Exception:
        pass

if os.path.exists(ibooster_asgar_parquet):
    try:
        df_ib_p = pd.read_parquet(ibooster_asgar_parquet)
        ibooster_asgar_cnt = len(df_ib_p)
        if ibooster_asgar_time == "Belum Ada Data":
            pq_mtime = os.path.getmtime(ibooster_asgar_parquet)
            ibooster_asgar_time = datetime.fromtimestamp(pq_mtime).strftime("%d %b %Y | %H:%M:%S")
    except Exception:
        pass

wfm_short_time = extract_time_short(last_sync_time)
ibooster_short_time = extract_time_short(ibooster_ao_time)
insera_short_time = extract_time_short(insera_time)
ibooster_asgar_short_time = extract_time_short(ibooster_asgar_time)

# Hitung rincian order WFM dari df
wfm_order_col = None
if not df.empty:
    for c in ['CECK BY ORDER', 'CEK INDIBIZ', 'PRODUCT TYPE', 'ORDER']:
        if c in df.columns:
            wfm_order_col = c
            break

wfm_ao_cnt = 0
wfm_pda_cnt = 0
wfm_ind_cnt = 0
wfm_vula_cnt = 0
wfm_total_cnt = len(df) if not df.empty else 0

if not df.empty and wfm_order_col:
    counts_wfm = df[wfm_order_col].astype(str).str.upper().value_counts()
    wfm_ao_cnt = counts_wfm.get('AO TSEL', 0) + counts_wfm.get('AO', 0)
    wfm_pda_cnt = counts_wfm.get('PDA TSEL', 0) + counts_wfm.get('PDA', 0)
    wfm_ind_cnt = counts_wfm.get('INDIBIZ', 0)
    wfm_vula_cnt = counts_wfm.get('ISP VULA', 0)

# --- HEADER BERSAMA & POP-UP SINKRONISASI 4 SEGMENTASI DATA ---
sync_header_html = f'''
<div class="header-container">
    <div class="header-left">
        <h1 class="dash-title">SERVICE AREA ULIN</h1>
        <p class="dash-subtitle" style="display: flex; align-items: center; font-size: 1.45rem; letter-spacing: 1px; margin-top: -8px;">OPERATION DASHBOARD &ndash;&nbsp;<span style="font-family: 'Superstar M54', sans-serif; color: #dc2626; font-size: 1.5rem; letter-spacing: 2px; text-transform: uppercase; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); padding-top: 2px;">YOU'LL NEVER WALK ALONE</span></p>
    </div>
    <div class="header-right">
        
        <!-- PILL SINKRONISASI 4 DATA (MEMANJANG & INTERAKTIF) -->
        <div id="btn-open-sync-modal" class="sync-status-pill" title="Klik untuk membuka rincian lengkap 4 segmentasi data penarikan" style="position: fixed; top: 12px; right: 140px; z-index: 999990; border: 1.5px solid #eab308; border-radius: 24px; padding: 5px 13px; display: flex; align-items: center; gap: 10px; background: rgba(15, 23, 42, 0.95); backdrop-filter: blur(10px); box-shadow: 0 4px 15px rgba(234, 179, 8, 0.25); cursor: pointer; transition: all 0.2s ease; white-space: nowrap;">
            
            <!-- Live Pulse Status -->
            <div style="display: flex; align-items: center; gap: 6px;">
                <span class="sync-pulse-dot" style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background-color: #10b981; box-shadow: 0 0 8px #10b981;"></span>
                <span style="color: #fbbf24; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.5px;">SYNC:</span>
            </div>
            
            <!-- 1. WFM & ADING -->
            <div style="display: flex; align-items: center; gap: 5px; border-left: 1px solid rgba(255,255,255,0.15); padding-left: 9px;" title="WFM &amp; ADING: {last_sync_time} ({sync_source})">
                <span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background-color: #38bdf8;"></span>
                <span style="font-size: 0.74rem; color: #94a3b8; font-weight: 600;">WFM &amp; ADING :</span>
                <span style="font-size: 0.78rem; color: #f8fafc; font-weight: bold;">{wfm_short_time}</span>
            </div>

            <!-- 2. IBOOSTER FFG -->
            <div style="display: flex; align-items: center; gap: 5px; border-left: 1px solid rgba(255,255,255,0.15); padding-left: 9px;" title="IBOOSTER FFG: AO ({ibooster_ao_time}) | INDIBIZ ({ibooster_ind_time})">
                <span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background-color: #c084fc;"></span>
                <span style="font-size: 0.74rem; color: #94a3b8; font-weight: 600;">IBOOSTER FFG :</span>
                <span style="font-size: 0.78rem; color: #f8fafc; font-weight: bold;">{ibooster_short_time}</span>
            </div>

            <!-- 3. INSERA ASR -->
            <div style="display: flex; align-items: center; gap: 5px; border-left: 1px solid rgba(255,255,255,0.15); padding-left: 9px;" title="INSERA ASR: {insera_time} ({insera_source})">
                <span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background-color: #34d399;"></span>
                <span style="font-size: 0.74rem; color: #94a3b8; font-weight: 600;">INSERA ASR :</span>
                <span style="font-size: 0.78rem; color: #f8fafc; font-weight: bold;">{insera_short_time}</span>
            </div>

            <!-- 4. IBOOSTER ASGAR -->
            <div style="display: flex; align-items: center; gap: 5px; border-left: 1px solid rgba(255,255,255,0.15); padding-left: 9px;" title="IBOOSTER ASGAR: {ibooster_asgar_time} ({ibooster_asgar_source})">
                <span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background-color: #f59e0b;"></span>
                <span style="font-size: 0.74rem; color: #94a3b8; font-weight: 600;">IBOOSTER ASGAR :</span>
                <span style="font-size: 0.78rem; color: #f8fafc; font-weight: bold;">{ibooster_asgar_short_time}</span>
            </div>

            <!-- Badge Buka Pop-up -->
            <div style="background: rgba(234, 179, 8, 0.2); border: 1px solid rgba(234, 179, 8, 0.5); color: #fef08a; font-size: 0.68rem; padding: 2px 8px; border-radius: 12px; font-weight: bold; display: flex; align-items: center; gap: 4px; margin-left: 2px;">
                <span>Detail</span>
                <span style="font-size: 0.65rem;">▼</span>
            </div>
        </div>

        <div class="update-time" id="live-clock-inline" style="color: #60a5fa; font-weight: bold; font-size: 1.1rem; text-align: right;">Memuat waktu...</div>
        <div class="export-btn">📥 Export ▾</div>
    </div>
</div>

<!-- POP-UP MODAL DETAIL 4 SEGMENTASI DATA PENARIKAN (MEMANJANG) -->
<div id="modal-sync-summary" class="sync-summary-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0, 0, 0, 0.75); backdrop-filter: blur(6px); z-index: 9999999; justify-content: center; align-items: center;">
    <div style="background: #0f172a; width: 96%; max-width: 1280px; max-height: 88vh; border: 2px solid #eab308; border-radius: 16px; box-shadow: 0 25px 60px -15px rgba(0,0,0,0.9), 0 0 25px rgba(234, 179, 8, 0.3); display: flex; flex-direction: column; overflow: hidden;">
        
        <!-- Header Pop-Up -->
        <div style="padding: 16px 24px; background: linear-gradient(90deg, #1e293b, #0f172a); border-bottom: 1px solid #334155; display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="background: rgba(234, 179, 8, 0.2); border: 1px solid #eab308; width: 38px; height: 38px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem;">
                    🔄
                </div>
                <div>
                    <h2 style="margin: 0; color: #f8fafc; font-size: 1.22rem; font-weight: 800; letter-spacing: 0.5px; text-transform: uppercase;">
                        DETAIL 4 SEGMENTASI DATA PENARIKAN OPERASIONAL
                    </h2>
                    <p style="margin: 2px 0 0 0; color: #94a3b8; font-size: 0.8rem;">
                        Status &amp; Rincian Lengkap Penarikan: <b>WFM &amp; ADING</b> &bull; <b>IBOOSTER FFG</b> &bull; <b>INSERA ASR</b> &bull; <b>IBOOSTER ASGAR</b>
                    </p>
                </div>
            </div>
            <button id="btn-close-sync-modal" style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); color: #cbd5e1; font-size: 1.6rem; cursor: pointer; border-radius: 8px; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; line-height: 1; transition: all 0.2s;">&times;</button>
        </div>

        <!-- Body Pop-Up (4 Kolom Memanjang Side-by-Side) -->
        <div style="padding: 20px 24px; overflow-y: auto; flex: 1;">
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;">
                
                <!-- KOLOM 1: WFM & ADING -->
                <div style="background: rgba(30, 41, 59, 0.6); border: 1.5px solid #0284c7; border-top: 4px solid #38bdf8; border-radius: 12px; padding: 15px; display: flex; flex-direction: column; gap: 12px;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px;">
                        <div>
                            <div style="color: #38bdf8; font-size: 0.72rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">SEGMENTASI 1: FULFILLMENT</div>
                            <div style="color: #ffffff; font-size: 1.05rem; font-weight: bold; margin-top: 2px;">WFM &amp; ADING</div>
                        </div>
                        <span style="background: #0284c7; color: white; font-size: 0.68rem; padding: 3px 8px; border-radius: 10px; font-weight: bold;">AKTIF</span>
                    </div>

                    <!-- Waktu & Info -->
                    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 10px; font-size: 0.8rem;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="color: #94a3b8;">Terakhir Sinkron:</span>
                            <span style="color: #f8fafc; font-weight: bold;">{last_sync_time}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="color: #94a3b8;">Metode:</span>
                            <span style="color: #38bdf8; font-weight: 600;">{sync_source}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #94a3b8;">Total Terpantau:</span>
                            <span style="color: #fbbf24; font-weight: bold;">{wfm_total_cnt} Workorder</span>
                        </div>
                    </div>

                    <!-- Detail Segmentasi Produk -->
                    <div>
                        <div style="color: #cbd5e1; font-size: 0.78rem; font-weight: bold; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">
                            📌 Segmentasi Order &amp; WO:
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 6px;">
                            <!-- AO TSEL -->
                            <div style="background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 7px 10px; display: flex; justify-content: space-between; align-items: center;">
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <span style="width: 8px; height: 8px; border-radius: 2px; background: #be123c;"></span>
                                    <span style="color: #f1f5f9; font-weight: 600; font-size: 0.82rem;">AO TSEL</span>
                                </div>
                                <span style="color: #f8fafc; font-weight: bold; font-size: 0.85rem;">{wfm_ao_cnt} <span style="font-size: 0.72rem; color: #94a3b8; font-weight: normal;">WO</span></span>
                            </div>
                            <!-- PDA TSEL -->
                            <div style="background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 7px 10px; display: flex; justify-content: space-between; align-items: center;">
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <span style="width: 8px; height: 8px; border-radius: 2px; background: #166534;"></span>
                                    <span style="color: #f1f5f9; font-weight: 600; font-size: 0.82rem;">PDA TSEL</span>
                                </div>
                                <span style="color: #f8fafc; font-weight: bold; font-size: 0.85rem;">{wfm_pda_cnt} <span style="font-size: 0.72rem; color: #94a3b8; font-weight: normal;">WO</span></span>
                            </div>
                            <!-- INDIBIZ -->
                            <div style="background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 7px 10px; display: flex; justify-content: space-between; align-items: center;">
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <span style="width: 8px; height: 8px; border-radius: 2px; background: #1d4ed8;"></span>
                                    <span style="color: #f1f5f9; font-weight: 600; font-size: 0.82rem;">INDIBIZ</span>
                                </div>
                                <span style="color: #f8fafc; font-weight: bold; font-size: 0.85rem;">{wfm_ind_cnt} <span style="font-size: 0.72rem; color: #94a3b8; font-weight: normal;">WO</span></span>
                            </div>
                            <!-- ISP VULA -->
                            <div style="background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 7px 10px; display: flex; justify-content: space-between; align-items: center;">
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <span style="width: 8px; height: 8px; border-radius: 2px; background: #d97706;"></span>
                                    <span style="color: #f1f5f9; font-weight: 600; font-size: 0.82rem;">ISP VULA</span>
                                </div>
                                <span style="color: #f8fafc; font-weight: bold; font-size: 0.85rem;">{wfm_vula_cnt} <span style="font-size: 0.72rem; color: #94a3b8; font-weight: normal;">WO</span></span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- KOLOM 2: IBOOSTER FFG -->
                <div style="background: rgba(30, 41, 59, 0.6); border: 1.5px solid #7c3aed; border-top: 4px solid #c084fc; border-radius: 12px; padding: 15px; display: flex; flex-direction: column; gap: 12px;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px;">
                        <div>
                            <div style="color: #c084fc; font-size: 0.72rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">SEGMENTASI 2: QUALITY &amp; SQI</div>
                            <div style="color: #ffffff; font-size: 1.05rem; font-weight: bold; margin-top: 2px;">IBOOSTER FFG</div>
                        </div>
                        <span style="background: #7c3aed; color: white; font-size: 0.68rem; padding: 3px 8px; border-radius: 10px; font-weight: bold;">FFG 60 HARI</span>
                    </div>

                    <!-- Target Segmentasi 1: AO TSEL -->
                    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 10px; font-size: 0.8rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="color: #f472b6; font-weight: bold;">📱 Target AO TSEL</span>
                            <span style="background: rgba(244, 114, 182, 0.15); color: #f472b6; font-size: 0.68rem; padding: 1px 6px; border-radius: 4px;">Validated</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 2px;">
                            <span style="color: #94a3b8;">Terakhir Sinkron:</span>
                            <span style="color: #f8fafc; font-weight: bold;">{ibooster_ao_time}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #94a3b8;">Sumber:</span>
                            <span style="color: #c084fc; font-weight: 600;">{ibooster_ao_source}</span>
                        </div>
                    </div>

                    <!-- Target Segmentasi 2: INDIBIZ -->
                    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 10px; font-size: 0.8rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="color: #60a5fa; font-weight: bold;">🏢 Target INDIBIZ</span>
                            <span style="background: rgba(96, 165, 250, 0.15); color: #60a5fa; font-size: 0.68rem; padding: 1px 6px; border-radius: 4px;">Validated</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 2px;">
                            <span style="color: #94a3b8;">Terakhir Sinkron:</span>
                            <span style="color: #f8fafc; font-weight: bold;">{ibooster_ind_time}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #94a3b8;">Sumber:</span>
                            <span style="color: #c084fc; font-weight: 600;">{ibooster_ind_source}</span>
                        </div>
                    </div>

                    <!-- Info Fitur -->
                    <div style="background: rgba(15, 23, 42, 0.4); border: 1px dashed rgba(255,255,255,0.1); border-radius: 8px; padding: 10px; font-size: 0.75rem; color: #94a3b8; line-height: 1.4;">
                        <div style="color: #cbd5e1; font-weight: 600; margin-bottom: 2px;">🎯 Kegunaan Data:</div>
                        Validasi kualitas sinyal optik / redaman, profil FFG H-60, serta filter status ukur i-Booster di tabel detail ODS.
                    </div>
                </div>

                <!-- KOLOM 3: INSERA ASR -->
                <div style="background: rgba(30, 41, 59, 0.6); border: 1.5px solid #059669; border-top: 4px solid #34d399; border-radius: 12px; padding: 15px; display: flex; flex-direction: column; gap: 12px;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px;">
                        <div>
                            <div style="color: #34d399; font-size: 0.72rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">SEGMENTASI 3: INCIDENT ASSURANCE</div>
                            <div style="color: #ffffff; font-size: 1.05rem; font-weight: bold; margin-top: 2px;">INSERA ASR</div>
                        </div>
                        <span style="background: #059669; color: white; font-size: 0.68rem; padding: 3px 8px; border-radius: 10px; font-weight: bold;">TELKOM ASR</span>
                    </div>

                    <!-- Waktu & Status -->
                    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 10px; font-size: 0.8rem;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="color: #94a3b8;">Terakhir Sinkron:</span>
                            <span style="color: #f8fafc; font-weight: bold;">{insera_time}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="color: #94a3b8;">Metode:</span>
                            <span style="color: #34d399; font-weight: 600;">{insera_source}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #94a3b8;">Spreadsheet:</span>
                            <span style="color: #fef08a; font-weight: 600;">SA ULIN - ASSURANCE</span>
                        </div>
                    </div>

                    <!-- Detail Segmentasi Sheet & Data -->
                    <div>
                        <div style="color: #cbd5e1; font-size: 0.78rem; font-weight: bold; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">
                            📌 Segmentasi Sheet &amp; Tiket:
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 6px;">
                            <!-- ALL TICKET LIST -->
                            <div style="background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 7px 10px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <div style="color: #f1f5f9; font-weight: 600; font-size: 0.82rem;">ALL TICKET LIST</div>
                                    <div style="color: #94a3b8; font-size: 0.7rem;">Tiket Aktif / Open</div>
                                </div>
                                <span style="color: #38bdf8; font-weight: bold; font-size: 0.88rem;">{insera_all_cnt:,} <span style="font-size: 0.7rem; color: #94a3b8; font-weight: normal;">data</span></span>
                            </div>
                            <!-- CLOSED TICKET LIST -->
                            <div style="background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 7px 10px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <div style="color: #f1f5f9; font-weight: 600; font-size: 0.82rem;">CLOSED TICKET LIST</div>
                                    <div style="color: #94a3b8; font-size: 0.7rem;">Tiket Closed / Selesai</div>
                                </div>
                                <span style="color: #10b981; font-weight: bold; font-size: 0.88rem;">{insera_closed_cnt:,} <span style="font-size: 0.7rem; color: #94a3b8; font-weight: normal;">data</span></span>
                            </div>
                            <!-- PROACTIVE TICKET -->
                            <div style="background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 7px 10px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <div style="color: #f1f5f9; font-weight: 600; font-size: 0.82rem;">PROACTIVE TICKET</div>
                                    <div style="color: #94a3b8; font-size: 0.7rem;">Tiket Sumber Proactive</div>
                                </div>
                                <span style="color: #a855f7; font-weight: bold; font-size: 0.88rem;">{insera_proactive_cnt:,} <span style="font-size: 0.7rem; color: #94a3b8; font-weight: normal;">data</span></span>
                            </div>
                            <!-- ADING ASSR -->
                            <div style="background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 7px 10px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <div style="color: #f1f5f9; font-weight: 600; font-size: 0.82rem;">ADING ASSR</div>
                                    <div style="color: #ec4899; font-size: 0.7rem;">Assurance Productivity</div>
                                </div>
                                <span style="color: #ec4899; font-weight: bold; font-size: 0.88rem;">{insera_ading_cnt:,} <span style="font-size: 0.7rem; color: #94a3b8; font-weight: normal;">data</span></span>
                            </div>
                            <!-- GABUNGAN -->
                            <div style="background: rgba(234, 179, 8, 0.1); border: 1px solid rgba(234, 179, 8, 0.3); border-radius: 6px; padding: 7px 10px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <div style="color: #fbbf24; font-weight: bold; font-size: 0.82rem;">GABUNGAN ALL &amp; CLOSE</div>
                                    <div style="color: #fef08a; font-size: 0.7rem;">Total Konsolidasi (Header Baku)</div>
                                </div>
                                <span style="color: #fbbf24; font-weight: 800; font-size: 0.92rem;">{insera_total_cnt:,} <span style="font-size: 0.7rem; color: #cbd5e1; font-weight: normal;">data</span></span>
                            </div>
                        </div>
                    </div>

                    <!-- Filter Insera -->
                    <div style="font-size: 0.72rem; color: #64748b; margin-top: -2px;">
                        Filter: Segmen <b style="color:#94a3b8;">DCS, PL-TSEL</b> &bull; Zone <b style="color:#94a3b8;">GMB, ULI</b> &bull; <b style="color:#94a3b8;">TECHNICAL</b>
                    </div>
                </div>

                <!-- KOLOM 4: IBOOSTER ASGAR -->
                <div style="background: rgba(30, 41, 59, 0.6); border: 1.5px solid #d97706; border-top: 4px solid #f59e0b; border-radius: 12px; padding: 15px; display: flex; flex-direction: column; gap: 12px;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px;">
                        <div>
                            <div style="color: #f59e0b; font-size: 0.72rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">SEGMENTASI 4: ASSURANCE QUALITY</div>
                            <div style="color: #ffffff; font-size: 1.05rem; font-weight: bold; margin-top: 2px;">IBOOSTER ASGAR</div>
                        </div>
                        <span style="background: #d97706; color: white; font-size: 0.68rem; padding: 3px 8px; border-radius: 10px; font-weight: bold;">ASR 30 HARI</span>
                    </div>

                    <!-- Waktu & Info -->
                    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 10px; font-size: 0.8rem;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="color: #94a3b8;">Terakhir Sinkron:</span>
                            <span style="color: #f8fafc; font-weight: bold;">{ibooster_asgar_time}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="color: #94a3b8;">Metode:</span>
                            <span style="color: #f59e0b; font-weight: 600;">{ibooster_asgar_source}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #94a3b8;">Spreadsheet:</span>
                            <span style="color: #fef08a; font-weight: 600;">UKUR IBOOSTER ASR</span>
                        </div>
                    </div>

                    <!-- Detail Segmentasi Target -->
                    <div>
                        <div style="color: #cbd5e1; font-size: 0.78rem; font-weight: bold; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">
                            📌 Target Pengukuran:
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 6px;">
                            <div style="background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 7px 10px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <div style="color: #f1f5f9; font-weight: 600; font-size: 0.82rem;">TIKET CLOSE ≤ 30 HARI</div>
                                    <div style="color: #94a3b8; font-size: 0.7rem;">Evaluasi Gangguan Ulang</div>
                                </div>
                                <span style="color: #f59e0b; font-weight: bold; font-size: 0.88rem;">{ibooster_asgar_cnt:,} <span style="font-size: 0.7rem; color: #94a3b8; font-weight: normal;">nomor</span></span>
                            </div>
                        </div>
                    </div>

                    <!-- Info Fitur -->
                    <div style="background: rgba(15, 23, 42, 0.4); border: 1px dashed rgba(255,255,255,0.1); border-radius: 8px; padding: 10px; font-size: 0.75rem; color: #94a3b8; line-height: 1.4;">
                        <div style="color: #cbd5e1; font-weight: 600; margin-bottom: 2px;">🎯 Kegunaan Data:</div>
                        Validasi kualitas redaman Rx dBm, status ONU (LOS/ONLINE), dan identifikasi potensi gangguan ulang (ASGAR) pada pelanggan yang tiketnya telah diselesaikan teknisi.
                    </div>
                </div>

            </div>
        </div>

        <!-- Footer Pop-Up -->
        <div style="padding: 12px 24px; background: #1e293b; border-top: 1px solid #334155; display: flex; justify-content: space-between; align-items: center;">
            <div style="color: #94a3b8; font-size: 0.78rem; display: flex; align-items: center; gap: 6px;">
                <span>💡</span>
                <span>Untuk menarik data terbaru kapan saja, gunakan menu <b>"⚙️ TARIK DATA MANUAL"</b> pada sidebar Admin di sebelah kiri.</span>
            </div>
            <button id="btn-close-sync-modal-bottom" style="background: #334155; border: 1px solid #475569; color: white; padding: 6px 16px; border-radius: 6px; font-size: 0.82rem; font-weight: 600; cursor: pointer; transition: all 0.2s;">Tutup Jendela ✕</button>
        </div>

    </div>
</div>
'''
st.markdown(sync_header_html.replace('\n', ' '), unsafe_allow_html=True)

# Inject JS untuk Live Clock Real-time & Modal Sinkronisasi 3 Segmentasi Data
js_clock = """
<script>
    function updateClock() {
        const days = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'];
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        const monthsLong = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
        
        const now = new Date();
        const dayName = days[now.getDay()];
        const day = String(now.getDate()).padStart(2, '0');
        const monthName = months[now.getMonth()];
        const monthLongName = monthsLong[now.getMonth()];
        const year = now.getFullYear();
        
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        
        const timeTop = `${day} ${monthName} ${year} | ${hours}:${minutes}`;
        const timeInline = `${dayName}, ${now.getDate()} ${monthLongName} ${year} | ${hours}:${minutes}:${seconds}`;
        
        try {
            const elInline = window.parent.document.getElementById('live-clock-inline');
            if(elInline) elInline.innerText = timeInline;
        } catch(e) {}
    }
    
    function attachSyncModalListeners() {
        try {
            const parentDoc = window.parent.document;
            const badgeBtn = parentDoc.getElementById('btn-open-sync-modal');
            const syncModal = parentDoc.getElementById('modal-sync-summary');
            const closeBtn1 = parentDoc.getElementById('btn-close-sync-modal');
            const closeBtn2 = parentDoc.getElementById('btn-close-sync-modal-bottom');

            if (badgeBtn && !badgeBtn.dataset.listener) {
                badgeBtn.dataset.listener = 'true';
                badgeBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    if (syncModal) syncModal.style.display = 'flex';
                });
            }

            function closeSync(e) {
                if (e) { e.preventDefault(); e.stopPropagation(); }
                if (syncModal) syncModal.style.display = 'none';
            }

            if (closeBtn1 && !closeBtn1.dataset.listener) {
                closeBtn1.dataset.listener = 'true';
                closeBtn1.addEventListener('click', closeSync);
            }
            if (closeBtn2 && !closeBtn2.dataset.listener) {
                closeBtn2.dataset.listener = 'true';
                closeBtn2.addEventListener('click', closeSync);
            }
            if (syncModal && !syncModal.dataset.listener) {
                syncModal.dataset.listener = 'true';
                syncModal.addEventListener('click', function(e) {
                    if (e.target === syncModal) {
                        closeSync(e);
                    }
                });
            }
        } catch(e) {}
    }

    setInterval(updateClock, 1000);
    setInterval(attachSyncModalListeners, 500);
    updateClock();
    attachSyncModalListeners();
</script>
"""
import streamlit.components.v1 as components
components.html(js_clock, width=0, height=0)

with st.spinner("Mempersiapkan dasbor..."):
      pass # df sudah diload di atas

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
    customer_col = find_col(['Customer Name', 'CUSTOMER NAME', 'NAMA PELANGGAN'])

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
        
    with st.sidebar:
        from streamlit_option_menu import option_menu

        all_opts = [
            "PS/RE", "KENDALA", "DETAIL RE PERIODE", "DETAIL MANJA", "WO ODS PERIODE", "TRIAL & FFG 60 HARI", "PROGRESS PROVI", "MONITORING SERVER",
            "DAILY REPORT", "IBOOSTER ASGAR", "GRAFIK TIKET PERIODE", "PROGRESS ASSURANCE"
        ]
        all_icons = [
            "trophy", "exclamation-triangle", "card-list", "hourglass-split", "clipboard-data", "pie-chart", "camera", "server",
            "file-earmark-text", "speedometer2", "graph-up", "camera"
        ]

        if "active_menu" not in st.session_state:
            st.session_state.active_menu = "PS/RE"

        if st.session_state.active_menu == "IBOOSTER GAUL":
            st.session_state.active_menu = "IBOOSTER ASGAR"

        query_menu = st.query_params.get("menu")
        if query_menu == "IBOOSTER GAUL":
            query_menu = "IBOOSTER ASGAR"
        if query_menu and query_menu in all_opts:
            st.session_state.active_menu = query_menu

        if st.session_state.active_menu not in all_opts:
            st.session_state.active_menu = "PS/RE"

        cur_idx = all_opts.index(st.session_state.active_menu)

        st.markdown('<p style="color: #94a3b8; font-size: 0.8rem; font-weight: bold; letter-spacing: 1px; margin-bottom: 5px; margin-top: 15px;">DASHBOARD FULFILLMENT</p>', unsafe_allow_html=True)

        selected_menu = option_menu(
            menu_title=None,
            options=all_opts,
            icons=all_icons,
            default_index=cur_idx,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent", "border": "none"},
                "icon": {"color": "#94a3b8", "font-size": "18px"},
                "nav-link": {"font-size": "15px", "text-align": "left", "margin": "2px 0px", "color": "#cbd5e1", "--hover-color": "#1e293b", "border-radius": "8px"},
                "nav-link-selected": {
                    "background-color": "#3f2b34",
                    "border-left": "4px solid #ef4444",
                    "color": "white",
                    "border-radius": "8px",
                    "border-top-left-radius": "8px",
                    "border-bottom-left-radius": "8px"
                }
            },
            key="unified_sidebar_menu"
        )

        if selected_menu != st.session_state.active_menu:
            st.session_state.active_menu = selected_menu
            st.rerun()

        menu = st.session_state.active_menu

        import streamlit.components.v1 as components
        components.html('''
        <script>
        function injectAssuranceHeader() {
            try {
                const parentDoc = window.parent.document;
                if (!parentDoc) return;
                
                const iframes = parentDoc.querySelectorAll('iframe');
                iframes.forEach(iframe => {
                    try {
                        const doc = iframe.contentDocument || (iframe.contentWindow && iframe.contentWindow.document);
                        if (!doc) return;
                        
                        const links = doc.querySelectorAll('.nav-link');
                        links.forEach(link => {
                            const txt = (link.innerText || '').trim().toUpperCase();
                            if (txt.includes('DAILY REPORT')) {
                                const li = link.closest('.nav-item');
                                if (li && !doc.getElementById('sec-hdr-assurance')) {
                                    const hdr = doc.createElement('div');
                                    hdr.id = 'sec-hdr-assurance';
                                    hdr.innerHTML = '<p style="color: #94a3b8; font-size: 0.8rem; font-weight: bold; letter-spacing: 1px; margin-bottom: 6px; margin-top: 24px; text-transform: uppercase; font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif; padding-left: 2px;">DASHBOARD ASSURANCE</p>';
                                    li.parentNode.insertBefore(hdr, li);
                                }
                            }
                        });
                        
                        // Ensure iframe is always tall enough without scrollbars
                        if (doc.getElementById('sec-hdr-assurance') && doc.body) {
                            doc.body.style.overflow = 'hidden';
                            iframe.style.overflow = 'hidden';
                            const neededH = Math.max(doc.body.scrollHeight + 30, 625);
                            if (parseInt(iframe.style.height) < neededH) {
                                iframe.style.height = neededH + 'px';
                            }
                        }
                    } catch(err) {}
                });
            } catch(e) {}
        }
        setInterval(injectAssuranceHeader, 250);
        injectAssuranceHeader();
        </script>
        ''', height=0, width=0)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Sinkronisasi Data:**")
    
    if "is_admin" not in st.session_state:
        if st.query_params.get("admin") == "true":
            st.session_state.is_admin = True
        else:
            st.session_state.is_admin = False

    is_cloud = os.environ.get("STREAMLIT_CLOUD") == "true"

    if is_cloud:
        st.sidebar.info("☁️ **Mode Cloud Aktif**\n\nUntuk penarikan data (Sync WFM), silakan gunakan **Bot Telegram BIMA** Anda. Data di layar pantau ini akan otomatis terupdate setelah bot selesai.")
    else:
        if not st.session_state.is_admin:
            admin_pin = st.sidebar.text_input("🔑 PIN Admin (Untuk Tarik Data):", type="password")
            if admin_pin == "888888":
                st.session_state.is_admin = True
                st.query_params["admin"] = "true"
                st.rerun()
            elif admin_pin != "":
                st.sidebar.error("❌ PIN Salah! Akses View-Only.")
        else:
            st.sidebar.success("✅ Mode Admin Aktif")
            st.sidebar.markdown("---")
            st.sidebar.markdown("⚙️ **TARIK DATA MANUAL (WFM, IBOOSTER & INSERA):**")
            
            # Pilihan Tarik Manual WFM & ADING
            if st.sidebar.button("🚀 Tarik WFM & ADING"):
                with st.spinner("⏳ Robot sedang bekerja... (Tunggu 1-2 menit)"):
                    try:
                        import sys
                        py_exec = sys.executable or "python"
                        base_dir = os.path.dirname(os.path.abspath(__file__))
                        script_path = os.path.join(base_dir, "main.py")
                        subprocess.run([py_exec, script_path, "DASHBOARD", "Admin Web", "WFM_MORNING", "Manual"], cwd=base_dir, capture_output=True, text=True, check=True, timeout=600)
                        st.cache_data.clear()
                        if auto_puller.running:
                            auto_puller.reset_timer()
                        st.sidebar.success("✅ Berhasil menarik data! Halaman akan dimuat ulang...")
                        time.sleep(2)
                        st.rerun()
                    except Exception as e:
                        st.sidebar.error(f"❌ Terjadi kesalahan: {e}")
                        
            # Pilihan Tarik Manual IBOOSTER FFG
            if st.sidebar.button("🚀 Tarik IBOOSTER FFG"):
                with st.spinner("⏳ Robot menarik data Ibooster (AO & INDIBIZ)... (Tunggu agak lama)"):
                    try:
                        import sys
                        py_exec = sys.executable or "python"
                        base_dir = os.path.dirname(os.path.abspath(__file__))
                        script_path = os.path.join(base_dir, "main.py")
                        subprocess.run([py_exec, script_path, "DASHBOARD", "Admin Web", "IBOOSTER", "Manual"], cwd=base_dir, capture_output=True, text=True, check=True, timeout=3600)
                        st.sidebar.success("✅ Berhasil menarik data Ibooster gabungan!")
                        time.sleep(2)
                    except Exception as e:
                        st.sidebar.error("❌ Robot Gagal menarik data.")

            # Pilihan Tarik Manual IBOOSTER ASGAR (ASSURANCE)
            if st.sidebar.button("🚀 Tarik IBOOSTER ASGAR"):
                with st.spinner("⏳ Robot menarik data Ibooster Assurance (CLOSE <= 30 Hari)... (Tunggu agak lama)"):
                    try:
                        import sys
                        py_exec = sys.executable or "python"
                        base_dir = os.path.dirname(os.path.abspath(__file__))
                        script_path = os.path.join(base_dir, "main.py")
                        subprocess.run([py_exec, script_path, "DASHBOARD", "Admin Web", "IBOOSTER_ASR", "Manual"], cwd=base_dir, capture_output=True, text=True, check=True, timeout=3600)
                        if ibooster_asgar_auto_puller.running:
                            ibooster_asgar_auto_puller.reset_timer()
                        st.cache_data.clear()
                        st.sidebar.success("✅ Berhasil menarik data Ibooster ASGAR (Assurance)!")
                        time.sleep(2)
                        st.rerun()
                    except Exception as e:
                        st.sidebar.error("❌ Robot Gagal menarik data Ibooster ASGAR.")
                        
            # Pilihan Tarik Manual INSERA & ADING ASSR
            if st.sidebar.button("🚀 Tarik INSERA & ADING ASSR"):
                with st.spinner("⏳ Robot menarik data ASSURANCE (INSERA ALL, CLOSED, PROACTIVE & ADING ASSR)... (Tunggu 1-3 menit)"):
                    try:
                        import sys
                        py_exec = sys.executable or "python"
                        base_dir = os.path.dirname(os.path.abspath(__file__))
                        script_path = os.path.join(base_dir, "main_assurance.py")
                        subprocess.run([py_exec, script_path, "DASHBOARD", "Admin Web", "Manual"], cwd=base_dir, capture_output=True, text=True, check=True)
                        if insera_auto_puller.running:
                            insera_auto_puller.reset_timer()
                        st.sidebar.success("✅ Berhasil menarik data INSERA & ADING ASSR ke Google Sheets!")
                        time.sleep(2)
                        st.rerun()
                    except subprocess.CalledProcessError as e:
                        st.sidebar.error("❌ Robot Gagal menarik data INSERA ASR.")
                    except Exception as e:
                        st.sidebar.error(f"❌ Terjadi kesalahan: {e}")

            # =====================================================================
            # MENU TARIK DATA OTOMATIS (DESAIN KARTU MODERN KHUSUS TEMA GELAP)
            # =====================================================================
            import streamlit.components.v1 as components

            # Helper generator HTML baris konten otomatis (Icon, Title, Chevron, Pill Badge)
            def _gen_auto_pull_card_html(icon, title, pill_prefix, target_ts, pill_bg, pill_border, pill_text_color, pill_val_color, is_hms=False, is_active=True):
                is_hms_js = "true" if is_hms else "false"
                target_ts_val = target_ts or 0

                if is_active and target_ts:
                    prefix_html = f"{pill_prefix}: " if pill_prefix else ""
                    badge_html = f'''
                    <div class="pill" style="background: {pill_bg}; border: 1px solid {pill_border}; color: {pill_text_color};">
                        <span style="font-size: 11px;">⏱️</span>
                        <span>{prefix_html}<span id="timer_val" style="font-weight: 700; color: {pill_val_color};">--:--</span></span>
                    </div>
                    <script>
                        var target = {target_ts_val} * 1000;
                        var elem = document.getElementById("timer_val");
                        function updateTimer() {{
                            var now = new Date().getTime();
                            var diff = target - now;
                            if (diff < 0) {{
                                elem.innerHTML = "Menarik data...";
                                return;
                            }}
                            var h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                            var m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
                            var s = Math.floor((diff % (1000 * 60)) / 1000);
                            if ({is_hms_js}) {{
                                elem.innerHTML = (h < 10 ? "0" + h : h) + ":" + (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s);
                            }} else {{
                                elem.innerHTML = (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s);
                            }}
                        }}
                        updateTimer();
                        setInterval(updateTimer, 1000);
                    </script>
                    '''
                else:
                    badge_html = '''
                    <div class="pill" style="background: rgba(100, 116, 139, 0.12); border: 1px solid rgba(100, 116, 139, 0.25); color: #94a3b8;">
                        <span style="font-size: 7px; opacity: 0.7;">⚪</span>
                        <span style="font-size: 10.5px;">Nonaktif</span>
                    </div>
                    '''

                return f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    * {{ box-sizing: border-box; }}
    body {{
        margin: 0;
        padding: 0;
        background: transparent;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        overflow: hidden;
        user-select: none;
    }}
    .row-card {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 3.5px;
        height: 50px;
        border-left: 1px solid rgba(255, 255, 255, 0.12);
        padding-left: 9px;
    }}
    .top-line {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
    }}
    .title-wrap {{
        display: flex;
        align-items: center;
        gap: 6px;
        color: #f1f5f9;
        font-size: 12.5px;
        font-weight: 700;
        letter-spacing: 0.2px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }}
    .chevron {{
        color: #64748b;
        font-size: 13px;
        font-weight: 800;
        margin-right: 2px;
    }}
    .pill {{
        display: inline-flex;
        align-items: center;
        gap: 4px;
        border-radius: 12px;
        padding: 1.5px 8px;
        font-size: 10.5px;
        font-weight: 600;
        width: fit-content;
        white-space: nowrap;
    }}
</style>
</head>
<body>
    <div class="row-card">
        <div class="top-line">
            <div class="title-wrap">
                <span>{icon}</span>
                <span>{title}</span>
            </div>
            <span class="chevron">&#10095;</span>
        </div>
        <div>
            {badge_html}
        </div>
    </div>
</body>
</html>'''

            # CSS Custom styling khusus sidebar card container
            st.sidebar.markdown("""
            <style>
            /* Card wrapper container auto pull */
            [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {
                background: #141f36 !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                border-radius: 12px !important;
                padding: 3px 6px !important;
                margin-bottom: 7px !important;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25) !important;
                transition: all 0.2s ease !important;
            }
            [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"]:hover {
                border-color: rgba(56, 189, 248, 0.3) !important;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4) !important;
            }
            /* Centering the toggle switch */
            [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stToggle"] {
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                height: 50px !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stToggle"] label {
                margin: 0 !important;
                padding: 0 !important;
            }
            /* Toggle Switch Active: Emerald Green */
            [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stToggle"] input[type="checkbox"]:checked + span {
                background-color: #10b981 !important;
            }
            /* Toggle Switch Inactive: Red */
            [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stToggle"] input[type="checkbox"]:not(:checked) + span {
                background-color: #ef4444 !important;
            }
            </style>
            """, unsafe_allow_html=True)

            # Header Kartu "Menu Tarik Data Otomatis" (Sesuai Gambar 2 versi Dark Theme)
            st.sidebar.markdown("""
            <div style="background: linear-gradient(180deg, #0f172a 0%, #0d1527 100%); border: 1.5px solid #1e293b; border-radius: 14px; padding: 12px 14px 10px 14px; margin-top: 15px; margin-bottom: 10px; box-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.45);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <div style="width: 4px; height: 18px; background: linear-gradient(180deg, #06b6d4 0%, #38bdf8 100%); border-radius: 4px; box-shadow: 0 0 10px rgba(6, 182, 212, 0.7);"></div>
                        <span style="font-size: 14.2px; font-weight: 800; color: #f8fafc; letter-spacing: 0.3px;">Menu Tarik Data Otomatis</span>
                    </div>
                    <div style="color: #64748b; font-size: 16px; font-weight: bold; letter-spacing: 2px; line-height: 1;">•••</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # --- 1. ROW WFM (Icon Petir ⚡) ---
            with st.sidebar.container(border=True):
                col_wfm_tog, col_wfm_info = st.columns([0.85, 3.15])
                with col_wfm_tog:
                    is_auto = st.toggle("", value=auto_puller.running, key="is_auto_wfm", label_visibility="collapsed")
                    if is_auto and not auto_puller.running:
                        auto_puller.start()
                    elif not is_auto and auto_puller.running:
                        auto_puller.stop()

                with col_wfm_info:
                    html_wfm = _gen_auto_pull_card_html(
                        icon="⚡",
                        title="WFM",
                        pill_prefix="",
                        target_ts=auto_puller.next_run_time,
                        pill_bg="rgba(6, 182, 212, 0.15)",
                        pill_border="rgba(6, 182, 212, 0.35)",
                        pill_text_color="#22d3ee",
                        pill_val_color="#67e8f9",
                        is_hms=False,
                        is_active=auto_puller.running
                    )
                    components.html(html_wfm, height=50)

            # --- 2. ROW IBOOSTER / FFG (Icon Jam Pasir ⌛) ---
            with st.sidebar.container(border=True):
                col_ib_tog, col_ib_info = st.columns([0.85, 3.15])
                with col_ib_tog:
                    is_auto_ibooster = st.toggle("", value=ibooster_auto_puller.running, key="is_auto_ibooster", label_visibility="collapsed")
                    if is_auto_ibooster and not ibooster_auto_puller.running:
                        ibooster_auto_puller.start()
                    elif not is_auto_ibooster and ibooster_auto_puller.running:
                        ibooster_auto_puller.stop()

                with col_ib_info:
                    html_ib = _gen_auto_pull_card_html(
                        icon="⌛",
                        title="iBOOSTER FFG",
                        pill_prefix="",
                        target_ts=ibooster_auto_puller.next_run_time,
                        pill_bg="rgba(168, 85, 247, 0.15)",
                        pill_border="rgba(168, 85, 247, 0.35)",
                        pill_text_color="#c084fc",
                        pill_val_color="#ddd6fe",
                        is_hms=True,
                        is_active=ibooster_auto_puller.running
                    )
                    components.html(html_ib, height=50)

            # --- 3. ROW INSERA ASR (Icon Gear ⚙️) ---
            if insera_auto_puller.running and insera_auto_puller.next_run_time and (insera_auto_puller.next_run_time - time.time() > 900):
                insera_auto_puller.reset_timer()

            with st.sidebar.container(border=True):
                col_ins_tog, col_ins_info = st.columns([0.85, 3.15])
                with col_ins_tog:
                    is_auto_insera = st.toggle("", value=insera_auto_puller.running, key="is_auto_insera", label_visibility="collapsed")
                    if is_auto_insera and not insera_auto_puller.running:
                        insera_auto_puller.start()
                    elif not is_auto_insera and insera_auto_puller.running:
                        insera_auto_puller.stop()

                with col_ins_info:
                    html_ins = _gen_auto_pull_card_html(
                        icon="⚙️",
                        title="INSERA ASR",
                        pill_prefix="",
                        target_ts=insera_auto_puller.next_run_time,
                        pill_bg="rgba(16, 185, 129, 0.15)",
                        pill_border="rgba(16, 185, 129, 0.35)",
                        pill_text_color="#34d399",
                        pill_val_color="#6ee7b7",
                        is_hms=False,
                        is_active=insera_auto_puller.running
                    )
                    components.html(html_ins, height=50)

            # --- 4. ROW IBOOSTER ASGAR (Icon Roket 🚀) ---
            with st.sidebar.container(border=True):
                col_asg_tog, col_asg_info = st.columns([0.85, 3.15])
                with col_asg_tog:
                    is_auto_asgar = st.toggle("", value=ibooster_asgar_auto_puller.running, key="is_auto_asgar", label_visibility="collapsed")
                    if is_auto_asgar and not ibooster_asgar_auto_puller.running:
                        ibooster_asgar_auto_puller.start()
                    elif not is_auto_asgar and ibooster_asgar_auto_puller.running:
                        ibooster_asgar_auto_puller.stop()

                with col_asg_info:
                    html_asg = _gen_auto_pull_card_html(
                        icon="🚀",
                        title="IBOOSTER ASGAR",
                        pill_prefix="",
                        target_ts=ibooster_asgar_auto_puller.next_run_time,
                        pill_bg="rgba(245, 158, 11, 0.15)",
                        pill_border="rgba(245, 158, 11, 0.35)",
                        pill_text_color="#fbbf24",
                        pill_val_color="#fef08a",
                        is_hms=True,
                        is_active=ibooster_asgar_auto_puller.running
                    )
                    components.html(html_asg, height=50)

            # Aksen gelombang modern di bagian bawah kartu (Sesuai Gambar 2)
            st.sidebar.markdown("""
            <div style="height: 4px; width: 100%; background: linear-gradient(90deg, rgba(6, 182, 212, 0.25) 0%, rgba(56, 189, 248, 0.45) 50%, rgba(139, 92, 246, 0.3) 100%); border-radius: 4px; margin-top: 4px; margin-bottom: 12px; box-shadow: 0 0 10px rgba(6, 182, 212, 0.3);"></div>
            """, unsafe_allow_html=True)

            st.sidebar.markdown("---")
            
            if st.sidebar.button("🔒 Keluar Admin"):
                st.session_state.is_admin = False
                if "admin" in st.query_params:
                    del st.query_params["admin"]
                st.rerun()

    # --- PERSIAPAN DATA BERDASARKAN TANGGAL ---
    df['Parsed_Date_PS'] = pd.to_datetime(df[date_col], format='mixed', errors='coerce').dt.date if date_col else None
    df['Parsed_Date_RE'] = pd.to_datetime(df[re_col], format='mixed', errors='coerce').dt.date if re_col else None
    
    jam_re_col = find_col(['JAM RE MASUK REAL', 'JAM RE MASUK', 'JAM RE'])
    if jam_re_col:
        df['Jam_RE'] = df[jam_re_col].astype(str).str.replace('nan', 'Unknown')
    elif re_col:
        temp_dt = pd.to_datetime(df[re_col], format='mixed', errors='coerce')
        df['Jam_RE'] = temp_dt.dt.strftime('%H:%M:%S').fillna('Unknown')
    else:
        df['Jam_RE'] = 'Unknown'
        
    jam_mod_col = find_col(['DATE MODIFIED REAL', 'Date Modified', 'Status Date'])
    if jam_mod_col:
        temp_dt_mod = pd.to_datetime(df[jam_mod_col], format='mixed', errors='coerce')
        df['Jam_Update'] = temp_dt_mod.dt.strftime('%H:%M:%S').fillna('Unknown')
        df['Parsed_Date_Mod'] = temp_dt_mod.dt.date
    else:
        df['Jam_Update'] = 'Unknown'
        df['Parsed_Date_Mod'] = None
    
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
    df_re_today = df[(df['Parsed_Date_RE'] >= start_date) & (df['Parsed_Date_RE'] <= end_date) & (~df['Status_Upper'].str.contains('COMPLETE', na=False)) & (~df['Status_Upper'].str.contains('WAPPR', na=False))].copy()
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
    
    prog_df = df[(df[morning_status_col].astype(str).str.strip().str.upper().isin(['SEDANG DIKERJAKAN', 'PROGRESS'])) & (df['Status_Upper'] == 'STARTWORK')].copy() if morning_status_col else pd.DataFrame()
    brk_prog = get_breakdown(prog_df)
    
    pending_df = df[(df[morning_status_col].astype(str).str.strip().str.upper() == 'PENDING') & (df['Parsed_Date_Mod'] >= start_date) & (df['Parsed_Date_Mod'] <= end_date)].copy() if morning_status_col else pd.DataFrame()
    brk_pending = get_breakdown(pending_df)
    
    kendala_df = df[(df['Status_Upper'].isin(['WORKFAIL', 'CANCLWORK'])) & (df['Parsed_Date_PS'] >= start_date) & (df['Parsed_Date_PS'] <= end_date)].copy()
    brk_ken = get_breakdown(kendala_df)
    
    validasi_df = df[
        ((df['Status_Upper'] == 'WAPPR') & (df['Parsed_Date_RE'] >= start_date) & (df['Parsed_Date_RE'] <= end_date)) |
        ((df['Status_Upper'] == 'COMPLETE') & (df['Parsed_Date_PS'] >= start_date) & (df['Parsed_Date_PS'] <= end_date))
    ].copy()
    
    startwork_df = df[df['Status_Upper'] == "STARTWORK"].copy()
    
    # Manja (H-, HI, H+)
    if flag_manja_col and flag_manja_col in df.columns:
        is_err = df[flag_manja_col].astype(str).str.contains('#VALUE!', na=False)
        if is_err.any():
            booking_col = find_col(['Booking Date', 'BOOKING DATE REAL', 'BOOKING DATE'])
            if booking_col and booking_col in df.columns:
                today_norm = pd.Timestamp.now().normalize()
                def calc_fallback_manja(val):
                    if pd.isna(val) or str(val).strip() in ['', '-', 'nan']:
                        return 'NON MANJA'
                    try:
                        dt = pd.to_datetime(val, errors='coerce')
                        if pd.isna(dt): return 'NON MANJA'
                        diff = (dt.normalize() - today_norm).days
                        if diff < 0: return 'MANJA H-1'
                        elif diff == 0: return 'MANJA HI'
                        else: return 'MANJA H++'
                    except:
                        return 'NON MANJA'
                df.loc[is_err, flag_manja_col] = df.loc[is_err, booking_col].apply(calc_fallback_manja)

    manja_df = df[(df[flag_manja_col].notna()) & (~df[flag_manja_col].astype(str).str.upper().isin(['NON MANJA', '-', '', 'NAN'])) & (df['Status_Upper'] == 'STARTWORK')].copy() if flag_manja_col else pd.DataFrame()
    
    # =====================================================================


    def compute_ttr_badge(ttr_val, cust_type_val, rep_val=None):
        import math
        elapsed_sec = None

        # 1. Coba baca dari kolom TTR jika ada
        if ttr_val is not None:
            try:
                if isinstance(ttr_val, (int, float)):
                    if not math.isnan(ttr_val):
                        if 0 < ttr_val < 10:
                            elapsed_sec = float(ttr_val) * 86400
                        else:
                            elapsed_sec = float(ttr_val)
                else:
                    s_ttr = str(ttr_val).strip()
                    if s_ttr and s_ttr.lower() not in ['nan', 'none', '-', '', '<na>', 'nat']:
                        parts = s_ttr.split(':')
                        if len(parts) == 3:
                            elapsed_sec = float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
                        elif len(parts) == 2:
                            elapsed_sec = float(parts[0]) * 3600 + float(parts[1]) * 60
                        else:
                            val = float(parts[0])
                            if not math.isnan(val):
                                elapsed_sec = val * 3600
            except Exception:
                elapsed_sec = None

        # 2. Fallback hitung otomatis dari selisih REPORTED DATE (WIB -> WITA +1 jam) ke saat ini
        if elapsed_sec is None or math.isnan(elapsed_sec) or elapsed_sec < 0:
            if rep_val:
                try:
                    dt_rep = pd.to_datetime(rep_val, errors='coerce')
                    if pd.notna(dt_rep):
                        from datetime import datetime as dt_cls
                        now_dt = dt_cls.now()
                        dt_rep_wita = dt_rep + pd.Timedelta(hours=1)
                        diff = (now_dt - dt_rep_wita.to_pydatetime()).total_seconds()
                        if diff >= 0:
                            elapsed_sec = diff
                except Exception:
                    pass

        if elapsed_sec is None or math.isnan(elapsed_sec) or elapsed_sec < 0:
            elapsed_sec = 0.0

        elapsed_sec = float(elapsed_sec)
        c_up = str(cust_type_val).upper()
        # Target SLA TTR:
        # - HVC DIAMOND : 3 Jam
        # - HVC PLATINUM: 6 Jam
        # - HVC GOLD    : 12 Jam
        # - REGULER : 24 Jam
        if 'DIAMOND' in c_up:
            target_sec = 3 * 3600
        elif 'PLATINUM' in c_up:
            target_sec = 6 * 3600
        elif 'GOLD' in c_up:
            target_sec = 12 * 3600
        else:
            target_sec = 24 * 3600

        remain_sec = target_sec - elapsed_sec
        remain_pct = (remain_sec / target_sec) * 100

        h = int(elapsed_sec // 3600)
        m = int((elapsed_sec % 3600) // 60)
        s = int(elapsed_sec % 60)
        # Menghilangkan detik pada display utama agar seragam (hh:mm), detik tetap ada di tooltip
        time_str = f"{h:02d}:{m:02d}"
        time_str_full = f"{h:02d}:{m:02d}:{s:02d}"

        if remain_pct >= 71.0:
            # Hijau (100% sampai 71%)
            bg = "rgba(16, 185, 129, 0.18)"
            bd = "#10b981"
            cl = "#34d399"
            ic = "🟢"
            lbl = f"({int(round(remain_pct))}%)"
        elif remain_pct >= 41.0:
            # Kuning (70% sampai 41%)
            bg = "rgba(234, 179, 8, 0.18)"
            bd = "#eab308"
            cl = "#facc15"
            ic = "🟡"
            lbl = f"({int(round(remain_pct))}%)"
        else:
            # Merah (40% sampai 0% atau minus / OSLA)
            bg = "rgba(239, 68, 68, 0.18)"
            bd = "#ef4444"
            cl = "#f87171"
            ic = "🔴" if remain_pct >= 0 else "⚠️"
            lbl = f"({int(round(max(0, remain_pct)))}%)" if remain_pct >= 0 else "(OSLA)"

        target_hours = int(target_sec // 3600)
        return (
            f'<span style="background: {bg}; border: 1px solid {bd}; color: {cl}; '
            f'font-size: 0.76rem; font-weight: 700; padding: 4px 10px; border-radius: 12px; '
            f'display: inline-flex; align-items: center; justify-content: center; gap: 5px; white-space: nowrap;" '
            f'title="TTR Berjalan: {time_str_full} | Sisa Waktu SLA: {lbl} (Target: {target_hours} Jam)">'
            f'{ic} <span style="font-family: monospace; font-size: 0.82rem;">{time_str}</span> '
            f'<span style="font-size: 0.69rem; opacity: 0.9;">{lbl}</span>'
            f'</span>'
        )

    # HALAMAN 1: DASHBOARD UTAMA
    # =====================================================================
    if menu == "PS/RE":
        
        # Helper to make numbers clickable
        def make_link(val, cat, prod):
            if val > 0:
                underline = "none" if prod == "ALL" else "underline"
                return f'<a href="javascript:void(0)" class="modal-trigger" data-cat="{cat}" data-prod="{prod}" style="color:white; text-decoration:{underline}; cursor:pointer;">{val}</a>'
            return f'<span style="color:white">-</span>'
            
        # --- 5 GRID CARDS ---
        def bd_html(brk, cat_name):
            total = sum(brk.values()) if brk else 0
            def fmt(prod):
                val = brk.get(prod, 0)
                pct = f"({(val/total*100):.0f}%)" if total > 0 else "(0%)"
                val_html = make_link(val, cat_name, prod) if val > 0 else f'<span>{val}</span>'
                return f'<div class="dc-row-val" style="display: flex; justify-content: flex-end; align-items: center; gap: 4px;"><span>{val_html}</span><span style="font-size: 1.05rem; color: #94a3b8; width: 52px; text-align: right; font-weight: bold; white-space: nowrap;">{pct}</span></div>'
            
            return f'''
                <div style="font-size:0.85rem; margin-bottom:8px; visibility:hidden;">&nbsp;</div>
                <div class="dc-row"><span>AO TSEL</span><span style="color:#475569">:</span>{fmt('AO TSEL')}</div>
                <div class="dc-row"><span>PDA TSEL</span><span style="color:#475569">:</span>{fmt('PDA TSEL')}</div>
                <div class="dc-row"><span>INDIBIZ</span><span style="color:#475569">:</span>{fmt('INDIBIZ')}</div>
                <div class="dc-row"><span>ISP VULA</span><span style="color:#475569">:</span>{fmt('ISP VULA')}</div>
            '''
            
        manja_total = len(manja_df)
        manja_html = ""
        if flag_manja_col and order_col:
            manja_html += '<div class="dc-row-manja" style="color:white; font-weight:bold; font-size:0.85rem; margin-bottom:8px;"><span></span><span class="header-badge-text">H-</span><span class="header-badge-text">HI</span><span class="header-badge-text">H+</span></div>'
            for prod in PROD_COLS:
                sub = manja_df[manja_df[order_col].astype(str).str.upper().str.contains(prod.split()[0], na=False)]
                h_min = len(sub[sub[flag_manja_col].astype(str).str.contains("H-", regex=False, na=False)])
                h_i = len(sub[sub[flag_manja_col].astype(str).str.contains("HI", regex=False, na=False)])
                h_plus = len(sub[sub[flag_manja_col].astype(str).str.contains("H+", regex=False, na=False)])
                manja_html += f'<div class="dc-row-manja"><span>{prod}</span><span>{make_link(h_min, "MANJA H-", prod)}</span><span>{make_link(h_i, "MANJA HI", prod)}</span><span>{make_link(h_plus, "MANJA H+", prod)}</span></div>'
        else:
            manja_html = "<div style='text-align:center; padding-top:20px'>NO DATA</div>"
            
        kendala_html = ""
        if order_col:
            kendala_html += '<div class="dc-row-kendala" style="color:white; font-size:0.85rem; font-weight:bold; margin-bottom:8px;"><span></span><span class="header-badge-text">WFM</span><span class="header-badge-text">UNSC</span></div>'
            for prod in PROD_COLS:
                sub = kendala_df[kendala_df[order_col].astype(str).str.upper().str.contains(prod.split()[0], na=False)]
                wfm = len(sub[sub['Status_Upper'] == 'WORKFAIL'])
                unsc = len(sub[sub['Status_Upper'] == 'CANCLWORK'])
                kendala_html += f'<div class="dc-row-kendala"><span>{prod}</span><span>{make_link(wfm, "KENDALA WFM", prod)}</span><span>{make_link(unsc, "KENDALA UNSC", prod)}</span></div>'
        else:
            kendala_html = "<div style='text-align:center; padding-top:20px'>NO DATA</div>"
            
        validasi_html = ""
        if order_col:
            validasi_html += '<div class="dc-row-kendala" style="color:white; font-size:0.85rem; font-weight:bold; margin-bottom:8px;"><span></span><span class="header-badge-text">WAPPR</span><span class="header-badge-text">COMPLETE</span></div>'
            for prod in PROD_COLS:
                sub = validasi_df[validasi_df[order_col].astype(str).str.upper().str.contains(prod.split()[0], na=False)]
                wfm = len(sub[sub['Status_Upper'] == 'WAPPR'])
                unsc = len(sub[sub['Status_Upper'] == 'COMPLETE'])
                validasi_html += f'<div class="dc-row-kendala"><span>{prod}</span><span>{make_link(wfm, "WO VALIDASI WFM", prod)}</span><span>{make_link(unsc, "WO VALIDASI UNSC", prod)}</span></div>'
        else:
            validasi_html = "<div style='text-align:center; padding-top:20px'>NO DATA</div>"
            
        grid_html = f'''
        <div class="grid-6">
            <!-- BARIS 1 -->
            <!-- CARD 1: RE MASUK -->
            <div class="d-card c-blue">
                <div class="dc-header">
                    <div class="dc-header-left">
                        <div class="dc-icon ic-blue">📥</div>
                        <div class="dc-title">RE MASUK</div>
                    </div>
                    <div class="dc-value">{make_link(len(df_re_today), "RE MASUK HI", "ALL")}</div>
                </div>
                <div class="dc-breakdown">{bd_html(brk_re, "RE MASUK HI").strip()}<div class="dc-row" style="border-top: 3px dashed #334155; margin-top: 8px; padding-top: 8px; font-size: 1.15rem; font-weight: bold;"><span style="color: #cbd5e1; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8);">PS/RE</span><span></span><span style="color:{ps_re_color}; font-size: 1.25rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8);"><span style="color:white; font-weight:bold; font-size:1.25rem; margin-right:12px;">{ps_hi_ao}/{re_hi_ao}</span>{ps_re_pct}</span></div></div>
            </div>
            <!-- CARD 2: WO VALIDASI -->
            <div class="d-card c-indigo">
                <div class="dc-header">
                    <div class="dc-header-left">
                        <div class="dc-icon ic-indigo">🔍</div>
                        <div class="dc-title">WO VALIDASI</div>
                    </div>
                    <div class="dc-value">{make_link(len(validasi_df), "WO VALIDASI", "ALL")}</div>
                </div>
                <div class="dc-breakdown">{validasi_html}</div>
            </div>
            <!-- CARD 3: MANJA -->
            <div class="d-card c-teal">
                <div class="dc-header">
                    <div class="dc-header-left">
                        <div class="dc-icon ic-teal">👤</div>
                        <div class="dc-title">MANJA</div>
                    </div>
                    <div class="dc-value">{make_link(manja_total, "MANJA", "ALL")}</div>
                </div>
                <div class="dc-breakdown">{manja_html}</div>
            </div>
            <!-- CARD 4: KENDALA HI -->
            <div class="d-card c-orange">
                <div class="dc-header">
                    <div class="dc-header-left">
                        <div class="dc-icon ic-orange">⚠️</div>
                        <div class="dc-title">KENDALA HI</div>
                    </div>
                    <div class="dc-value">{make_link(len(kendala_df), "KENDALA HI", "ALL")}</div>
                </div>
                <div class="dc-breakdown">{kendala_html}</div>
            </div>

            <!-- BARIS 2 -->
            <!-- CARD 4: DONE PS -->
            <div class="d-card c-green">
                <div class="dc-header">
                    <div class="dc-header-left">
                        <div class="dc-icon ic-green">✅</div>
                        <div class="dc-title">DONE PS</div>
                    </div>
                    <div class="dc-value">{make_link(len(df_ps_today), "DONE PS", "ALL")}</div>
                </div>
                <div class="dc-breakdown">{bd_html(brk_ps, "DONE PS")}</div>
            </div>
            <!-- CARD 5: POTENSI PS -->
            <div class="d-card c-purple">
                <div class="dc-header">
                    <div class="dc-header-left">
                        <div class="dc-icon ic-purple">🎯</div>
                        <div class="dc-title">POTENSI PS</div>
                    </div>
                    <div class="dc-value">{make_link(len(potensi_df), "POTENSI PS", "ALL")}</div>
                </div>
                <div class="dc-breakdown">{bd_html(brk_pot, "POTENSI PS")}</div>
            </div>
            <!-- CARD 7: PROGRESS -->
            <div class="d-card c-cyan">
                <div class="dc-header">
                    <div class="dc-header-left">
                        <div class="dc-icon ic-cyan">⚙️</div>
                        <div class="dc-title">PROGRESS</div>
                    </div>
                    <div class="dc-value">{make_link(len(prog_df), "PROGRESS", "ALL")}</div>
                </div>
                <div class="dc-breakdown">{bd_html(brk_prog, "PROGRESS")}</div>
            </div>
            <!-- CARD 8: PENDING -->
            <div class="d-card c-slate">
                <div class="dc-header">
                    <div class="dc-header-left">
                        <div class="dc-icon ic-slate">⏳</div>
                        <div class="dc-title">PENDING</div>
                    </div>
                    <div class="dc-value">{make_link(len(pending_df), "PENDING", "ALL")}</div>
                </div>
                <div class="dc-breakdown">{bd_html(brk_pending, "PENDING")}</div>
            </div>
        </div>
        '''
        st.markdown(grid_html.replace('\n', ''), unsafe_allow_html=True)
        
        # --- PRE-RENDER ALL MODALS ---
        c_date = find_col(['DATE CREATE REAL', 'DATE CREATE', 'TANGGAL PS', 'PS', 'Booking Date', 'Date Modified'])
        c_date_mod = find_col(['DATE MODIFIED REAL', 'Date Modified', 'DATE MODIFIED'])
        c_order = order_col if order_col else ''
        c_sto = find_col(['WORKZONE', 'WORZONE', 'ZONE'])
        c_wonum_ao = find_col(['NO WONUM & AO', 'NO WONUM'])
        c_cust = find_col(['CUSTOMER NAME', 'NAMA PELANGGAN'])
        c_status = find_col(['STATUS', 'Status'])
        c_tim = tim_col if tim_col else ''
        c_stat_wo = morning_status_col if morning_status_col else ''
        
        cats = ["RE MASUK HI", "DONE PS", "POTENSI PS", "PROGRESS", "KENDALA WFM", "KENDALA UNSC", "KENDALA HI", "MANJA H-", "MANJA HI", "MANJA H+", "MANJA", "WO VALIDASI WFM", "WO VALIDASI UNSC", "WO VALIDASI", "PENDING"]
        
        all_modals_html = ""
        for cat in cats:
            for prod in PROD_COLS + ["ALL"]:
                src_df = pd.DataFrame()
                if cat == "RE MASUK HI": src_df = df_re_today.copy()
                elif cat == "DONE PS": src_df = df_ps_today.copy()
                elif cat == "POTENSI PS": src_df = potensi_df.copy()
                elif cat == "PROGRESS": src_df = prog_df.copy()
                elif cat == "KENDALA WFM": src_df = kendala_df[kendala_df['Status_Upper'] == 'WORKFAIL'].copy()
                elif cat == "KENDALA UNSC": src_df = kendala_df[kendala_df['Status_Upper'] == 'CANCLWORK'].copy()
                elif cat == "KENDALA HI": src_df = kendala_df.copy()
                elif cat == "MANJA H-": src_df = manja_df[manja_df[flag_manja_col].astype(str).str.contains("H-", regex=False, na=False)].copy() if flag_manja_col else pd.DataFrame()
                elif cat == "MANJA HI": src_df = manja_df[manja_df[flag_manja_col].astype(str).str.contains("HI", regex=False, na=False)].copy() if flag_manja_col else pd.DataFrame()
                elif cat == "MANJA H+": src_df = manja_df[manja_df[flag_manja_col].astype(str).str.contains("H+", regex=False, na=False)].copy() if flag_manja_col else pd.DataFrame()
                elif cat == "MANJA": src_df = manja_df.copy()
                elif cat == "WO VALIDASI WFM": src_df = validasi_df[validasi_df['Status_Upper'] == 'WAPPR'].copy()
                elif cat == "WO VALIDASI UNSC": src_df = validasi_df[validasi_df['Status_Upper'] == 'COMPLETE'].copy()
                elif cat == "WO VALIDASI": src_df = validasi_df.copy()
                elif cat == "PENDING": src_df = pending_df.copy()
                
                if len(src_df) > 0 and order_col:
                    if prod != "ALL":
                        if cat.startswith("MANJA") or cat.startswith("KENDALA"):
                            src_df = src_df[src_df[order_col].astype(str).str.upper().str.contains(prod.split()[0], na=False)]
                        else:
                            src_df = src_df[src_df[order_col].astype(str).str.upper() == prod.upper()]
                        
                if len(src_df) > 0:
                    if c_date and c_date in src_df.columns:
                        src_df = src_df.sort_values(by=c_date, ascending=False)
                    html_table = '<div style="width: 100%; display: flex; flex-direction: column;"><div style="position: sticky; top: 0; z-index: 10; display: grid; width: 100%; padding: 0; margin: 0; border-bottom: 2px solid #3b82f6; background: #0f172a; grid-template-columns: 45px 160px 160px 110px 80px minmax(220px, 1.8fr) minmax(150px, 1.5fr) 130px minmax(150px, 1.2fr) minmax(180px, 1.2fr); font-size: 12px; text-transform: uppercase;">'
                    html_table += '<div style="display: flex; justify-content: center; align-items: center; text-align: center; padding: 10px; border-right: 1px solid rgba(255,255,255,0.15);"><span style="transform: translateY(-3px); display: inline-block; font-weight: 900; font-size: 16px; letter-spacing: 0.5px; color: #ffffff; text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5);">NO</span></div><div style="display: flex; justify-content: center; align-items: center; text-align: center; padding: 10px; border-right: 1px solid rgba(255,255,255,0.15);"><span style="transform: translateY(-3px); display: inline-block; font-weight: 900; font-size: 16px; letter-spacing: 0.5px; color: #ffffff; text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5);">DATE CREATE</span></div><div style="display: flex; justify-content: center; align-items: center; text-align: center; padding: 10px; border-right: 1px solid rgba(255,255,255,0.15);"><span style="transform: translateY(-3px); display: inline-block; font-weight: 900; font-size: 16px; letter-spacing: 0.5px; color: #ffffff; text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5);">DATE MODIFIED</span></div><div style="display: flex; justify-content: center; align-items: center; text-align: center; padding: 10px; border-right: 1px solid rgba(255,255,255,0.15);"><span style="transform: translateY(-3px); display: inline-block; font-weight: 900; font-size: 16px; letter-spacing: 0.5px; color: #ffffff; text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5);">ORDER</span></div><div style="display: flex; justify-content: center; align-items: center; text-align: center; padding: 10px; border-right: 1px solid rgba(255,255,255,0.15);"><span style="transform: translateY(-3px); display: inline-block; font-weight: 900; font-size: 16px; letter-spacing: 0.5px; color: #ffffff; text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5);">STO</span></div><div style="display: flex; justify-content: center; align-items: center; text-align: center; padding: 10px; border-right: 1px solid rgba(255,255,255,0.15);"><span style="transform: translateY(-3px); display: inline-block; font-weight: 900; font-size: 16px; letter-spacing: 0.5px; color: #ffffff; text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5);">NO WONUM & AO</span></div><div style="display: flex; justify-content: center; align-items: center; text-align: center; padding: 10px; border-right: 1px solid rgba(255,255,255,0.15);"><span style="transform: translateY(-3px); display: inline-block; font-weight: 900; font-size: 16px; letter-spacing: 0.5px; color: #ffffff; text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5);">CUSTOMER NAME</span></div><div style="display: flex; justify-content: center; align-items: center; text-align: center; padding: 10px; border-right: 1px solid rgba(255,255,255,0.15);"><span style="transform: translateY(-3px); display: inline-block; font-weight: 900; font-size: 16px; letter-spacing: 0.5px; color: #ffffff; text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5);">STATUS</span></div><div style="display: flex; justify-content: center; align-items: center; text-align: center; padding: 10px; border-right: 1px solid rgba(255,255,255,0.15);"><span style="transform: translateY(-3px); display: inline-block; font-weight: 900; font-size: 16px; letter-spacing: 0.5px; color: #ffffff; text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5);">TIM</span></div><div style="display: flex; justify-content: center; align-items: center; text-align: center; padding: 10px; border-right: 1px solid rgba(255,255,255,0.15); white-space: normal; word-break: break-word; line-height: 1.3;"><span style="transform: translateY(-3px); display: inline-block; font-weight: 900; font-size: 16px; letter-spacing: 0.5px; color: #ffffff; text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5);">STATUS WO</span></div></div>'
                    
                    for idx, row in enumerate(src_df.to_dict('records'), 1):
                        def get_val(col_name): return str(row.get(col_name, '-')) if pd.notna(row.get(col_name)) else '-'
                        
                        status_val_raw = get_val(c_status).upper()
                        if status_val_raw == 'COMPWORK':
                            status_bg = "background-color: #14532d; color: white; border: 1px solid #166534;"
                        elif status_val_raw == 'STARTWORK':
                            status_bg = "background-color: #1e3a8a; color: white; border: 1px solid #1d4ed8;"
                        elif status_val_raw == 'INPRG':
                            status_bg = "background-color: #713f12; color: white; border: 1px solid #854d0e;"
                        elif status_val_raw in ['WORKFAIL', 'CANCLWORK']:
                            status_bg = "background-color: #7f1d1d; color: white; border: 1px solid #991b1b;"
                        elif status_val_raw == 'WAPPR':
                            status_bg = "background-color: #334155; color: white; border: 1px solid #475569;"
                        elif status_val_raw == 'VALSTART':
                            status_bg = "background-color: #7c3aed; color: white; border: 1px solid #8b5cf6;"
                        else:
                            status_bg = "background-color: rgba(255,255,255,0.1); color: white;"
                            
                        order_val_raw = get_val(c_order).strip().upper()
                        if order_val_raw == 'AO TSEL':
                            order_bg_css = "background: #831843; color: white; border: 1px solid #be123c;"
                        elif order_val_raw == 'PDA TSEL':
                            order_bg_css = "background: #14532d; color: white; border: 1px solid #166534;"
                        elif order_val_raw == 'INDIBIZ':
                            order_bg_css = "background: #1e3a8a; color: white; border: 1px solid #1d4ed8;"
                        else:
                            order_bg_css = "background: rgba(220,38,38,0.2); color: #fca5a5; border: 1px solid rgba(220,38,38,0.4);"
                            
                        html_table += f'''
                        <div class="prov-modal-row" style="display: grid; width: 100%; padding: 0; margin: 0; font-size: 14px; grid-template-columns: 45px 160px 160px 110px 80px minmax(220px, 1.8fr) minmax(150px, 1.5fr) 130px minmax(150px, 1.2fr) minmax(180px, 1.2fr); background: rgba(30,41,59,0.5); border-bottom: 1px solid rgba(255,255,255,0.05);">
                            <div style="padding: 10px; text-align: center; border-right: 1px solid rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center;"><span style="transform: translateY(-3px); display: inline-block; font-weight: 600; text-shadow: 1px 1px 3px rgba(0,0,0,0.9);">{idx}</span></div>
                            <div style="padding: 10px; font-size: 14px; text-align: center; border-right: 1px solid rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center;"><span style="transform: translateY(-3px); display: inline-block; font-weight: 600; text-shadow: 1px 1px 3px rgba(0,0,0,0.9);">{get_val(c_date)}</span></div>
                            <div style="padding: 10px; font-size: 14px; text-align: center; border-right: 1px solid rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center;"><span style="transform: translateY(-3px); display: inline-block; font-weight: 600; text-shadow: 1px 1px 3px rgba(0,0,0,0.9);">{get_val(c_date_mod)}</span></div>
                            <div style="padding: 10px; text-align: center; border-right: 1px solid rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center;"><span style="transform: translateY(-3px); display: inline-block; {order_bg_css} padding: 2px 8px; border-radius: 4px; font-size: 14px; font-weight: bold;">{get_val(c_order)}</span></div>
                            <div style="padding: 10px; text-align: center; border-right: 1px solid rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center;"><span style="transform: translateY(-3px); display: inline-block; font-weight: 600; text-shadow: 1px 1px 3px rgba(0,0,0,0.9);">{get_val(c_sto)}</span></div>
                            <div style="padding: 10px; font-size: 14px; word-break: break-all; text-align: center; border-right: 1px solid rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center;"><span style="transform: translateY(-3px); display: inline-block; font-weight: 600; text-shadow: 1px 1px 3px rgba(0,0,0,0.9);">{get_val(c_wonum_ao)}</span></div>
                            <div style="padding: 10px; font-size: 14px; text-align: center; border-right: 1px solid rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center; white-space: normal; word-break: break-word; line-height: 1.3;"><span style="transform: translateY(-3px); display: inline-block; font-weight: 600; text-shadow: 1px 1px 3px rgba(0,0,0,0.9);">{get_val(c_cust).upper()}</span></div>
                            <div style="padding: 10px; text-align: center; border-right: 1px solid rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center;"><span style="transform: translateY(-3px); display: inline-block; {status_bg} padding: 4px 12px; border-radius: 12px; font-size: 14px; font-weight: bold;">{get_val(c_status)}</span></div>
                            <div style="padding: 10px; font-size: 14px; text-align: center; border-right: 1px solid rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center;"><span style="transform: translateY(-3px); display: inline-block; font-weight: 600; text-shadow: 1px 1px 3px rgba(0,0,0,0.9);">{get_val(c_tim)}</span></div>
                            <div style="padding: 10px; font-size: 14px; text-align: center; display: flex; justify-content: center; align-items: center; white-space: normal; word-break: break-word; line-height: 1.3;"><span style="transform: translateY(-3px); display: inline-block; font-weight: 600; text-shadow: 1px 1px 3px rgba(0,0,0,0.9);">{get_val(c_stat_wo)}</span></div>
                        </div>
                        '''
                    html_table += '</div>'
                    
                    # Create the modal container
                    modal_id = f"modal-{cat.replace(' ', '_')}-{prod.replace(' ', '_')}"
                    all_modals_html += f'''
                    <div id="{modal_id}" class="detail-modal" style="display:none; position:fixed; top:10%; left:5%; right:5%; bottom:10%; background:#0f172a; z-index:999999; border: 2.5px solid #eab308; border-radius:12px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.8); flex-direction:column; overflow:hidden;">
                        <div style="padding:12px 20px; background:#1e293b; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #334155; gap:16px;">
                            <div style="display:flex; align-items:center; gap:12px; min-width:0; flex-shrink:1;">
                                <h3 style="margin:0; color:white; font-size:1.15rem; font-weight:700; letter-spacing:0.5px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">Detail Data: {cat} - {prod}</h3>
                                <span class="prov-modal-counter-badge" style="background:rgba(234,179,8,0.2); color:#facc15; border:1px solid #eab308; padding:3px 12px; border-radius:12px; font-size:0.8rem; font-weight:700; white-space:nowrap;" data-total="{len(src_df)}">{len(src_df):,} WO</span>
                            </div>
                            <div style="display:flex; align-items:center; gap:14px; flex-shrink:0;">
                                <div style="position:relative; display:flex; align-items:center;">
                                    <span style="position:absolute; left:11px; color:#60a5fa; font-size:0.88rem; pointer-events:none;">🔍</span>
                                    <input type="text" class="prov-modal-search-box" placeholder="Cari WONUM / AO / Pelanggan / Tim..." autocomplete="off" />
                                    <button type="button" class="prov-modal-search-clear" style="display:none; position:absolute; right:8px; background:none; border:none; color:#94a3b8; font-size:1.15rem; cursor:pointer; padding:0 4px; line-height:1;" title="Hapus Pencarian">&times;</button>
                                </div>
                                <button class="modal-close" style="background:none; border:none; color:#cbd5e1; font-size:2rem; cursor:pointer; line-height:1; padding:0 6px;" title="Tutup Modal">&times;</button>
                            </div>
                        </div>
                        <div style="padding:0; overflow-y:auto; flex:1;">
                            {html_table}
                        </div>
                    </div>
                    '''
        
        if all_modals_html:
            prov_modal_css = '''
            <style>
            .prov-modal-search-box {
                background: #0f172a !important;
                color: #f8fafc !important;
                border: 1.8px solid #3b82f6 !important;
                border-radius: 8px !important;
                padding: 6px 32px 6px 34px !important;
                font-size: 0.84rem !important;
                width: 300px !important;
                outline: none !important;
                transition: all 0.2s ease !important;
                box-shadow: 0 2px 5px rgba(0,0,0,0.4) !important;
            }
            .prov-modal-search-box:focus {
                border-color: #60a5fa !important;
                box-shadow: 0 0 10px rgba(96, 165, 250, 0.6) !important;
            }
            .prov-modal-search-box::placeholder {
                color: #94a3b8 !important;
            }
            </style>
            '''
            st.markdown((prov_modal_css + all_modals_html).replace('\n', ''), unsafe_allow_html=True)
            
        import streamlit.components.v1 as components
        components.html('''
        <script>
        setInterval(function() {
            const parentDoc = window.parent.document;
            if (!parentDoc) return;
            
            // Open modal listeners
            const triggers = parentDoc.querySelectorAll('.modal-trigger');
            triggers.forEach(t => {
                if(t.dataset.listener) return;
                t.dataset.listener = 'true';
                t.addEventListener('click', function(e) {
                    e.preventDefault();
                    const cat = this.getAttribute('data-cat');
                    const prod = this.getAttribute('data-prod');
                    
                    const modals = parentDoc.querySelectorAll('.detail-modal');
                    modals.forEach(m => m.style.display = 'none');
                    
                    const targetId = this.getAttribute('data-target') || ('modal-' + (cat||'').replace(/ /g, '_') + '-' + (prod||'').replace(/ /g, '_'));
                    const target = parentDoc.getElementById(targetId);
                    if(target) {
                        target.style.display = 'flex';
                        const searchInput = target.querySelector('.prov-modal-search-box');
                        if (searchInput) {
                            searchInput.value = '';
                            const clearBtn = target.querySelector('.prov-modal-search-clear');
                            if (clearBtn) clearBtn.style.display = 'none';
                            const badge = target.querySelector('.prov-modal-counter-badge');
                            const totalCount = badge ? parseInt(badge.getAttribute('data-total') || '0') : 0;
                            if (badge) {
                                badge.textContent = totalCount.toLocaleString() + ' WO';
                                badge.style.background = 'rgba(234,179,8,0.2)';
                                badge.style.borderColor = '#eab308';
                                badge.style.color = '#facc15';
                            }
                            target.querySelectorAll('.prov-modal-row').forEach(r => r.style.display = 'grid');
                            setTimeout(() => searchInput.focus(), 80);
                        }
                    }
                });
            });
            
            // Real-time Search within Provisioning Modal
            const searchInputs = parentDoc.querySelectorAll('.prov-modal-search-box');
            searchInputs.forEach(input => {
                if (input.dataset.listener) return;
                input.dataset.listener = 'true';
                
                const modal = input.closest('.detail-modal');
                if (!modal) return;
                const clearBtn = modal.querySelector('.prov-modal-search-clear');
                const badge = modal.querySelector('.prov-modal-counter-badge');
                const totalCount = badge ? parseInt(badge.getAttribute('data-total') || '0') : 0;
                
                function doProvFilter() {
                    const val = input.value.toLowerCase().trim();
                    if (clearBtn) {
                        clearBtn.style.display = val.length > 0 ? 'block' : 'none';
                    }
                    const rows = modal.querySelectorAll('.prov-modal-row');
                    let matched = 0;
                    rows.forEach(r => {
                        const text = (r.textContent || '').toLowerCase();
                        if (!val || text.indexOf(val) !== -1) {
                            r.style.display = 'grid';
                            matched++;
                        } else {
                            r.style.display = 'none';
                        }
                    });
                    if (badge) {
                        if (!val) {
                            badge.textContent = totalCount.toLocaleString() + ' WO';
                            badge.style.background = 'rgba(234,179,8,0.2)';
                            badge.style.borderColor = '#eab308';
                            badge.style.color = '#facc15';
                        } else {
                            badge.textContent = matched.toLocaleString() + ' / ' + totalCount.toLocaleString() + ' WO';
                            if (matched === 0) {
                                badge.style.background = 'rgba(239,68,68,0.2)';
                                badge.style.borderColor = '#ef4444';
                                badge.style.color = '#f87171';
                            } else {
                                badge.style.background = 'rgba(56,189,248,0.2)';
                                badge.style.borderColor = '#38bdf8';
                                badge.style.color = '#38bdf8';
                            }
                        }
                    }
                }
                
                input.addEventListener('input', doProvFilter);
                input.addEventListener('keydown', function(e) {
                    if (e.key === 'Escape') {
                        if (input.value) {
                            input.value = '';
                            doProvFilter();
                            e.stopPropagation();
                        }
                    }
                });
                
                if (clearBtn) {
                    clearBtn.addEventListener('click', function(e) {
                        e.preventDefault();
                        input.value = '';
                        doProvFilter();
                        input.focus();
                    });
                }
            });
            
            // Close modal listeners
            const closers = parentDoc.querySelectorAll('.modal-close');
            closers.forEach(c => {
                if(c.dataset.listener) return;
                c.dataset.listener = 'true';
                c.addEventListener('click', function(e) {
                    e.preventDefault();
                    const modal = this.closest('.detail-modal');
                    if(modal) {
                        modal.style.display = 'none';
                    }
                });
            });
            
        }, 500);
        </script>
        ''', height=0, width=0)
        
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
                
                html_str = '<div style="background-color: #0b1120; border: 2.5px solid #334155; border-radius: 12px; padding: 20px; font-family: sans-serif; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">'
                
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
                    <div style="border: 1px solid #334155; padding: 4px 10px; border-radius: 6px; color: #cbd5e1; font-size: 12px; display: flex; align-items: center; gap: 6px;">
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
                            <div style="color: #cbd5e1; font-size: 1.05rem; font-weight: 700; margin-bottom: 6px;">{str(name).upper()}</div>
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
                            <div style="color: #cbd5e1; font-size: 12px; margin-bottom: 4px; line-height: 1.2;">Total Done PS<br>hari ini</div>
                            <div style="color: #10b981; font-size: 1.4rem; font-weight: bold;">{total_done_ps}</div>
                        </div>
                    </div>
                    <!-- Stat 2 -->
                    <div style="flex: 1; background-color: #0f172a; border-radius: 8px; padding: 15px; display: flex; align-items: center; gap: 15px;">
                        <div style="background-color: #1e3a8a; color: #3b82f6; width: 45px; height: 45px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 1.5rem; flex-shrink: 0;">
                            🛠️
                        </div>
                        <div>
                            <div style="color: #cbd5e1; font-size: 12px; margin-bottom: 4px; line-height: 1.2;">Total Teknisi<br>Aktif</div>
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
                no_complete_mask = ~df['Status_Upper'].str.contains('COMPLETE', na=False) & ~df['Status_Upper'].str.contains('WAPPR', na=False)
                
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
                    html_table = '<div style="background-color: #0b1120; border: 2.5px solid #334155; border-radius: 12px; padding: 20px; font-family: sans-serif; height: 40rem; display: flex; flex-direction: column;">'
                    
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
                        html_table += f'<th style="padding: 15px 12px; border-bottom: 2px solid #334155; color: {color}; font-size: 1.1rem; text-align: center;">{title}</th>'
                    html_table += '</tr></thead><tbody>'
                    
                    for _, row in summary.iterrows():
                        pct_val = (row["PS"] / row["RE"] * 100) if row["RE"] > 0 else 0
                        pct_color = "#34d399" if pct_val >= 85.0 else "#ef4444"
                        
                        html_table += '<tr style="border-bottom: 1px solid #1e293b;">'
                        html_table += f'<td style="padding: 12px 10px; font-weight: bold; color: white; font-size: 1.1rem; text-align: center;">{row["TANGGAL"]}</td>'
                        html_table += f'<td style="padding: 12px 10px; color: #38bdf8; font-weight: bold; font-size: 1.1rem; text-align: center;">{row["RE"]}</td>'
                        html_table += f'<td style="padding: 12px 10px; color: #34d399; font-weight: bold; font-size: 1.1rem; text-align: center;">{row["PS"]}</td>'
                        html_table += f'<td style="padding: 12px 10px; font-weight: bold; color: {pct_color}; font-size: 1.1rem; text-align: center;">'
                        html_table += f'<div style="display:flex; align-items:center; justify-content:center; gap:10px;">'
                        html_table += f'<span style="width: 80px; text-align:right; white-space: nowrap;">{row["% PS/RE"]}</span>'
                        html_table += f'<div style="width: 60px; height: 6px; background: #1e293b; border-radius: 4px; overflow: hidden;">'
                        html_table += f'<div style="width: {min(pct_val, 100)}%; height: 100%; background: {pct_color};"></div>'
                        html_table += f'</div></div></td>'
                        html_table += '</tr>'
                        
                    html_table += '</tbody>'
                    
                    # Sticky Footer for Totals
                    html_table += '<tfoot style="background-color: #1e293b; position: sticky; bottom: -1px; z-index: 2;">'
                    html_table += '<tr>'
                    html_table += '<th style="padding: 12px; text-align: center; color: white; font-size: 1.1rem; border-top: 2px solid #334155;">'
                    html_table += '<div style="display:flex; align-items:center; justify-content:center; gap:10px;">'
                    html_table += '<div style="background: rgba(139, 92, 246, 0.2); color:#a855f7; padding: 6px 10px; border-radius: 6px; font-weight:900; font-size:1.2rem;">∑</div>'
                    html_table += 'TOTAL'
                    html_table += '</div></th>'
                    html_table += f'<th style="padding: 12px; text-align: center; border-top: 2px solid #334155;"><div style="color: #38bdf8; font-size: 1.3rem;">{tot_re}</div><div style="font-size: 14px; color: #94a3b8; font-weight: normal; margin-top: 4px;">Total RE</div></th>'
                    html_table += f'<th style="padding: 12px; text-align: center; border-top: 2px solid #334155;"><div style="color: #34d399; font-size: 1.3rem;">{tot_ps}</div><div style="font-size: 14px; color: #94a3b8; font-weight: normal; margin-top: 4px;">Total PS</div></th>'
                    html_table += f'<th style="padding: 12px; text-align: center; border-top: 2px solid #334155;"><div style="color: white; font-size: 1.3rem;">{tot_pct}</div><div style="font-size: 14px; color: #94a3b8; font-weight: normal; margin-top: 4px;">Rata-rata % PS/RE</div></th>'
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
            
        # --- TABEL PS & KENDALA LENGKAP ---
        st.markdown('<div class="section-title-wrap" style="margin-top: 40px;"><div class="section-title"> <b>REKAP PS & JENIS KENDALA</b></div></div>', unsafe_allow_html=True)
        st.markdown("<p style='font-size:0.85rem; color:#94a3b8; margin-top:-10px; margin-bottom:15px;'>Detail seluruh pesanan yang sudah Closing (PS) maupun Kendala (Teknis & Pelanggan), dikelompokkan berdasarkan teknisi dan jenis order.</p>", unsafe_allow_html=True)

        df_combined = pd.concat([df_ps_today, kendala_df]) if len(df_ps_today) > 0 or len(kendala_df) > 0 else pd.DataFrame()

        if len(df_combined) > 0 and tim_col and order_col:
            def map_category(row):
                status = str(row.get('Status_Upper', '')).strip()
                order = str(row.get(order_col, '')).strip().upper()
                if 'COMPWORK' in status:
                    if 'AO' in order and 'TSEL' in order: return 'AO TSEL'
                    if order == 'AO': return 'AO TSEL'
                    if 'PDA' in order: return 'PDA TSEL'
                    if 'INDIBIZ' in order: return 'INDIBIZ'
                    if 'VULA' in order or 'ISP' in order: return 'ISP VULA'
                    return 'AO TSEL'
                elif status in ['WORKFAIL', 'CANCLWORK']:
                    m_status = str(row.get(morning_status_col, '')).strip().upper() if morning_status_col else ''
                    if m_status in ['BATAL', 'GANTI PAKET', 'KENDALA IZIN', 'PENDING', 'RUMAH KOSONG']:
                        return 'KENDALA PELANGGAN'
                    else:
                        return 'KENDALA TEKNIS'
                return None
                
            df_combined['TAB_CAT'] = df_combined.apply(map_category, axis=1)
            df_combined = df_combined.dropna(subset=['TAB_CAT'])
            
            tims = sorted(df_combined[tim_col].dropna().unique())
            
            html2 = '''
            <style>
            .cp2-header { display: grid; grid-template-columns: 50px 3.0fr 3.8fr 0.8fr 0.8fr 0.8fr 0.8fr 1.0fr 1.0fr 0.8fr; background-color: #172554; font-size: 0.95rem; font-weight: 700; color: white; text-transform: uppercase; border-bottom: 2px solid #3b82f6; text-align: center; position: sticky; top: 0; z-index: 10; }
            .cp2-header > div { padding: 10px 5px; border-right: 1px solid #64748b; border-bottom: 1px solid #64748b; display: flex; align-items: center; justify-content: center; line-height: 1.2; }
            .cp2-header > div:last-child { border-right: none; }
            .cp2-body-grid { display: grid; grid-template-columns: 50px 3.0fr 3.8fr 0.8fr 0.8fr 0.8fr 0.8fr 1.0fr 1.0fr 0.8fr; font-size: 0.8rem; color: white; }
            .cp2-grand { background-color: #172554; display: grid; grid-template-columns: 50px 3.0fr 3.8fr 0.8fr 0.8fr 0.8fr 0.8fr 1.0fr 1.0fr 0.8fr; padding: 12px 15px; font-weight: bold; color: white; border-top: 2px solid #3b82f6; text-align: center; position: sticky; bottom: -1px; z-index: 10; font-size: 1.05rem; }
            </style>
            <div class="cp-container">
                <div class="cp2-header">
                    <div style="grid-row: span 2; justify-content: center; text-align: center;">NO.</div>
                    <div style="grid-row: span 2; justify-content: center; text-align: center;">MORNING TIM</div>
                    <div style="grid-row: span 2; justify-content: center; text-align: center;">NO. WONUM & AO</div>
                    <div style="grid-column: span 4; background-color: #15803d; color: white;">PS (OK)</div>
                    <div style="grid-column: span 2; background-color: #b91c1c; color: white;">JENIS KENDALA</div>
                    <div style="grid-row: span 2;">GRAND TOTAL</div>
                    
                    <div style="background-color: #15803d; color: white; border-bottom: none; border-right: 1px solid rgba(255,255,255,0.4);">AO TSEL</div>
                    <div style="background-color: #15803d; color: white; border-bottom: none; border-right: 1px solid rgba(255,255,255,0.4);">PDA TSEL</div>
                    <div style="background-color: #15803d; color: white; border-bottom: none; border-right: 1px solid rgba(255,255,255,0.4);">INDIBIZ</div>
                    <div style="background-color: #15803d; color: white; border-bottom: none; border-right: 1px solid rgba(255,255,255,0.4);">ISP VULA</div>
                    <div style="background-color: #b91c1c; color: white; border-bottom: none; border-right: 1px solid rgba(255,255,255,0.4);">TEKNIS</div>
                    <div style="background-color: #b91c1c; color: white; border-bottom: none; border-right: 1px solid rgba(255,255,255,0.4);">PELANGGAN</div>
                </div>
                <div class="cp2-body-grid">
            '''
            
            col_names = ['AO TSEL', 'PDA TSEL', 'INDIBIZ', 'ISP VULA', 'KENDALA TEKNIS', 'KENDALA PELANGGAN']
            grand_totals = {c: 0 for c in col_names}
            
            no = 1
            for tim in tims:
                tim_data = df_combined[df_combined[tim_col] == tim]
                wonums = tim_data['INFO ORDER'].unique()
                row_span = len(wonums)
                if row_span == 0: continue
                
                tech_total_orders = len(tim_data)
                total_ps = tim_data['TAB_CAT'].isin(['AO TSEL', 'PDA TSEL', 'INDIBIZ', 'ISP VULA']).sum()
                total_ken = tim_data['TAB_CAT'].isin(['KENDALA TEKNIS', 'KENDALA PELANGGAN']).sum()
                
                shadow = "text-shadow: 1px 1px 2px rgba(0,0,0,0.9), -1px -1px 1px rgba(0,0,0,0.5);"
                badges = f'<span class="cp-badge" style="background-color: #3b82f6; color: white; {shadow}">{tech_total_orders} WO</span>'
                badges += f'<span class="cp-badge" style="background-color: #15803d; color: white; {shadow}">{total_ps} PS</span>'
                badges += f'<span class="cp-badge" style="background-color: #b91c1c; color: white; {shadow}">{total_ken} KEN</span>'
                
                col1 = f'<div style="display: flex; align-items: center; justify-content: flex-start; gap: 4px; flex-wrap: wrap;">{tim} {badges}</div>'
                
                border_thick = "border-top: 2px solid #cbd5e1;"
                
                html2 += f'<div class="cp-cell" style="grid-row: span {row_span}; {border_thick} justify-content: center; font-weight: bold; font-size: 0.95rem;">{no}</div>'
                html2 += f'<div class="cp-cell-left" style="grid-row: span {row_span}; {border_thick} font-weight: bold; font-size: 0.95rem;">{col1}</div>'
                
                for i, wonum in enumerate(wonums):
                    wonum_data = tim_data[tim_data['INFO ORDER'] == wonum]
                    counts = wonum_data['TAB_CAT'].value_counts()
                    
                    row_border = border_thick if i == 0 else ""
                    
                    html2 += f'<div class="cp-cell" style="{row_border} font-weight: bold; font-size: 0.95rem;">{wonum}</div>'
                    
                    row_tot = 0
                    for c in col_names:
                        c_val = counts.get(c, 0)
                        if c_val > 0:
                            row_tot += c_val
                            html2 += f'<div class="cp-cell" style="{row_border}">{c_val}</div>'
                        else:
                            html2 += f'<div class="cp-cell" style="{row_border}"></div>'
                    
                    html2 += f'<div class="cp-cell" style="font-weight:bold; {row_border}">{row_tot}</div>'
                
                for c in col_names:
                    grand_totals[c] += (tim_data['TAB_CAT'] == c).sum()
                no += 1
                    
            html2 += '</div>'
            
            # FOOTER
            html2 += f'''
            <div class="cp2-grand" style="padding: 0;">
                <div style="grid-column: span 3; text-align:center; justify-content: center; display: flex; align-items: center; padding: 12px 15px;">GRAND TOTAL</div>
                <div style="background-color: #15803d; padding: 12px 15px; display: flex; align-items: center; justify-content: center; border-right: 1px solid rgba(255,255,255,0.4);">{grand_totals["AO TSEL"]}</div>
                <div style="background-color: #15803d; padding: 12px 15px; display: flex; align-items: center; justify-content: center; border-right: 1px solid rgba(255,255,255,0.4);">{grand_totals["PDA TSEL"]}</div>
                <div style="background-color: #15803d; padding: 12px 15px; display: flex; align-items: center; justify-content: center; border-right: 1px solid rgba(255,255,255,0.4);">{grand_totals["INDIBIZ"]}</div>
                <div style="background-color: #15803d; padding: 12px 15px; display: flex; align-items: center; justify-content: center; border-right: 1px solid rgba(255,255,255,0.4);">{grand_totals["ISP VULA"]}</div>
                <div style="background-color: #b91c1c; padding: 12px 15px; display: flex; align-items: center; justify-content: center; border-right: 1px solid rgba(255,255,255,0.4);">{grand_totals["KENDALA TEKNIS"]}</div>
                <div style="background-color: #b91c1c; padding: 12px 15px; display: flex; align-items: center; justify-content: center; border-right: 1px solid rgba(255,255,255,0.4);">{grand_totals["KENDALA PELANGGAN"]}</div>
                <div style="padding: 12px 15px; display: flex; align-items: center; justify-content: center;">{sum(grand_totals.values())}</div>
            </div>
            </div>
            </div>
            '''
            
            import re
            html2_clean = re.sub(r'^\s+', '', html2, flags=re.MULTILINE)
            st.markdown(html2_clean, unsafe_allow_html=True)
            
    # =====================================================================
    # HALAMAN LAINNYA
    # =====================================================================
    elif menu == "KENDALA":
        # 1. Hitung Metrik
        total_kendala = len(kendala_df)
        
        wfm_df = kendala_df[kendala_df['Status_Upper'] == 'WORKFAIL']
        wfm_count = len(wfm_df)
        
        cancl_df = kendala_df[kendala_df['Status_Upper'] == 'CANCLWORK']
        cancl_count = len(cancl_df)
        
        wfm_pct = f"{(wfm_count/total_kendala*100):.2f}%".replace('.', ',') if total_kendala > 0 else "0,00%"
        cancl_pct = f"{(cancl_count/total_kendala*100):.2f}%".replace('.', ',') if total_kendala > 0 else "0,00%"
        
        color_map_order = {
            'AO TSEL': '#b91c1c', 
            'INDIBIZ': '#1d4ed8', 
            'PDA TSEL': '#15803d', 
            'ISP VULA': '#475569', 
            'DATIN': '#ca8a04'
        }
        def get_color(order):
            for key, val in color_map_order.items():
                if key in str(order).upper(): return val
            return '#94a3b8'

        # Hitung breakdown order untuk WORKFAIL
        wfm_breakdown_html = ""
        wfm_items = []
        brk_wfm = get_breakdown(wfm_df)
        for k, v in brk_wfm.items():
            if v > 0:
                pct = f"{(v/wfm_count*100):.1f}%".replace('.', ',') if wfm_count > 0 else "0,0%"
                clr = get_color(k)
                wfm_items.append(f'<div style="color: white; font-size: 12px; display: flex; align-items: center; justify-content: flex-start; gap: 8px;"><div style="width: 10px; height: 10px; background-color: {clr}; border-radius: 50%;"></div><div style="white-space: nowrap;">{k} <span style="margin-left: 4px;">{v} ({pct})</span></div></div>')
        wfm_breakdown_html = f'<div style="display: flex; flex-direction: column; gap: 6px; justify-content: center;">{"".join(wfm_items)}</div>'
            
        # Hitung breakdown order untuk CANCLWORK
        cancl_breakdown_html = ""
        cancl_items = []
        brk_cancl = get_breakdown(cancl_df)
        for k, v in brk_cancl.items():
            if v > 0:
                pct = f"{(v/cancl_count*100):.1f}%".replace('.', ',') if cancl_count > 0 else "0,0%"
                clr = get_color(k)
                cancl_items.append(f'<div style="color: white; font-size: 12px; display: flex; align-items: center; justify-content: flex-start; gap: 8px;"><div style="width: 10px; height: 10px; background-color: {clr}; border-radius: 50%;"></div><div style="white-space: nowrap;">{k} <span style="margin-left: 4px;">{v} ({pct})</span></div></div>')
        cancl_breakdown_html = f'<div style="display: flex; flex-direction: column; gap: 6px; justify-content: center;">{"".join(cancl_items)}</div>'
        
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
                <div style="flex: 1; background-color: #0f172a; border-radius: 12px; border: 2.5px solid #94a3b8; display: flex; flex-direction: column; position: relative; overflow: hidden;">
                    <div style="padding: 15px 20px; display: flex; gap: 15px; flex-grow: 1;">
                        <div style="background-color: #ef4444; width: 60px; height: 60px; border-radius: 12px; display: flex; justify-content: center; align-items: center; flex-shrink: 0;">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 2L1 21H23L12 2ZM11 16H13V18H11V16ZM11 10H13V14H11V10Z"/>
                            </svg>
                        </div>
                        <div style="display: flex; flex-direction: column; justify-content: center;">
                            <div style="color: white; font-size: 0.95rem; font-weight: 900; letter-spacing: 0.5px; margin-bottom: 2px;">WORKFAIL</div>
                            <div style="color: #ef4444; font-size: 1.8rem; font-weight: bold; line-height: 1;">{wfm_count}</div>
                            <div style="color: white; font-size: 0.9rem; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8); margin-top: 4px;">({wfm_pct})</div>
                        </div>
                        <div style="margin-left: auto; display: flex; flex-direction: column; justify-content: center; gap: 3px;">
                            {wfm_breakdown_html}
                        </div>
                    </div>
                    <div style="height: 3px; background-color: #ef4444; margin: 0 15px 15px 15px; border-radius: 2px;"></div>
                </div>

                <!-- CANCEL Card -->
                <div style="flex: 1; background-color: #0f172a; border-radius: 12px; border: 2.5px solid #94a3b8; display: flex; flex-direction: column; position: relative; overflow: hidden;">
                    <div style="padding: 15px 20px; display: flex; gap: 15px; flex-grow: 1;">
                        <div style="background-color: #f97316; width: 60px; height: 60px; border-radius: 12px; display: flex; justify-content: center; align-items: center; flex-shrink: 0;">
                            <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="12" r="10"></circle>
                                <line x1="15" y1="9" x2="9" y2="15"></line>
                                <line x1="9" y1="9" x2="15" y2="15"></line>
                            </svg>
                        </div>
                        <div style="display: flex; flex-direction: column; justify-content: center;">
                            <div style="color: white; font-size: 0.95rem; font-weight: 900; letter-spacing: 0.5px; margin-bottom: 2px;">CANCLWORK</div>
                            <div style="color: #f97316; font-size: 1.8rem; font-weight: bold; line-height: 1;">{cancl_count}</div>
                            <div style="color: white; font-size: 0.9rem; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8); margin-top: 4px;">({cancl_pct})</div>
                        </div>
                        <div style="margin-left: auto; display: flex; flex-direction: column; justify-content: center; gap: 3px;">
                            {cancl_breakdown_html}
                        </div>
                    </div>
                    <div style="height: 3px; background-color: #f97316; margin: 0 15px 15px 15px; border-radius: 2px;"></div>
                </div>

                <!-- TOTAL Card -->
                <div style="flex: 1; background-color: #0f172a; border-radius: 12px; border: 2.5px solid #94a3b8; display: flex; flex-direction: column; position: relative; overflow: hidden;">
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
                            <div style="color: white; font-size: 0.95rem; font-weight: 900; letter-spacing: 0.5px; margin-bottom: 2px;">TOTAL WO</div>
                            <div style="color: #3b82f6; font-size: 1.8rem; font-weight: bold; line-height: 1;">{total_kendala}</div>
                            <div style="color: white; font-size: 0.9rem; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8); margin-top: 4px;">[100%]</div>
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
            col1, col1b, col2, col3 = st.columns([1, 1, 1.3, 1.3])
            
            # --- Chart 1: Donut ---
            with col1:
                with st.container():
                    st.markdown("<div class='custom-border-target'></div>", unsafe_allow_html=True)
                    st.markdown('<div style="color: white; font-size: 1.1rem; font-weight: 900; margin-top: -15px; margin-bottom: 10px;">DISTRIBUSI STATUS WO</div>', unsafe_allow_html=True)
                    
                    donut_df = pd.DataFrame({
                        'Status': ['WORKFAIL', 'CANCLWORK'],
                        'Jumlah': [wfm_count, cancl_count],
                        'Color': ['#ef4444', '#f97316'],
                        'Label': [f'WORKFAIL  {wfm_count} ({wfm_pct})', f'CANCLWORK  {cancl_count} ({cancl_pct})']
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
                            showlegend=False,
                            annotations=[dict(text=f"TOTAL<br><b>{total_kendala}</b><br>WO", x=0.5, y=0.5, font_size=13, font_color="white", showarrow=False)],
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            margin=dict(t=0, b=10, l=0, r=0),
                            height=250
                        )
                        # Center the pie
                        fig1.update_traces(domain=dict(x=[0, 1]))
                        st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False}, theme=None)
                        
                        leg_html = '<div style="display: flex; flex-direction: column; gap: 8px; margin-left: 10px; margin-top: 5px;">'
                        for _, row in donut_df.iterrows():
                            pct_val = wfm_pct if row['Status'] == 'WORKFAIL' else cancl_pct
                            leg_html += f'<div style="display: flex; align-items: center; gap: 8px;"><div style="width: 10px; height: 10px; background-color: {row["Color"]}; border-radius: 1px; flex-shrink: 0;"></div><div style="color: white; font-weight: bold; font-size: 0.85rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8);">{row["Status"]} &nbsp;&nbsp; {row["Jumlah"]} ({pct_val})</div></div>'
                        leg_html += '</div>'
                        st.markdown(leg_html, unsafe_allow_html=True)
                    else:
                        st.info("No Data")
                        
            # --- Chart 1b: Donut Proporsi Kendala Berdasarkan Jenis Order ---
            with col1b:
                with st.container():
                    st.markdown("<div class='custom-border-target'></div>", unsafe_allow_html=True)
                    st.markdown('<div style="color: white; font-size: 1.1rem; font-weight: 900; margin-top: -15px; margin-bottom: 10px;">KENDALA DARI JENIS ORDER</div>', unsafe_allow_html=True)
                    
                    if order_col and order_col in kendala_df.columns:
                        order_counts = kendala_df[order_col].dropna().astype(str).str.upper().value_counts().reset_index()
                        order_counts.columns = ['Order', 'Jumlah']
                        
                        if not order_counts.empty:
                            # Predefine colors for known types to match the ORDER column table styling
                            color_map = {'INDIBIZ': '#1e3a8a', 'AO TSEL': '#7f1d1d', 'AO': '#7f1d1d', 'PDA TSEL': '#14532d', 'PDA': '#14532d', 'ISP VULA': '#4b5563'}
                            default_colors = ['#3b82f6', '#8b5cf6', '#ec4899', '#14b8a6', '#f97316']
                            
                            colors = []
                            labels = []
                            for idx, row in order_counts.iterrows():
                                order_type = row['Order']
                                count = row['Jumlah']
                                pct = f"{(count / total_kendala) * 100:.1f}%"
                                
                                c = color_map.get(order_type)
                                if not c:
                                    c = default_colors[idx % len(default_colors)]
                                colors.append(c)
                                
                                labels.append(f'{order_type}  {count} ({pct})')
                                
                            order_counts['Color'] = colors
                            order_counts['Label'] = labels
                            
                            fig1b = go.Figure(data=[go.Pie(
                                labels=order_counts['Label'], 
                                values=order_counts['Jumlah'], 
                                hole=.65,
                                marker_colors=order_counts['Color'],
                                textinfo='percent',
                                textfont=dict(color='white', size=11, family="sans-serif"),
                                hoverinfo='label'
                            )])
                            
                            fig1b.update_layout(
                                showlegend=False,
                                annotations=[dict(text=f"TOTAL<br><span style='font-size: 18px; font-weight: bold;'>{total_kendala}</span><br>KENDALA", x=0.5, y=0.5, font_size=11, font_color="white", showarrow=False)],
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                margin=dict(t=0, b=10, l=0, r=0),
                                height=250
                            )
                            fig1b.update_traces(domain=dict(x=[0, 1]))
                            st.plotly_chart(fig1b, use_container_width=True, config={'displayModeBar': False}, theme=None)
                            
                            leg_html2 = '<div style="display: flex; flex-direction: column; gap: 8px; margin-left: 10px; margin-top: 5px;">'
                            for idx, row in order_counts.iterrows():
                                order_type = row['Order']
                                count = row['Jumlah']
                                pct = f"{(count / total_kendala) * 100:.1f}%"
                                leg_html2 += f'<div style="display: flex; align-items: center; gap: 8px;"><div style="width: 10px; height: 10px; background-color: {row["Color"]}; border-radius: 1px; flex-shrink: 0;"></div><div style="color: white; font-weight: bold; font-size: 0.85rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8);">{order_type} &nbsp;&nbsp; {count} ({pct})</div></div>'
                            leg_html2 += '</div>'
                            st.markdown(leg_html2, unsafe_allow_html=True)
                        else:
                            st.info("No Order Data")
                    else:
                        st.info("Kolom Order Tidak Ditemukan")
            
            # --- Chart 2: Top 5 Kendala ---
            with col2:
                with st.container():
                    st.markdown("<div class='custom-border-target'></div>", unsafe_allow_html=True)
                    st.markdown('<div style="color: white; font-size: 1.1rem; font-weight: 900; margin-top: -15px; margin-bottom: 10px;">TOP 5 KENDALA</div>', unsafe_allow_html=True)
                    if morning_status_col:
                        top_reasons = kendala_df[morning_status_col].dropna().astype(str).str.upper().value_counts().nlargest(5).reset_index()
                        top_reasons.columns = ['Alasan', 'Jumlah']
                        if not top_reasons.empty:
                            html_bars2 = '<div style="display: flex; flex-direction: column; justify-content: space-evenly; height: 300px; padding: 5px 0;">'
                            max_val2 = top_reasons['Jumlah'].max()
                            rank_colors2 = ['#ef4444', '#f97316', '#f59e0b', '#eab308', '#facc15']
                            
                            for i, row in enumerate(top_reasons.itertuples()):
                                name2 = row.Alasan
                                val2 = row.Jumlah
                                color2 = rank_colors2[i] if i < len(rank_colors2) else rank_colors2[-1]
                                width_pct2 = (val2 / max_val2) * 100 if max_val2 > 0 else 0
                                
                                html_bars2 += f'<div style="display: flex; align-items: center; width: 100%;">'
                                html_bars2 += f'<div style="color: white; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8); width: 170px; white-space: normal; word-wrap: break-word; line-height: 1.2; font-size: 0.9rem; margin-right: 10px; flex-shrink: 0;" title="{name2}">{name2}</div>'
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
                with st.container():
                    st.markdown("<div class='custom-border-target'></div>", unsafe_allow_html=True)
                    st.markdown('<div style="color: white; font-size: 1.1rem; font-weight: 900; margin-top: -15px; margin-bottom: 10px;">TOP 5 TEKNISI DENGAN KENDALA</div>', unsafe_allow_html=True)
                    if tim_col:
                        top_tek = kendala_df[tim_col].dropna().astype(str).str.upper().value_counts().nlargest(5).reset_index()
                        if not top_tek.empty:
                            top_tek.columns = ['Teknisi', 'Jumlah']
                            html_bars = '<div style="display: flex; flex-direction: column; justify-content: space-evenly; height: 300px; padding: 5px 0;">'
                            max_val = top_tek['Jumlah'].max()
                            rank_colors = ['#ef4444', '#f97316', '#f59e0b', '#eab308', '#facc15']
                            
                            for i, row in enumerate(top_tek.itertuples()):
                                rank = i + 1
                                name = row.Teknisi
                                val = row.Jumlah
                                color = rank_colors[i] if i < len(rank_colors) else rank_colors[-1]
                                width_pct = (val / max_val) * 100 if max_val > 0 else 0
                                
                                html_bars += f'<div style="display: flex; align-items: center; width: 100%;">'
                                html_bars += f'<div style="background-color: #1e293b; color: #94a3b8; border-radius: 4px; width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold; margin-right: 12px; flex-shrink: 0;">{rank}</div>'
                                html_bars += f'<div style="color: white; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8); width: 140px; white-space: normal; word-wrap: break-word; line-height: 1.2; font-size: 0.9rem; margin-right: 10px; flex-shrink: 0;" title="{name}">{name}</div>'
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
                        
        import streamlit.components.v1 as components
        components.html("""
        <script>
        setTimeout(function() {
            const markers = window.parent.document.querySelectorAll('.custom-border-target');
            markers.forEach(marker => {
                let parent = marker.closest('[data-testid="stVerticalBlockBorderWrapper"]');
                if (!parent) parent = marker.closest('[data-testid="stVerticalBlock"]');
                if (parent) {
                    parent.style.setProperty('border', '2.5px solid #94a3b8', 'important');
                    parent.style.setProperty('border-radius', '12px', 'important');
                    parent.style.setProperty('padding', '15px', 'important');
                    parent.style.setProperty('background-color', '#0f172a', 'important');
                }
            });
        }, 100);
        </script>
        """, height=0, width=0)
        
        st.markdown('<br>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-title-wrap"><div class="section-title">🚨 DAFTAR LENGKAP WO KENDALA (REAL-TIME)</div></div>', unsafe_allow_html=True)
        if len(kendala_df) > 0 and tim_col:
              kendala_df = kendala_df.reset_index(drop=True)
              kendala_df['NO'] = kendala_df.index + 1
              
              date_create_col = None
              if 'DATE CREATE REAL' in kendala_df.columns:
                  date_create_col = 'DATE CREATE REAL'
                  
              date_modified_col = None
              if 'DATE MODIFIED REAL' in kendala_df.columns:
                  date_modified_col = 'DATE MODIFIED REAL'
              
              cols_to_show = ['NO']
              if date_create_col:
                  cols_to_show.append(date_create_col)
              if date_modified_col:
                  cols_to_show.append(date_modified_col)
                  
              cols_to_show.append(tim_col)
              
              if order_col and order_col in kendala_df.columns:
                  cols_to_show.append(order_col)
                  
              cols_to_show.extend(['INFO ORDER', status_col])
              
              if morning_status_col: cols_to_show.append(morning_status_col)
              
              rename_dict = {
                  tim_col: 'MORNING TIM',
                  'INFO ORDER': 'NO WONUM & AO',
                  status_col: 'STATUS'
              }
              if date_create_col:
                  rename_dict[date_create_col] = 'DATE RE MASUK'
              if date_modified_col:
                  rename_dict[date_modified_col] = 'DATE MODIFIED'
              if order_col and order_col in kendala_df.columns:
                  rename_dict[order_col] = 'ORDER'
              
              disp_fail = kendala_df[cols_to_show].rename(columns=rename_dict)
              
              html_table = '<table style="width:100%; border-collapse: collapse; margin-top: 15px; font-size: 1.05rem; font-family: sans-serif; border: 2.5px solid #94a3b8;">'
              html_table += '<thead><tr style="background-color: #7f1d1d; color: white; text-align: center;">'
              for col in disp_fail.columns:
                  html_table += f'<th style="border: 1.5px solid #64748b; padding: 12px 8px;">{col}</th>'
              html_table += '</tr></thead><tbody>'
              
              for _, row in disp_fail.iterrows():
                  html_table += '<tr style="background-color: #0f172a; color: #cbd5e1; text-align: center;">'
                  for col_name in disp_fail.columns:
                      val = row[col_name]
                      display_val = val if pd.notna(val) and str(val).strip() != "" else "-"
                      
                      if col_name == 'STATUS':
                          val_str = str(val).upper().strip()
                          bg_color = 'transparent'
                          text_color = '#cbd5e1'
                          if val_str == 'STARTWORK': bg_color, text_color = '#6B7280', 'black'
                          elif val_str == 'CONTWORK': bg_color, text_color = '#2563EB', 'white'
                          elif val_str == 'INSTCOMP': bg_color, text_color = '#3B82F6', 'white'
                          elif val_str == 'ACTCOMP': bg_color, text_color = '#06B6D4', 'white'
                          elif val_str == 'VALCOMP': bg_color, text_color = '#14B8A6', 'white'
                          elif val_str == 'VALSTART': bg_color, text_color = '#10B981', 'white'
                          elif val_str == 'COMPWORK': bg_color, text_color = '#39ff14', 'black'
                          elif val_str == 'WORKFAIL': bg_color, text_color = '#DC2626', 'white'
                          elif val_str == 'CANCLWORK': bg_color, text_color = '#F59E0B', 'black'
                          
                          if bg_color != 'transparent':
                              display_val = f'<div style="background-color: {bg_color}; color: {text_color}; border-radius: 12px; padding: 4px 10px; display: inline-block; font-weight: bold; font-size: 12px;">{val_str}</div>'
                      elif col_name == 'ORDER':
                          val_str = str(val).upper().strip()
                          bg_color, text_color = 'transparent', 'white'
                          if val_str == 'AO TSEL': bg_color, text_color = '#7f1d1d', 'white'
                          elif val_str == 'PDA TSEL': bg_color, text_color = '#14532d', 'white'
                          elif val_str == 'INDIBIZ': bg_color, text_color = '#1e3a8a', 'white'
                          elif val_str == 'ISP VULA': bg_color, text_color = '#4b5563', 'black'
                          
                          if bg_color != 'transparent':
                              display_val = f'<div style="background-color: {bg_color}; color: {text_color}; border-radius: 12px; padding: 4px 10px; display: inline-block; font-weight: bold; font-size: 12px;">{val}</div>'
                              
                      if str(display_val).startswith('<div'):
                          html_table += f'<td style="border: 1.5px solid #475569; padding: 10px 8px; font-size: 0.8rem;">{display_val}</td>'
                      else:
                          html_table += f'<td style="border: 1.5px solid #475569; padding: 10px 8px; font-size: 0.8rem; font-weight: bold; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8);">{display_val}</td>'
                  html_table += '</tr>'
              html_table += '</tbody></table>'
              
              st.markdown(html_table.replace('\n', ''), unsafe_allow_html=True)
        else:
            st.success("🎉 Luar Biasa! Bersih, tidak ada satupun pesanan yang mengalami kendala.")

    elif menu == "DETAIL RE PERIODE":
        df_re_today_all = df_re_today.copy()
        if order_col:
            df_re_today = df_re_today[df_re_today[order_col].astype(str).str.upper().str.contains('AO', na=False)]
            df_ps_today = df_ps_today[df_ps_today[order_col].astype(str).str.upper().str.contains('AO', na=False)]
            kendala_df = kendala_df[kendala_df[order_col].astype(str).str.upper().str.contains('AO', na=False)]
            
        st.markdown(f'<div class="metric-container mc-blue" style="margin-bottom: 20px;"><div class="mc-title">📥 TOTAL JUMLAH RE HARI INI (AO TSEL)</div><div class="mc-value">{len(df_re_today)} <span style="font-size:1rem; color:#94a3b8">WO</span></div></div>', unsafe_allow_html=True)
        main_chart_container = st.container()
        with main_chart_container:
            st.markdown("<div class='custom-border-target'></div>", unsafe_allow_html=True)
            st.markdown('<div class="section-title-wrap"><div class="section-title">📈 DISTRIBUSI JAM MASUK RE & PROGRESS</div></div>', unsafe_allow_html=True)
        if len(df_re_today) > 0 and 'Jam_RE' in df_re_today.columns:
            jam_df = df_re_today[df_re_today['Jam_RE'] != 'Unknown'].copy()
            if not jam_df.empty:
                # Menyiapkan data 24 Jam dengan format 00:00
                all_hours = pd.DataFrame({'Jam': [f"{i:02d}:00" for i in range(24)]})
                
                # Tambahkan :00 ke Jam untuk formatting sumbu X
                jam_df['Jam'] = jam_df['Jam_RE'].astype(str).apply(lambda x: x.split(':')[0].zfill(2) + ':00' if ':' in str(x) else '00:00')
                
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
                ch_col1, ch_col2 = main_chart_container.columns([3, 1])
                
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
                    fig_jam.update_traces(line=dict(width=3, shape='spline'), fill='tozeroy', marker=dict(size=8), textposition='top center', textfont=dict(color='#ffffff'))
                    
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
                        trace.name = f'<b><span style="color:white; text-shadow:2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8);">{trace.name}</span></b>'

                    fig_jam.add_vrect(x0="00:00", x1="07:00", fillcolor="rgba(160, 160, 160, 0.25)", layer="below", line_width=0)
                    fig_jam.add_vrect(x0="16:00", x1="23:00", fillcolor="rgba(160, 160, 160, 0.25)", layer="below", line_width=0)
                            
                    fig_jam.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
                                         font=dict(color='#cbd5e1'), xaxis_title="Waktu (Jam)", yaxis_title="Jumlah WO", 
                                         margin=dict(t=10, b=40, l=50, r=10),
                                         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title=""),
                                         hovermode="x unified",
                                         hoverlabel=dict(bgcolor='#1e293b', font=dict(color='#ffffff')),
                                         xaxis=dict(fixedrange=True, dtick=2, range=[-0.5, 23.5], showgrid=True, gridwidth=1, gridcolor='#334155'),
                                         yaxis=dict(fixedrange=True, showgrid=True, gridwidth=1, gridcolor='#334155'))
                    fig_jam.update_xaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_jam.update_yaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_jam.update_traces(cliponaxis=False)
                    st.plotly_chart(fig_jam, use_container_width=True, config={'displayModeBar': False}, theme=None)
                    
                with ch_col2:
                    tot_re = len(df_re_today)
                    try:
                        df_re_today.to_csv(r"C:\Users\User\.gemini\antigravity\scratch\wfm_automation\debug_df_re.csv", index=False)
                    except Exception as e:
                        print(e)
                    tot_ps = len(df_ps_today)
                    tot_ken = len(kendala_df)
                    
                    if 'JAM KERJA' in df_re_today.columns:
                        tot_jk = len(df_re_today[df_re_today['JAM KERJA'].astype(str).str.upper() == 'JAM KERJA'])
                        df_djk = df_re_today[df_re_today['JAM KERJA'].astype(str).str.upper() != 'JAM KERJA']
                        tot_djk = len(df_djk)
                    else:
                        tot_jk = tot_re
                        df_djk = pd.DataFrame()
                        tot_djk = 0
                        
                    pct_jk = f"{(tot_jk/tot_re)*100:.1f}".rstrip('0').rstrip('.') if tot_re > 0 else "0"
                    pct_djk = f"{(tot_djk/tot_re)*100:.1f}".rstrip('0').rstrip('.') if tot_re > 0 else "0"

                    # Detail RE DILUAR JAM KERJA: DINI HARI (< 12:00) & SORE-MALAM (>= 12:00)
                    tot_dini = 0
                    tot_sore = 0
                    if not df_djk.empty:
                        def _extract_h_re(row):
                            for col in ['Jam_RE', 'JAM RE MASUK REAL', 'JAM RE MASUK', 'JAM RE', 'Jam']:
                                if col in row and pd.notna(row[col]):
                                    s = str(row[col]).strip()
                                    if ':' in s:
                                        try:
                                            return int(s.split(':')[0])
                                        except Exception:
                                            pass
                                    elif len(s) >= 2 and s[:2].isdigit():
                                        try:
                                            return int(s[:2])
                                        except Exception:
                                            pass
                            return None

                        h_series = df_djk.apply(_extract_h_re, axis=1)
                        tot_dini = int((h_series.fillna(0) < 12).sum())
                        tot_sore = int(tot_djk - tot_dini)
                        if tot_sore < 0:
                            tot_sore = 0

                    pct_dini = f"{(tot_dini/tot_re)*100:.1f}".rstrip('0').rstrip('.') if tot_re > 0 else "0"
                    pct_sore = f"{(tot_sore/tot_re)*100:.1f}".rstrip('0').rstrip('.') if tot_re > 0 else "0"
                    pct_dini_djk = f"{(tot_dini/tot_djk)*100:.1f}".rstrip('0').rstrip('.') if tot_djk > 0 else "0"
                    pct_sore_djk = f"{(tot_sore/tot_djk)*100:.1f}".rstrip('0').rstrip('.') if tot_djk > 0 else "0"
                    
                    ps_re_val = (tot_ps/tot_re)*100 if tot_re > 0 else 0
                    ps_re_pct = f"{ps_re_val:.2f}"
                    ps_re_color = "#22c55e" if ps_re_val >= 85.0 else "#ef4444"
                    
                    html_str = (
                        '<div style="border: 1px solid #334155; border-radius: 8px; padding: 20px; text-align: center; background-color: #0f172a; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">'
                        '<div style="font-size: 0.9rem; font-weight: bold; color: #cbd5e1; margin-bottom: 20px;">GRAND TOTAL WO AO TSEL</div>'
                        '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px 10px; margin-bottom: 20px;">'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #3b82f6; line-height: 1;">{tot_re}</div><div style="font-size: 12px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">RE Masuk</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #22c55e; line-height: 1;">{tot_ps}</div><div style="font-size: 12px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">Done PS</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #f59e0b; line-height: 1;">{tot_ken}</div><div style="font-size: 12px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">Kendala</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: {ps_re_color}; line-height: 1;">{ps_re_pct}%</div><div style="font-size: 12px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">PS/RE</div></div>'
                        '</div>'
                        f'<div style="border-top: 1px dashed #334155; padding-top: 16px; margin-top: auto; font-size: 1.05rem; font-weight: bold; color: #94a3b8; text-align: left;">'
                        f'<div style="display:flex; justify-content:space-between; margin-bottom:10px;"><span>RE JAM KERJA</span> <span style="color:white;">{tot_jk} ({pct_jk}%)</span></div>'
                        f'<div style="display:flex; justify-content:space-between; margin-bottom:6px;"><span>RE DILUAR JAM KERJA</span> <span style="color:white;">{tot_djk} ({pct_djk}%)</span></div>'
                        f'<div style="display:flex; justify-content:space-between; padding-left:14px; margin-bottom:4px; font-size:0.90rem; font-weight:bold; color:#a78bfa;" title="{pct_dini}% dari Total RE ({pct_dini_djk}% dari RE Diluar Jam Kerja)">'
                        f'<span>&bull; DINI HARI</span> <span style="color:#f1f5f9; font-weight:600;">{tot_dini} ({pct_dini}%)</span>'
                        f'</div>'
                        f'<div style="display:flex; justify-content:space-between; padding-left:14px; font-size:0.90rem; font-weight:bold; color:#a78bfa;" title="{pct_sore}% dari Total RE ({pct_sore_djk}% dari RE Diluar Jam Kerja)">'
                        f'<span>&bull; SORE-MALAM</span> <span style="color:#f1f5f9; font-weight:600;">{tot_sore} ({pct_sore}%)</span>'
                        f'</div>'
                        '</div>'
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
                    max_y_mini = df_cat['Jumlah'].max() if not df_cat.empty else 5
                    
                    fig_mini = px.line(df_cat, x='Jam', y='Jumlah', text='Text', markers=True)
                    fig_mini.update_traces(line=dict(width=2, color=color, shape='spline'), 
                                           fill='tozeroy', fillcolor=fill_color, 
                                           marker=dict(size=4, color=color), textposition='top center', 
                                           textfont=dict(color='#ffffff'), cliponaxis=False)
                    
                    fig_mini.update_layout(
                        title=dict(text=cat, font=dict(color=color, size=13), x=0.5, xanchor='center'),
                        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='#0f172a',
                        margin=dict(t=40, b=45, l=50, r=10),
                        xaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, dtick=8, title="Waktu (Jam)"),
                        yaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, showticklabels=True, title="Jumlah WO", range=[0, max_y_mini * 1.25 if max_y_mini > 0 else 1]),
                        hovermode="x unified",
                        hoverlabel=dict(bgcolor='#1e293b', font=dict(color='#ffffff')),
                        height=280
                    )
                    # Create a border around the plot area
                    fig_mini.update_xaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_mini.update_yaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    
                    with mini_cols[i]:
                        fig_mini.update_traces(cliponaxis=False)
                        st.plotly_chart(fig_mini, use_container_width=True, config={'displayModeBar': False}, theme=None)
            else:
                st.info("Format jam tidak valid.")
        else:
            st.info("Belum ada RE masuk hari ini.")
            
        def get_stats(df_data, jam_col):
            if df_data.empty or jam_col not in df_data.columns: return 0, "-", 0, "-"
            df_valid = df_data[df_data[jam_col].astype(str).str.contains(r'^\d{2}', regex=True, na=False)].copy()
            if df_valid.empty: return 0, "-", 0, "-"
            hours = pd.to_numeric(df_valid[jam_col].astype(str).str[:2], errors='coerce').dropna().astype(int)
            if hours.empty: return 0, "-", 0, "-"
            total = len(hours)
            min_h, max_h = hours.min(), hours.max()
            span = (max_h - min_h) + 1
            rata2 = total / span if span > 0 else 0
            val_counts = hours.value_counts()
            peak_h = val_counts.idxmax()
            peak_val = val_counts.max()
            rentang = f"{min_h:02d}:00 - {max_h:02d}:00 ({span} jam)"
            puncak = f"{peak_h:02d}:00 &rarr; {peak_val} WO"
            return total, rentang, rata2, puncak
            
        jam_df_ao = df_re_today[df_re_today['Jam_RE'] != 'Unknown'].copy()
        re_jk_ao = jam_df_ao[jam_df_ao['JAM KERJA'].astype(str).str.upper() == 'JAM KERJA']
        re_djk_ao = jam_df_ao[jam_df_ao['JAM KERJA'].astype(str).str.upper() != 'JAM KERJA']
        
        ps_df_ao = df_ps_today.copy()
        if 'Jam_Update' in ps_df_ao.columns:
            ps_df_ao['Hour'] = pd.to_numeric(ps_df_ao['Jam_Update'].astype(str).str[:2], errors='coerce')
        else:
            ps_df_ao['Hour'] = 0
        ps_jk_ao = ps_df_ao[ps_df_ao['Hour'] < 17]
        ps_djk_ao = ps_df_ao[ps_df_ao['Hour'] >= 17]
        
        t_re_jk, r_re_jk, rata_re_jk, p_re_jk = get_stats(re_jk_ao, 'Jam_RE')
        t_re_djk, r_re_djk, rata_re_djk, p_re_djk = get_stats(re_djk_ao, 'Jam_RE')
        t_ps_jk, r_ps_jk, rata_ps_jk, p_ps_jk = get_stats(ps_jk_ao, 'Jam_Update')
        t_ps_djk, r_ps_djk, rata_ps_djk, p_ps_djk = get_stats(ps_djk_ao, 'Jam_Update')
        
        total_re = t_re_jk + t_re_djk
        total_ps = t_ps_jk + t_ps_djk
        pct_re_jk = int((t_re_jk / total_re * 100) if total_re > 0 else 0)
        pct_re_djk = int((t_re_djk / total_re * 100) if total_re > 0 else 0)
        pct_ps_jk = int((t_ps_jk / total_ps * 100) if total_ps > 0 else 0)
        pct_ps_djk = int((t_ps_djk / total_ps * 100) if total_ps > 0 else 0)
        
        insight_re_text = f"Rata-rata RE masuk mencapai {rata_re_jk:.2f} WO/jam pada jam kerja, dan {rata_re_djk:.2f} WO/jam di luar jam kerja."
        insight_re_title = "Arus RE lebih tinggi pada jam kerja" if rata_re_jk >= rata_re_djk else "Arus RE lebih tinggi di luar jam kerja"
        insight_re_color = "#3b82f6" if rata_re_jk >= rata_re_djk else "#8b5cf6"
        
        insight_ps_text = f"Rata-rata PS mencapai {rata_ps_djk:.2f} WO/jam di luar jam kerja, dibandingkan {rata_ps_jk:.2f} WO/jam pada jam kerja."
        insight_ps_title = "Penyelesaian PS lebih tinggi di luar jam kerja" if rata_ps_djk >= rata_ps_jk else "Penyelesaian PS lebih optimal pada jam kerja"
        insight_ps_color = "#22c55e" if rata_ps_jk >= rata_ps_djk else "#f59e0b"
        
        analisa_header_html = f'''
        <style>
        .anl-wrapper {{ background-color: #0f172a; padding: 25px; border-radius: 15px; border: 1px solid #1e293b; margin-top: 20px; }}
        .anl-top {{ display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 25px; }}
        .anl-title-box {{ display: flex; flex-direction: column; }}
        .anl-title {{ font-size: 1.6rem; font-weight: 800; color: white; display: flex; align-items: center; gap: 10px; margin-bottom: 5px; }}
        .anl-subtitle {{ color: #cbd5e1; font-size: 0.95rem; }}
        .anl-period {{ display: flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.05); padding: 8px 15px; border-radius: 8px; color: #94a3b8; font-size: 0.85rem; border: 1px solid #334155; }}
        .anl-cards {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-bottom: 25px; }}
        .anl-card {{ border-radius: 12px; padding: 15px; display: flex; flex-direction: column; position: relative; overflow: hidden; border: 1px solid #334155; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }}
        .anl-c-blue {{ background: linear-gradient(135deg, rgba(59,130,246,0.15) 0%, rgba(59,130,246,0.02) 100%); border-top: 3.5px solid #3b82f6; }}
        .anl-c-purp {{ background: linear-gradient(135deg, rgba(139,92,246,0.15) 0%, rgba(139,92,246,0.02) 100%); border-top: 3.5px solid #8b5cf6; }}
        .anl-c-gren {{ background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(34,197,94,0.02) 100%); border-top: 3.5px solid #22c55e; }}
        .anl-c-orng {{ background: linear-gradient(135deg, rgba(245,158,11,0.15) 0%, rgba(245,158,11,0.02) 100%); border-top: 3.5px solid #f59e0b; }}
        .anl-c-icon {{ display: flex; align-items: center; gap: 10px; margin-bottom: 12px; z-index: 2; }}
        .anl-c-circle {{ width: 35px; height: 35px; border-radius: 50%; display: flex; justify-content: center; align-items: center; color: white; font-weight: bold; font-size: 1.1rem; }}
        .anl-c-blue .anl-c-circle {{ background-color: #3b82f6; box-shadow: 0 0 10px rgba(59,130,246,0.5); }}
        .anl-c-purp .anl-c-circle {{ background-color: #8b5cf6; box-shadow: 0 0 10px rgba(139,92,246,0.5); }}
        .anl-c-gren .anl-c-circle {{ background-color: #22c55e; box-shadow: 0 0 10px rgba(34,197,94,0.5); }}
        .anl-c-orng .anl-c-circle {{ background-color: #f59e0b; box-shadow: 0 0 10px rgba(245,158,11,0.5); }}
        .anl-c-title {{ color: white; font-weight: bold; font-size: 0.95rem; line-height: 1.2; }}
        .anl-c-body {{ display: flex; justify-content: space-between; align-items: flex-end; z-index: 2; }}
        .anl-c-mainval {{ font-size: 2.2rem; font-weight: 900; color: #38bdf8; line-height: 1; }}
        .anl-c-purp .anl-c-mainval {{ color: #c084fc; }}
        .anl-c-gren .anl-c-mainval {{ color: #4ade80; }}
        .anl-c-orng .anl-c-mainval {{ color: #fbbf24; }}
        .anl-c-subval {{ font-size: 0.8rem; color: #94a3b8; font-weight: bold; }}
        .anl-c-right {{ text-align: right; }}
        .anl-c-r-title {{ font-size: 0.75rem; color: #cbd5e1; }}
        .anl-c-r-val {{ font-size: 1.1rem; color: white; font-weight: bold; line-height:1.2; }}
        .anl-c-r-sub {{ font-size: 0.7rem; color: #94a3b8; }}
        </style>
        <div class="anl-wrapper" style="margin-bottom: 20px;">
            <div class="anl-top">
                <div class="anl-title-box">
                    <div class="anl-title"><span style="color:#38bdf8;">&#128202;</span> Analisa Distribusi Jam Masuk RE & Progress PS (AO TSEL)</div>
                    <div class="anl-subtitle">Perbandingan rata-rata aktivitas pada jam kerja dan di luar jam kerja</div>
                </div>
                <div class="anl-period">
                    <span style="font-size:1.1rem; color:#60a5fa;">&#128197;</span>
                    <div>
                        <div style="font-size:0.7rem; font-weight:bold; color:white;">Periode Analisa</div>
                        Jam Kerja 07:00 - 15:00 <span style="margin:0 5px; color:#475569;">|</span> Di Luar Jam Kerja 18:00 - 22:00
                    </div>
                </div>
            </div>
            
            <div class="anl-cards">
                <div class="anl-card anl-c-blue">
                    <div class="anl-c-icon"><div class="anl-c-circle">&#128100;</div><div class="anl-c-title">Rata-rata RE Masuk<br><span style="font-weight:normal; font-size:0.8rem; color:#cbd5e1;">(Jam Kerja)</span></div></div>
                    <div class="anl-c-body">
                        <div><div class="anl-c-mainval">{rata_re_jk:.2f}</div><div class="anl-c-subval">WO / jam</div></div>
                        <div class="anl-c-right"><div class="anl-c-r-title">Total RE</div><div class="anl-c-r-val">{t_re_jk} <span style="font-size:0.7rem;">WO</span></div><div class="anl-c-r-sub">({pct_re_jk}% dari harian)</div></div>
                    </div>
                </div>
                <div class="anl-card anl-c-purp">
                    <div class="anl-c-icon"><div class="anl-c-circle">&#128100;</div><div class="anl-c-title">Rata-rata RE Masuk<br><span style="font-weight:normal; font-size:0.8rem; color:#cbd5e1;">(Di Luar Jam Kerja)</span></div></div>
                    <div class="anl-c-body">
                        <div><div class="anl-c-mainval">{rata_re_djk:.2f}</div><div class="anl-c-subval">WO / jam</div></div>
                        <div class="anl-c-right"><div class="anl-c-r-title">Total RE</div><div class="anl-c-r-val">{t_re_djk} <span style="font-size:0.7rem;">WO</span></div><div class="anl-c-r-sub">({pct_re_djk}% dari harian)</div></div>
                    </div>
                </div>
                <div class="anl-card anl-c-gren">
                    <div class="anl-c-icon"><div class="anl-c-circle">&#10004;</div><div class="anl-c-title">Rata-rata PS<br><span style="font-weight:normal; font-size:0.8rem; color:#cbd5e1;">(Jam Kerja)</span></div></div>
                    <div class="anl-c-body">
                        <div><div class="anl-c-mainval">{rata_ps_jk:.2f}</div><div class="anl-c-subval">WO / jam</div></div>
                        <div class="anl-c-right"><div class="anl-c-r-title">Total PS</div><div class="anl-c-r-val">{t_ps_jk} <span style="font-size:0.7rem;">WO</span></div><div class="anl-c-r-sub">({pct_ps_jk}% dari total)</div></div>
                    </div>
                </div>
                <div class="anl-card anl-c-orng">
                    <div class="anl-c-icon"><div class="anl-c-circle">&#10004;</div><div class="anl-c-title">Rata-rata PS<br><span style="font-weight:normal; font-size:0.8rem; color:#cbd5e1;">(Di Luar Jam Kerja)</span></div></div>
                    <div class="anl-c-body">
                        <div><div class="anl-c-mainval">{rata_ps_djk:.2f}</div><div class="anl-c-subval">WO / jam</div></div>
                        <div class="anl-c-right"><div class="anl-c-r-title">Total PS</div><div class="anl-c-r-val">{t_ps_djk} <span style="font-size:0.7rem;">WO</span></div><div class="anl-c-r-sub">({pct_ps_djk}% dari total)</div></div>
                    </div>
                </div>
            </div>
        </div>
        '''
        st.markdown('\n'.join(line.strip() for line in analisa_header_html.split('\n')), unsafe_allow_html=True)
        
        col_chart, col_side = st.columns([65, 35])
        
        with col_chart:
            ao_frames = []
            
            # Extract hourly bin for RE
            if not re_jk_ao.empty:
                re_jk_ao['Jam'] = re_jk_ao['Jam_RE'].astype(str).str[:2] + ":00"
                rjk = pd.merge(all_hours, re_jk_ao.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                rjk['Kategori'] = 'RE Masuk (Kerja)'
                ao_frames.append(rjk)
            if not re_djk_ao.empty:
                re_djk_ao['Jam'] = re_djk_ao['Jam_RE'].astype(str).str[:2] + ":00"
                rdjk = pd.merge(all_hours, re_djk_ao.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                rdjk['Kategori'] = 'RE Masuk (Luar Kerja)'
                ao_frames.append(rdjk)
            
            jam_ps_ao = ps_df_ao[ps_df_ao['Jam_Update'] != 'Unknown'].copy()
            if not jam_ps_ao.empty:
                jam_ps_ao['Jam'] = jam_ps_ao['Jam_Update'].astype(str).str[:2] + ":00"
                psjk = jam_ps_ao[jam_ps_ao['Hour'] < 17]
                psdjk = jam_ps_ao[jam_ps_ao['Hour'] >= 17]
                
                if not psjk.empty:
                    p1 = pd.merge(all_hours, psjk.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                    p1['Kategori'] = 'Done PS (Kerja)'
                    ao_frames.append(p1)
                if not psdjk.empty:
                    p2 = pd.merge(all_hours, psdjk.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                    p2['Kategori'] = 'Done PS (Luar Kerja)'
                    ao_frames.append(p2)
                
            if ao_frames:
                ao_chart_df = pd.concat(ao_frames, ignore_index=True)
                ao_chart_df['Text'] = ao_chart_df['Jumlah'].apply(lambda x: str(int(x)) if x > 0 else '')
                
                fig_ao = px.line(ao_chart_df, x='Jam', y='Jumlah', color='Kategori', text='Text', markers=True,
                                color_discrete_map={
                                    'RE Masuk (Kerja)': '#3b82f6', 
                                    'RE Masuk (Luar Kerja)': '#8b5cf6', 
                                    'Done PS (Kerja)': '#22c55e', 
                                    'Done PS (Luar Kerja)': '#f59e0b'
                                })
                fig_ao.update_traces(line=dict(width=3, shape='spline'), textposition='top center', 
                                    textfont=dict(size=11, color='white', weight='bold'), 
                                    marker=dict(size=8, line=dict(width=2, color='white')))
                for i, trace in enumerate(fig_ao.data):
                    trace.fill = 'tozeroy'
                    if trace.name == 'RE Masuk (Kerja)': trace.fillcolor = 'rgba(59, 130, 246, 0.12)'
                    elif trace.name == 'RE Masuk (Luar Kerja)': trace.fillcolor = 'rgba(139, 92, 246, 0.12)'
                    elif trace.name == 'Done PS (Kerja)': trace.fillcolor = 'rgba(34, 197, 94, 0.12)'
                    elif trace.name == 'Done PS (Luar Kerja)': trace.fillcolor = 'rgba(245, 158, 11, 0.12)'

                fig_ao.update_layout(
                    plot_bgcolor='#0f172a', paper_bgcolor='#0f172a',
                    margin=dict(l=40, r=40, t=20, b=40),
                    xaxis=dict(title="Waktu (Jam)", color='#cbd5e1', showgrid=True, gridcolor='#1e293b', dtick=1),
                    yaxis=dict(title="Jumlah WO", color='#cbd5e1', showgrid=True, gridcolor='#1e293b'),
                    legend=dict(title="", orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color="#cbd5e1", size=13)),
                    height=490
                )
                st.plotly_chart(fig_ao, use_container_width=True, config={'displayModeBar': False})
            else:
                st.info("Data tidak tersedia untuk grafik.")

        with col_side:
            side_html = f'''
            <style>
            .side-panel {{ background-color: #0f172a; border-radius: 12px; border: 1px solid #1e293b; padding: 15px; height: 100%; display: flex; flex-direction: column; gap: 12px; }}
            .sp-section {{ border: 1px solid #1e293b; border-radius: 8px; padding: 12px; background-color: #020617; }}
            .sp-title {{ font-size: 0.9rem; color: white; font-weight: bold; display: flex; align-items: center; gap: 8px; margin-bottom: 12px; border-bottom: 1px dashed #334155; padding-bottom: 8px; }}
            .sp-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; text-align: center; }}
            .sp-box {{ background: rgba(255,255,255,0.03); border-radius: 6px; padding: 10px 5px; }}
            .sp-box-title {{ font-size: 0.8rem; color: #cbd5e1; font-weight: bold; margin-bottom: 5px; }}
            .sp-box-val {{ font-size: 1.4rem; font-weight: 900; color: white; }}
            .sp-box-val span {{ font-size: 0.75rem; color: #3b82f6; font-weight: bold; }}
            .sp-box-sub {{ font-size: 0.65rem; color: #94a3b8; margin-top: 3px; }}
            .sp-row {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; font-size: 0.85rem; }}
            .sp-row-label {{ color: white; display: flex; align-items: center; gap: 6px; font-weight: bold; }}
            .sp-row-val {{ color: #cbd5e1; font-weight: bold; }}
            .sp-row-val span {{ font-size: 0.7rem; font-weight: normal; margin-left: 2px; }}
            .insight-item {{ margin-bottom: 10px; font-size: 0.75rem; color: #cbd5e1; line-height: 1.4; position: relative; padding-left: 15px; }}
            .insight-item::before {{ content: "●"; position: absolute; left: 0; color: #3b82f6; font-size: 0.8rem; line-height: 1; top: 1px; }}
            .insight-item strong {{ color: white; font-size: 0.8rem; display: block; margin-bottom: 2px; }}
            .insight-item:nth-child(2)::before {{ color: #22c55e; }}
            .insight-item:nth-child(3)::before {{ color: #f59e0b; }}
            </style>
            <div class="side-panel">
                <div class="sp-section">
                    <div class="sp-title"><span style="color:#3b82f6;">&#128196;</span> Ringkasan Total</div>
                    <div class="sp-grid">
                        <div class="sp-box">
                            <div class="sp-box-title">RE Masuk</div>
                            <div class="sp-box-val">{total_re} <span>WO</span></div>
                            <div class="sp-box-sub">({pct_re_jk}% Kerja | {pct_re_djk}% Luar)</div>
                        </div>
                        <div class="sp-box">
                            <div class="sp-box-title">PS / Done</div>
                            <div class="sp-box-val">{total_ps} <span>WO</span></div>
                            <div class="sp-box-sub">({pct_ps_jk}% Kerja | {pct_ps_djk}% Luar)</div>
                        </div>
                    </div>
                </div>
                
                <div class="sp-section">
                    <div class="sp-title"><span style="color:#3b82f6;">&#128202;</span> Perbandingan Rata-rata <span style="font-size:0.7rem; color:#64748b; font-weight:normal;">(WO/jam)</span></div>
                    <div class="sp-row">
                        <div class="sp-row-label"><div class="badge-no b-blue" style="width:16px; height:16px; font-size:0.5rem; margin-right:3px;">&#128100;</div> RE Masuk</div>
                        <div class="sp-row-val">{rata_re_jk:.2f} <span>(Kerja)</span> <span style="color:#475569; margin:0 3px;">|</span> {rata_re_djk:.2f} <span>(Luar)</span></div>
                    </div>
                    <div class="sp-row" style="margin-bottom:0;">
                        <div class="sp-row-label"><div class="badge-no b-green" style="width:16px; height:16px; font-size:0.5rem; margin-right:3px;">&#10004;</div> PS / Done</div>
                        <div class="sp-row-val">{rata_ps_jk:.2f} <span>(Kerja)</span> <span style="color:#475569; margin:0 3px;">|</span> {rata_ps_djk:.2f} <span>(Luar)</span></div>
                    </div>
                </div>
                
                <div class="sp-section" style="flex-grow: 1; border: none; background: transparent; padding: 0;">
                    <div class="sp-title" style="border:none; margin-bottom:5px;"><span style="color:#3b82f6;">&#128161;</span> Insight Utama</div>
                    <div class="insight-item">
                        <strong style="color: {insight_re_color};">{insight_re_title}</strong>
                        {insight_re_text}
                    </div>
                    <div class="insight-item">
                        <strong style="color: {insight_ps_color};">{insight_ps_title}</strong>
                        {insight_ps_text}
                    </div>
                    <div class="insight-item">
                        <strong style="color: #f59e0b;">Pola Puncak Aktivitas WO</strong>
                        Puncak RE terjadi pada {p_re_jk[:5]} dan {p_re_djk[:5]}. Eksekusi PS memuncak pada {p_ps_jk[:5]}.
                    </div>
                </div>
            </div>
            '''
            st.markdown('\n'.join(line.strip() for line in side_html.split('\n')), unsafe_allow_html=True)

        analisa_table_html = f'''
        <style>
        .anl-bot-wrap {{ background-color: #0f172a; border-radius: 12px; border: 1px solid #1e293b; padding: 20px; margin-top: 10px; margin-bottom: 25px; }}
        .analisa-header {{ display: flex; align-items: center; gap: 10px; border-bottom: 2px solid #334155; padding-bottom: 12px; margin-bottom: 15px; }}
        .analisa-header span {{ font-size: 1.25rem; font-weight: bold; color: white; }}
        .analisa-table {{ width: 100%; border-collapse: collapse; text-align: center; color: white; font-size: 0.9rem; }}
        .analisa-table th {{ background-color: transparent; border-bottom: 1.5px solid #3b82f6; padding: 12px; font-weight: bold; color: #cbd5e1; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 0.5px; }}
        .analisa-table td {{ padding: 12px; border-bottom: 1px solid #1e293b; vertical-align: middle; }}
        .analisa-table tr:hover {{ background-color: rgba(255,255,255,0.02); }}
        .analisa-table tr:last-child td {{ border-bottom: none; }}
        .badge-no {{ display: inline-flex; justify-content: center; align-items: center; width: 22px; height: 22px; border-radius: 50%; color: white; font-weight: bold; font-size: 0.75rem; }}
        .b-blue {{ background-color: #3b82f6; }}
        .b-purple {{ background-color: #8b5cf6; }}
        .b-green {{ background-color: #22c55e; }}
        .b-orange {{ background-color: #f59e0b; }}
        .val-rata {{ color: #0ea5e9; font-weight: bold; font-size: 1.05rem; }}
        .val-rata span {{ font-size: 0.7rem; color: #94a3b8; font-weight: normal; margin-left: 2px; }}
        </style>
        <div class="anl-bot-wrap">
            <div class="analisa-header">
                <span style="font-size:1.5rem;">&#128196;</span><span>Tabel Analisa Detail</span>
            </div>
            <table class="analisa-table">
                <tr>
                    <th style="width:5%;">No</th>
                    <th style="text-align:left; width:25%;">Indikator</th>
                    <th style="width:15%;">Periode</th>
                    <th style="width:10%;">Total WO</th>
                    <th style="width:20%;">Rentang Waktu</th>
                    <th style="width:15%;">Rata-rata</th>
                    <th style="width:10%;">Puncak Aktivitas</th>
                </tr>
                <tr>
                    <td><div class="badge-no b-blue">1</div></td>
                    <td style="text-align:left; font-weight:bold;">RE Masuk &ndash; Jam Kerja</td>
                    <td style="color:#60a5fa; font-weight:bold;">Jam Kerja</td>
                    <td style="font-weight:bold; font-size:1rem;">{t_re_jk}</td>
                    <td>{r_re_jk}</td>
                    <td class="val-rata">{rata_re_jk:.2f} <span>WO/jam</span></td>
                    <td>{p_re_jk}</td>
                </tr>
                <tr>
                    <td><div class="badge-no b-purple">2</div></td>
                    <td style="text-align:left; font-weight:bold;">RE Masuk &ndash; Di Luar Jam Kerja</td>
                    <td style="color:#a78bfa; font-weight:bold;">Di Luar Jam Kerja</td>
                    <td style="font-weight:bold; font-size:1rem;">{t_re_djk}</td>
                    <td>{r_re_djk}</td>
                    <td class="val-rata">{rata_re_djk:.2f} <span>WO/jam</span></td>
                    <td>{p_re_djk}</td>
                </tr>
                <tr>
                    <td><div class="badge-no b-green">3</div></td>
                    <td style="text-align:left; font-weight:bold;">PS &ndash; Jam Kerja</td>
                    <td style="color:#4ade80; font-weight:bold;">Jam Kerja</td>
                    <td style="font-weight:bold; font-size:1rem;">{t_ps_jk}</td>
                    <td>{r_ps_jk}</td>
                    <td class="val-rata">{rata_ps_jk:.2f} <span>WO/jam</span></td>
                    <td>{p_ps_jk}</td>
                </tr>
                <tr>
                    <td><div class="badge-no b-orange">4</div></td>
                    <td style="text-align:left; font-weight:bold;">PS &ndash; Di Luar Jam Kerja</td>
                    <td style="color:#fbbf24; font-weight:bold;">Di Luar Jam Kerja</td>
                    <td style="font-weight:bold; font-size:1rem;">{t_ps_djk}</td>
                    <td>{r_ps_djk}</td>
                    <td class="val-rata">{rata_ps_djk:.2f} <span>WO/jam</span></td>
                    <td>{p_ps_djk}</td>
                </tr>
            </table>
        </div>
        '''
        st.markdown('\n'.join(line.strip() for line in analisa_table_html.split('\n')), unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-title-wrap"><div class="section-title">📑 Rekap RE Masuk Harian</div></div>', unsafe_allow_html=True)
        if len(df_re_today_all) > 0:
            try:
                rekap_df = df_re_today_all.copy()
                if 'DATE CREATE REAL' in rekap_df.columns:
                    rekap_df = rekap_df.sort_values('DATE CREATE REAL', ascending=True)
                elif 'Jam_RE' in rekap_df.columns:
                    rekap_df = rekap_df.sort_values('Jam_RE', ascending=True)
                
                cols_to_show = []
                cols_rename = {}
                
                if 'DATE CREATE REAL' in rekap_df.columns:
                    cols_to_show.append('DATE CREATE REAL')
                    cols_rename['DATE CREATE REAL'] = 'DATE RE MASUK'
                elif 'Jam_RE' in rekap_df.columns:
                    cols_to_show.append('Jam_RE')
                    cols_rename['Jam_RE'] = 'JAM RE MASUK REAL'
                    
                if order_col and order_col in rekap_df.columns:
                    cols_to_show.append(order_col)
                    cols_rename[order_col] = 'ORDER'
                    
                wz_col = find_col(['WORZONE', 'WORKZONE', 'Workzone', 'ZONE', 'Zone'])
                if wz_col and wz_col in rekap_df.columns:
                    cols_to_show.append(wz_col)
                    cols_rename[wz_col] = 'STO'
                    
                if 'INFO ORDER' in rekap_df.columns:
                    cols_to_show.append('INFO ORDER')
                    cols_rename['INFO ORDER'] = 'NO WONUM & AO'
                    
                if customer_col and customer_col in rekap_df.columns:
                    cols_to_show.append(customer_col)
                    cols_rename[customer_col] = 'CUSTOMER NAME'
                    
                if 'Status_Upper' in rekap_df.columns:
                    cols_to_show.append('Status_Upper')
                    cols_rename['Status_Upper'] = 'Status'
                    
                if tim_col and tim_col in rekap_df.columns:
                    cols_to_show.append(tim_col)
                    cols_rename[tim_col] = 'TIM'
                    
                if morning_status_col and morning_status_col in rekap_df.columns:
                    cols_to_show.append(morning_status_col)
                    cols_rename[morning_status_col] = 'STATUS WO'
                
                final_df = rekap_df[cols_to_show].copy()
                final_df = final_df.rename(columns=cols_rename)
                final_df.insert(0, 'NO', range(1, len(final_df) + 1))
                final_df = final_df.fillna('-')
                
                if 'CUSTOMER NAME' in final_df.columns:
                    final_df['CUSTOMER NAME'] = final_df['CUSTOMER NAME'].astype(str).str.upper()
                    
                with open(r"C:\Users\User\.gemini\antigravity\scratch\wfm_automation\debug_cols.txt", "w") as f_dbg: f_dbg.write(str(final_df.columns.tolist()))
                
                html_table = '<div style="height: 800px; overflow-y: auto; border: 2.5px solid #94a3b8; border-radius: 12px;">'
                html_table += '<table style="width: 100%; border-collapse: collapse; text-align: center; color: white; font-size: 0.85rem; font-family: sans-serif;">'
                html_table += '<thead style="position: sticky; top: 0; background-color: #16a34a; z-index: 1;"><tr>'
                for i, col in enumerate(final_df.columns):
                    unique_vals = sorted(list(set([str(x).strip() for x in final_df[col] if str(x).strip() != ''])))
                    
                    checkboxes_html = ""
                    for val in unique_vals:
                        import re as regex
                        clean_val = regex.sub('<[^<]+>', '', val)
                        checkboxes_html += f'''
                        <label style="display: flex; align-items: center; gap: 8px; cursor: pointer; color: #cbd5e1; font-size: 12px; padding: 2px 0;">
                            <input type="checkbox" class="filter-cb-{i}" value="{clean_val}" checked style="cursor: pointer; accent-color: #3b82f6; width: 14px; height: 14px;">
                            <span class="filter-text-{i}">{clean_val}</span>
                        </label>
                        '''
                        
                    html_table += f'''
                    <th style="padding: 12px; border-bottom: 2px solid #334155; vertical-align: middle; text-align: center; white-space: nowrap; position: relative;">
                        <div style="display: flex; justify-content: center; align-items: center; gap: 4px;">
                            <span style="font-weight: 900; font-size: 0.85rem; color: #ffffff; text-transform: uppercase; text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8); letter-spacing: 0.5px;">{col}</span>
                            <div class="custom-filter-icon" data-colindex="{i}" title="Filter {col}" style="cursor: pointer; color: #38bdf8; font-size: 12px; padding: 2px 4px; border-radius: 4px;">▼</div>
                        </div>
                        <div class="custom-filter-menu" id="filter-menu-{i}" style="display: none; position: absolute; top: 100%; right: 50%; transform: translateX(50%); background-color: #1e293b; border: 1px solid #475569; border-radius: 8px; padding: 12px; z-index: 100; text-align: left; min-width: 220px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);">
                            <input type="text" class="filter-search" data-colindex="{i}" placeholder="Cari..." style="width: 100%; padding: 6px 10px; margin-bottom: 12px; background-color: #0f172a; color: white; border: 1px solid #334155; border-radius: 4px; box-sizing: border-box; font-size: 12px; outline: none;">
                            <div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.7rem; color: #38bdf8; font-weight: bold; border-bottom: 1px solid #334155; padding-bottom: 8px;">
                                <span class="filter-select-all" data-colindex="{i}" style="cursor: pointer;">Pilih Semua</span>
                                <span class="filter-clear-all" data-colindex="{i}" style="cursor: pointer;">Bersihkan</span>
                            </div>
                            <div class="filter-options-container" style="max-height: 200px; overflow-y: auto; display: flex; flex-direction: column; gap: 4px; margin-bottom: 12px; padding-right: 5px;">
                                {checkboxes_html}
                            </div>
                            <div style="text-align: right; border-top: 1px solid #334155; padding-top: 12px;">
                                <button class="filter-apply-btn" style="background-color: #3b82f6; color: white; border: none; border-radius: 4px; padding: 6px 16px; font-size: 12px; font-weight: bold; cursor: pointer; width: 100%;">Terapkan</button>
                            </div>
                        </div>
                    </th>'''
                html_table += '</tr></thead><tbody id="rekap-tbody">'
                
                for _, row in final_df.iterrows():
                    html_table += '<tr style="border-bottom: 2px solid #1e293b; background-color: #0f172a;">'
                    for col in final_df.columns:
                        val = row[col]
                        
                        if col == 'Status':
                            val_str = str(val).upper().strip()
                            bg_color = 'transparent'
                            text_color = 'white'
                            if val_str == 'STARTWORK':
                                bg_color = '#6B7280'
                                text_color = 'black'
                            elif val_str == 'CONTWORK':
                                bg_color = '#2563EB'
                                text_color = 'white'
                            elif val_str == 'INSTCOMP':
                                bg_color = '#3B82F6'
                                text_color = 'white'
                            elif val_str == 'ACTCOMP':
                                bg_color = '#06B6D4'
                                text_color = 'white'
                            elif val_str == 'VALCOMP':
                                bg_color = '#14B8A6'
                                text_color = 'white'
                            elif val_str == 'VALSTART':
                                bg_color = '#10B981'
                                text_color = 'white'
                            elif val_str == 'COMPWORK':
                                bg_color = '#39ff14'
                                text_color = 'black'
                            elif val_str == 'WORKFAIL':
                                bg_color = '#DC2626'
                                text_color = 'white'
                            elif val_str == 'CANCLWORK':
                                bg_color = '#F59E0B'
                                text_color = 'black'
                            
                            pill = f'<div style="background-color: {bg_color}; color: {text_color}; border-radius: 12px; padding: 4px 10px; display: inline-block; font-weight: bold; font-size: 12px;">{val}</div>'
                            html_table += f'<td style="padding: 10px;">{pill}</td>'
                        elif col == 'ORDER':
                            val_str = str(val).upper().strip()
                            bg_color, text_color = 'transparent', 'white'
                            if val_str == 'AO TSEL': bg_color, text_color = '#7f1d1d', 'white'
                            elif val_str == 'PDA TSEL': bg_color, text_color = '#14532d', 'white'
                            elif val_str == 'INDIBIZ': bg_color, text_color = '#1e3a8a', 'white'
                            elif val_str == 'ISP VULA': bg_color, text_color = '#4b5563', 'black'
                            
                            if bg_color != 'transparent':
                                pill = f'<div style="background-color: {bg_color}; color: {text_color}; border-radius: 12px; padding: 4px 10px; display: inline-block; font-weight: bold; font-size: 12px;">{val}</div>'
                                html_table += f'<td style="padding: 10px;">{pill}</td>'
                            else:
                                html_table += f'<td style="padding: 10px; font-size: 0.75rem; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8);">{val}</td>'
                        else:
                            html_table += f'<td style="padding: 10px; font-size: 0.75rem; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8);">{val}</td>'
                    html_table += '</tr>'
                
                html_table += '</tbody></table></div>'
                
                st.markdown(html_table.replace('\n', ''), unsafe_allow_html=True)
                
                # --- JAVASCRIPT INJECTION UNTUK FILTER TABEL (ADVANCED) ---
                js_filter = '''
                <script>
                const parentDoc = window.parent.document;
                function setupAdvancedFilters() {
                    const icons = parentDoc.querySelectorAll('.custom-filter-icon');
                    if (icons.length === 0) return;
                    
                    icons.forEach(icon => {
                        if (icon.dataset.listener) return;
                        icon.addEventListener('click', function(e) {
                            e.stopPropagation();
                            const colIdx = this.getAttribute('data-colindex');
                            const menu = parentDoc.getElementById('filter-menu-' + colIdx);
                            const isHidden = menu.style.display === 'none';
                            parentDoc.querySelectorAll('.custom-filter-menu').forEach(m => m.style.display = 'none');
                            if (isHidden) {
                                menu.style.display = 'block';
                            }
                        });
                        icon.dataset.listener = 'true';
                    });

                    if (!parentDoc.body.dataset.filterClick) {
                        parentDoc.body.addEventListener('click', function(e) {
                            if (!e.target.closest('.custom-filter-menu') && !e.target.closest('.custom-filter-icon')) {
                                parentDoc.querySelectorAll('.custom-filter-menu').forEach(m => m.style.display = 'none');
                            }
                        });
                        parentDoc.body.dataset.filterClick = 'true';
                    }

                    const searchInputs = parentDoc.querySelectorAll('.filter-search');
                    searchInputs.forEach(input => {
                        if (input.dataset.listener) return;
                        input.addEventListener('keyup', function() {
                            const term = this.value.toLowerCase();
                            const colIdx = this.getAttribute('data-colindex');
                            const labels = parentDoc.querySelectorAll('.filter-text-' + colIdx);
                            labels.forEach(label => {
                                const text = label.textContent.toLowerCase();
                                const container = label.parentElement;
                                if (text.includes(term)) {
                                    container.style.display = 'flex';
                                } else {
                                    container.style.display = 'none';
                                }
                            });
                        });
                        input.dataset.listener = 'true';
                    });

                    parentDoc.querySelectorAll('.filter-select-all').forEach(btn => {
                        if (btn.dataset.listener) return;
                        btn.addEventListener('click', function() {
                            const colIdx = this.getAttribute('data-colindex');
                            parentDoc.querySelectorAll('.filter-cb-' + colIdx).forEach(cb => {
                                if (cb.parentElement.style.display !== 'none') {
                                    cb.checked = true;
                                }
                            });
                        });
                        btn.dataset.listener = 'true';
                    });

                    parentDoc.querySelectorAll('.filter-clear-all').forEach(btn => {
                        if (btn.dataset.listener) return;
                        btn.addEventListener('click', function() {
                            const colIdx = this.getAttribute('data-colindex');
                            parentDoc.querySelectorAll('.filter-cb-' + colIdx).forEach(cb => {
                                if (cb.parentElement.style.display !== 'none') {
                                    cb.checked = false;
                                }
                            });
                        });
                        btn.dataset.listener = 'true';
                    });

                    parentDoc.querySelectorAll('.filter-apply-btn').forEach(btn => {
                        if (btn.dataset.listener) return;
                        btn.addEventListener('click', function() {
                            applyTableFilters();
                            parentDoc.querySelectorAll('.custom-filter-menu').forEach(m => m.style.display = 'none');
                        });
                        btn.dataset.listener = 'true';
                    });
                }

                function applyTableFilters() {
                    const tbody = parentDoc.getElementById('rekap-tbody');
                    if (!tbody) return;
                    const trs = tbody.getElementsByTagName('tr');
                    
                    const menus = parentDoc.querySelectorAll('.custom-filter-menu');
                    const filters = {};
                    menus.forEach(menu => {
                        const id = menu.getAttribute('id');
                        const colIdx = parseInt(id.replace('filter-menu-', ''));
                        const checkboxes = menu.querySelectorAll('.filter-cb-' + colIdx + ':checked');
                        const selected = Array.from(checkboxes).map(cb => cb.value.toLowerCase().trim());
                        filters[colIdx] = selected;
                    });

                    let visibleCount = 1;
                    for (let i = 0; i < trs.length; i++) {
                        let tr = trs[i];
                        let show = true;
                        
                        for (let colIdx in filters) {
                            const allowedVals = filters[colIdx];
                            if (allowedVals.length === 0) {
                                show = false;
                                break;
                            }
                            
                            const totalCbs = parentDoc.querySelectorAll('.filter-cb-' + colIdx).length;
                            if (allowedVals.length === totalCbs) {
                                continue;
                            }

                            let td = tr.getElementsByTagName('td')[colIdx];
                            if (td) {
                                let cellText = (td.textContent || td.innerText).toLowerCase().trim();
                                if (!allowedVals.includes(cellText)) {
                                    show = false;
                                    break;
                                }
                            }
                        }
                        tr.style.display = show ? "" : "none";
                        if (show) {
                            let td0 = tr.getElementsByTagName('td')[0];
                            if (td0) {
                                td0.innerHTML = visibleCount;
                            }
                            visibleCount++;
                        }
                    }
                }

                let filterInterval = setInterval(() => {
                    if (parentDoc.getElementById('rekap-tbody')) {
                        setupAdvancedFilters();
                        clearInterval(filterInterval);
                    }
                }, 500);
                </script>
                '''
                import streamlit.components.v1 as components
                components.html(js_filter, width=0, height=0)
            except Exception as e:
                st.error(f"Gagal memproses Rekap RE: {e}")
        else:
            st.warning("Belum ada data RE masuk untuk hari ini.")

    elif menu == "DETAIL MANJA":
        st.markdown("""
        <style>
        .cp-container { color: #f1f5f9; font-size: 1.25rem; max-height: 800px; }
        .manja-header { display: grid; grid-template-columns: minmax(0, 2fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr); background: #4c1d95; font-weight: bold; color: #ffffff; font-size: 15px; align-items: stretch; padding: 0; }
        .manja-header > div { padding: 9px 10px; display: flex; align-items: center; justify-content: center; text-align: center; }
        .cp-container .manja-header > div:nth-child(1) { justify-content: center; text-align: center; }
        
        .manja-row { display: grid; grid-template-columns: minmax(0, 2fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr); border-bottom: 1px solid #334155; align-items: stretch; font-size: 13px; padding: 0; }
        .manja-row > div { padding: 4px 10px 10px 10px; border-right: 1px solid #334155; display: flex; align-items: center; justify-content: center; overflow: hidden; word-break: break-word; }
        .manja-row > div:nth-child(1) { justify-content: flex-start; text-align: left; }
        .manja-row > div:last-child { border-right: none; }
        
        .manja-grand { display: grid; grid-template-columns: minmax(0, 2fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr); background: #4c1d95; font-weight: bold; border-top: 2px solid #334155; color: #ffffff; font-size: 15px; align-items: stretch; padding: 0; }
        .manja-grand > div { padding: 9px 10px; border-right: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; text-align: center; }
        .cp-container .manja-grand > div:nth-child(1) { justify-content: center; text-align: center; }
        .manja-grand > div:last-child { border-right: none; }
        
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
                    <div style="display: flex; justify-content: space-between; margin-top: 15px; font-size: 12px; color: #cbd5e1; font-weight: bold;">
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
                            <div style="color: #f8fafc; font-size: 12px; font-weight: bold; font-family: sans-serif;">{flag} ({count})</div>
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
                    .node {{ background: #0f172a; border: 1px solid #3b82f6; border-radius: 8px; padding: 12px 8px; color: #f8fafc; font-size: 1.05rem; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.3); z-index: 3; position: relative; }}
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
                                <div style="display: flex; gap: 8px; color: white; font-weight: bold;"><div style="width: 20px; text-align: right;">{count_h1}</div><div style="width: 50px; text-align: right;">({int(round(pct_h1))}%)</div></div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 10px; color: #f8fafc; font-weight: bold; font-size: 0.9rem;">
                                <div style="width: 14px; height: 14px; border-radius: 50%; background-color: #f97316; box-shadow: 0 0 5px #f97316;"></div>
                                <div style="width: 85px;">MANJA HI</div>
                                <div style="display: flex; gap: 8px; color: white; font-weight: bold;"><div style="width: 20px; text-align: right;">{count_hi}</div><div style="width: 50px; text-align: right;">({int(round(pct_hi))}%)</div></div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 10px; color: #f8fafc; font-weight: bold; font-size: 0.9rem;">
                                <div style="width: 14px; height: 14px; border-radius: 50%; background-color: #eab308; box-shadow: 0 0 5px #eab308;"></div>
                                <div style="width: 85px;">MANJA H++</div>
                                <div style="display: flex; gap: 8px; color: white; font-weight: bold;"><div style="width: 20px; text-align: right;">{count_h2}</div><div style="width: 50px; text-align: right;">({int(round(pct_h2))}%)</div></div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 10px; color: #f8fafc; font-weight: bold; font-size: 0.9rem;">
                                <div style="width: 14px; height: 14px; border-radius: 50%; background-color: #22c55e; box-shadow: 0 0 5px #22c55e;"></div>
                                <div style="width: 85px;">NON MANJA</div>
                                <div style="display: flex; gap: 8px; color: white; font-weight: bold;"><div style="width: 20px; text-align: right;">{count_non}</div><div style="width: 50px; text-align: right;">({int(round(pct_non))}%)</div></div>
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
                    sc_html += f'<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; border-bottom: 1px solid #1e293b; padding-bottom: 10px;">'
                    sc_html += f'<div class="{t_class}" style="margin-bottom: 0;">{cbo}</div>'
                    sc_html += f'<div class="sc-total" style="margin-bottom: 0; font-size: 1.8rem;">{total_cbo} <span>WO</span></div>'
                    sc_html += f'</div>'
                    
                    cbo_data = hm_agg[hm_agg['CECK BY ORDER'] == cbo]
                    for j, flag in enumerate(flags):
                        count = cbo_data[cbo_data['FLAG MANJA'] == flag]['count'].sum() if flag in cbo_data['FLAG MANJA'].values else 0
                        pct = int(round((count / total_cbo * 100) if total_cbo > 0 else 0))
                        sc_html += f'<div class="sc-item">'
                        sc_html += f'<div class="sc-item-left"><div class="{dots[j]}"></div> {flag}</div>'
                        sc_html += f'<div style="display: flex; gap: 8px; color: white; font-weight: bold;"><div style="width: 20px; text-align: right;">{count}</div><div style="width: 50px; text-align: right;">({pct}%)</div></div>'
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
                html += f'<div style="font-weight: bold; color: #fbbf24;">{cbo}</div>'
                html += f'<div>{fmt_num(cbo_sum["MANJA H-1"])}</div><div>{fmt_num(cbo_sum["MANJA HI"])}</div><div>{fmt_num(cbo_sum["MANJA H++"])}</div><div>{fmt_num(cbo_sum["NON MANJA"])}</div><div>{fmt_num(cbo_sum["Grand Total"])}</div>'
                html += f'</div>'
                
                for wz, df_wz in df_cbo.groupby(level=1):
                    wz_sum = df_wz.sum()
                    html += f'<div class="manja-row" style="background-color: #0f172a;">'
                    html += f'<div style="padding-left: 16px; font-weight: bold; color: #38bdf8; border-left: 4px solid #3b82f6;">{wz}</div>'
                    html += f'<div>{fmt_num(wz_sum["MANJA H-1"])}</div><div>{fmt_num(wz_sum["MANJA HI"])}</div><div>{fmt_num(wz_sum["MANJA H++"])}</div><div>{fmt_num(wz_sum["NON MANJA"])}</div><div>{fmt_num(wz_sum["Grand Total"])}</div>'
                    html += f'</div>'
                    
                    for wonum, df_wonum in df_wz.groupby(level=2):
                        wonum_sum = df_wonum.sum()
                        html += f'<div class="manja-row">'
                        html += f'<div style="padding-left: 41px; color: white; font-weight: bold; border-left: 4px solid #10b981;">{wonum}</div>'
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

        # --- TREND CHARTS ---
        c1, c2 = st.columns(2)
        
        # Data preparation for both charts
        # Ensure we only use data for WO ODS (from GABUNGAN AV/AW columns)
        ods_col_tmp = find_col(['WO ODS', 'WO_ODS', 'ODS'])
        if ods_col_tmp:
            df_charts = df[df[ods_col_tmp].astype(str).str.strip().str.upper() == 'ONE DAY SERVICE'].copy()
        else:
            df_charts = df.copy()
            
        date_col = 'DATE CREATE REAL' if 'DATE CREATE REAL' in df_charts.columns else 'DATE RE'
        dt_series = pd.to_datetime(df_charts[date_col], format='mixed', errors='coerce')
        
        # Chart 1: Trend Status (Dalam Bulan) - Filter by start_date's month
        with c1:
            with st.container():
                st.markdown("<div class='custom-border-target'></div>", unsafe_allow_html=True)
                mask_month = (dt_series.dt.month == start_date.month) & (dt_series.dt.year == start_date.year)
                df_month = df_charts[mask_month].copy()
                df_month['Day'] = dt_series[mask_month].dt.day
                
                fig1 = go.Figure()
                max_y1 = 10
                if not df_month.empty:
                    counts = df_month.groupby(['Day', 'Status_Upper']).size().unstack(fill_value=0)
                    
                    import calendar
                    _, last_day = calendar.monthrange(start_date.year, start_date.month)
                    all_days = pd.Index(range(1, last_day + 1), name='Day')
                    counts = counts.reindex(all_days, fill_value=0)
                    
                    lines_config = [
                        ('COMPWORK', '#10b981', 'rgba(16, 185, 129, 0.2)', 'COMPWORK'),
                        ('STARTWORK', '#f59e0b', 'rgba(245, 158, 11, 0.2)', 'STARTWORK'),
                        ('WORKFAIL', '#ef4444', 'rgba(239, 68, 68, 0.2)', 'WORKFAIL'),
                        ('CANCLWORK', '#64748b', 'rgba(100, 116, 139, 0.2)', 'CANCELWORK')
                    ]
                    
                    for status, color, fill_color, label in lines_config:
                        y_vals = counts[status] if status in counts.columns else pd.Series(0, index=all_days)
                        text_vals = [str(int(v)) if v > 0 else "" for v in y_vals]
                        fig1.add_trace(go.Scatter(
                            x=all_days, y=y_vals, mode='lines+markers+text', name=label,
                            text=text_vals, textposition='top center', textfont=dict(color='white', size=11, weight='bold'),
                            line=dict(color=color, width=3, shape='spline'),
                            fill='tozeroy', fillcolor=fill_color,
                            marker=dict(color=color, size=6),
                            cliponaxis=False
                        ))
                    
                    max_y1 = counts.max().max() if not counts.empty else 10
                fig1.update_layout(
                    title=dict(text="TREND STATUS (DALAM BULAN)", font=dict(color="#f8fafc", size=14, family="sans-serif")),
                    plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='#0f172a',
                    font=dict(color='#cbd5e1', family="sans-serif"), margin=dict(l=30, r=20, t=50, b=30),
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=10)),
                    xaxis=dict(showgrid=False, tickmode='linear', dtick=3, tick0=1),
                    yaxis=dict(showgrid=True, gridcolor='#1e293b', zeroline=False, range=[0, max_y1 * 1.2 if max_y1 > 0 else 1]),
                    height=300
                )
                st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})
        
        # Chart 2: Trend WO Berdasarkan Date RE (Jam) - Filter by selected period
        with c2:
            with st.container():
                st.markdown("<div class='custom-border-target'></div>", unsafe_allow_html=True)
                mask_period = (dt_series.dt.date >= start_date) & (dt_series.dt.date <= end_date)
                df_period = df_charts[mask_period].copy()
                df_period['Hour'] = dt_series[mask_period].dt.hour
                
                fig2 = go.Figure()
                max_y2 = 10
                if not df_period.empty:
                    hourly = df_period.groupby('Hour').size()
                    all_hours = pd.Index(range(24), name='Hour')
                    hourly = hourly.reindex(all_hours, fill_value=0)
                    
                    x_labels = [f"{h:02d}:00" for h in all_hours]
                    text_vals = [str(int(v)) if v > 0 else "" for v in hourly]
                    
                    fig2.add_trace(go.Scatter(
                        x=x_labels, y=hourly, mode='lines+markers+text', name='WO',
                        text=text_vals, textposition='top center', textfont=dict(color='white', size=11, weight='bold'),
                        line=dict(color='#3b82f6', width=3, shape='spline'),
                        fill='tozeroy', fillcolor='rgba(59, 130, 246, 0.2)',
                        marker=dict(color='#3b82f6', size=6),
                        cliponaxis=False
                    ))
                    
                    max_y2 = hourly.max() if not hourly.empty else 10
                fig2.update_layout(
                    title=dict(text="TREND WO BERDASARKAN DATE RE (JAM)", font=dict(color="#f8fafc", size=14, family="sans-serif")),
                    plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='#0f172a',
                    font=dict(color='#cbd5e1', family="sans-serif"), margin=dict(l=30, r=20, t=50, b=30),
                    showlegend=False,
                    xaxis=dict(showgrid=False, tickangle=-45, nticks=12),
                    yaxis=dict(showgrid=True, gridcolor='#1e293b', zeroline=False, range=[0, max_y2 * 1.2 if max_y2 > 0 else 1]),
                    height=300
                )
                st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})
                
        import streamlit.components.v1 as components
        components.html("""
        <script>
        setTimeout(function() {
            const markers = window.parent.document.querySelectorAll('.custom-border-target');
            markers.forEach(marker => {
                let parent = marker.closest('[data-testid="stVerticalBlockBorderWrapper"]');
                if (!parent) parent = marker.closest('[data-testid="stVerticalBlock"]');
                if (parent) {
                    parent.style.setProperty('border', '2.5px solid #94a3b8', 'important');
                    parent.style.setProperty('border-radius', '12px', 'important');
                    parent.style.setProperty('padding', '15px', 'important');
                    parent.style.setProperty('background-color', '#0f172a', 'important');
                }
            });
        }, 100);
        </script>
        """, height=0, width=0)
            
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <style>
        .cp-container { color: #f1f5f9; font-size: 12px; max-height: 800px; }
        .manja-header { display: grid; grid-template-columns: 5% 30% 15% 10% 20% 10% 10%; background: linear-gradient(135deg, #d4af37 0%, #fef08a 50%, #d4af37 100%); font-weight: 900; color: #020617; font-size: 1.05rem; text-align: center; border-radius: 4px 4px 0 0; font-family: "Source Sans Pro", sans-serif; letter-spacing: 0.5px; text-transform: uppercase; padding: 0; }
        .manja-row { display: grid; grid-template-columns: 5% 30% 15% 10% 20% 10% 10%; border-bottom: 1px solid #334155; align-items: stretch; text-align: center; color: white; font-size: 13px; font-weight: bold; font-family: "Source Sans Pro", sans-serif; padding: 0; }
        .pill-compwork { background-color: #10b981; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold; font-size: 12px; display: inline-block; }
        .pill-startwork { background-color: #475569; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold; font-size: 12px; display: inline-block; }
        .pill-other { background-color: #3b82f6; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold; font-size: 12px; display: inline-block; }
        .manja-header > div { border-right: 2px solid rgba(0,0,0,0.3); display: flex; justify-content: center; align-items: center; padding: 6px 15px; }
        .manja-header > div:last-child { border-right: none; }
        .manja-row > div { border-right: 1px solid #64748b; display: flex; justify-content: center; align-items: center; padding: 8px 15px; }
        .cp-container .manja-row > div:nth-child(1) { justify-content: center !important; text-align: center !important; }
        .manja-row > div:last-child { border-right: none; }
        </style>
        <div class="section-title">📊 WO ODS HI</div>
        """, unsafe_allow_html=True)
        
        ods_col = find_col(['WO ODS', 'WO_ODS', 'ODS'])
        tgl_ods_col = find_col(['TANGGAL WO ODS', 'TGL ODS', 'TGL WO ODS'])
        
        if ods_col and tgl_ods_col:
            df['Parsed_Date_ODS'] = pd.to_datetime(df[tgl_ods_col], format='mixed', errors='coerce').dt.date
            df_ods = df[(df[ods_col].astype(str).str.strip().str.upper() == 'ONE DAY SERVICE') & 
                        (df['Parsed_Date_ODS'] >= start_date) & 
                        (df['Parsed_Date_ODS'] <= end_date) & 
                        (~df['Status_Upper'].str.contains('COMPLETE|WAPPR', na=False))].copy()
        else:
            df_ods = df[(df['Parsed_Date_RE'] >= start_date) & 
                        (df['Parsed_Date_RE'] <= end_date) & 
                        (~df['Status_Upper'].str.contains('COMPLETE|WAPPR', na=False))].copy()
        
        if len(df_ods) == 0:
            st.info("Tidak ada data WO ODS untuk periode ini.")
        else:
            html = '<div class="cp-container">'
            html += """
<div class="manja-header">
    <div>NO</div>
    <div>NO WONUM & AO</div>
    <div>DATE RE</div>
    <div>WORKZONE</div>
    <div>TIM</div>
    <div>STATUS</div>
    <div>DETAIL WO</div>
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
                val_str = status.upper().strip()
                bg_color = 'transparent'
                text_color = 'white'
                if val_str == 'STARTWORK':
                    bg_color = '#6B7280'
                    text_color = 'black'
                elif val_str == 'CONTWORK':
                    bg_color = '#2563EB'
                    text_color = 'white'
                elif val_str == 'INSTCOMP':
                    bg_color = '#3B82F6'
                    text_color = 'white'
                elif val_str == 'ACTCOMP':
                    bg_color = '#06B6D4'
                    text_color = 'white'
                elif val_str == 'VALCOMP':
                    bg_color = '#14B8A6'
                    text_color = 'white'
                elif val_str == 'VALSTART':
                    bg_color = '#10B981'
                    text_color = 'white'
                elif val_str == 'COMPWORK':
                    bg_color = '#39ff14'
                    text_color = 'black'
                elif val_str == 'WORKFAIL':
                    bg_color = '#DC2626'
                    text_color = 'white'
                elif val_str == 'CANCLWORK':
                    bg_color = '#F59E0B'
                    text_color = 'black'
                
                status_html = f'<div style="background-color: {bg_color}; color: {text_color}; border-radius: 12px; padding: 4px 10px; display: inline-block; font-weight: bold; font-size: 12px;">{status}</div>'
                    
                morning_st = str(row['MORNING STATUS WO']) if 'MORNING STATUS WO' in row and pd.notna(row['MORNING STATUS WO']) else ""
                if morning_st.lower() == 'nan': morning_st = ""
                
                html += f"""
<div class="manja-row">
    <div>{i}</div>
    <div>{no_wonum}</div>
    <div>{date_cr}</div>
    <div>{wz}</div>
    <div>{tim}</div>
    <div>{status_html}</div>
    <div>{morning_st}</div>
</div>
"""
            html += '</div>'
            st.markdown(html, unsafe_allow_html=True)
            
    elif menu == "TRIAL & FFG 60 HARI":
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
    <div style="background:#1e293b; padding:6px 15px; border-radius:6px; font-size:0.8rem; color:#94a3b8; border: 2px solid #475569;">
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
                <div style="position:absolute; left:{col0_x}px; top:10px; width:150px; text-align:center; background:#1e293b; padding:8px 0; border-radius:6px; border:2px solid #475569; color:#ffffff; font-size:1.0rem; font-weight:700; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">TOTAL ALL PS HI</div>
                <div style="position:absolute; left:{col1_x}px; top:10px; width:160px; text-align:center; background:#1e293b; padding:8px 0; border-radius:6px; border:2px solid #475569; color:#ffffff; font-size:1.0rem; font-weight:700; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">PS BY DATE RE</div>
                <div style="position:absolute; left:{col2_x}px; top:10px; width:160px; text-align:center; background:#1e293b; padding:8px 0; border-radius:6px; border:2px solid #475569; color:#ffffff; font-size:1.0rem; font-weight:700; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">JENIS ORDER</div>
                <div style="position:absolute; left:{col0_x}px; top:{root_y - 70}px; width:150px; height:140px; background:#0f172a; border:2px solid #475569; border-radius:12px; display:flex; flex-direction:column; justify-content:center; align-items:center; box-shadow: 0 4px 10px rgba(0,0,0,0.5); z-index:10;">
                    <i class="bi bi-file-earmark-text" style="color:#60a5fa; font-size:1.8rem; margin-bottom:8px;"></i>
                    <div style="color:#f8fafc; font-size:1.0rem; font-weight:700; margin-bottom:5px;">TOTAL PS</div>
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
                    <div style="position:absolute; left:{col1_x}px; top:{y - 40}px; width:160px; height:80px; background:#0f172a; border:2px solid #475569; border-left: 4px solid {col}; border-radius:8px; display:flex; flex-direction:column; justify-content:center; padding-left:15px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); z-index:10;">
                        <div style="color:#ffffff; font-size:1.1rem; font-weight:700; margin-bottom:3px; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">{k}</div>
                        <div style="display:flex; align-items:baseline; gap:5px;">
                            <div style="color:#f8fafc; font-size:1.2rem; font-weight:700;">{val}</div><div style="color:#ffffff; font-size:0.85rem; font-weight:700; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">WO</div><div style="color:{col}; font-size:0.9rem; font-weight:700; margin-left:3px; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">({pct:.0f}%)</div>
                        </div>
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
                    <div style="position:absolute; left:{col2_x}px; top:{y - 40}px; width:160px; height:80px; background:#0f172a; border:2px solid #475569; border-left: 4px solid {col}; border-radius:8px; display:flex; flex-direction:column; justify-content:center; padding-left:15px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); z-index:10;">
                        <div style="color:#ffffff; font-size:1.1rem; font-weight:700; margin-bottom:3px; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">{k}</div>
                        <div style="display:flex; align-items:baseline; gap:5px;">
                            <div style="color:#f8fafc; font-size:1.2rem; font-weight:700;">{val}</div><div style="color:#ffffff; font-size:0.85rem; font-weight:700; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">WO</div><div style="color:{col}; font-size:0.9rem; font-weight:700; margin-left:3px; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">({pct:.0f}%)</div>
                        </div>
                    </div>
                    """
                
                # --- INJECT PS TABLE (RIGHT SIDE) ---
                table_html = """
                <div style="position:absolute; left: 840px; right: 20px; top: 20px; bottom: 20px; background:#0f172a; border:2.5px solid #eab308; border-radius:8px; overflow-y:auto; overflow-x:auto; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.5);">
                    <table style="width:100%; border-collapse:collapse; color:white; font-size:11px; text-align:center; white-space:nowrap; font-family:sans-serif;">
                        <thead style="position:sticky; top:0; background:#eab308; color:black; font-weight:bold; border-bottom:2px solid #ca8a04; z-index:10;">
                            <tr>
                                <th style="padding:8px; border-right:1px solid #ca8a04;">NO</th>
                                <th style="padding:8px; border-right:1px solid #ca8a04;">DATE RE</th>
                                <th style="padding:8px; border-right:1px solid #ca8a04;">ORDER</th>
                                <th style="padding:8px; border-right:1px solid #ca8a04;">NO AO</th>
                                <th style="padding:8px;">PS BY DATE RE</th>
                            </tr>
                        </thead>
                        <tbody>
                """
                
                # Retrieve columns dynamically
                date_col = next((c for c in ['DATE CREATE REAL', 'Date Created', 'DATE CREATED', 'TANGGAL DATE CREATE'] if c in df_sankey.columns), None)
                wonum_col = next((c for c in ['INFO ORDER', 'NO WONUM & AO'] if c in df_sankey.columns), None)
                
                # Sort dataframe for the table
                df_table = df_sankey.copy()
                sort_order = {'PS HI': 0, 'PS H-': 1, 'PS H -': 1, 'PS H-²': 2, 'PS H -²': 2}
                df_table['sort_idx'] = df_table['PS_Kapan'].map(sort_order).fillna(99)
                df_table = df_table.sort_values(by=['sort_idx', date_col] if date_col else ['sort_idx'])
                
                for idx, row in enumerate(df_table.to_dict('records'), 1):
                    d_re = str(row.get(date_col, '')) if date_col else ''
                    if d_re.lower() == 'nan': d_re = ''
                    if '.' in d_re: d_re = d_re.split('.')[0]
                    
                    wonum_val = str(row.get(wonum_col, '')) if wonum_col else ''
                    no_ao = wonum_val
                    if '-' in wonum_val:
                        parts = wonum_val.split('-')
                        no_ao = parts[1].strip() if len(parts) > 1 else wonum_val.strip()
                    if no_ao.lower() == 'nan': no_ao = ''
                        
                    order_val = row.get('Order_Type', '')
                    ps_kapan = row.get('PS_Kapan', '')
                    
                    bg_row = '#1e293b' if idx % 2 == 0 else '#0f172a'
                    
                    table_html += f"""
                        <tr style="border-bottom:1px solid #334155; background:{bg_row};">
                            <td style="padding:8px; border-right:1px solid #334155;">{idx}</td>
                            <td style="padding:8px; border-right:1px solid #334155;">{d_re}</td>
                            <td style="padding:8px; border-right:1px solid #334155; font-weight:bold; color:#cbd5e1;">{order_val}</td>
                            <td style="padding:8px; border-right:1px solid #334155;">{no_ao}</td>
                            <td style="padding:8px; font-weight:bold; color:#eab308;">{ps_kapan}</td>
                        </tr>
                    """
                
                table_html += """
                        </tbody>
                    </table>
                </div>
                """
                
                final_html = f"""
                <div style="position:relative; width:100%; height:{height}px; background:#0b1120; border-radius:12px; border:2px solid #475569; overflow:hidden; margin-bottom:20px;">
                    <svg width="100%" height="100%" style="position:absolute; top:0; left:0; pointer-events:none;">
                        {svg_paths}
                    </svg>
                    {html_cards}
                    {table_html}
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
                            <div style="color:#ffffff; font-size:0.85rem; font-weight:700; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">{k}</div>
                        </div>
                        <div style="color:#f8fafc; font-size:1.7rem; font-weight:700; line-height:1; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">{v}</div>
                        <div style="color:#ffffff; font-size:0.85rem; margin-bottom:10px; font-weight:700; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">WO</div>
                        <div style="color:{col}; font-size:1.05rem; font-weight:700; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">{pct:.0f}%</div>
                    </div>
                    """
                    
                card2_inner = ""
                for k,v in l2_counts.items(): 
                    pct = (v / total_wo * 100) if total_wo > 0 else 0
                    col = color_map.get(k, '#ef4444')
                    card2_inner += f"""
                    <div style="display:flex; flex-direction:column; align-items:center; padding:0 15px;">
                        <div style="color:#ffffff; font-size:0.85rem; font-weight:700; margin-bottom:10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">{k}</div>
                        <div style="color:#f8fafc; font-size:1.7rem; font-weight:700; line-height:1; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">{v}</div>
                        <div style="color:#ffffff; font-size:0.85rem; margin-bottom:10px; font-weight:700; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">WO</div>
                        <div style="color:#10b981; font-size:1.05rem; font-weight:700; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">{pct:.0f}%</div>
                    </div>
                    """
                
                cards_html = f"""
                <div style="display:flex; gap:15px; margin-top:10px;">
                    <div style="flex:1; background:#0f172a; padding:15px; border-radius:8px; border: 2px solid #475569;">
                        <div style="color:#cbd5e1; font-size:0.9rem; font-weight:700; margin-bottom:15px;">RINGKASAN PS BY DATE RE</div>
                        <div style="display:flex; justify-content:space-around; text-align:center;">{card1_inner}</div>
                    </div>
                    <div style="flex:1; background:#0f172a; padding:15px; border-radius:8px; border: 2px solid #475569;">
                        <div style="color:#cbd5e1; font-size:0.9rem; font-weight:700; margin-bottom:15px;">RINGKASAN JENIS ORDER</div>
                        <div style="display:flex; justify-content:space-around; text-align:center;">{card2_inner}</div>
                    </div>
                    <div style="flex:1; background:#0f172a; padding:15px; border-radius:8px; border: 2px solid #475569; display:flex; flex-direction:column; justify-content:center; align-items:center;">
                        <div style="color:#cbd5e1; font-size:0.9rem; font-weight:700; margin-bottom:15px;">TOTAL KESELURUHAN</div>
                        <div style="display:flex; align-items:center; gap:15px;">
                            <i class="bi bi-clipboard-data" style="color:#60a5fa; font-size:2.5rem;"></i>
                            <div style="display:flex; flex-direction:column;">
                                <div style="display:flex; align-items:baseline; gap:5px;">
                                    <span style="color:#f8fafc; font-size:2rem; font-weight:700; line-height:1;">{total_wo}</span>
                                    <span style="color:#ffffff; font-size:0.95rem; font-weight:700; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">WO</span>
                                </div>
                                <div style="color:#10b981; font-size:1.25rem; font-weight:700; margin-top:5px; text-shadow: 2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.6);">100%</div>
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

        # --- TABEL MONITORING FFG ---
        st.markdown('<hr style="border-color: #334155; margin: 30px 0;">', unsafe_allow_html=True)
        import os
        ibooster_sync_time = "Belum Ada Data"
        ibooster_sync_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "last_ibooster_AO_TSEL.txt")
        if os.path.exists(ibooster_sync_file):
            try:
                with open(ibooster_sync_file, "r") as f:
                    content = f.read().strip()
                    parts = content.split(" | VIA ")
                    if len(parts) > 0:
                        ibooster_sync_time = parts[0].replace(" WIB", "")
            except:
                pass
                
        st.markdown(f'''
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
            <h3 style="color: #cbd5e1; font-weight: bold; margin: 0;">MONITORING FFG</h3>
            <div style="background-color: rgba(249, 115, 22, 0.15); border: 1px solid #ea580c; border-radius: 6px; padding: 4px 12px; color: #fb923c; font-size: 1.05rem; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                ⏱️ Last Ibooster: {ibooster_sync_time}
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        if 'PRIORITAS UNSPEC' in df.columns and 'DURASI FFG' in df.columns and 'HASIL UKUR IBOSSTER' in df.columns:
            df_ffg = df.copy()
            
            # Extract numeric duration
            df_ffg['Durasi_Num'] = df_ffg['DURASI FFG'].astype(str).str.extract(r'(\d+)')[0]
            df_ffg['Durasi_Num'] = pd.to_numeric(df_ffg['Durasi_Num'], errors='coerce').fillna(999)
            
            # Filter data
            if status_col in df_ffg.columns:
                df_ffg = df_ffg[df_ffg[status_col].astype(str).str.upper().str.strip() == 'COMPWORK']
            if 'CRM Order Type' in df_ffg.columns:
                df_ffg = df_ffg[df_ffg['CRM Order Type'].astype(str).str.upper().str.strip() == 'CREATE']
            
            # Filter Kategori FFG <= 60 hari:
            # 1. ONLINE tapi UNSPEC (PRIO 1 / PRIO 2)
            # 2. ðŸ”´ LOS (Loss of Signal)
            prio_unspec_s = df_ffg['PRIORITAS UNSPEC'].fillna('').astype(str).str.upper().str.strip()
            onu_status_s = df_ffg['ONU LINK STATUS'].fillna('').astype(str).str.upper().str.strip() if 'ONU LINK STATUS' in df_ffg.columns else pd.Series('', index=df_ffg.index)
            hasil_ukur_s = df_ffg['HASIL UKUR IBOSSTER'].fillna('').astype(str).str.upper().str.strip() if 'HASIL UKUR IBOSSTER' in df_ffg.columns else pd.Series('', index=df_ffg.index)
            
            is_online_unspec = (onu_status_s.isin(['ONLINE', 'UP'])) & prio_unspec_s.str.contains('PRIO 1|PRIO 2', na=False)
            is_los = (onu_status_s == 'LOS') | (hasil_ukur_s == 'LOS')
            
            if 'ONU LINK STATUS' not in df_ffg.columns:
                cond_ffg = prio_unspec_s.str.contains('PRIO 1|PRIO 2', na=False) | (hasil_ukur_s == 'LOS')
            else:
                cond_ffg = is_online_unspec | is_los
            
            df_ffg = df_ffg[
                cond_ffg &
                (df_ffg['Durasi_Num'] <= 60)
            ].copy()
            
            if not df_ffg.empty:
                # 1. Build a structured Display DataFrame first
                ffg_data = []
                for idx, row in enumerate(df_ffg.to_dict('records'), 1):
                    date_val = str(row.get(date_col, '')) if date_col else ''
                    bulan_str = '-'
                    month_idx = 99
                    if date_val and str(date_val).lower() != 'nan':
                        try:
                            dt_obj = pd.to_datetime(date_val)
                            months_id = {1:'JANUARI', 2:'FEBRUARI', 3:'MARET', 4:'APRIL', 5:'MEI', 6:'JUNI', 7:'JULI', 8:'AGUSTUS', 9:'SEPTEMBER', 10:'OKTOBER', 11:'NOVEMBER', 12:'DESEMBER'}
                            bulan_str = months_id.get(dt_obj.month, '-')
                            month_idx = dt_obj.month
                        except:
                            pass
                            
                    nama_teknisi = str(row.get(tim_col, '-')) if tim_col else '-'
                    if nama_teknisi.lower() == 'nan': nama_teknisi = '-'
                    
                    order_val = str(row.get(order_col, '-')) if order_col else '-'
                    if order_val.lower() == 'nan': order_val = '-'
                    
                    wonum_ao_val = '-'
                    wonum_num_val = '-'
                    if 'NO WONUM & AO' in df_ffg.columns:
                        val = str(row.get('NO WONUM & AO', '-'))
                        if '-' in val:
                            parts = val.split('-')
                            wonum_num_val = parts[0].strip()
                            wonum_ao_val = parts[1].strip() if len(parts) > 1 else '-'
                        else:
                            wonum_num_val = val
                    if wonum_ao_val.lower() == 'nan': wonum_ao_val = '-'
                    
                    no_inet = str(row.get('Service No.', '-'))
                    if no_inet.endswith('.0'): no_inet = no_inet[:-2]
                    if no_inet.lower() == 'nan' or not no_inet.strip(): no_inet = '-'
                    
                    hasil_raw = str(row.get('HASIL UKUR IBOSSTER', '-')).strip()
                    onu_raw = str(row.get('ONU LINK STATUS', '-')).strip()
                    if hasil_raw.lower() == 'nan': hasil_raw = '-'
                    if onu_raw.lower() == 'nan': onu_raw = '-'
                    
                    if onu_raw.upper() == 'LOS' or hasil_raw.upper() == 'LOS':
                        onu_status = 'LOS'
                        hasil_ukur = 'LOS'
                    else:
                        onu_status = 'ONLINE'
                        hasil_ukur = hasil_raw if hasil_raw not in ['', 'nan'] else '-'
                    
                    prioritas = str(row.get('PRIORITAS UNSPEC', '-')).strip()
                    if prioritas.lower() == 'nan' or not prioritas:
                        prioritas = '-'
                    
                    durasi = str(row.get('DURASI FFG', '-')).upper().strip()
                    if durasi.lower() == 'nan' or not durasi:
                        durasi = '-'
                    
                    ffg_data.append({
                        'NO': idx,
                        'BULAN PS': bulan_str,
                        'NAMA TEKNISI': nama_teknisi,
                        'ORDER': order_val,
                        'WONUM (AO)': wonum_ao_val,
                        'NO INET': no_inet,
                        'HASIL UKUR': hasil_ukur,
                        'ONU LINK STATUS': onu_status,
                        'PRIORITAS': prioritas,
                        'DURASI FFG': durasi,
                        'Month_Index': month_idx
                    })
                    
                df_display = pd.DataFrame(ffg_data)
                
                if not df_display.empty:
                    def get_status_rank(val):
                        v = str(val).upper()
                        if 'LOS' in v: return 1
                        if 'ONLINE' in v: return 2
                        return 3
                    
                    df_display['Status_Rank'] = df_display['ONU LINK STATUS'].apply(get_status_rank)
                    df_display = df_display.sort_values(by=['Month_Index', 'Status_Rank', 'PRIORITAS'], ascending=[True, True, True])
                    df_display = df_display.drop(columns=['Month_Index', 'Status_Rank'])
                    df_display['NO'] = range(1, len(df_display) + 1)
                
                # 2. Build the HTML Table with Filters
                html_table = '<div style="width: 100%; min-height: 400px; overflow-x: auto; background-color: #0f172a; border-radius: 8px; border: 1px solid #334155;">'
                html_table += '<table style="width: 100%; border-collapse: collapse; color: white; font-size: 13px; font-family: sans-serif; text-align: center;">'
                html_table += '<thead><tr style="background-color: #eab308; color: black; font-weight: bold; border-bottom: 2px solid #ca8a04; font-size: 15px;">'
                
                # Build Headers with Filters
                for i, col in enumerate(df_display.columns):
                    unique_vals = df_display[col].astype(str).unique()
                    unique_vals = sorted(unique_vals)
                    
                    checkboxes_html = ""
                    for val in unique_vals:
                        import re as regex
                        clean_val = regex.sub('<[^<]+>', '', val)
                        checkboxes_html += f'<label style="display: flex; align-items: center; gap: 8px; cursor: pointer; color: #cbd5e1; font-size: 12px; padding: 2px 0;"><input type="checkbox" class="ffg-filter-cb-{i}" value="{clean_val}" checked style="cursor: pointer; accent-color: #3b82f6; width: 14px; height: 14px;"><span class="ffg-filter-text-{i}">{clean_val}</span></label>'
                        
                    html_table += f'<th style="padding: 12px; border: 1px solid #334155; vertical-align: middle; text-align: center; white-space: nowrap; position: relative;">'
                    html_table += f'<div style="display: flex; justify-content: center; align-items: center; gap: 4px;"><span>{col}</span>'
                    html_table += f'<div class="ffg-filter-icon" data-colindex="{i}" title="Filter {col}" style="cursor: pointer; color: #475569; font-size: 12px; padding: 2px 4px; border-radius: 4px;">&#9660;</div></div>'
                    
                    # Filter Menu Dropdown
                    html_table += f'<div class="ffg-filter-menu" id="ffg-filter-menu-{i}" style="display: none; position: absolute; top: 100%; right: 50%; transform: translateX(50%); background-color: #1e293b; border: 1px solid #475569; border-radius: 8px; padding: 12px; z-index: 100; text-align: left; min-width: 220px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5); font-weight: normal;">'
                    html_table += f'<input type="text" class="ffg-filter-search" data-colindex="{i}" placeholder="Cari..." style="width: 100%; padding: 6px 10px; margin-bottom: 12px; background-color: #0f172a; color: white; border: 1px solid #334155; border-radius: 4px; box-sizing: border-box; font-size: 12px; outline: none;">'
                    html_table += f'<div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.7rem; color: #38bdf8; font-weight: bold; border-bottom: 1px solid #334155; padding-bottom: 8px;"><span class="ffg-filter-select-all" data-colindex="{i}" style="cursor: pointer;">Pilih Semua</span><span class="ffg-filter-clear-all" data-colindex="{i}" style="cursor: pointer;">Bersihkan</span></div>'
                    html_table += f'<div class="ffg-filter-options-container" style="max-height: 200px; overflow-y: auto; display: flex; flex-direction: column; gap: 4px; margin-bottom: 12px; padding-right: 5px;">{checkboxes_html}</div>'
                    html_table += f'<div style="text-align: right; border-top: 1px solid #334155; padding-top: 12px;"><button class="ffg-filter-apply-btn" style="background-color: #3b82f6; color: white; border: none; border-radius: 4px; padding: 6px 16px; font-size: 12px; font-weight: bold; cursor: pointer; width: 100%;">Terapkan</button></div>'
                    html_table += '</div></th>'
                    
                html_table += '</tr></thead><tbody id="ffg-tbody">'
                
                # Build Rows
                for _, row in df_display.iterrows():
                    html_table += '<tr style="border-bottom: 1px solid #334155; font-size: 13px;">'
                    html_table += f'<td style="padding: 10px; border-right: 1px solid #334155;">{row["NO"]}</td>'
                    html_table += f'<td style="padding: 10px; border-right: 1px solid #334155;">{row["BULAN PS"]}</td>'
                    html_table += f'<td style="padding: 10px; border-right: 1px solid #334155;">{row["NAMA TEKNISI"]}</td>'
                    order_val = str(row["ORDER"]).strip().upper()
                    if order_val == "AO TSEL":
                        order_bg = "background-color: #831843; color: white; border-radius: 12px; padding: 4px 0px; width: 85px; text-align: center; display: inline-block; font-weight: bold; border: 1px solid #be123c; font-size: 11px; letter-spacing: 0.5px;"
                    elif order_val == "PDA TSEL":
                        order_bg = "background-color: #14532d; color: white; border-radius: 12px; padding: 4px 0px; width: 85px; text-align: center; display: inline-block; font-weight: bold; border: 1px solid #166534; font-size: 11px; letter-spacing: 0.5px;"
                    elif order_val == "INDIBIZ":
                        order_bg = "background-color: #1e3a8a; color: white; border-radius: 12px; padding: 4px 0px; width: 85px; text-align: center; display: inline-block; font-weight: bold; border: 1px solid #1d4ed8; font-size: 11px; letter-spacing: 0.5px;"
                    else:
                        order_bg = "background-color: #334155; color: white; border-radius: 12px; padding: 4px 0px; width: 85px; text-align: center; display: inline-block; font-weight: bold; font-size: 11px; letter-spacing: 0.5px;"
                    
                    html_table += f'<td style="padding: 10px; border-right: 1px solid #334155;"><span style="{order_bg}">{row["ORDER"]}</span></td>'
                    html_table += f'<td style="padding: 10px; border-right: 1px solid #334155; word-break: break-all;">{row["WONUM (AO)"]}</td>'
                    html_table += f'<td style="padding: 10px; border-right: 1px solid #334155;">{row["NO INET"]}</td>'
                    ukur_content = str(row["HASIL UKUR"])
                    if ukur_content != "-":
                        ukur_content = f'<span style="background-color: #b91c1c; color: #ffffff; padding: 3px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #ef4444; font-size: 12.5px; display: inline-block;">{ukur_content}</span>'
                    else:
                        ukur_content = '-'
                    
                    html_table += f'<td style="padding: 10px; border-right: 1px solid #334155; text-align: center;">{ukur_content}</td>'
                    
                    onu_status_raw = str(row["ONU LINK STATUS"]).strip().upper()
                    if onu_status_raw in ["ONLINE", "UP"]:
                        onu_status_content = '<span style="background-color: rgba(34, 197, 94, 0.15); color: #4ade80; padding: 3px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #22c55e; font-size: 12.5px; display: inline-block;">ONLINE</span>'
                    elif onu_status_raw == "LOS":
                        onu_status_content = '<span style="background-color: #b91c1c; color: #ffffff; padding: 3px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #ef4444; font-size: 12.5px; display: inline-block;">LOS</span>'
                    elif "DYING" in onu_status_raw:
                        onu_status_content = f'<span style="background-color: #ea580c; color: #ffffff; padding: 3px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #f97316; font-size: 12.5px; display: inline-block;">{row["ONU LINK STATUS"]}</span>'
                    elif onu_status_raw in ["OFFLINE", "DOWN"]:
                        onu_status_content = '<span style="background-color: #475569; color: #f1f5f9; padding: 3px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #64748b; font-size: 12.5px; display: inline-block;">OFFLINE</span>'
                    elif onu_status_raw != "-":
                        onu_status_content = f'<span style="background-color: #475569; color: #f1f5f9; padding: 3px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #64748b; font-size: 12.5px; display: inline-block;">{row["ONU LINK STATUS"]}</span>'
                    else:
                        onu_status_content = '-'
                    
                    html_table += f'<td style="padding: 10px; border-right: 1px solid #334155; text-align: center;">{onu_status_content}</td>'
                    html_table += f'<td style="padding: 10px; border-right: 1px solid #334155;">{row["PRIORITAS"]}</td>'
                    html_table += f'<td style="padding: 10px;">{row["DURASI FFG"]}</td>'
                    html_table += '</tr>'
                    
                html_table += '</tbody></table></div>'
                
                st.markdown(html_table, unsafe_allow_html=True)
                
                # Inject Javascript for FFG Table Filtering
                js_ffg_filter = '''<script>
                const parentDoc = window.parent.document;
                function setupFFGFilters() {
                    const icons = parentDoc.querySelectorAll('.ffg-filter-icon');
                    if (icons.length === 0) return;
                    
                    icons.forEach(icon => {
                        if (icon.dataset.listener) return;
                        icon.addEventListener('click', function(e) {
                            e.stopPropagation();
                            const colIdx = this.getAttribute('data-colindex');
                            const menu = parentDoc.getElementById('ffg-filter-menu-' + colIdx);
                            const isHidden = menu.style.display === 'none';
                            parentDoc.querySelectorAll('.ffg-filter-menu').forEach(m => m.style.display = 'none');
                            if (isHidden) {
                                menu.style.display = 'block';
                            }
                        });
                        icon.dataset.listener = 'true';
                    });
  
                    if (!parentDoc.body.dataset.ffgFilterClick) {
                        parentDoc.body.addEventListener('click', function(e) {
                            if (!e.target.closest('.ffg-filter-menu') && !e.target.closest('.ffg-filter-icon')) {
                                parentDoc.querySelectorAll('.ffg-filter-menu').forEach(m => m.style.display = 'none');
                            }
                        });
                        parentDoc.body.dataset.ffgFilterClick = 'true';
                    }
  
                    const searchInputs = parentDoc.querySelectorAll('.ffg-filter-search');
                    searchInputs.forEach(input => {
                        if (input.dataset.listener) return;
                        input.addEventListener('keyup', function() {
                            const term = this.value.toLowerCase();
                            const colIdx = this.getAttribute('data-colindex');
                            const labels = parentDoc.querySelectorAll('.ffg-filter-text-' + colIdx);
                            labels.forEach(label => {
                                const text = label.textContent.toLowerCase();
                                const container = label.parentElement;
                                if (text.includes(term)) {
                                    container.style.display = 'flex';
                                } else {
                                    container.style.display = 'none';
                                }
                            });
                        });
                        input.dataset.listener = 'true';
                    });
  
                    const selectAllBtns = parentDoc.querySelectorAll('.ffg-filter-select-all');
                    selectAllBtns.forEach(btn => {
                        if (btn.dataset.listener) return;
                        btn.addEventListener('click', function() {
                            const colIdx = this.getAttribute('data-colindex');
                            parentDoc.querySelectorAll('.ffg-filter-cb-' + colIdx).forEach(cb => {
                                if (cb.parentElement.style.display !== 'none') cb.checked = true;
                            });
                        });
                        btn.dataset.listener = 'true';
                    });
  
                    const clearAllBtns = parentDoc.querySelectorAll('.ffg-filter-clear-all');
                    clearAllBtns.forEach(btn => {
                        if (btn.dataset.listener) return;
                        btn.addEventListener('click', function() {
                            const colIdx = this.getAttribute('data-colindex');
                            parentDoc.querySelectorAll('.ffg-filter-cb-' + colIdx).forEach(cb => {
                                if (cb.parentElement.style.display !== 'none') cb.checked = false;
                            });
                        });
                        btn.dataset.listener = 'true';
                    });
  
                    const applyBtns = parentDoc.querySelectorAll('.ffg-filter-apply-btn');
                    applyBtns.forEach(btn => {
                        if (btn.dataset.listener) return;
                        btn.addEventListener('click', function() {
                            parentDoc.querySelectorAll('.ffg-filter-menu').forEach(m => m.style.display = 'none');
                            applyFFGFilters();
                        });
                        btn.dataset.listener = 'true';
                    });
                }
  
                function applyFFGFilters() {
                    const tbody = parentDoc.getElementById('ffg-tbody');
                    if (!tbody) return;
                    const trs = tbody.getElementsByTagName('tr');
                    
                    let filters = {};
                    const filterMenus = parentDoc.querySelectorAll('.ffg-filter-menu');
                    filterMenus.forEach(menu => {
                        const colIdx = menu.id.replace('ffg-filter-menu-', '');
                        const checkboxes = menu.querySelectorAll('.ffg-filter-cb-' + colIdx + ':checked');
                        const selected = Array.from(checkboxes).map(cb => cb.value.toLowerCase().trim());
                        filters[colIdx] = selected;
                    });
  
                    let visibleCount = 1;
                    for (let i = 0; i < trs.length; i++) {
                        let tr = trs[i];
                        let show = true;
                        
                        for (let colIdx in filters) {
                            const allowedVals = filters[colIdx];
                            if (allowedVals.length === 0) {
                                show = false;
                                break;
                            }
                            
                            const totalCbs = parentDoc.querySelectorAll('.ffg-filter-cb-' + colIdx).length;
                            if (allowedVals.length === totalCbs) {
                                continue;
                            }
  
                            let td = tr.getElementsByTagName('td')[colIdx];
                            if (td) {
                                let cellText = (td.textContent || td.innerText).toLowerCase().trim();
                                if (!allowedVals.includes(cellText)) {
                                    show = false;
                                    break;
                                }
                            }
                        }
                        tr.style.display = show ? "" : "none";
                        if (show) {
                            let td0 = tr.getElementsByTagName('td')[0];
                            if (td0) {
                                td0.innerHTML = visibleCount;
                            }
                            visibleCount++;
                        }
                    }
                }
  
                let ffgFilterInterval = setInterval(() => {
                    if (parentDoc.getElementById('ffg-tbody')) {
                        setupFFGFilters();
                        clearInterval(ffgFilterInterval);
                    }
                }, 500);
                </script>'''
                import streamlit.components.v1 as components
                components.html(js_ffg_filter, width=0, height=0)
            else:
                st.markdown('<div style="padding: 20px; color: #94a3b8; text-align: center; border: 1px solid #334155; border-radius: 8px; background: #0f172a;">Tidak ada data FFG yang memenuhi kriteria (PRIO 1/2 dan &le; 60 hari).</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="padding: 20px; color: #ef4444; text-align: center; border: 1px solid #334155; border-radius: 8px; background: #0f172a;">Kolom HASIL UKUR IBOSSTER, PRIORITAS UNSPEC, atau DURASI FFG tidak ditemukan di sumber data!</div>', unsafe_allow_html=True)

    elif menu == "PROGRESS PROVI":
        st.markdown('<div class="section-title-wrap"><div class="section-title">📸 REKAP & GRAFIK HARIAN PROGRESS TEKNISI PROVISIONING</div></div>', unsafe_allow_html=True)

        @st.cache_data(ttl=60, show_spinner=False)
        def load_rekap_progress_provi():
            import urllib.parse
            sheet_id = "1zA5ucYxE9gOSnKZIhEKQyV2rEdV5je__knsS9neA5iA"
            sheet_name = urllib.parse.quote("REKAP REPORTING PROGRESS TEKNISI")
            csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
            df_p = pd.read_csv(csv_url)
            df_p.columns = df_p.columns.astype(str).str.strip().str.upper()
            return df_p

        try:
            df_prog_raw = load_rekap_progress_provi()
        except Exception as e_prog:
            st.error(f"Gagal memuat sheet REKAP REPORTING PROGRESS TEKNISI: {e_prog}")
            df_prog_raw = pd.DataFrame()

        if not df_prog_raw.empty:
            tgl_col = next((c for c in df_prog_raw.columns if 'TANGGAL' in c), None)
            jam_col = next((c for c in df_prog_raw.columns if 'JAM' in c), None)
            tek_col = next((c for c in df_prog_raw.columns if 'TEKNISI' in c), None)
            wo_col = next((c for c in df_prog_raw.columns if 'WONUM' in c), None)
            notes_col = next((c for c in df_prog_raw.columns if 'NOTE' in c), None)
            wita_col = next((c for c in df_prog_raw.columns if 'WITA' in c), None)
            stat_col = next((c for c in df_prog_raw.columns if 'STATUS' in c), None)

            if tgl_col and jam_col and wo_col:
                # Bersihkan baris kosong (seperti nomor urut 1..1000 tanpa data WONUM / TANGGAL)
                df_prog = df_prog_raw[
                    df_prog_raw[wo_col].notna() &
                    (df_prog_raw[wo_col].astype(str).str.strip() != '') &
                    (df_prog_raw[wo_col].astype(str).str.strip().str.upper() != 'NAN') &
                    df_prog_raw[tgl_col].notna() &
                    (df_prog_raw[tgl_col].astype(str).str.strip() != '') &
                    (df_prog_raw[tgl_col].astype(str).str.strip().str.upper() != 'NAN')
                ].copy()

                # Parse tanggal dan filter sesuai periode di sidebar
                df_prog['Parsed_Date'] = pd.to_datetime(df_prog[tgl_col].astype(str).str.strip(), errors='coerce').dt.date
                df_prog_period = df_prog[
                    (df_prog['Parsed_Date'] >= start_date) &
                    (df_prog['Parsed_Date'] <= end_date)
                ].copy()

                # Parse Jam Kirim Progress (HH:MM:SS -> Hour 0..23 & label HH:00)
                def extract_hour_int(val):
                    s = str(val).strip()
                    if ':' in s:
                        p = s.split(':')[0].strip()
                        if p.isdigit():
                            h = int(p)
                            if 0 <= h <= 23:
                                return h
                    return -1

                df_prog_period['Hour_Int'] = df_prog_period[jam_col].apply(extract_hour_int)
                df_prog_period = df_prog_period[df_prog_period['Hour_Int'] >= 0].copy()
                df_prog_period['Jam'] = df_prog_period['Hour_Int'].apply(lambda h: f"{int(h):02d}:00")

                # Klasifikasi 4 Pembagian Progress:
                # - Progress Pagi  : 07:00 s/d 10:00 (Hour 7..10, termasuk <7 bila ada kiriman dini hari)
                # - Progress Siang : 11:00 s/d 14:00 (Hour 11..14)
                # - Progress Sore  : 15:00 s/d 18:00 (Hour 15..18)
                # - Progress Malam : 19:00 s/d 23:59 (Hour 19..23)
                def classify_sesi_progress(h):
                    if 7 <= h <= 10 or h < 7:
                        return 'PROGRESS PAGI'
                    elif 11 <= h <= 14:
                        return 'PROGRESS SIANG'
                    elif 15 <= h <= 18:
                        return 'PROGRESS SORE'
                    else:
                        return 'PROGRESS MALAM'

                df_prog_period['Kategori_Sesi'] = df_prog_period['Hour_Int'].apply(classify_sesi_progress)

                # Bersihkan nama teknisi (tanpa / PROV agar rapi di rekap)
                if tek_col:
                    df_prog_period['Teknisi_Clean'] = (
                        df_prog_period[tek_col].astype(str).str.strip()
                        .str.replace(r'(?i)\s*/\s*PROV.*$', '', regex=True)
                        .str.strip().str.upper()
                    )
                else:
                    df_prog_period['Teknisi_Clean'] = 'UNKNOWN'

                tot_all_prog = len(df_prog_period)
                tot_uniq_wo = df_prog_period[wo_col].astype(str).str.strip().nunique() if not df_prog_period.empty else 0
                tot_active_tek = df_prog_period['Teknisi_Clean'].nunique() if not df_prog_period.empty else 0

                tot_pagi = int((df_prog_period['Kategori_Sesi'] == 'PROGRESS PAGI').sum())
                tot_siang = int((df_prog_period['Kategori_Sesi'] == 'PROGRESS SIANG').sum())
                tot_sore = int((df_prog_period['Kategori_Sesi'] == 'PROGRESS SORE').sum())
                tot_malam = int((df_prog_period['Kategori_Sesi'] == 'PROGRESS MALAM').sum())

                # Top Metric Cards
                mc_c1, mc_c2, mc_c3, mc_c4, mc_c5 = st.columns(5)
                with mc_c1:
                    st.markdown(f'<div class="metric-container mc-blue" style="margin-bottom: 18px;"><div class="mc-title">📸 TOTAL PROGRESS</div><div class="mc-value">{tot_all_prog} <span style="font-size:0.95rem; color:#94a3b8">FOTO ({tot_uniq_wo} WO)</span></div></div>', unsafe_allow_html=True)
                with mc_c2:
                    st.markdown(f'<div class="metric-container mc-blue" style="margin-bottom: 18px; border-left-color:#38bdf8;"><div class="mc-title">🌅 PROGRESS PAGI (07-10)</div><div class="mc-value" style="color:#38bdf8;">{tot_pagi} <span style="font-size:0.95rem; color:#94a3b8">PROGRESS</span></div></div>', unsafe_allow_html=True)
                with mc_c3:
                    st.markdown(f'<div class="metric-container mc-green" style="margin-bottom: 18px;"><div class="mc-title">☀️ PROGRESS SIANG (11-14)</div><div class="mc-value" style="color:#22c55e;">{tot_siang} <span style="font-size:0.95rem; color:#94a3b8">PROGRESS</span></div></div>', unsafe_allow_html=True)
                with mc_c4:
                    st.markdown(f'<div class="metric-container mc-orange" style="margin-bottom: 18px;"><div class="mc-title">🌇 PROGRESS SORE (15-18)</div><div class="mc-value" style="color:#f59e0b;">{tot_sore} <span style="font-size:0.95rem; color:#94a3b8">PROGRESS</span></div></div>', unsafe_allow_html=True)
                with mc_c5:
                    st.markdown(f'<div class="metric-container" style="margin-bottom: 18px; border-left: 4px solid #8b5cf6;"><div class="mc-title">🌙 PROGRESS MALAM (19-23)</div><div class="mc-value" style="color:#a78bfa;">{tot_malam} <span style="font-size:0.95rem; color:#94a3b8">PROGRESS</span></div></div>', unsafe_allow_html=True)

                # Container Grafik Utama (Gaya identik dengan DETAIL RE PERIODE pada Gambar 2)
                prog_chart_container = st.container()
                with prog_chart_container:
                    st.markdown("<div class='custom-border-target'></div>", unsafe_allow_html=True)
                    st.markdown('<div class="section-title-wrap"><div class="section-title">📈 DISTRIBUSI JAM LAPORAN FOTO PROGRESS TEKNISI (PAGI / SIANG / SORE / MALAM)</div></div>', unsafe_allow_html=True)

                all_hours_prog = pd.DataFrame({'Jam': [f"{i:02d}:00" for i in range(24)]})
                sesi_list = ['PROGRESS PAGI', 'PROGRESS SIANG', 'PROGRESS SORE', 'PROGRESS MALAM']
                frames_prog = []
                for sesi_name in sesi_list:
                    df_sub_sesi = df_prog_period[df_prog_period['Kategori_Sesi'] == sesi_name]
                    cnt_df = pd.merge(
                        all_hours_prog,
                        df_sub_sesi.groupby('Jam').size().reset_index(name='Jumlah'),
                        on='Jam',
                        how='left'
                    ).fillna(0)
                    cnt_df['Kategori'] = sesi_name
                    frames_prog.append(cnt_df)

                chart_prog_df = pd.concat(frames_prog, ignore_index=True)
                chart_prog_df['Text'] = chart_prog_df['Jumlah'].apply(lambda x: str(int(x)) if x > 0 else '')

                ch_p1, ch_p2 = prog_chart_container.columns([3, 1])

                with ch_p1:
                    fig_prog = px.line(
                        chart_prog_df,
                        x='Jam',
                        y='Jumlah',
                        color='Kategori',
                        text='Text',
                        markers=True,
                        color_discrete_map={
                            'PROGRESS PAGI': '#3b82f6',
                            'PROGRESS SIANG': '#22c55e',
                            'PROGRESS SORE': '#f59e0b',
                            'PROGRESS MALAM': '#8b5cf6'
                        }
                    )
                    fig_prog.update_traces(
                        line=dict(width=3, shape='spline'),
                        fill='tozeroy',
                        marker=dict(size=8),
                        textposition='top center',
                        textfont=dict(color='#ffffff')
                    )

                    fill_colors_prog = {
                        'PROGRESS PAGI': 'rgba(59, 130, 246, 0.16)',
                        'PROGRESS SIANG': 'rgba(34, 197, 94, 0.16)',
                        'PROGRESS SORE': 'rgba(245, 158, 11, 0.16)',
                        'PROGRESS MALAM': 'rgba(139, 92, 246, 0.16)'
                    }
                    for trace in fig_prog.data:
                        if trace.name in fill_colors_prog:
                            trace.fillcolor = fill_colors_prog[trace.name]
                        trace.name = f'<b><span style="color:white; text-shadow:2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8);">{trace.name}</span></b>'

                    # Area background shading seperti pada contoh grafik Gambar 2
                    fig_prog.add_vrect(x0="00:00", x1="07:00", fillcolor="rgba(160, 160, 160, 0.25)", layer="below", line_width=0)
                    fig_prog.add_vrect(x0="18:00", x1="23:00", fillcolor="rgba(160, 160, 160, 0.25)", layer="below", line_width=0)

                    max_y_prog = chart_prog_df['Jumlah'].max() if not chart_prog_df.empty else 5
                    fig_prog.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(color='#cbd5e1'),
                        xaxis_title="Waktu (Jam)",
                        yaxis_title="Jumlah Progress",
                        margin=dict(t=10, b=40, l=50, r=10),
                        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title=""),
                        hovermode="x unified",
                        hoverlabel=dict(bgcolor='#1e293b', font=dict(color='#ffffff')),
                        xaxis=dict(fixedrange=True, dtick=2, range=[-0.5, 23.5], showgrid=True, gridwidth=1, gridcolor='#334155'),
                        yaxis=dict(fixedrange=True, showgrid=True, gridwidth=1, gridcolor='#334155', range=[0, max(max_y_prog * 1.22, 4)])
                    )
                    fig_prog.update_xaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_prog.update_yaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_prog.update_traces(cliponaxis=False)
                    st.plotly_chart(fig_prog, use_container_width=True, config={'displayModeBar': False}, theme=None)

                with ch_p2:
                    pct_pagi = f"{(tot_pagi / tot_all_prog) * 100:.1f}".rstrip('0').rstrip('.') if tot_all_prog > 0 else "0"
                    pct_siang = f"{(tot_siang / tot_all_prog) * 100:.1f}".rstrip('0').rstrip('.') if tot_all_prog > 0 else "0"
                    pct_sore = f"{(tot_sore / tot_all_prog) * 100:.1f}".rstrip('0').rstrip('.') if tot_all_prog > 0 else "0"
                    pct_malam = f"{(tot_malam / tot_all_prog) * 100:.1f}".rstrip('0').rstrip('.') if tot_all_prog > 0 else "0"

                    html_summary_prog = (
                        '<div style="border: 1px solid #334155; border-radius: 8px; padding: 20px; text-align: center; background-color: #0f172a; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">'
                        '<div style="font-size: 0.9rem; font-weight: bold; color: #cbd5e1; margin-bottom: 18px; letter-spacing: 0.5px;">GRAND TOTAL PROGRESS PROVI</div>'
                        '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 22px 10px; margin-bottom: 18px;">'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #3b82f6; line-height: 1;">{tot_pagi}</div><div style="font-size: 11px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">PAGI (07-10)</div><div style="font-size: 11px; color: #94a3b8;">{pct_pagi}%</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #22c55e; line-height: 1;">{tot_siang}</div><div style="font-size: 11px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">SIANG (11-14)</div><div style="font-size: 11px; color: #94a3b8;">{pct_siang}%</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #f59e0b; line-height: 1;">{tot_sore}</div><div style="font-size: 11px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">SORE (15-18)</div><div style="font-size: 11px; color: #94a3b8;">{pct_sore}%</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #8b5cf6; line-height: 1;">{tot_malam}</div><div style="font-size: 11px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">MALAM (19-23)</div><div style="font-size: 11px; color: #94a3b8;">{pct_malam}%</div></div>'
                        '</div>'
                        f'<div style="border-top: 1px dashed #334155; padding-top: 16px; margin-top: auto; font-size: 0.92rem; font-weight: bold; color: #94a3b8; text-align: left;">'
                        f'<div style="display:flex; justify-content:space-between; margin-bottom:8px;"><span>TOTAL PROGRESS</span> <span style="color:#38bdf8;">{tot_all_prog} FOTO</span></div>'
                        f'<div style="display:flex; justify-content:space-between; margin-bottom:8px;"><span>WO UNIK</span> <span style="color:#22c55e;">{tot_uniq_wo} WO</span></div>'
                        f'<div style="display:flex; justify-content:space-between;"><span>TEKNISI AKTIF</span> <span style="color:white;">{tot_active_tek} TIM</span></div>'
                        '</div>'
                        '</div>'
                    )
                    st.markdown(html_summary_prog, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                # --- 4 MINI SPARKLINE CHARTS (PAGI, SIANG, SORE, MALAM) ---
                mini_p_cols = st.columns(4)
                prog_categories_meta = [
                    ('PROGRESS PAGI', 'PROGRESS PAGI (07:00 - 10:00)', '#3b82f6', 'rgba(59, 130, 246, 0.16)'),
                    ('PROGRESS SIANG', 'PROGRESS SIANG (11:00 - 14:00)', '#22c55e', 'rgba(34, 197, 94, 0.16)'),
                    ('PROGRESS SORE', 'PROGRESS SORE (15:00 - 18:00)', '#f59e0b', 'rgba(245, 158, 11, 0.16)'),
                    ('PROGRESS MALAM', 'PROGRESS MALAM (19:00 - 23:59)', '#8b5cf6', 'rgba(139, 92, 246, 0.16)')
                ]
                for idx_m, (cat_key, cat_title, cat_color, cat_fill) in enumerate(prog_categories_meta):
                    df_cat_p = chart_prog_df[chart_prog_df['Kategori'] == cat_key]
                    max_y_m = df_cat_p['Jumlah'].max() if not df_cat_p.empty else 4
                    fig_m_prog = px.line(df_cat_p, x='Jam', y='Jumlah', text='Text', markers=True)
                    fig_m_prog.update_traces(
                        line=dict(width=2.2, color=cat_color, shape='spline'),
                        fill='tozeroy',
                        fillcolor=cat_fill,
                        marker=dict(size=5, color=cat_color),
                        textposition='top center',
                        textfont=dict(color='#ffffff'),
                        cliponaxis=False
                    )
                    fig_m_prog.update_layout(
                        title=dict(text=cat_title, font=dict(color=cat_color, size=12), x=0.5, xanchor='center'),
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='#0f172a',
                        margin=dict(t=40, b=45, l=45, r=10),
                        xaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, dtick=6, title="Waktu (Jam)"),
                        yaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, showticklabels=True, title="Progress", range=[0, max(max_y_m * 1.28, 2)]),
                        hovermode="x unified",
                        hoverlabel=dict(bgcolor='#1e293b', font=dict(color='#ffffff')),
                        height=260
                    )
                    fig_m_prog.update_xaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_m_prog.update_yaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    with mini_p_cols[idx_m]:
                        st.plotly_chart(fig_m_prog, use_container_width=True, config={'displayModeBar': False}, theme=None)

                st.markdown("<br>", unsafe_allow_html=True)

                # --- TABEL REKAP PER TEKNISI (ATAS) & DETAIL PROGRESS (BAWAH) ---
                st.markdown('<div class="section-title-wrap"><div class="section-title" style="font-size: 1.15rem;">👷 REKAP PROGRESS PER TEKNISI</div></div>', unsafe_allow_html=True)
                if not df_prog_period.empty:
                    piv_tek = (
                        df_prog_period.groupby(['Teknisi_Clean', 'Kategori_Sesi'])
                        .size()
                        .unstack(fill_value=0)
                        .reset_index()
                    )
                    for s_col in ['PROGRESS PAGI', 'PROGRESS SIANG', 'PROGRESS SORE', 'PROGRESS MALAM']:
                        if s_col not in piv_tek.columns:
                            piv_tek[s_col] = 0
                    piv_tek['TOTAL'] = (
                        piv_tek['PROGRESS PAGI'] +
                        piv_tek['PROGRESS SIANG'] +
                        piv_tek['PROGRESS SORE'] +
                        piv_tek['PROGRESS MALAM']
                    )
                    piv_tek = piv_tek.sort_values(by=['TOTAL', 'Teknisi_Clean'], ascending=[False, True]).reset_index(drop=True)

                    rows_tek_html = ""
                    for idx_t, r_t in piv_tek.iterrows():
                        rows_tek_html += (
                            f'<tr style="border-bottom: 1px solid #1e293b;">'
                            f'<td style="padding: 12px 12px; text-align:center; color:#ffffff; font-weight:bold; font-size:1.05rem;">{idx_t + 1}</td>'
                            f'<td style="padding: 12px 16px; text-align:left; color:#ffffff; font-weight:800; font-size:1.05rem;">{r_t["Teknisi_Clean"]}</td>'
                            f'<td style="padding: 12px 12px; text-align:center; color:#38bdf8; font-weight:800; font-size:1.1rem;">{int(r_t["PROGRESS PAGI"])}</td>'
                            f'<td style="padding: 12px 12px; text-align:center; color:#22c55e; font-weight:800; font-size:1.1rem;">{int(r_t["PROGRESS SIANG"])}</td>'
                            f'<td style="padding: 12px 12px; text-align:center; color:#f59e0b; font-weight:800; font-size:1.1rem;">{int(r_t["PROGRESS SORE"])}</td>'
                            f'<td style="padding: 12px 12px; text-align:center; color:#a78bfa; font-weight:800; font-size:1.1rem;">{int(r_t["PROGRESS MALAM"])}</td>'
                            f'<td style="padding: 12px 14px; text-align:center;"><span style="background:rgba(59,130,246,0.2); color:#ffffff; border:1px solid #3b82f6; padding:4px 15px; border-radius:999px; font-weight:800; font-size:1.05rem;">{int(r_t["TOTAL"])}</span></td>'
                            f'</tr>'
                        )

                    gt_pagi = int(piv_tek["PROGRESS PAGI"].sum())
                    gt_siang = int(piv_tek["PROGRESS SIANG"].sum())
                    gt_sore = int(piv_tek["PROGRESS SORE"].sum())
                    gt_malam = int(piv_tek["PROGRESS MALAM"].sum())
                    gt_total = int(piv_tek["TOTAL"].sum())

                    rows_tek_html += (
                        f'<tr style="background: #1e293b; border-top: 2px solid #eab308;">'
                        f'<td colspan="2" style="padding: 14px 16px; text-align:center; color:#ffffff; font-weight:900; font-size:1.1rem; letter-spacing:1px;">GRAND TOTAL</td>'
                        f'<td style="padding: 14px 12px; text-align:center; color:#38bdf8; font-weight:900; font-size:1.15rem;">{gt_pagi}</td>'
                        f'<td style="padding: 14px 12px; text-align:center; color:#22c55e; font-weight:900; font-size:1.15rem;">{gt_siang}</td>'
                        f'<td style="padding: 14px 12px; text-align:center; color:#f59e0b; font-weight:900; font-size:1.15rem;">{gt_sore}</td>'
                        f'<td style="padding: 14px 12px; text-align:center; color:#a78bfa; font-weight:900; font-size:1.15rem;">{gt_malam}</td>'
                        f'<td style="padding: 14px 14px; text-align:center;"><span style="background:rgba(234,179,8,0.25); color:#ffffff; border:1.5px solid #eab308; padding:4px 16px; border-radius:999px; font-weight:900; font-size:1.1rem;">{gt_total}</span></td>'
                        f'</tr>'
                    )

                    tek_table_html = (
                        '<div style="border: 1px solid #334155; border-radius: 10px; overflow: hidden; background: #0f172a; margin-bottom: 28px;">'
                        '<table style="width: 100%; border-collapse: collapse; font-size: 1.05rem;">'
                        '<thead>'
                        '<tr style="background: #1e293b; color: #ffffff; text-transform: uppercase; font-size: 0.96rem;">'
                        '<th style="padding: 14px 12px; text-align:center; width: 70px; color:#ffffff;">NO</th>'
                        '<th style="padding: 14px 16px; text-align:center; color:#ffffff;">TEKNISI</th>'
                        '<th style="padding: 14px 12px; text-align:center; color:#38bdf8;">PAGI<br><span style="font-size:12.5px;color:#ffffff;">07:00 - 10:00</span></th>'
                        '<th style="padding: 14px 12px; text-align:center; color:#22c55e;">SIANG<br><span style="font-size:12.5px;color:#ffffff;">11:00 - 14:00</span></th>'
                        '<th style="padding: 14px 12px; text-align:center; color:#f59e0b;">SORE<br><span style="font-size:12.5px;color:#ffffff;">15:00 - 18:00</span></th>'
                        '<th style="padding: 14px 12px; text-align:center; color:#a78bfa;">MALAM<br><span style="font-size:12.5px;color:#ffffff;">19:00 - 23:59</span></th>'
                        '<th style="padding: 14px 14px; text-align:center; color:#ffffff;">TOTAL</th>'
                        '</tr>'
                        '</thead>'
                        f'<tbody>{rows_tek_html}</tbody>'
                        '</table>'
                        '</div>'
                    )
                    st.markdown(tek_table_html, unsafe_allow_html=True)
                else:
                    st.info("Belum ada data teknisi yang melapor pada periode tanggal ini.")

                st.markdown('<div class="section-title-wrap"><div class="section-title">📋 DETAIL LOG FOTO PROGRESS TEKNISI</div></div>', unsafe_allow_html=True)
                search_prog_q = st.text_input("🔍 Cari Teknisi / Wonum / Notes / Status BIMA / Sesi Waktu:", "", key="search_prog_provi_detail", placeholder="Ketik nama teknisi, AO/WONUM, ODP, STARTWORK, PAGI, SIANG...")
                if not df_prog_period.empty:
                    df_det_p = df_prog_period.sort_values(by=['Parsed_Date', jam_col], ascending=[False, False]).copy()
                    if search_prog_q.strip():
                        q_low = search_prog_q.strip().lower()
                        mask_q = (
                            df_det_p['Teknisi_Clean'].astype(str).str.lower().str.contains(q_low, na=False) |
                            df_det_p[wo_col].astype(str).str.lower().str.contains(q_low, na=False) |
                            df_det_p['Kategori_Sesi'].astype(str).str.lower().str.contains(q_low, na=False) |
                            (df_det_p[notes_col].astype(str).str.lower().str.contains(q_low, na=False) if notes_col else False) |
                            (df_det_p[stat_col].astype(str).str.lower().str.contains(q_low, na=False) if stat_col else False)
                        )
                        df_det_p = df_det_p[mask_q]

                    sesi_badge_map = {
                        'PROGRESS PAGI': ('#38bdf8', 'rgba(56,189,248,0.15)', 'PAGI (07-10)'),
                        'PROGRESS SIANG': ('#22c55e', 'rgba(34,197,94,0.15)', 'SIANG (11-14)'),
                        'PROGRESS SORE': ('#f59e0b', 'rgba(245,158,11,0.15)', 'SORE (15-18)'),
                        'PROGRESS MALAM': ('#a78bfa', 'rgba(167,139,250,0.15)', 'MALAM (19-23)')
                    }

                    rows_det_html = ""
                    for idx_d, (_, r_d) in enumerate(df_det_p.iterrows(), 1):
                        tgl_v = str(r_d.get(tgl_col, '-')).strip()
                        jam_v = str(r_d.get(jam_col, '-')).strip()
                        tek_v = str(r_d.get('Teknisi_Clean', '-')).strip()
                        wo_v = str(r_d.get(wo_col, '-')).strip()
                        note_v = str(r_d.get(notes_col, '-')).strip() if notes_col and pd.notna(r_d.get(notes_col)) else '-'
                        wita_v = str(r_d.get(wita_col, '-')).strip() if wita_col and pd.notna(r_d.get(wita_col)) else '-'
                        stat_v = str(r_d.get(stat_col, '-')).strip() if stat_col and pd.notna(r_d.get(stat_col)) else '-'
                        sesi_v = str(r_d.get('Kategori_Sesi', 'PROGRESS PAGI'))
                        b_col, b_bg, b_lbl = sesi_badge_map.get(sesi_v, ('#38bdf8', 'rgba(56,189,248,0.15)', sesi_v))

                        stat_color = '#22c55e' if stat_v.upper() in ['COMPLETE', 'COMPWORK', 'ACTCOMP'] else ('#ef4444' if stat_v.upper() in ['WORKFAIL', 'CANCLWORK'] else '#38bdf8')

                        rows_det_html += (
                            f'<tr style="border-bottom: 1px solid #1e293b;">'
                            f'<td style="padding: 10px 8px; text-align:center; color:#94a3b8; font-weight:bold;">{idx_d}</td>'
                            f'<td style="padding: 10px 10px; text-align:center; color:#e2e8f0; white-space:nowrap;">{tgl_v} &bull; <span style="color:#38bdf8; font-weight:700;">{jam_v}</span></td>'
                            f'<td style="padding: 10px 10px; text-align:center;"><span style="background:{b_bg}; color:{b_col}; border:1px solid {b_col}; padding:3px 10px; border-radius:6px; font-size:0.74rem; font-weight:700; white-space:nowrap;">{b_lbl}</span></td>'
                            f'<td style="padding: 10px 12px; text-align:left; color:#f8fafc; font-weight:700; white-space:nowrap;">{tek_v}</td>'
                            f'<td style="padding: 10px 12px; text-align:left; color:#fbbf24; font-family:monospace; font-size:0.84rem; white-space:nowrap;">{wo_v}</td>'
                            f'<td style="padding: 10px 12px; text-align:left; color:#cbd5e1;">{note_v}</td>'
                            f'<td style="padding: 10px 10px; text-align:center; color:#94a3b8; white-space:nowrap;">{wita_v}</td>'
                            f'<td style="padding: 10px 10px; text-align:center;"><span style="color:{stat_color}; font-weight:700; font-size:0.78rem;">{stat_v}</span></td>'
                            f'</tr>'
                        )

                    det_table_html = (
                        '<div style="border: 1px solid #334155; border-radius: 10px; overflow: hidden; background: #0f172a; max-height: 550px; overflow-y: auto;">'
                        '<table style="width: 100%; border-collapse: collapse; font-size: 0.83rem;">'
                        '<thead>'
                        '<tr style="background: #1e293b; color: #cbd5e1; text-transform: uppercase; font-size: 0.76rem; position: sticky; top: 0; z-index: 2;">'
                        '<th style="padding: 12px 8px; text-align:center; width: 55px;">NO</th>'
                        '<th style="padding: 12px 10px; text-align:center;">TANGGAL & JAM KIRIM</th>'
                        '<th style="padding: 12px 10px; text-align:center;">SESI PROGRESS</th>'
                        '<th style="padding: 12px 12px; text-align:left;">TEKNISI</th>'
                        '<th style="padding: 12px 12px; text-align:left;">NOMER WONUM</th>'
                        '<th style="padding: 12px 12px; text-align:left;">NOTES</th>'
                        '<th style="padding: 12px 10px; text-align:center;">DATE MODIFIED WITA</th>'
                        '<th style="padding: 12px 10px; text-align:center;">STATUS BIMA</th>'
                        '</tr>'
                        '</thead>'
                        f'<tbody>{rows_det_html}</tbody>'
                        '</table>'
                        '</div>'
                    )
                    st.markdown(det_table_html, unsafe_allow_html=True)
                else:
                    st.info("Tidak ada detail log foto progress pada rentang tanggal yang dipilih.")
            else:
                st.warning("Kolom TANGGAL, JAM KIRIM PROGRESS, atau NOMER WONUM tidak ditemukan pada sheet REKAP REPORTING PROGRESS TEKNISI.")
        else:
            st.info("Data REKAP REPORTING PROGRESS TEKNISI belum tersedia atau kosong.")

    elif menu == "MONITORING SERVER":
        st.markdown('<div class="section-title-wrap"><div class="section-title">🖥️ SYSTEM MONITORING SERVER</div></div>', unsafe_allow_html=True)
        
        try:
          # CPU
          cpu_usage = psutil.cpu_percent(interval=0.5)
          cpu_cores = psutil.cpu_count(logical=True)
          cpu_freq = psutil.cpu_freq().current if psutil.cpu_freq() else 0
          
          # RAM
          mem = psutil.virtual_memory()
          ram_usage = mem.percent
          ram_used_gb = mem.used / (1024 ** 3)
          ram_total_gb = mem.total / (1024 ** 3)
          ram_avail_gb = mem.available / (1024 ** 3)
          
          # DISK
          disk = psutil.disk_usage('/')
          disk_usage = disk.percent
          disk_used_gb = disk.used / (1024 ** 3)
          disk_total_gb = disk.total / (1024 ** 3)
          disk_free_gb = disk.free / (1024 ** 3)
          
          # UPTIME
          import datetime
          boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
          now = datetime.datetime.now()
          uptime_td = now - boot_time
          days = uptime_td.days
          hours, remainder = divmod(uptime_td.seconds, 3600)
          minutes, _ = divmod(remainder, 60)
          uptime_str = f"{days}d {hours}h {minutes}m"
          boot_str = boot_time.strftime("%Y-%m-%d %H:%M")
        except Exception as e:
          st.error(f"Error reading system metrics: {e}")
          cpu_usage = ram_usage = disk_usage = 0
          cpu_cores = cpu_freq = ram_used_gb = ram_total_gb = ram_avail_gb = 0
          disk_used_gb = disk_total_gb = disk_free_gb = 0
          uptime_str = "N/A"
          boot_str = "N/A"

        # USE textwrap.dedent HERE SO MARKDOWN DOESNT SEE INDENTS
        html_content = textwrap.dedent(f'''
        <style>
        .mon-grid {{
          display: grid;
          grid-template-columns: repeat(5, 1fr);
          gap: 15px;
          margin-bottom: 20px;
        }}
        .mon-card {{
          background-color: #0f172a;
          border-radius: 12px;
          padding: 20px;
          box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3);
          border: 1px solid #1e293b;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
        }}
        .mon-header {{
          display: flex;
          align-items: center;
          gap: 12px;
          margin-bottom: 10px;
        }}
        .mon-icon {{
          width: 40px;
          height: 40px;
          border-radius: 10px;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 1.5rem;
        }}
        .mon-title {{
          font-size: 14px;
          color: #94a3b8;
          font-weight: bold;
          letter-spacing: 0.5px;
          margin: 0;
          text-transform: uppercase;
        }}
        .mon-val {{
          font-size: 1.8rem;
          font-weight: 800;
          color: #f8fafc;
          margin: 0;
        }}
        .mon-bar-bg {{
          height: 6px;
          background-color: #1e293b;
          border-radius: 3px;
          margin: 15px 0 10px 0;
          overflow: hidden;
        }}
        .mon-bar-fg {{
          height: 100%;
          border-radius: 3px;
        }}
        .mon-desc {{
          font-size: 0.7rem;
          color: #64748b;
          margin: 0;
        }}
        
        .ic-cpu {{ background-color: rgba(99, 102, 241, 0.15); color: #818cf8; }}
        .bg-cpu {{ background-color: #818cf8; width: {cpu_usage}%; }}
        
        .ic-ram {{ background-color: rgba(16, 185, 129, 0.15); color: #34d399; }}
        .bg-ram {{ background-color: #34d399; width: {ram_usage}%; }}
        
        .ic-disk {{ background-color: rgba(245, 158, 11, 0.15); color: #fbbf24; }}
        .bg-disk {{ background-color: #fbbf24; width: {disk_usage}%; }}
        
        .ic-up {{ background-color: rgba(239, 68, 68, 0.15); color: #f87171; }}
        
        .ic-temp {{ background-color: rgba(244, 63, 94, 0.15); color: #fb7185; }}
        
        /* Ensure responsiveness for small screens */
        @media (max-width: 1200px) {{
          .mon-grid {{ grid-template-columns: repeat(3, 1fr); }}
        }}
        @media (max-width: 768px) {{
          .mon-grid {{ grid-template-columns: 1fr; }}
        }}
        </style>
        
        <div class="mon-grid">
          <!-- CPU -->
          <div class="mon-card">
              <div class="mon-header">
                  <div class="mon-icon ic-cpu">🧠</div>
                  <div>
                      <p class="mon-title">CPU USAGE</p>
                      <p class="mon-val">{cpu_usage}%</p>
                  </div>
              </div>
              <div>
                  <div class="mon-bar-bg"><div class="mon-bar-fg bg-cpu"></div></div>
                  <p class="mon-desc">{cpu_cores} Core(s) • Freq: {cpu_freq:.0f} MHz</p>
              </div>
          </div>
          
          <!-- RAM -->
          <div class="mon-card">
              <div class="mon-header">
                  <div class="mon-icon ic-ram">📝</div>
                  <div>
                      <p class="mon-title">RAM</p>
                      <p class="mon-val">{ram_usage}%</p>
                  </div>
              </div>
              <div>
                  <div class="mon-bar-bg"><div class="mon-bar-fg bg-ram"></div></div>
                  <p class="mon-desc">{ram_used_gb:.2f} GB / {ram_total_gb:.2f} GB • Avail: {ram_avail_gb:.2f} GB</p>
              </div>
          </div>
          
          <!-- DISK -->
          <div class="mon-card">
              <div class="mon-header">
                  <div class="mon-icon ic-disk">💾</div>
                  <div>
                      <p class="mon-title">DISK</p>
                      <p class="mon-val">{disk_usage}%</p>
                  </div>
              </div>
              <div>
                  <div class="mon-bar-bg"><div class="mon-bar-fg bg-disk"></div></div>
                  <p class="mon-desc">{disk_used_gb:.2f} GB / {disk_total_gb:.2f} GB • Free: {disk_free_gb:.2f} GB</p>
              </div>
          </div>
          
          <!-- UPTIME -->
          <div class="mon-card">
              <div class="mon-header">
                  <div class="mon-icon ic-up">⏱️</div>
                  <div>
                      <p class="mon-title">UPTIME</p>
                      <p class="mon-val" style="font-size: 1.4rem; padding-top:4px;">{uptime_str}</p>
                  </div>
              </div>
              <div style="flex-grow:1; display:flex; align-items:flex-end;">
                  <p class="mon-desc" style="padding-top:15px;">Boot: {boot_str}</p>
              </div>
          </div>
          
          <!-- SUHU -->
          <div class="mon-card">
              <div class="mon-header">
                  <div class="mon-icon ic-temp">🌡️</div>
                  <div>
                      <p class="mon-title">SUHU SERVER</p>
                      <p class="mon-val">N/A</p>
                  </div>
              </div>
              <div style="flex-grow:1; display:flex; flex-direction:column; justify-content:flex-end;">
                  <div style="display:flex; justify-content:space-between; margin-bottom:5px; padding-top:10px;">
                      <span style="font-size:0.75rem; color:#94a3b8;">🟢 CPU (Tctl)</span>
                      <span style="font-size:0.75rem; color:#34d399; font-weight:bold;">N/A</span>
                  </div>
                  <div style="display:flex; justify-content:space-between;">
                      <span style="font-size:0.75rem; color:#94a3b8;">🟢 GPU (edge)</span>
                      <span style="font-size:0.75rem; color:#34d399; font-weight:bold;">N/A</span>
                  </div>
              </div>
          </div>
        </div>
        ''')
        
        import re
        html_content = re.sub(r'^\s+', '', html_content, flags=re.MULTILINE).replace('\n', '')
        st.markdown(html_content, unsafe_allow_html=True)
        
        st.info("💡 **Catatan Suhu Server:** Pembacaan suhu hardware di Windows memerlukan akses level Administrator dan Driver khusus (seperti HWMonitor), sehingga belum dapat ditampilkan secara langsung oleh sistem ini.")

        # Menampilkan Riwayat Penarikan Data (History Log)
        st.markdown('<div class="section-title-wrap" style="margin-top: 30px;"><div class="section-title">📊 RIWAYAT PENARIKAN DATA HARI INI</div></div>', unsafe_allow_html=True)
        
        history_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sync_history.csv")
        if os.path.exists(history_file):
          try:
              hist_df = pd.read_csv(history_file)
              today_str = datetime.datetime.now().strftime("%Y-%m-%d")
              # Filter hari ini
              hist_df = hist_df[hist_df['Date'] == today_str]
              total_tarik = len(hist_df)
              
              if total_tarik > 0:
                  # Render tabel elegan dengan markdown
                  table_html = f'''
                  <div style="background-color: #0f172a; padding: 20px; border-radius: 12px; border: 1px solid #1e293b; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3);">
                      <p style="color: #38bdf8; font-weight: bold; font-size: 1.1rem; margin-bottom: 15px;">TOTAL TRANSAKSI HARI INI: <span style="background-color: #38bdf8; color: #0f172a; padding: 3px 10px; border-radius: 20px; font-size: 1rem;">{total_tarik} Kali</span></p>
                      <table style="width: 100%; border-collapse: collapse; color: #cbd5e1; font-size: 0.9rem;">
                          <thead>
                              <tr style="border-bottom: 2px solid #1e293b; text-align: left; color: #94a3b8;">
                                  <th style="padding: 10px;">WAKTU</th>
                                  <th style="padding: 10px;">USER</th>
                                  <th style="padding: 10px;">SUMBER</th>
                                  <th style="padding: 10px;">TIPE</th>
                                  <th style="padding: 10px;">TARGET DATA</th>
                              </tr>
                          </thead>
                          <tbody>
                  '''
                  for _, row in hist_df.iterrows():
                      source_style = "color: #fbbf24;" if str(row['Source']).upper() == "DASHBOARD" else "color: #10b981;"
                      icon_source = "💻" if str(row['Source']).upper() == "DASHBOARD" else "📱"
                      
                      # Tipe Puller Styling
                      tipe = str(row.get('Type', 'Manual'))
                      if tipe.upper() == 'OTOMATIS':
                          tipe_html = '<span style="background-color: rgba(16,185,129,0.2); color: #10b981; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8rem;">🤖 OTOMATIS</span>'
                      else:
                          tipe_html = '<span style="background-color: rgba(99,102,241,0.2); color: #818cf8; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8rem;">👆 MANUAL</span>'
                          
                      # Target Data Styling
                      target = str(row.get('Target', 'ALL'))
                      if 'WFM' in target.upper():
                          target_html = f'<span style="background-color: rgba(239,68,68,0.2); color: #ef4444; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8rem;">🎯 {target}</span>'
                      else:
                          target_html = f'<span style="background-color: rgba(245,158,11,0.2); color: #f59e0b; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8rem;">🎯 {target}</span>'

                      table_html += f'''
                              <tr style="border-bottom: 1px solid #1e293b;">
                                  <td style="padding: 10px; font-weight: bold; color: #f8fafc;">⏰ {row['Time']}</td>
                                  <td style="padding: 10px; color: #c4b5fd;">👤 {row['User']}</td>
                                  <td style="padding: 10px; {source_style} font-weight: bold;">{icon_source} {row['Source']}</td>
                                  <td style="padding: 10px;">{tipe_html}</td>
                                  <td style="padding: 10px;">{target_html}</td>
                              </tr>
                      '''
                  table_html += '''
                          </tbody>
                      </table>
                  </div>
                  '''
                  import re
                  table_html = re.sub(r'^\s+', '', table_html, flags=re.MULTILINE).replace('\n', '')
                  st.markdown(table_html, unsafe_allow_html=True)
              else:
                  st.info("Belum ada transaksi penarikan data yang terekam hari ini.")
          except Exception as e:
              st.error(f"Gagal membaca riwayat: {e}")
        else:
          st.info("Belum ada histori penarikan data (file log belum terbentuk). Lakukan penarikan data minimal 1 kali.")

    elif menu == "DAILY REPORT":
        st.markdown("""
        <style>
        .asr-grid-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-bottom: 25px;
        }
        @media (max-width: 1280px) {
            .asr-grid-3 { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 768px) {
            .asr-grid-3 { grid-template-columns: 1fr; }
        }
        .asr-card {
            background-color: #0f172a;
            border-radius: 10px;
            padding: 16px 18px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3);
            border: 2.5px solid #334155;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .asr-card-blue    { border-top: 4px solid #3b82f6; }
        .asr-card-sky     { border-top: 4px solid #0ea5e9; }
        .asr-card-teal    { border-top: 4px solid #14b8a6; }
        .asr-card-green   { border-top: 4px solid #10b981; }
        .asr-card-emerald { border-top: 4px solid #059669; }
        .asr-card-amber   { border-top: 4px solid #f59e0b; }
        .asr-card-indigo  { border-top: 4px solid #6366f1; }
        .asr-card-violet  { border-top: 4px solid #a855f7; }
        .asr-card-purple  { border-top: 4px solid #8b5cf6; }

        .asr-card-hdr {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            margin-bottom: 12px;
        }
        .asr-card-hdr-left {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .asr-card-icon {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.35rem;
        }
        .asr-card-title {
            font-size: 1.18rem;
            font-weight: 800;
            color: #ffffff;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
        }
        .asr-card-val {
            font-size: 2.5rem;
            font-weight: 800;
            color: #ffffff;
            line-height: 1;
            text-align: right;
            font-family: monospace;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
        }
        .asr-card-tbl-hdr {
            display: grid;
            padding: 6px 0 8px 0;
            border-bottom: 2px solid #334155;
            font-size: 0.92rem;
            font-weight: 800;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .asr-card-tbl-row {
            display: grid;
            align-items: center;
            padding: 7px 0;
            border-bottom: 1px solid rgba(255,255,255,0.06);
            font-size: 0.98rem;
            font-weight: 700;
        }
        .asr-card-tbl-row:last-child {
            border-bottom: none;
        }

        /* Modal & Link Trigger Styling */
        .asr-modal-trigger {
            transition: all 0.15s ease;
            text-decoration: none !important;
            font-weight: 800 !important;
            font-size: 1.02rem;
            display: inline-block;
        }
        .asr-modal-trigger:hover {
            filter: brightness(1.4) drop-shadow(0 0 6px rgba(56, 189, 248, 0.9));
            text-decoration: none !important;
        }
        .asr-card-val a {
            color: #ffffff;
            text-decoration: none !important;
            font-weight: 800 !important;
            cursor: pointer;
            transition: all 0.15s ease;
        }
        .asr-card-val a:hover {
            color: #38bdf8 !important;
            text-shadow: 0 0 12px rgba(56, 189, 248, 0.9);
            text-decoration: none !important;
        }
        .asr-modal-box {
            animation: asrModalFadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }
        @keyframes asrModalFadeIn {
            from { opacity: 0; transform: scale(0.97); }
            to { opacity: 1; transform: scale(1); }
        }
        .modal-close:hover {
            color: #f87171 !important;
            transform: scale(1.15);
        }

        /* Modal & Table Sticky Header & Custom Scrollbars */
        .asr-modal-scroll {
            width: 100%;
            overflow-x: scroll !important;
            overflow-y: auto !important;
            scrollbar-color: #3b82f6 #090d16;
            scrollbar-width: auto;
        }
        .asr-modal-scroll::-webkit-scrollbar {
            height: 14px !important;
            width: 12px !important;
        }
        .asr-modal-scroll::-webkit-scrollbar-track {
            background: #090d16 !important;
            border-top: 2px solid #1e3a8a !important;
            border-radius: 6px !important;
        }
        .asr-modal-scroll::-webkit-scrollbar-thumb {
            background: #2563eb !important;
            border-radius: 6px !important;
            border: 2px solid #090d16 !important;
        }
        .asr-modal-scroll::-webkit-scrollbar-thumb:hover {
            background: #3b82f6 !important;
            box-shadow: 0 0 10px rgba(59, 130, 246, 0.9) !important;
        }
        .asr-modal-scroll::-webkit-scrollbar-corner {
            background: #090d16 !important;
        }
        .asr-modal-search-box {
            background: #0f172a !important;
            color: #f8fafc !important;
            border: 1.8px solid #3b82f6 !important;
            border-radius: 8px !important;
            padding: 6px 32px 6px 34px !important;
            font-size: 0.84rem !important;
            width: 300px !important;
            outline: none !important;
            transition: all 0.2s ease !important;
            box-shadow: 0 2px 5px rgba(0,0,0,0.4) !important;
        }
        .asr-modal-search-box:focus {
            border-color: #60a5fa !important;
            box-shadow: 0 0 10px rgba(96, 165, 250, 0.6) !important;
        }
        .asr-modal-search-box::placeholder {
            color: #94a3b8 !important;
        }
        .asr-modal-table th,
        .asr-table-custom th {
            position: sticky;
            top: 0;
            z-index: 50;
            background-color: #1e3a8a !important;
            color: #ffffff !important;
            font-weight: 800;
            border-bottom: 2.5px solid #3b82f6;
            border-right: 1px solid rgba(255,255,255,0.12);
            box-shadow: inset 0 -2.5px 0 #3b82f6, 0 3px 6px rgba(0,0,0,0.4);
        }
        .asr-scroll-container {
            width: 100%;
            overflow-x: auto !important;
            overflow-y: auto !important;
            max-height: 800px;
            border: 1px solid #334155;
            border-radius: 8px;
            background-color: #0b1120;
            margin-top: 12px;
            scrollbar-width: thin;
            scrollbar-color: #3b82f6 #0b1120;
        }
        .asr-table-custom {
            width: 100%;
            min-width: 1750px;
            border-collapse: separate;
            border-spacing: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            text-align: left;
            font-size: 0.82rem;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-title-wrap"><div class="section-title" style="font-size: 1.25rem; font-weight: 800; letter-spacing: 0.5px;">\U0001F4CA DAILY REPORT ASSURANCE</div></div>', unsafe_allow_html=True)
        
        df_asr, asr_source = load_assurance_data(insera_time)
        df_proactive_raw, pro_source = load_proactive_data(insera_time)
        
        if df_asr.empty:
            st.warning("\u26A0\uFE0F **Data tiket Assurance belum berhasil dimuat.**")
            st.info("\U0001F4A1 Pastikan Anda telah melakukan penarikan data minimal 1 kali melalui tombol **'\U0001F680 Tarik INSERA ASR'** di sidebar.")
        else:
            import math
            import html as html_lib

            # 1. Deteksi Kolom Otomatis
            # 1. Deteksi Kolom Otomatis dengan Prioritas Terjamin
            priority_defs = [
                ('incident', ['INCIDENT', 'ID TICKET', 'TICKET ID', 'NO TIKET']),
                ('reported_date', ['REPORTED DATE', 'REPORTED_DATE', 'TANGGAL TIKET', 'TANGGAL']),
                ('status_date', ['STATUS DATE', 'STATUS_DATE', 'DATE MODIFIED', 'DATEMODIFIED', 'RESOLVE DATE', 'RESOLVED DATE']),
                ('status', ['STATUS TIKET', 'STATUS', 'TICKET STATUS', 'TICKET_STATUS']),
                ('cust_type', ['CUSTOMER TYPE', 'CUSTOMER_TYPE', 'TIPE CUSTOMER', 'TIPE PELANGGAN']),
                ('workzone', ['WORKZONE', 'WORK_ZONE', 'STO', 'ZONE']),
                ('booking_date', ['BOOKING DATE', 'BOOKING_DATE', 'TANGGAL BOOKING', 'TGL BOOKING']),
                ('summary', ['SUMMARY', 'SUMMARY TIKET', 'DESCRIPTION']),
                ('owner_group', ['OWNER GROUP', 'OWNER_GROUP', 'C_OWNER_GROUP']),
                ('ttr_val', ['TTR CUSTOMER', 'TTR_CUSTOMER', 'TTR']),
                ('incident', ['INCIDENT', 'ID TICKET', 'TICKET ID', 'NO TIKET']),
                ('cust_name', ['CUSTOMER NAME', 'CUSTOMER_NAME', 'NAMA PELANGGAN']),
                ('service', ['SERVICE TYPE', 'SERVICE_TYPE', 'SERVICE']),
                ('alpro_ok', ['ALPRO OK', 'ALPRO_OK', 'ALPRO', 'ODC']),
                ('rk_info', ['RK INFORMATION', 'RK_INFORMATION']),
                ('device_name', ['DEVICE NAME', 'DEVICE_NAME']),
                ('osla_col', ['OSLA', 'OSLA STATUS', 'STATUS OSLA']),
                ('teknisi', ['NAMA TEKNISI', 'TEKNISI ADING', 'TEKNISI', 'NAMA TIM'])
            ]
            col_map = {}
            for key, candidates in priority_defs:
                for cand in candidates:
                    for c in df_asr.columns:
                        if str(c).strip().upper() == cand:
                            col_map[key] = c
                            break
                    if key in col_map:
                        break

            import re
            def get_alpro_ok(r):
                # 1. Direct column in sheet/dataframe
                for k in ['alpro_ok', 'ALPRO OK', 'ALPRO', 'alpro']:
                    val = safe_val(r, col_map.get(k, k))
                    if val and val.strip() not in ['-', '', 'nan', 'None', 'null', '0']:
                        cleaned = val.strip()
                        if cleaned.startswith('ODC-'):
                            cleaned = cleaned[4:]
                        return cleaned
                # 2. Derive from RK INFORMATION
                rk = safe_val(r, col_map.get('rk_info', 'RK INFORMATION'))
                if rk and rk.strip() not in ['-', '', 'nan', 'None', 'null', '0']:
                    token = rk.strip().split()[0]
                    cleaned = token.replace('mODC-', 'ODC-').replace('ODC-ULN-', 'ODC-ULI-')
                    if cleaned.startswith('ODC-'):
                        cleaned = cleaned[4:]
                    return cleaned
                # 3. Derive from DEVICE NAME (ODP -> ODC)
                dev = safe_val(r, col_map.get('device_name', 'DEVICE NAME'))
                if dev and 'ODP-' in dev:
                    odp_part = dev.split('/')[0].split()[0]
                    cleaned = odp_part.replace('ODP-', '')
                    return cleaned
                # 4. Search in SUMMARY
                summ = safe_val(r, col_map.get('summary', 'SUMMARY'))
                if summ:
                    m = re.search(r'\b(OD[CP]-[A-Z]{3}-[A-Z0-9]+)', summ)
                    if m:
                        cleaned = m.group(1).replace('ODP-', '').replace('ODC-', '')
                        return cleaned
                return '-'

            # Parsed Reported Date
            if 'reported_date' in col_map:
                df_asr['dt_rep'] = pd.to_datetime(df_asr[col_map['reported_date']], errors='coerce')
                df_asr['date_rep'] = df_asr['dt_rep'].dt.date
            else:
                df_asr['dt_rep'] = pd.NaT
                df_asr['date_rep'] = None

            # Parsed Status/Close Date
            if 'status_date' in col_map:
                df_asr['dt_status'] = pd.to_datetime(df_asr[col_map['status_date']], errors='coerce')
                df_asr['date_status'] = df_asr['dt_status'].dt.date
            else:
                df_asr['dt_status'] = df_asr['dt_rep']
                df_asr['date_status'] = df_asr['date_rep']

            # Normalisasi Status Open vs Close
            if 'status' in col_map:
                stat_series = df_asr[col_map['status']].astype(str).str.upper().str.strip()
                is_closed = stat_series.str.contains('CLOSE|RESOLV|CANCEL|SALAMSIM|MEDIACARE', na=False)
                df_asr['is_closed'] = is_closed
                df_asr['is_open'] = ~is_closed
            else:
                df_asr['is_closed'] = False
                df_asr['is_open'] = True

            # Normalisasi Customer Tier
            def parse_cust_tier(val):
                s = str(val).upper().strip()
                if 'DIAMOND' in s:
                    return 'HVC DIAMOND'
                elif 'PLATINUM' in s:
                    return 'HVC PLATINUM'
                elif 'GOLD' in s:
                    return 'HVC GOLD'
                else:
                    return 'REGULER'

            if 'cust_type' in col_map:
                df_asr['cust_tier'] = df_asr[col_map['cust_type']].apply(parse_cust_tier)
            else:
                df_asr['cust_tier'] = 'REGULER'

            # Normalisasi Workzone (ULI vs GMB)
            def parse_workzone(val):
                s = str(val).upper().strip()
                if 'GMB' in s:
                    return 'GMB'
                return 'ULI'

            if 'workzone' in col_map:
                df_asr['wzone_clean'] = df_asr[col_map['workzone']].apply(parse_workzone)
            else:
                df_asr['wzone_clean'] = 'ULI'

            # MANJA Flag
            has_booking = pd.Series(False, index=df_asr.index)
            if 'booking_date' in col_map:
                b_str = df_asr[col_map['booking_date']].astype(str).str.strip().str.lower()
                has_booking = df_asr[col_map['booking_date']].notna() & (~b_str.isin(['', 'nan', 'none', '-', '<na>', 'nat']))
            
            has_kw_manja = pd.Series(False, index=df_asr.index)
            if 'summary' in col_map:
                has_kw_manja = df_asr[col_map['summary']].astype(str).str.upper().str.contains('MANJA', na=False)

            df_asr['is_manja'] = has_booking | has_kw_manja

            # TTR SLA OSLA vs NOT OSLA Calculation (Diamond: 3 Jam, Platinum: 6 Jam, Gold: 12 Jam, Reguler: 24 Jam)
            def calc_osla_status(row):
                # 0. Jika ada kolom OSLA langsung dari Google Sheets (ARRAYFORMULA Kolom 90)
                if 'osla_col' in col_map and pd.notna(row.get(col_map['osla_col'])):
                    raw_osla = str(row[col_map['osla_col']]).strip().upper()
                    if 'NOT OSLA' in raw_osla:
                        return 'NOT OSLA'
                    elif 'OSLA' in raw_osla:
                        return 'OSLA'

                tier = row['cust_tier']
                if 'DIAMOND' in tier:
                    target_sec = 3 * 3600
                elif 'PLATINUM' in tier:
                    target_sec = 6 * 3600
                elif 'GOLD' in tier:
                    target_sec = 12 * 3600
                else:
                    target_sec = 24 * 3600

                elapsed_sec = None
                if 'ttr_val' in col_map and pd.notna(row.get(col_map['ttr_val'])):
                    s_ttr = str(row[col_map['ttr_val']]).strip()
                    if s_ttr.lower() not in ['nan', 'none', '-', '', '<na>', 'nat']:
                        try:
                            parts = s_ttr.split(':')
                            if len(parts) == 3:
                                elapsed_sec = float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
                            elif len(parts) == 2:
                                elapsed_sec = float(parts[0]) * 3600 + float(parts[1]) * 60
                            else:
                                val = float(parts[0])
                                if not math.isnan(val):
                                    elapsed_sec = val * 3600
                        except Exception:
                            pass

                if elapsed_sec is None or math.isnan(elapsed_sec) or elapsed_sec < 0:
                    if pd.notna(row.get('dt_rep')):
                        try:
                            # Konversi REPORTED DATE dari WIB ke WITA (+1 jam)
                            dt_wita = row['dt_rep'] + pd.Timedelta(hours=1)
                            diff = (datetime.now() - dt_wita.to_pydatetime().replace(tzinfo=None)).total_seconds()
                            if diff >= 0:
                                elapsed_sec = diff
                        except Exception:
                            pass

                if elapsed_sec is None or math.isnan(elapsed_sec) or elapsed_sec < 0:
                    elapsed_sec = 0.0

                return 'OSLA' if elapsed_sec > target_sec else 'NOT OSLA'

            df_asr['osla_status'] = df_asr.apply(calc_osla_status, axis=1)

            # Owner Group
            if 'owner_group' in col_map:
                df_asr['owner_group_clean'] = df_asr[col_map['owner_group']].astype(str).str.strip()
                df_asr['owner_group_clean'] = df_asr['owner_group_clean'].replace({'nan': 'UNASSIGNED', 'None': 'UNASSIGNED', '': 'UNASSIGNED', '<NA>': 'UNASSIGNED'})
            else:
                df_asr['owner_group_clean'] = 'UNASSIGNED'

            # 2. Pemisahan Data untuk 9 Kartu (Layout 3x3 Sesuai Konsep Baru)
            # Periode terpilih dari sidebar (start_date s/d end_date)
            if start_date and end_date and df_asr['date_rep'].notna().any():
                df_masuk_hi = df_asr[(df_asr['date_rep'] >= start_date) & (df_asr['date_rep'] <= end_date)].copy()
            else:
                df_masuk_hi = df_asr.copy()

            df_all_open = df_asr[df_asr['is_open']].copy()
            df_all_closed = df_asr[df_asr['is_closed']].copy()
            
            # MANJA OPEN: tiket open yang berstatus MANJA
            df_manja_open = df_all_open[df_all_open['is_manja']].copy()

            # Tiket Close dalam periode terpilih (start_date s/d end_date)
            if start_date and end_date and df_asr['date_status'].notna().any():
                df_close_filtered = df_asr[df_asr['is_closed'] & (df_asr['date_status'] >= start_date) & (df_asr['date_status'] <= end_date)].copy()
            else:
                df_close_filtered = df_all_closed.copy()

            # Tiket Close HI: tiket closed yang status date / resolve date nya dalam periode
            df_close_hi = df_close_filtered.copy()

            # TTR TIKET CLOSE: tiket closed dalam periode yang dianalisis TTR nya
            df_ttr_close = df_close_filtered.copy()

            # MANJA CLOSE: tiket closed yang berstatus MANJA dalam periode terpilih
            df_manja_close = df_close_filtered[df_close_filtered['is_manja']].copy()

            df_ttr_open = df_all_open.copy()
            df_owner_open = df_all_open.copy()

            # Normalisasi data PROACTIVE TICKET
            df_proactive = df_proactive_raw.copy() if not df_proactive_raw.empty else pd.DataFrame()
            if not df_proactive.empty:
                col_map_pro = {}
                for c in df_proactive.columns:
                    cu = str(c).strip().upper()
                    if cu in ['REPORTED DATE', 'REPORTED_DATE', 'TANGGAL TIKET', 'TANGGAL']:
                        col_map_pro['reported_date'] = c
                    elif cu in ['STATUS', 'STATUS TIKET', 'TICKET STATUS', 'TICKET_STATUS']:
                        col_map_pro['status'] = c
                    elif cu in ['CUSTOMER SEGMENT', 'CUSTOMER_SEGMENT', 'SEGMEN']:
                        col_map_pro['cust_seg'] = c
                    elif cu in ['JENIS TIKET', 'JENIS_TIKET']:
                        col_map_pro['jenis_tiket'] = c
                    elif cu in ['CUSTOMER TYPE', 'CUSTOMER_TYPE']:
                        col_map_pro['cust_type'] = c
                    elif cu in ['WORKZONE', 'WORK_ZONE', 'STO', 'ZONE']:
                        col_map_pro['workzone'] = c
                    elif cu in ['SUMMARY', 'SUMMARY TIKET', 'DESCRIPTION']:
                        col_map_pro['summary'] = c
                    elif cu in ['OWNER GROUP', 'OWNER_GROUP']:
                        col_map_pro['owner_group'] = c
                    elif cu in ['TTR CUSTOMER', 'TTR']:
                        col_map_pro['ttr_val'] = c
                    elif cu in ['INCIDENT', 'ID TICKET', 'TICKET ID']:
                        col_map_pro['incident'] = c
                    elif cu in ['CUSTOMER NAME', 'CUSTOMER_NAME']:
                        col_map_pro['cust_name'] = c
                    elif cu in ['SERVICE TYPE', 'SERVICE_TYPE']:
                        col_map_pro['service'] = c
                    elif cu in ['ALPRO OK', 'ALPRO']:
                        col_map_pro['alpro_ok'] = c

                # Normalisasi Kolom Segmen: DGS, DPS, DSS, RBS disederhanakan menjadi HSI (B2B)
                def parse_proactive_seg(val):
                    s = str(val).upper().strip()
                    if 'PL-TSEL' in s or 'TSEL' in s:
                        return 'PL-TSEL'
                    return 'HSI (B2B)'

                seg_col = col_map_pro.get('cust_seg', 'CUSTOMER SEGMENT')
                if seg_col in df_proactive.columns:
                    df_proactive['seg_clean'] = df_proactive[seg_col].apply(parse_proactive_seg)
                else:
                    df_proactive['seg_clean'] = 'HSI (B2B)'

                # Normalisasi Kolom JENIS TIKET (Kolom CD)
                def parse_proactive_jenis(row):
                    for k in ['JENIS TIKET', 'JENIS_TIKET', col_map_pro.get('jenis_tiket', '')]:
                        if k and k in row and pd.notna(row[k]) and str(row[k]).strip():
                            v = str(row[k]).strip().upper()
                            if 'PRA SQM GAUL' in v or 'GAUL' in v:
                                return 'PRA SQM GAUL'
                            elif 'PRA SQM' in v:
                                return 'PRA SQM'
                            elif 'UNSPEC' in v:
                                return 'UNSPEC'
                            elif 'SQM' in v:
                                return 'SQM'
                    summ = str(row.get('SUMMARY', '')).upper()
                    symp = str(row.get('SYMPTOM', '')).upper()
                    if '[PRA SQM GAUL]' in summ or 'PRA SQM INTERNET GAUL' in symp:
                        return 'PRA SQM GAUL'
                    elif '[PRA SQM]' in summ or 'PREDICTIVE INTERNET OFFLINE' in symp:
                        return 'PRA SQM'
                    elif '[UNSPEC]' in summ or 'PROACTIVE UNSPEC' in symp or 'UNDERSPEC' in symp:
                        return 'UNSPEC'
                    elif '[SQM]' in summ or 'SQM' in symp:
                        return 'SQM'
                    return 'UNSPEC'

                df_proactive['jenis_clean'] = df_proactive.apply(parse_proactive_jenis, axis=1)

                # Status Open
                if 'status' in col_map_pro:
                    s_series = df_proactive[col_map_pro['status']].astype(str).str.upper()
                    df_proactive['is_open'] = ~s_series.str.contains('CLOSE|RESOLV|CANCEL', na=False)
                else:
                    df_proactive['is_open'] = True
                    
                if 'cust_type' in col_map_pro:
                    df_proactive['cust_tier'] = df_proactive[col_map_pro['cust_type']].apply(parse_cust_tier)
                else:
                    df_proactive['cust_tier'] = 'REGULER'
                    
                if 'workzone' in col_map_pro:
                    df_proactive['wzone_clean'] = df_proactive[col_map_pro['workzone']].apply(parse_workzone)
                else:
                    df_proactive['wzone_clean'] = 'ULI'

                if 'owner_group' in col_map_pro:
                    df_proactive['owner_group_clean'] = df_proactive[col_map_pro['owner_group']].astype(str).str.strip()
                else:
                    df_proactive['owner_group_clean'] = 'UNASSIGNED'

                df_proactive_open = df_proactive[df_proactive['is_open']].copy()
            else:
                df_proactive_open = pd.DataFrame()

            # 3. Helper Render Tabel Per Kartu & Dynamic Pop-Up Modal
            tiers_list = [
                ('HVC DIAMOND', '#22d3ee', '\U0001F48E'),
                ('HVC PLATINUM', '#c084fc', '\U0001F451'),
                ('HVC GOLD', '#facc15', '\U0001F3C6'),
                ('REGULER', '#60a5fa', '\U0001F464')
            ]

            cust_badges_daily = {
                'HVC GOLD': '<span style="background: rgba(234,179,8,0.18); border: 1px solid #eab308; color: #facc15; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">HVC_GOLD</span>',
                'HVC PLATINUM': '<span style="background: rgba(168,85,247,0.18); border: 1px solid #a855f7; color: #c084fc; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">HVC_PLATINUM</span>',
                'HVC DIAMOND': '<span style="background: rgba(6,182,212,0.18); border: 1px solid #06b6d4; color: #22d3ee; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">HVC_DIAMOND</span>',
                'REGULER': '<span style="background: rgba(59,130,246,0.18); border: 1px solid #3b82f6; color: #60a5fa; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">REGULER</span>',
                'HVC REGULER': '<span style="background: rgba(59,130,246,0.18); border: 1px solid #3b82f6; color: #60a5fa; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">REGULER</span>',
            }
            status_badges_daily = {
                'ANALYSIS': '<span style="background: rgba(245,158,11,0.18); border: 1px solid #f59e0b; color: #fbbf24; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">ANALYSIS</span>',
                'BACKEND': '<span style="background: rgba(234,179,8,0.18); border: 1px solid #eab308; color: #facc15; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">BACKEND</span>',
                'CLOSED': '<span style="background: rgba(16,185,129,0.18); border: 1px solid #10b981; color: #34d399; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">CLOSED</span>',
                'RESOLVED': '<span style="background: rgba(16,185,129,0.18); border: 1px solid #10b981; color: #34d399; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">RESOLVED</span>',
                'DRAFT': '<span style="background: rgba(148,163,184,0.18); border: 1px solid #64748b; color: #cbd5e1; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">DRAFT</span>'
            }

            def make_slug(s):
                return re.sub(r'[^a-zA-Z0-9]+', '_', str(s).strip().lower()).strip('_')

            def safe_val(row, col_key, default='-'):
                c = col_map.get(col_key, col_key)
                if c in row:
                    v = row.get(c, default)
                    if pd.notna(v) and v is not None and str(v).strip().lower() not in ['nan', 'none', '<na>', 'nat', '']:
                        return str(v).strip()
                alt_keys = {
                    'incident': ['INCIDENT', 'ID TICKET', 'TICKET ID', 'NO TIKET'],
                    'reported_date': ['REPORTED DATE', 'REPORTED_DATE', 'TANGGAL TIKET', 'TANGGAL'],
                    'status': ['STATUS', 'STATUS TIKET', 'TICKET STATUS'],
                    'cust_name': ['CUSTOMER NAME', 'CUSTOMER_NAME'],
                    'service': ['SERVICE TYPE', 'SERVICE_TYPE', 'SERVICE'],
                    'summary': ['SUMMARY', 'SUMMARY TIKET', 'DESCRIPTION'],
                    'owner_group': ['OWNER GROUP', 'OWNER_GROUP']
                }
                for alt in alt_keys.get(col_key, []):
                    if alt in row and pd.notna(row[alt]):
                        v = str(row[alt]).strip()
                        if v and v.lower() not in ['nan', 'none', '<na>', 'nat']:
                            return v
                return default

            asr_modals = {}

            def make_asr_link(val, modal_id, modal_title, sub_df, underline=False, color=None, is_header=False):
                if val and val > 0 and sub_df is not None and len(sub_df) > 0:
                    asr_modals[modal_id] = (modal_title, sub_df)
                    c = f"color:{color};" if color else ""
                    fs = "font-size:2.5rem;" if is_header else "font-size:1.02rem;"
                    return f'<a href="javascript:void(0)" class="modal-trigger asr-modal-trigger" data-target="{modal_id}" style="{c} text-decoration:none !important; font-weight:800 !important; {fs} cursor:pointer; font-family:monospace,sans-serif;">{val}</a>'
                if is_header:
                    return '<span style="color:#ffffff; font-weight:800; font-size:2.5rem;">0</span>'
                return '<span style="color:#64748b; font-weight:700; font-size:1.02rem;">-</span>'

            def render_wzone_rows(df_sub, card_slug, card_title):
                html_rows = []
                for tier_name, color, icon in tiers_list:
                    sub = df_sub[df_sub['cust_tier'] == tier_name]
                    sub_uli = sub[sub['wzone_clean'] == 'ULI']
                    sub_gmb = sub[sub['wzone_clean'] == 'GMB']
                    tot_cnt = len(sub)
                    tier_slug = make_slug(tier_name)
                    
                    uli_str = make_asr_link(len(sub_uli), f"modal-asr-{card_slug}-{tier_slug}-uli", f"{card_title} - {tier_name} (ULI)", sub_uli, underline=False, color="#ffffff")
                    gmb_str = make_asr_link(len(sub_gmb), f"modal-asr-{card_slug}-{tier_slug}-gmb", f"{card_title} - {tier_name} (GMB)", sub_gmb, underline=False, color="#ffffff")
                    tot_str = make_asr_link(tot_cnt, f"modal-asr-{card_slug}-{tier_slug}-total", f"{card_title} - {tier_name} (TOTAL)", sub, underline=False, color="#38bdf8")
                    
                    html_rows.append(
                        f'<div class="asr-card-tbl-row" style="grid-template-columns: 2fr 1fr 1fr 1fr;">'
                        f'<span style="color:{color}; font-weight:700; font-size:0.96rem; white-space:nowrap;">{icon} {tier_name}</span>'
                        f'<span style="text-align:center;">{uli_str}</span>'
                        f'<span style="text-align:center;">{gmb_str}</span>'
                        f'<span style="text-align:center;">{tot_str}</span>'
                        f'</div>'
                    )
                return "".join(html_rows)

            def render_ttr_rows(df_sub, card_slug="ttr-open", card_title="TTR TIKET OPEN"):
                html_rows = []
                for tier_name, color, icon in tiers_list:
                    sub = df_sub[df_sub['cust_tier'] == tier_name]
                    sub_not = sub[sub['osla_status'] == 'NOT OSLA']
                    sub_osla = sub[sub['osla_status'] == 'OSLA']
                    tot_cnt = len(sub)
                    tier_slug = make_slug(tier_name)
                    
                    not_str = make_asr_link(len(sub_not), f"modal-asr-{card_slug}-{tier_slug}-not-osla", f"{card_title} - {tier_name} (NOT OSLA)", sub_not, underline=False, color="#34d399")
                    osla_str = make_asr_link(len(sub_osla), f"modal-asr-{card_slug}-{tier_slug}-osla", f"{card_title} - {tier_name} (OSLA)", sub_osla, underline=False, color="#f87171")
                    tot_str = make_asr_link(tot_cnt, f"modal-asr-{card_slug}-{tier_slug}-total", f"{card_title} - {tier_name} (TOTAL)", sub, underline=False, color="#38bdf8")
                    
                    html_rows.append(
                        f'<div class="asr-card-tbl-row" style="grid-template-columns: 1.8fr 1.1fr 1.1fr 1.1fr;">'
                        f'<span style="color:{color}; font-weight:700; font-size:0.96rem; white-space:nowrap;">{icon} {tier_name}</span>'
                        f'<span style="text-align:center;">{not_str}</span>'
                        f'<span style="text-align:center;">{osla_str}</span>'
                        f'<span style="text-align:center;">{tot_str}</span>'
                        f'</div>'
                    )
                return "".join(html_rows)

            def render_owner_rows(df_sub, card_slug="owner-open", card_title="OWNER GRUP OPEN"):
                html_rows = []
                if df_sub.empty:
                    for _ in range(4):
                        html_rows.append(
                            '<div class="asr-card-tbl-row" style="grid-template-columns: 2.1fr 1fr 1fr 1fr; opacity:0.3;">'
                            '<span style="color:#64748b; font-size:0.96rem;">-</span>'
                            '<span style="text-align:center; color:#64748b; font-size:1.02rem; font-weight:700;">-</span>'
                            '<span style="text-align:center; color:#64748b; font-size:1.02rem; font-weight:700;">-</span>'
                            '<span style="text-align:center; color:#64748b; font-size:1.02rem; font-weight:700;">-</span>'
                            '</div>'
                        )
                    return "".join(html_rows)

                grp_counts = df_sub['owner_group_clean'].value_counts()
                top_grps = list(grp_counts.index[:3])
                has_others = len(grp_counts) > 3

                for grp in top_grps:
                    sub = df_sub[df_sub['owner_group_clean'] == grp]
                    sub_uli = sub[sub['wzone_clean'] == 'ULI']
                    sub_gmb = sub[sub['wzone_clean'] == 'GMB']
                    tot_cnt = len(sub)
                    grp_slug = make_slug(grp)
                    
                    uli_str = make_asr_link(len(sub_uli), f"modal-asr-{card_slug}-{grp_slug}-uli", f"{card_title} - {grp} (ULI)", sub_uli, underline=False, color="#ffffff")
                    gmb_str = make_asr_link(len(sub_gmb), f"modal-asr-{card_slug}-{grp_slug}-gmb", f"{card_title} - {grp} (GMB)", sub_gmb, underline=False, color="#ffffff")
                    tot_str = make_asr_link(tot_cnt, f"modal-asr-{card_slug}-{grp_slug}-total", f"{card_title} - {grp} (TOTAL)", sub, underline=False, color="#38bdf8")
                    
                    disp_label = grp if len(grp) <= 18 else grp[:16] + '..'
                    html_rows.append(
                        f'<div class="asr-card-tbl-row" style="grid-template-columns: 2.1fr 1fr 1fr 1fr;">'
                        f'<span style="color:#e2e8f0; font-weight:700; font-size:0.96rem; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;" title="{html_lib.escape(grp)}">{html_lib.escape(disp_label)}</span>'
                        f'<span style="text-align:center;">{uli_str}</span>'
                        f'<span style="text-align:center;">{gmb_str}</span>'
                        f'<span style="text-align:center;">{tot_str}</span>'
                        f'</div>'
                    )

                if has_others:
                    other_grps = list(grp_counts.index[3:])
                    sub_oth = df_sub[df_sub['owner_group_clean'].isin(other_grps)]
                    sub_oth_uli = sub_oth[sub_oth['wzone_clean'] == 'ULI']
                    sub_oth_gmb = sub_oth[sub_oth['wzone_clean'] == 'GMB']
                    tot_oth = len(sub_oth)
                    
                    uli_str = make_asr_link(len(sub_oth_uli), f"modal-asr-{card_slug}-lainnya-uli", f"{card_title} - LAINNYA (ULI)", sub_oth_uli, underline=False, color="#ffffff")
                    gmb_str = make_asr_link(len(sub_oth_gmb), f"modal-asr-{card_slug}-lainnya-gmb", f"{card_title} - LAINNYA (GMB)", sub_oth_gmb, underline=False, color="#ffffff")
                    tot_str = make_asr_link(tot_oth, f"modal-asr-{card_slug}-lainnya-total", f"{card_title} - LAINNYA (TOTAL)", sub_oth, underline=False, color="#38bdf8")
                    oth_title = html_lib.escape(", ".join(other_grps))
                    
                    html_rows.append(
                        f'<div class="asr-card-tbl-row" style="grid-template-columns: 2.1fr 1fr 1fr 1fr;">'
                        f'<span style="color:#94a3b8; font-weight:700; font-size:0.96rem; font-style:italic;" title="Grup Lainnya: {oth_title}">LAINNYA ({len(other_grps)})</span>'
                        f'<span style="text-align:center;">{uli_str}</span>'
                        f'<span style="text-align:center;">{gmb_str}</span>'
                        f'<span style="text-align:center;">{tot_str}</span>'
                        f'</div>'
                    )
                elif len(top_grps) < 4:
                    for _ in range(4 - len(top_grps)):
                        html_rows.append(
                            '<div class="asr-card-tbl-row" style="grid-template-columns: 2.1fr 1fr 1fr 1fr; opacity:0.3;">'
                            '<span style="color:#64748b; font-size:0.96rem;">-</span>'
                            '<span style="text-align:center; color:#64748b; font-size:1.02rem; font-weight:700;">-</span>'
                            '<span style="text-align:center; color:#64748b; font-size:1.02rem; font-weight:700;">-</span>'
                            '<span style="text-align:center; color:#64748b; font-size:1.02rem; font-weight:700;">-</span>'
                            '</div>'
                        )
                return "".join(html_rows)

            proactive_rows_def = [
                ('PRA SQM', '#38bdf8'),
                ('PRA SQM GAUL', '#fbbf24'),
                ('SQM', '#c084fc'),
                ('UNSPEC', '#f87171')
            ]

            def render_proactive_rows(df_sub, card_slug="proactive-open", card_title="TIKET PROACTIVE OPEN"):
                html_rows = []
                for jenis_name, color in proactive_rows_def:
                    sub = df_sub[df_sub['jenis_clean'] == jenis_name] if ('jenis_clean' in df_sub.columns and not df_sub.empty) else pd.DataFrame()
                    sub_tsel = sub[sub['seg_clean'] == 'PL-TSEL'] if ('seg_clean' in sub.columns and not sub.empty) else pd.DataFrame()
                    sub_hsi = sub[sub['seg_clean'] == 'HSI (B2B)'] if ('seg_clean' in sub.columns and not sub.empty) else pd.DataFrame()
                    tot_cnt = len(sub)
                    jenis_slug = make_slug(jenis_name)
                    
                    tsel_str = make_asr_link(len(sub_tsel), f"modal-asr-{card_slug}-{jenis_slug}-tsel", f"{card_title} - {jenis_name} (PL-TSEL)", sub_tsel, underline=False, color="#ffffff")
                    hsi_str = make_asr_link(len(sub_hsi), f"modal-asr-{card_slug}-{jenis_slug}-hsi", f"{card_title} - {jenis_name} (HSI B2B)", sub_hsi, underline=False, color="#ffffff")
                    tot_str = make_asr_link(tot_cnt, f"modal-asr-{card_slug}-{jenis_slug}-total", f"{card_title} - {jenis_name} (TOTAL)", sub, underline=False, color="#38bdf8")
                    
                    html_rows.append(
                        f'<div class="asr-card-tbl-row" style="grid-template-columns: 2fr 1fr 1fr 1fr;">'
                        f'<span style="color:{color}; font-weight:700; font-size:0.96rem; white-space:nowrap;">{jenis_name}</span>'
                        f'<span style="text-align:center;">{tsel_str}</span>'
                        f'<span style="text-align:center;">{hsi_str}</span>'
                        f'<span style="text-align:center;">{tot_str}</span>'
                        f'</div>'
                    )
                return "".join(html_rows)

            def build_asr_modal_html(modal_id, modal_title, sub_df):
                if 'dt_rep' in sub_df.columns:
                    sub_df = sub_df.sort_values(by='dt_rep', ascending=False)
                
                rows_html = []
                limit_modal = 300
                disp_df = sub_df.head(limit_modal)
                for idx, row in enumerate(disp_df.to_dict('records'), 1):
                    bg_tr = "#0f172a" if idx % 2 == 1 else "rgba(30,41,59,0.55)"
                    inc_val = html_lib.escape(safe_val(row, 'incident'))
                    rep_val = html_lib.escape(safe_val(row, 'reported_date'))
                    
                    raw_stat = safe_val(row, 'status').upper()
                    stat_badge = status_badges_daily.get(raw_stat, f'<span style="background: rgba(148,163,184,0.18); border: 1px solid #64748b; color: #cbd5e1; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">{html_lib.escape(raw_stat)}</span>')
                    
                    c_tier = row.get('cust_tier', 'REGULER')
                    cust_badge = cust_badges_daily.get(c_tier, f'<span style="background: rgba(59,130,246,0.18); border: 1px solid #3b82f6; color: #60a5fa; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">{html_lib.escape(c_tier)}</span>')
                    
                    ttr_val = row.get(col_map.get('ttr_val', 'TTR CUSTOMER'), None)
                    ttr_badge = compute_ttr_badge(ttr_val, c_tier, safe_val(row, 'reported_date'))
                    
                    cname_val = html_lib.escape(safe_val(row, 'cust_name'))
                    stype_val = html_lib.escape(safe_val(row, 'service'))
                    wzone_val = html_lib.escape(str(row.get('wzone_clean', '-')))
                    owner_val = html_lib.escape(safe_val(row, 'owner_group', str(row.get('owner_group_clean', '-'))))
                    alpro_val = html_lib.escape(get_alpro_ok(row))
                    tek_val = html_lib.escape(safe_val(row, 'teknisi', safe_val(row, 'NAMA TEKNISI', safe_val(row, 'TEKNISI ADING', '-'))))
                    if tek_val.startswith('['):
                        tek_val = '-'
                    summary_val = html_lib.escape(safe_val(row, 'summary'))
                    
                    r = (
                        f'<tr style="background-color:{bg_tr}; border-bottom:1px solid rgba(255,255,255,0.06);">'
                        f'<td style="padding:10px 8px; text-align:center; color:#94a3b8; font-weight:600; border-right:1px solid rgba(255,255,255,0.08);">{idx}</td>'
                        f'<td style="padding:10px 10px; text-align:center; font-family:monospace; font-size:0.85rem; font-weight:700; color:#38bdf8; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.08);">{inc_val}</td>'
                        f'<td style="padding:10px 10px; text-align:center; color:#ffffff; font-weight:600; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.08);">{rep_val}</td>'
                        f'<td style="padding:10px 10px; text-align:center; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.08);">{stat_badge}</td>'
                        f'<td style="padding:10px 10px; text-align:center; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.08);">{cust_badge}</td>'
                        f'<td style="padding:10px 8px; text-align:center; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.08);">{ttr_badge}</td>'
                        f'<td style="padding:10px 10px; text-align:center; color:#ffffff; font-weight:600; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.08);">{cname_val}</td>'
                        f'<td style="padding:10px 10px; text-align:center; color:#ffffff; font-weight:600; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.08);">{stype_val}</td>'
                        f'<td style="padding:10px 10px; text-align:center; font-weight:700; color:#f8fafc; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.08);">{wzone_val}</td>'
                        f'<td style="padding:10px 10px; text-align:center; color:#cbd5e1; font-size:0.82rem; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.08);">{owner_val}</td>'
                        f'<td style="padding:10px 10px; text-align:center; font-family:monospace; font-size:0.83rem; font-weight:700; color:#38bdf8; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.08);">{alpro_val}</td>'
                        f'<td style="padding:10px 10px; text-align:center; font-weight:700; color:#facc15; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.08);">{tek_val}</td>'
                        f'<td style="padding:10px 16px; min-width:700px; max-width:900px; line-height:1.5; color:#cbd5e1; font-size:0.80rem; white-space:normal; word-break:break-word; text-align:justify; text-justify:inter-word;">{summary_val}</td>'
                        f'</tr>'
                    )
                    rows_html.append(r)
                
                table_body = "".join(rows_html)
                
                modal_html = (
                    f'<div id="{modal_id}" class="detail-modal asr-modal-box" style="display:none; position:fixed; top:6%; left:3%; right:3%; bottom:6%; background:#0f172a; z-index:999999; border:2.5px solid #eab308; border-radius:12px; box-shadow:0 25px 50px -12px rgba(0,0,0,0.95); flex-direction:column; overflow:hidden;">'
                    f'<div style="padding:12px 20px; background:#1e293b; display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid #334155; flex-shrink:0; gap:16px;">'
                    f'<div style="display:flex; align-items:center; gap:12px; min-width:0; flex-shrink:1;">'
                    f'<h3 style="margin:0; color:#ffffff; font-size:1.15rem; font-weight:700; letter-spacing:0.5px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">Detail Data: {modal_title}</h3>'
                    f'<span class="asr-modal-counter-badge" style="background:rgba(234,179,8,0.2); color:#facc15; border:1px solid #eab308; padding:3px 12px; border-radius:12px; font-size:0.8rem; font-weight:700; white-space:nowrap;" data-total="{len(sub_df)}">{len(sub_df):,} Tiket</span>'
                    f'</div>'
                    f'<div style="display:flex; align-items:center; gap:14px; flex-shrink:0;">'
                    f'<div style="position:relative; display:flex; align-items:center;">'
                    f'<span style="position:absolute; left:11px; color:#60a5fa; font-size:0.88rem; pointer-events:none;">🔍</span>'
                    f'<input type="text" class="asr-modal-search-box" placeholder="Cari Tiket / Pelanggan / Summary..." autocomplete="off" />'
                    f'<button type="button" class="asr-modal-search-clear" style="display:none; position:absolute; right:8px; background:none; border:none; color:#94a3b8; font-size:1.15rem; cursor:pointer; padding:0 4px; line-height:1;" title="Hapus Pencarian">&times;</button>'
                    f'</div>'
                    f'<button class="modal-close" style="background:none; border:none; color:#cbd5e1; font-size:2rem; cursor:pointer; line-height:1; padding:0 6px;" title="Tutup Modal">&times;</button>'
                    f'</div>'
                    f'</div>'
                    f'<div class="asr-modal-scroll" style="padding:0; overflow-y:auto; overflow-x:scroll !important; flex:1; min-height:0; background:#0b1120;">'
                    f'<table class="asr-modal-table" style="width:100%; border-collapse:separate; border-spacing:0; font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,sans-serif; text-align:left; font-size:0.82rem; min-width:2350px;">'
                    f'<thead>'
                    f'<tr>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 8px; width:50px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">NO</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 10px; width:150px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">INCIDENT</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 10px; width:165px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">REPORTED DATE</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 10px; width:130px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">STATUS</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 10px; width:150px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">CUSTOMER TYPE</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 8px; width:160px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">TTR CUSTOMER</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 10px; width:220px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">CUSTOMER NAME</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 10px; width:120px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">SERVICE</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 10px; width:95px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">WORKZONE</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 10px; width:240px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">OWNER GROUP</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 10px; width:160px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">ALPRO OK</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; border-right:1px solid rgba(255,255,255,0.15); padding:12px 10px; width:140px; text-align:center; font-weight:900; color:#facc15; font-size:0.82rem; letter-spacing:0.5px;">TEKNISI ADING</th>'
                    f'<th style="position:sticky; top:0; z-index:50; background:#1e3a8a; border-bottom:2.5px solid #3b82f6; padding:12px 16px; min-width:700px; text-align:center; font-weight:900; color:#ffffff; font-size:0.82rem; letter-spacing:0.5px;">SUMMARY TIKET</th>'
                    f'</tr>'
                    f'</thead>'
                    f'<tbody>'
                    f'{table_body}'
                    f'</tbody>'
                    f'</table>'
                    f'</div>'
                    f'</div>'
                )
                return modal_html

            # 4. Render 9 KPI Grid Cards (Layout 3x3 Sesuai Konsep Baru)
            cards_html = f'''<div class="asr-grid-3">

<div class="asr-card asr-card-blue">
<div class="asr-card-hdr">
<div class="asr-card-hdr-left">
<div class="asr-card-icon" style="background:rgba(59,130,246,0.2); color:#3b82f6;">\U0001F4E5</div>
<div class="asr-card-title">TIKET MASUK HI</div>
</div>
<div class="asr-card-val">{make_asr_link(len(df_masuk_hi), "modal-asr-masuk-hi-total", "TIKET MASUK HI - SEMUA TIKET", df_masuk_hi, underline=False, is_header=True)}</div>
</div>
<div class="asr-card-tbl-hdr" style="grid-template-columns: 2fr 1fr 1fr 1fr;">
<span></span><span style="text-align:center;">ULI</span><span style="text-align:center;">GMB</span><span style="text-align:center; color:#38bdf8;">TOTAL</span>
</div>
<div>{render_wzone_rows(df_masuk_hi, "masuk-hi", "TIKET MASUK HI")}</div>
</div>

<div class="asr-card asr-card-emerald">
<div class="asr-card-hdr">
<div class="asr-card-hdr-left">
<div class="asr-card-icon" style="background:rgba(5,150,105,0.2); color:#10b981;">\u23F1\uFE0F</div>
<div class="asr-card-title">TTR TIKET CLOSE</div>
</div>
<div class="asr-card-val">{make_asr_link(len(df_ttr_close), "modal-asr-ttr-close-total", "TTR TIKET CLOSE - SEMUA TIKET", df_ttr_close, underline=False, is_header=True)}</div>
</div>
<div class="asr-card-tbl-hdr" style="grid-template-columns: 1.8fr 1.1fr 1.1fr 1.1fr;">
<span></span><span style="text-align:center; color:#34d399;">NOT OSLA</span><span style="text-align:center; color:#f87171;">OSLA</span><span style="text-align:center; color:#38bdf8;">TOTAL</span>
</div>
<div>{render_ttr_rows(df_ttr_close, "ttr-close", "TTR TIKET CLOSE")}</div>
</div>

<div class="asr-card asr-card-teal">
<div class="asr-card-hdr">
<div class="asr-card-hdr-left">
<div class="asr-card-icon" style="background:rgba(20,184,166,0.2); color:#14b8a6;">\U0001F91D</div>
<div class="asr-card-title">MANJA CLOSE</div>
</div>
<div class="asr-card-val">{make_asr_link(len(df_manja_close), "modal-asr-manja-close-total", "MANJA CLOSE - SEMUA TIKET", df_manja_close, underline=False, is_header=True)}</div>
</div>
<div class="asr-card-tbl-hdr" style="grid-template-columns: 2fr 1fr 1fr 1fr;">
<span></span><span style="text-align:center;">ULI</span><span style="text-align:center;">GMB</span><span style="text-align:center; color:#38bdf8;">TOTAL</span>
</div>
<div>{render_wzone_rows(df_manja_close, "manja-close", "MANJA CLOSE")}</div>
</div>

<div class="asr-card asr-card-sky">
<div class="asr-card-hdr">
<div class="asr-card-hdr-left">
<div class="asr-card-icon" style="background:rgba(14,165,233,0.2); color:#0ea5e9;">\U0001F4C2</div>
<div class="asr-card-title">ALL TIKET OPEN</div>
</div>
<div class="asr-card-val">{make_asr_link(len(df_all_open), "modal-asr-all-open-total", "ALL TIKET OPEN - SEMUA TIKET", df_all_open, underline=False, is_header=True)}</div>
</div>
<div class="asr-card-tbl-hdr" style="grid-template-columns: 2fr 1fr 1fr 1fr;">
<span></span><span style="text-align:center;">ULI</span><span style="text-align:center;">GMB</span><span style="text-align:center; color:#38bdf8;">TOTAL</span>
</div>
<div>{render_wzone_rows(df_all_open, "all-open", "ALL TIKET OPEN")}</div>
</div>

<div class="asr-card asr-card-amber">
<div class="asr-card-hdr">
<div class="asr-card-hdr-left">
<div class="asr-card-icon" style="background:rgba(245,158,11,0.2); color:#f59e0b;">\u23F3</div>
<div class="asr-card-title">ALL TTR TIKET OPEN</div>
</div>
<div class="asr-card-val">{make_asr_link(len(df_ttr_open), "modal-asr-ttr-open-total", "ALL TTR TIKET OPEN - SEMUA TIKET", df_ttr_open, underline=False, is_header=True)}</div>
</div>
<div class="asr-card-tbl-hdr" style="grid-template-columns: 1.8fr 1.1fr 1.1fr 1.1fr;">
<span></span><span style="text-align:center; color:#34d399;">NOT OSLA</span><span style="text-align:center; color:#f87171;">OSLA</span><span style="text-align:center; color:#38bdf8;">TOTAL</span>
</div>
<div>{render_ttr_rows(df_ttr_open, "ttr-open", "ALL TTR TIKET OPEN")}</div>
</div>

<div class="asr-card asr-card-indigo">
<div class="asr-card-hdr">
<div class="asr-card-hdr-left">
<div class="asr-card-icon" style="background:rgba(99,102,241,0.2); color:#6366f1;">\U0001F91D</div>
<div class="asr-card-title">ALL MANJA OPEN</div>
</div>
<div class="asr-card-val">{make_asr_link(len(df_manja_open), "modal-asr-manja-open-total", "ALL MANJA OPEN - SEMUA TIKET", df_manja_open, underline=False, is_header=True)}</div>
</div>
<div class="asr-card-tbl-hdr" style="grid-template-columns: 2fr 1fr 1fr 1fr;">
<span></span><span style="text-align:center;">ULI</span><span style="text-align:center;">GMB</span><span style="text-align:center; color:#38bdf8;">TOTAL</span>
</div>
<div>{render_wzone_rows(df_manja_open, "manja-open", "ALL MANJA OPEN")}</div>
</div>

<div class="asr-card asr-card-green">
<div class="asr-card-hdr">
<div class="asr-card-hdr-left">
<div class="asr-card-icon" style="background:rgba(16,185,129,0.2); color:#10b981;">\u2705</div>
<div class="asr-card-title">TIKET CLOSE HI</div>
</div>
<div class="asr-card-val">{make_asr_link(len(df_close_hi), "modal-asr-close-hi-total", "TIKET CLOSE HI - SEMUA TIKET", df_close_hi, underline=False, is_header=True)}</div>
</div>
<div class="asr-card-tbl-hdr" style="grid-template-columns: 2fr 1fr 1fr 1fr;">
<span></span><span style="text-align:center;">ULI</span><span style="text-align:center;">GMB</span><span style="text-align:center; color:#38bdf8;">TOTAL</span>
</div>
<div>{render_wzone_rows(df_close_hi, "close-hi", "TIKET CLOSE HI")}</div>
</div>

<div class="asr-card asr-card-violet">
<div class="asr-card-hdr">
<div class="asr-card-hdr-left">
<div class="asr-card-icon" style="background:rgba(168,85,247,0.2); color:#a855f7;">\u26A1</div>
<div class="asr-card-title">TIKET PROACTIVE OPEN</div>
</div>
<div class="asr-card-val">{make_asr_link(len(df_proactive_open), "modal-asr-proactive-open-total", "TIKET PROACTIVE OPEN - SEMUA TIKET", df_proactive_open, underline=False, is_header=True)}</div>
</div>
<div class="asr-card-tbl-hdr" style="grid-template-columns: 2fr 1fr 1fr 1fr;">
<span></span><span style="text-align:center;">PL-TSEL</span><span style="text-align:center;">HSI (B2B)</span><span style="text-align:center; color:#38bdf8;">TOTAL</span>
</div>
<div>{render_proactive_rows(df_proactive_open, "proactive-open", "TIKET PROACTIVE OPEN")}</div>
</div>

<div class="asr-card asr-card-purple">
<div class="asr-card-hdr">
<div class="asr-card-hdr-left">
<div class="asr-card-icon" style="background:rgba(139,92,246,0.2); color:#8b5cf6;">\U0001F465</div>
<div class="asr-card-title">OWNER GRUP OPEN</div>
</div>
<div class="asr-card-val">{make_asr_link(len(df_owner_open), "modal-asr-owner-total", "OWNER GRUP OPEN - SEMUA TIKET", df_owner_open, underline=False, is_header=True)}</div>
</div>
<div class="asr-card-tbl-hdr" style="grid-template-columns: 2.1fr 1fr 1fr 1fr;">
<span></span><span style="text-align:center;">ULI</span><span style="text-align:center;">GMB</span><span style="text-align:center; color:#38bdf8;">TOTAL</span>
</div>
<div>{render_owner_rows(df_owner_open, "owner", "OWNER GRUP OPEN")}</div>
</div>

</div>'''
            st.markdown(cards_html, unsafe_allow_html=True)

            # Render All Modals for Clicked Numbers
            if asr_modals:
                modals_html_list = [
                    '<div id="asr-modal-backdrop" class="modal-backdrop" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.65); backdrop-filter:blur(3px); z-index:999998;"></div>'
                ]
                for m_id, (m_title, m_df) in asr_modals.items():
                    modals_html_list.append(build_asr_modal_html(m_id, m_title, m_df))
                
                all_asr_modals_html = "".join(modals_html_list).replace('\n', '')
                st.markdown(all_asr_modals_html, unsafe_allow_html=True)

            # Client-Side Modal Event Handlers
            import streamlit.components.v1 as components
            components.html('''
            <script>
            setInterval(function() {
                const parentDoc = window.parent.document;
                if (!parentDoc) return;
                
                // Backdrop element listener
                const backdrop = parentDoc.getElementById('asr-modal-backdrop');
                if (backdrop && !backdrop.dataset.listener) {
                    backdrop.dataset.listener = 'true';
                    backdrop.addEventListener('click', function() {
                        const modals = parentDoc.querySelectorAll('.detail-modal');
                        modals.forEach(m => m.style.display = 'none');
                        this.style.display = 'none';
                    });
                }

                // Open modal triggers
                const triggers = parentDoc.querySelectorAll('.modal-trigger');
                triggers.forEach(t => {
                    if(t.dataset.listener) return;
                    t.dataset.listener = 'true';
                    t.addEventListener('click', function(e) {
                        e.preventDefault();
                        const targetId = this.getAttribute('data-target') || ('modal-' + (this.getAttribute('data-cat')||'').replace(/ /g, '_') + '-' + (this.getAttribute('data-prod')||'').replace(/ /g, '_'));
                        
                        const modals = parentDoc.querySelectorAll('.detail-modal');
                        modals.forEach(m => m.style.display = 'none');
                        
                        const target = parentDoc.getElementById(targetId);
                        if(target) {
                            target.style.display = 'flex';
                            if(backdrop) backdrop.style.display = 'block';

                            // Reset and focus search input on open
                            const searchInput = target.querySelector('.asr-modal-search-box');
                            if (searchInput) {
                                searchInput.value = '';
                                const clearBtn = target.querySelector('.asr-modal-search-clear');
                                if (clearBtn) clearBtn.style.display = 'none';
                                const badge = target.querySelector('.asr-modal-counter-badge');
                                const totalCount = badge ? parseInt(badge.getAttribute('data-total') || '0') : 0;
                                if (badge) {
                                    badge.textContent = totalCount.toLocaleString() + ' Tiket';
                                    badge.style.background = 'rgba(234,179,8,0.2)';
                                    badge.style.borderColor = '#eab308';
                                    badge.style.color = '#facc15';
                                }
                                const tableBody = target.querySelector('.asr-modal-table tbody');
                                if (tableBody) {
                                    tableBody.querySelectorAll('tr').forEach(r => r.style.display = '');
                                }
                                setTimeout(() => searchInput.focus(), 80);
                            }
                        }
                    });
                });
                
                // Real-time Search within Modal
                const searchInputs = parentDoc.querySelectorAll('.asr-modal-search-box');
                searchInputs.forEach(input => {
                    if (input.dataset.listener) return;
                    input.dataset.listener = 'true';
                    
                    const modal = input.closest('.detail-modal');
                    if (!modal) return;
                    const clearBtn = modal.querySelector('.asr-modal-search-clear');
                    const badge = modal.querySelector('.asr-modal-counter-badge');
                    const tableBody = modal.querySelector('.asr-modal-table tbody');
                    const totalCount = badge ? parseInt(badge.getAttribute('data-total') || '0') : 0;
                    
                    function doFilter() {
                        const val = input.value.toLowerCase().trim();
                        if (clearBtn) {
                            clearBtn.style.display = val.length > 0 ? 'block' : 'none';
                        }
                        if (!tableBody) return;
                        const rows = tableBody.querySelectorAll('tr');
                        let matched = 0;
                        rows.forEach(r => {
                            const text = (r.textContent || '').toLowerCase();
                            if (!val || text.indexOf(val) !== -1) {
                                r.style.display = '';
                                matched++;
                            } else {
                                r.style.display = 'none';
                            }
                        });
                        if (badge) {
                            if (!val) {
                                badge.textContent = totalCount.toLocaleString() + ' Tiket';
                                badge.style.background = 'rgba(234,179,8,0.2)';
                                badge.style.borderColor = '#eab308';
                                badge.style.color = '#facc15';
                            } else {
                                badge.textContent = matched.toLocaleString() + ' / ' + totalCount.toLocaleString() + ' Tiket';
                                if (matched === 0) {
                                    badge.style.background = 'rgba(239,68,68,0.2)';
                                    badge.style.borderColor = '#ef4444';
                                    badge.style.color = '#f87171';
                                } else {
                                    badge.style.background = 'rgba(56,189,248,0.2)';
                                    badge.style.borderColor = '#38bdf8';
                                    badge.style.color = '#38bdf8';
                                }
                            }
                        }
                    }
                    
                    input.addEventListener('input', doFilter);
                    input.addEventListener('keydown', function(e) {
                        if (e.key === 'Escape') {
                            if (input.value) {
                                input.value = '';
                                doFilter();
                                e.stopPropagation();
                            }
                        }
                    });
                    
                    if (clearBtn) {
                        clearBtn.addEventListener('click', function(e) {
                            e.preventDefault();
                            input.value = '';
                            doFilter();
                            input.focus();
                        });
                    }
                });

                // Horizontal wheel scroll helper for modal table
                const scrollContainers = parentDoc.querySelectorAll('.asr-modal-scroll');
                scrollContainers.forEach(sc => {
                    if (sc.dataset.wheelListener) return;
                    sc.dataset.wheelListener = 'true';
                    sc.addEventListener('wheel', function(e) {
                        const rect = sc.getBoundingClientRect();
                        if (e.shiftKey || (e.clientY >= rect.bottom - 45 && e.clientY <= rect.bottom)) {
                            if (e.deltaY !== 0) {
                                sc.scrollLeft += (e.deltaY * 1.5);
                                e.preventDefault();
                            }
                        }
                    }, { passive: false });
                });

                // Close modal buttons
                const closers = parentDoc.querySelectorAll('.modal-close');
                closers.forEach(c => {
                    if(c.dataset.listener) return;
                    c.dataset.listener = 'true';
                    c.addEventListener('click', function(e) {
                        e.preventDefault();
                        const modal = this.closest('.detail-modal');
                        if(modal) {
                            modal.style.display = 'none';
                        }
                        if(backdrop) backdrop.style.display = 'none';
                    });
                });

                // ESC key closes modal
                if (!parentDoc.dataset.asrEscListener) {
                    parentDoc.dataset.asrEscListener = 'true';
                    parentDoc.addEventListener('keydown', function(e) {
                        if (e.key === 'Escape') {
                            const modals = parentDoc.querySelectorAll('.detail-modal');
                            modals.forEach(m => m.style.display = 'none');
                            if(backdrop) backdrop.style.display = 'none';
                        }
                    });
                }
            }, 400);
            </script>
            ''', height=0, width=0)

            # 5. Tabel Detail Interaktif di Bawah Kartu
            st.markdown('<div class="section-title-wrap" style="margin-top: 20px;"><div class="section-title">\U0001F4CB TABEL RINCIAN TIKET DAILY ASSURANCE</div></div>', unsafe_allow_html=True)
            
            detail_filter = st.radio(
                "Filter Kategori Tampilan:",
                options=["\U0001F4E5 Tiket Masuk HI", "\U0001F4C2 All Tiket Open", "\U0001F91D MANJA", "\u2705 Tiket Close HI", "\u23F1\uFE0F Tiket OSLA (Lewat Batas SLA)", "\U0001F310 Semua Tiket"],
                horizontal=True,
                key="radio_asr_daily_cat"
            )

            if "Tiket Masuk HI" in detail_filter:
                df_view_tbl = df_masuk_hi
            elif "All Tiket Open" in detail_filter:
                df_view_tbl = df_all_open
            elif "MANJA" in detail_filter:
                df_view_tbl = df_manja
            elif "Tiket Close HI" in detail_filter:
                df_view_tbl = df_close_hi
            elif "Tiket OSLA" in detail_filter:
                df_view_tbl = df_all_open[df_all_open['osla_status'] == 'OSLA']
            else:
                df_view_tbl = df_asr

            c_flt1, c_flt2, c_flt3 = st.columns([1, 1, 2])
            with c_flt1:
                opt_cust = ["Semua"] + [t[0] for t in tiers_list]
                sel_cust = st.selectbox("Filter Tipe Pelanggan:", opt_cust, key="sel_daily_cust")
            with c_flt2:
                sel_wz = st.selectbox("Filter Workzone:", ["Semua", "ULI", "GMB"], key="sel_daily_wz")
            with c_flt3:
                srch_txt = st.text_input("\U0001F50D Cari Tiket / Pelanggan / Summary:", key="txt_daily_search")

            df_tbl_final = df_view_tbl.copy()
            if sel_cust != "Semua":
                df_tbl_final = df_tbl_final[df_tbl_final['cust_tier'] == sel_cust]
            if sel_wz != "Semua":
                df_tbl_final = df_tbl_final[df_tbl_final['wzone_clean'] == sel_wz]
            if srch_txt:
                s_lower = srch_txt.lower()
                m1 = df_tbl_final[col_map.get('incident', 'INCIDENT')].astype(str).str.lower().str.contains(s_lower, na=False) if 'incident' in col_map else False
                m2 = df_tbl_final[col_map.get('cust_name', 'CUSTOMER NAME')].astype(str).str.lower().str.contains(s_lower, na=False) if 'cust_name' in col_map else False
                m3 = df_tbl_final[col_map.get('summary', 'SUMMARY')].astype(str).str.lower().str.contains(s_lower, na=False) if 'summary' in col_map else False
                df_tbl_final = df_tbl_final[m1 | m2 | m3]

            st.caption(f"Menampilkan **{len(df_tbl_final):,}** tiket dari kategori **{detail_filter}**.")

            if df_tbl_final.empty:
                st.info("Tidak ada tiket yang cocok dengan filter yang dipilih.")
            else:
                cust_badges_daily = {
                    'HVC GOLD': '<span style="background: rgba(234,179,8,0.18); border: 1px solid #eab308; color: #facc15; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">HVC_GOLD</span>',
                    'HVC PLATINUM': '<span style="background: rgba(168,85,247,0.18); border: 1px solid #a855f7; color: #c084fc; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">HVC_PLATINUM</span>',
                    'HVC DIAMOND': '<span style="background: rgba(6,182,212,0.18); border: 1px solid #06b6d4; color: #22d3ee; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">HVC_DIAMOND</span>',
                    'REGULER': '<span style="background: rgba(59,130,246,0.18); border: 1px solid #3b82f6; color: #60a5fa; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">REGULER</span>',
                    'HVC REGULER': '<span style="background: rgba(59,130,246,0.18); border: 1px solid #3b82f6; color: #60a5fa; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">REGULER</span>',
                }
                status_badges_daily = {
                    'ANALYSIS': '<span style="background: rgba(245,158,11,0.18); border: 1px solid #f59e0b; color: #fbbf24; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">ANALYSIS</span>',
                    'BACKEND': '<span style="background: rgba(234,179,8,0.18); border: 1px solid #eab308; color: #facc15; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">BACKEND</span>',
                    'CLOSED': '<span style="background: rgba(16,185,129,0.18); border: 1px solid #10b981; color: #34d399; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">CLOSED</span>',
                    'RESOLVED': '<span style="background: rgba(16,185,129,0.18); border: 1px solid #10b981; color: #34d399; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">RESOLVED</span>',
                    'DRAFT': '<span style="background: rgba(148,163,184,0.18); border: 1px solid #64748b; color: #cbd5e1; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">DRAFT</span>'
                }

                limit_view = 200
                df_disp = df_tbl_final.head(limit_view)
                t_rows = []
                for idx, row in enumerate(df_disp.to_dict('records')):
                    bg_tr = "#0f172a" if idx % 2 == 0 else "#0b1120"
                    inc_val = html_lib.escape(str(row.get(col_map.get('incident', 'INCIDENT'), '-')))
                    rep_val = html_lib.escape(str(row.get(col_map.get('reported_date', 'REPORTED DATE'), '-')))
                    
                    raw_stat = str(row.get(col_map.get('status', 'STATUS'), '-')).upper().strip()
                    stat_badge = status_badges_daily.get(raw_stat, f'<span style="background: rgba(148,163,184,0.18); border: 1px solid #64748b; color: #cbd5e1; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">{html_lib.escape(raw_stat)}</span>')
                    
                    c_tier = row.get('cust_tier', 'REGULER')
                    cust_badge = cust_badges_daily.get(c_tier, f'<span style="background: rgba(59,130,246,0.18); border: 1px solid #3b82f6; color: #60a5fa; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">{html_lib.escape(c_tier)}</span>')
                    
                    ttr_val = row.get(col_map.get('ttr_val', 'TTR CUSTOMER'), None)
                    ttr_badge = compute_ttr_badge(ttr_val, c_tier, row.get(col_map.get('reported_date', 'REPORTED DATE')))

                    cname_val = html_lib.escape(str(row.get(col_map.get('cust_name', 'CUSTOMER NAME'), '-')))
                    stype_val = html_lib.escape(str(row.get(col_map.get('service', 'SERVICE TYPE'), '-')))
                    wzone_val = html_lib.escape(str(row.get('wzone_clean', '-')))
                    owner_val = html_lib.escape(safe_val(row, 'owner_group', str(row.get('owner_group_clean', '-'))))
                    alpro_val = html_lib.escape(get_alpro_ok(row))
                    tek_val = html_lib.escape(safe_val(row, 'teknisi', safe_val(row, 'NAMA TEKNISI', safe_val(row, 'TEKNISI ADING', '-'))))
                    if tek_val.startswith('['):
                        tek_val = '-'
                    summary_val = html_lib.escape(str(row.get(col_map.get('summary', 'SUMMARY'), '-')))

                    r_html = f'''<tr style="background-color: {bg_tr}; border-bottom: 1px solid #1e293b; transition: background 0.15s ease;">
                        <td style="padding: 12px 8px; text-align: center; color: #64748b; font-weight: 600; border-right: 1px solid rgba(255,255,255,0.08);">{idx+1}</td>
                        <td style="padding: 12px 12px; text-align: center; font-family: monospace; font-size: 0.85rem; font-weight: 700; color: #38bdf8; white-space: nowrap; border-right: 1px solid rgba(255,255,255,0.08);">{inc_val}</td>
                        <td style="padding: 12px 12px; text-align: center; color: #ffffff; font-weight: 700; white-space: nowrap; border-right: 1px solid rgba(255,255,255,0.08);">{rep_val}</td>
                        <td style="padding: 12px 12px; text-align: center; white-space: nowrap; border-right: 1px solid rgba(255,255,255,0.08);">{stat_badge}</td>
                        <td style="padding: 12px 12px; text-align: center; white-space: nowrap; border-right: 1px solid rgba(255,255,255,0.08);">{cust_badge}</td>
                        <td style="padding: 12px 10px; text-align: center; white-space: nowrap; border-right: 1px solid rgba(255,255,255,0.08);">{ttr_badge}</td>
                        <td style="padding: 12px 12px; text-align: center; color: #ffffff; font-weight: 600; white-space: nowrap; border-right: 1px solid rgba(255,255,255,0.08);">{cname_val}</td>
                        <td style="padding: 12px 12px; text-align: center; color: #ffffff; font-weight: 700; white-space: nowrap; border-right: 1px solid rgba(255,255,255,0.08);">{stype_val}</td>
                        <td style="padding: 12px 12px; text-align: center; font-weight: 700; color: #f8fafc; white-space: nowrap; border-right: 1px solid rgba(255,255,255,0.08);">{wzone_val}</td>
                        <td style="padding: 12px 12px; text-align: center; color: #cbd5e1; font-size: 0.82rem; white-space: nowrap; border-right: 1px solid rgba(255,255,255,0.08);">{owner_val}</td>
                        <td style="padding: 12px 12px; text-align: center; font-family: monospace; font-size: 0.83rem; font-weight: 700; color: #38bdf8; white-space: nowrap; border-right: 1px solid rgba(255,255,255,0.08);">{alpro_val}</td>
                        <td style="padding: 12px 12px; text-align: center; font-weight: 700; color: #facc15; white-space: nowrap; border-right: 1px solid rgba(255,255,255,0.08);">{tek_val}</td>
                        <td style="padding: 12px 18px; min-width: 450px; max-width: 750px; line-height: 1.5; color: #cbd5e1; font-size: 0.80rem; white-space: normal; word-break: break-word; text-align: justify; text-justify: inter-word;">{summary_val}</td>
                    </tr>'''
                    t_rows.append(r_html)

                t_body = "".join(t_rows)
                tbl_html = f'''
                <div class="asr-scroll-container">
                    <table class="asr-table-custom">
                        <thead>
                            <tr>
                                <th style="width: 50px; text-align: center;">NO</th>
                                <th style="width: 145px; text-align: center;">INCIDENT</th>
                                <th style="width: 165px; text-align: center;">REPORTED DATE</th>
                                <th style="width: 130px; text-align: center;">STATUS</th>
                                <th style="width: 155px; text-align: center;">CUSTOMER TYPE</th>
                                <th style="width: 165px; text-align: center;">TTR CUSTOMER</th>
                                <th style="width: 180px; text-align: center;">CUSTOMER NAME</th>
                                <th style="width: 110px; text-align: center;">SERVICE</th>
                                <th style="width: 90px; text-align: center;">WORKZONE</th>
                                <th style="width: 170px; text-align: center;">OWNER GROUP</th>
                                <th style="width: 135px; text-align: center;">ALPRO OK</th>
                                <th style="width: 140px; text-align: center; color: #facc15;">TEKNISI ADING</th>
                                <th style="min-width: 450px; text-align: center;">SUMMARY TIKET</th>
                            </tr>
                        </thead>
                        <tbody>
                            {t_body}
                        </tbody>
                    </table>
                </div>
                '''
                st.markdown(tbl_html, unsafe_allow_html=True)
                if len(df_tbl_final) > limit_view:
                    st.caption(f"\u26A1 Menampilkan {limit_view:,} dari total {len(df_tbl_final):,} tiket untuk menjaga performa rendering browser.")

    elif menu in ["IBOOSTER ASGAR", "IBOOSTER GAUL"]:
        import os
        import re as regex

        base_dir_gaul = os.path.dirname(os.path.abspath(__file__))
        ibooster_asr_sync_time = "Belum Ada Data"
        for sync_candidate in ["last_ibooster_ASR.txt", "last_ibooster_AO_TSEL.txt"]:
            cand_path = os.path.join(base_dir_gaul, sync_candidate)
            if os.path.exists(cand_path):
                try:
                    with open(cand_path, "r", encoding="utf-8") as f_ib:
                        c_txt = f_ib.read().strip()
                        if c_txt:
                            ibooster_asr_sync_time = c_txt.split(" | VIA ")[0].replace(" WIB", "")
                            break
                except Exception:
                    pass

        @st.cache_data(ttl=120, show_spinner=False)
        def load_ibooster_gaul_dataset(insera_key, ibooster_key):
            # 1. Muat data GABUNGAN ALL & CLOSE TIKET (utamakan Google Sheets agar kolom CR / FORMAT IBOOSTER & DURASI PELAPORAN TIKET terbaca)
            df_gab = pd.DataFrame()
            gs_gab_url = "https://docs.google.com/spreadsheets/d/1bUXmomLo6DJYdk0CHGW9KCnoRgG8EqsUdOtALJ0_r7o/gviz/tq?tqx=out:csv&sheet=GABUNGAN%20ALL%20%26%20CLOSE%20TIKET"
            try:
                import io
                headers_gs = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
                resp_gs = requests.get(gs_gab_url, headers=headers_gs, timeout=25)
                if resp_gs.status_code == 200 and not resp_gs.text.strip().startswith("<!DOCTYPE"):
                    df_gab = pd.read_csv(io.StringIO(resp_gs.text), low_memory=False)
                else:
                    df_gab = pd.read_csv(gs_gab_url, low_memory=False)
                if 'INCIDENT' in df_gab.columns:
                    df_gab = df_gab[df_gab['INCIDENT'].astype(str) != 'METADATA_SYNC']
            except Exception:
                df_gab, _ = load_assurance_data(insera_key)

            if df_gab is None or df_gab.empty:
                df_gab, _ = load_assurance_data(insera_key)

            # 2. Muat data hasil ukur dari UKUR IBOOSTER ASR (cache parquet lokal -> Google Sheets UKUR IBOOSTER ASR -> fallback UKUR IBOOSTER)
            ib_map = {}
            local_ib_parquet = os.path.join(base_dir_gaul, "last_ibooster_asr.parquet")
            if os.path.exists(local_ib_parquet):
                try:
                    df_ib_loc = pd.read_parquet(local_ib_parquet)
                    for _, r_ib in df_ib_loc.iterrows():
                        nd_k = ''.join(ch for ch in str(r_ib.get('ND', '')).split('.')[0] if ch.isdigit())
                        if nd_k:
                            ib_map[nd_k] = (
                                str(r_ib.get('ONU LINK STATUS', '')).strip().upper(),
                                str(r_ib.get('HASIL UKUR IBOSSTER', '')).strip()
                            )
                except Exception:
                    pass

            if not ib_map:
                for sheet_ib_url in [
                    "https://docs.google.com/spreadsheets/d/1bUXmomLo6DJYdk0CHGW9KCnoRgG8EqsUdOtALJ0_r7o/export?format=csv&gid=1551994456",
                    "https://docs.google.com/spreadsheets/d/1bUXmomLo6DJYdk0CHGW9KCnoRgG8EqsUdOtALJ0_r7o/gviz/tq?tqx=out:csv&sheet=UKUR%20IBOOSTER%20ASR",
                    "https://docs.google.com/spreadsheets/d/1zA5ucYxE9gOSnKZIhEKQyV2rEdV5je__knsS9neA5iA/gviz/tq?tqx=out:csv&sheet=UKUR%20IBOOSTER"
                ]:
                    try:
                        df_ib_gs = pd.read_csv(sheet_ib_url, header=None, low_memory=False)
                        if not df_ib_gs.empty and df_ib_gs.shape[1] > 13:
                            for _, r_ib in df_ib_gs.iterrows():
                                raw_nd = str(r_ib.iloc[1]).strip().split('.')[0]
                                nd_k = ''.join(ch for ch in raw_nd if ch.isdigit())
                                if len(nd_k) >= 9:
                                    onu_v = str(r_ib.iloc[7]).strip().upper()
                                    rx_v = str(r_ib.iloc[13]).strip()
                                    if onu_v == 'LOS':
                                        rx_v = 'LOS'
                                    if nd_k not in ib_map:
                                        ib_map[nd_k] = (onu_v, rx_v)
                            if ib_map:
                                break
                    except Exception:
                        pass

            # 3. Muat mapping NIK & Nama Teknisi ke NAMA ALIAS (dari sheet TEKNISI ASSURANCE)
            FALLBACK_TEKNISI_ALIAS = {
                '26960116': 'HADINATA',
                '25920087': 'FAJRI',
                '25940110': 'IRWANSYAH',
                '25910103': 'HARIS',
                '25940111': 'FADEL',
                '25980159': 'EURO',
                '25030188': 'FIRDAUS',
                '25030187': 'RISKY',
                '25730020': 'BAMBANG',
                '25960168': 'DANI',
                '25020227': 'ALIMIN',
                '25980160': 'KHALIL',
                '25000179': 'AKBAR',
                '25980162': 'FEBRI',
                '25960167': 'DIPA',
                '25030189': 'HAFIZ',
                '25980161': 'AMAT',
                '25890089': 'RAHIM',
                '26000271': 'HALDI',
                '25930142': 'BAGUS',
                '25900066': 'TAUFIK',
                '25990215': 'SYAHRIL',
                '25990177': 'RAHMANA',
                '25030190': 'ARI',
                '18960013': 'ADI',
                # Nama lengkap ke alias
                'HADINATA AS\'AD': 'HADINATA',
                'HADINATA ASAD': 'HADINATA',
                'FAJRIANNOOR': 'FAJRI',
                'MUHAMMAD IRWANSYAH': 'IRWANSYAH',
                'HAJIS SANDI': 'HARIS',
                'FADEL AULIA': 'FADEL',
                'EURO HADI': 'EURO',
                'MUHAMMAD FIRDAUS': 'FIRDAUS',
                'MUHAMMAD RISKI': 'RISKY',
                'BAMBANG SUSILOTOMO': 'BAMBANG',
                'NOVRI WARDIANI': 'DANI',
                'M.KHALILURRAHMAN': 'KHALIL',
                'M. KHALILURRAHMAN': 'KHALIL',
                'KHAIRUL AKBAR': 'AKBAR',
                'M FEBRIANOOR': 'FEBRI',
                'M. FEBRIANOOR': 'FEBRI',
                'SANDRA DIPA MAURYA': 'DIPA',
                'MUHAMMAD HAFIZ': 'HAFIZ',
                'SELAMAT': 'AMAT',
                'ABDUL RAHIM': 'RAHIM',
                'MUHAMMAD HALDIANOOR': 'HALDI',
                'BAGUS PRAMANA': 'BAGUS',
                'TAUFIKKURRAHMAN': 'TAUFIK',
                'MUHAMMAD SYAHRIL': 'SYAHRIL',
                'ARI RAMADHAN': 'ARI',
                'MUHAMMAD ADI AMAYYANI': 'ADI',
            }

            alias_map = dict(FALLBACK_TEKNISI_ALIAS)
            try:
                gs_tek_url = "https://docs.google.com/spreadsheets/d/1bUXmomLo6DJYdk0CHGW9KCnoRgG8EqsUdOtALJ0_r7o/gviz/tq?tqx=out:csv&sheet=TEKNISI%20ASSURANCE"
                df_tek = pd.read_csv(gs_tek_url, low_memory=False)
                if not df_tek.empty:
                    col_map_t = {str(c).strip().upper(): c for c in df_tek.columns}
                    nik_c = col_map_t.get('NIK')
                    alias_c = col_map_t.get('NAMA ALIAS') or col_map_t.get('ALIAS')
                    nama_c = col_map_t.get('NAMA') or col_map_t.get('NAMA TEKNISI')
                    if nik_c and alias_c:
                        for _, r_t in df_tek.iterrows():
                            al_val = str(r_t.get(alias_c, '')).strip().upper()
                            if not al_val or al_val == 'NAN':
                                continue
                            raw_nik_val = str(r_t.get(nik_c, '')).strip().split('.')[0]
                            if raw_nik_val and raw_nik_val != 'nan':
                                alias_map[raw_nik_val] = al_val
                            if nama_c and pd.notna(r_t.get(nama_c)):
                                nm_val = str(r_t.get(nama_c, '')).strip().upper()
                                if nm_val and nm_val != 'NAN':
                                    alias_map[nm_val] = al_val
            except Exception:
                pass

            return df_gab, ib_map, alias_map

        with st.spinner("Memuat data IBOOSTER ASGAR (Assurance)..."):
            df_asr_gaul, ibooster_asr_map, teknisi_alias_map = load_ibooster_gaul_dataset(insera_time, ibooster_asr_sync_time)

        if df_asr_gaul is None or df_asr_gaul.empty:
            st.warning("⚠️ **Data tiket Assurance belum berhasil dimuat.**")
            st.info("💡 Pastikan Anda telah menarik data minimal 1 kali melalui tombol **'🚀 Tarik INSERA ASR'** dan **'🚀 Tarik IBOOSTER ASGAR'** di sidebar.")
        else:
            df_g = df_asr_gaul.copy()

            # 1. Filter STATUS TIKET harus CLOSE / CLOSED
            stat_col_g = 'STATUS TIKET' if 'STATUS TIKET' in df_g.columns else ('STATUS' if 'STATUS' in df_g.columns else None)
            if stat_col_g:
                df_g = df_g[df_g[stat_col_g].astype(str).str.strip().str.upper().str.contains('CLOSE', na=False)].copy()

            # 2. Hitung & Filter DURASI PELAPORAN TIKET <= 30 HARI
            dur_series = pd.Series(np.nan, index=df_g.index)
            if 'DURASI PELAPORAN TIKET' in df_g.columns:
                dur_series = pd.to_numeric(
                    df_g['DURASI PELAPORAN TIKET'].astype(str).str.extract(r'(\d+)')[0],
                    errors='coerce'
                )
            rep_col_g = next((c for c in ['REPORTED DATE', 'TANGGAL REPORTED', 'STATUS DATE'] if c in df_g.columns), None)
            if rep_col_g:
                rep_dt_g = pd.to_datetime(df_g[rep_col_g], format='mixed', dayfirst=True, errors='coerce')
                fallback_dur = (pd.Timestamp.now().normalize() - rep_dt_g.dt.normalize()).dt.days
                dur_series = dur_series.fillna(fallback_dur)

            df_g['Durasi_Num'] = dur_series.fillna(999)
            df_g = df_g[(df_g['Durasi_Num'] >= 0) & (df_g['Durasi_Num'] <= 30)].copy()
            total_closed_30d = len(df_g)

            # 3. Enrich Nomor Internet (Kolom CR = FORMAT IBOOSTER / SERVICE NO), Hasil Ukur Rx dBm, ONU Link Status, dan Prioritas Unspec
            hasil_col_existing = next((c for c in ['HASIL UKUR IBOSSTER', 'HASIL UKUR IBOOSTER', 'HASIL UKUR'] if c in df_g.columns), None)
            onu_col_existing = next((c for c in ['ONU LINK STATUS', 'GPON ONU LINK STATUS'] if c in df_g.columns), None)
            prio_col_existing = next((c for c in ['PRIORITAS UNSPEC', 'PRIORITAS'] if c in df_g.columns), None)

            gaul_records = []
            months_id_map = {1:'JANUARI', 2:'FEBRUARI', 3:'MARET', 4:'APRIL', 5:'MEI', 6:'JUNI', 7:'JULI', 8:'AGUSTUS', 9:'SEPTEMBER', 10:'OKTOBER', 11:'NOVEMBER', 12:'DESEMBER'}

            for _, row_g in df_g.iterrows():
                # Nomor Internet dari FORMAT IBOOSTER (CR) atau SERVICE NO
                raw_inet = str(row_g.get('FORMAT IBOOSTER', '')).strip().rstrip(';')
                if raw_inet.endswith('.0'):
                    raw_inet = raw_inet[:-2]
                if not raw_inet or raw_inet.lower() == 'nan':
                    raw_inet = str(row_g.get('SERVICE NO', '')).strip().rstrip(';')
                    if raw_inet.endswith('.0'):
                        raw_inet = raw_inet[:-2]
                inet_digits = ''.join(ch for ch in raw_inet if ch.isdigit())
                no_inet_disp = inet_digits if len(inet_digits) >= 6 else (raw_inet if raw_inet and raw_inet.lower() != 'nan' else '-')

                # Cek hasil ukur dari kolom sheet (jika ada VLOOKUP) atau dari ibooster_asr_map
                onu_val = str(row_g.get(onu_col_existing, '')).strip().upper() if onu_col_existing else ''
                rx_val = str(row_g.get(hasil_col_existing, '')).strip() if hasil_col_existing else ''
                if onu_val in ['NAN', 'NONE', '-', '']:
                    onu_val = ''
                if rx_val.upper() in ['NAN', 'NONE', '-', '']:
                    rx_val = ''

                if (not onu_val or not rx_val) and inet_digits in ibooster_asr_map:
                    map_onu, map_rx = ibooster_asr_map[inet_digits]
                    if not onu_val:
                        onu_val = map_onu
                    if not rx_val:
                        rx_val = map_rx

                # Normalisasi LOS & Rx dBm
                if onu_val == 'LOS' or rx_val.upper() == 'LOS':
                    onu_status_final = 'LOS'
                    hasil_ukur_final = 'LOS'
                else:
                    onu_status_final = onu_val if onu_val else '-'
                    hasil_ukur_final = rx_val if rx_val else '-'

                # Hitung Prioritas Unspec (PRIO 1 / PRIO 2)
                prio_val = str(row_g.get(prio_col_existing, '')).strip().upper() if prio_col_existing else ''
                if prio_val in ['NAN', 'NONE', '']:
                    prio_val = ''

                rx_num = None
                if hasil_ukur_final not in ['-', 'LOS', '']:
                    try:
                        rx_num = float(str(hasil_ukur_final).replace(',', '.'))
                    except Exception:
                        rx_num = None

                if not prio_val and rx_num is not None:
                    if rx_num <= -27.0:
                        prio_val = 'PRIO 1'
                    elif rx_num <= -25.0:
                        prio_val = 'PRIO 2'
                    elif rx_num <= -23.0:
                        prio_val = 'PRIO 3'

                # Tentukan apakah masuk kategori GAUL UNSPEC (PRIO 1 / PRIO 2) atau LOS
                is_los_row = (onu_status_final == 'LOS') or (hasil_ukur_final == 'LOS')
                is_unspec_prio = (onu_status_final in ['ONLINE', 'UP', '-']) and ('PRIO 1' in prio_val or 'PRIO 2' in prio_val)

                if not (is_los_row or is_unspec_prio):
                    continue

                if is_los_row:
                    kat_ukur = 'LOS'
                    prio_disp = prio_val if ('PRIO 1' in prio_val or 'PRIO 2' in prio_val) else '-'
                elif 'PRIO 1' in prio_val:
                    kat_ukur = 'PRIO 1'
                    prio_disp = 'PRIO 1'
                    if onu_status_final == '-':
                        onu_status_final = 'ONLINE'
                else:
                    kat_ukur = 'PRIO 2'
                    prio_disp = 'PRIO 2'
                    if onu_status_final == '-':
                        onu_status_final = 'ONLINE'

                # Penentuan Tanggal & Bulan Tiket yang akurat
                month_name_to_num = {
                    'JANUARI': 1, 'FEBRUARI': 2, 'MARET': 3, 'APRIL': 4, 'MEI': 5, 'JUNI': 6,
                    'JULI': 7, 'AGUSTUS': 8, 'SEPTEMBER': 9, 'OKTOBER': 10, 'NOVEMBER': 11, 'DESEMBER': 12,
                    'JANUARY': 1, 'FEBRUARY': 2, 'MARCH': 3, 'MAY': 5, 'JUNE': 6, 'JULY': 7,
                    'AUGUST': 8, 'OCTOBER': 10, 'DECEMBER': 12
                }
                raw_bulan_col = str(row_g.get('BULAN', '')).strip().upper() if 'BULAN' in df_g.columns else ''
                bulan_str = '-'
                month_idx = 0
                tgl_tiket_str = '-'

                # Ambil tanggal raw (utamakan TANGGAL REPORTED berformat YYYY-MM-DD)
                rep_raw = ''
                for c_rep in ['TANGGAL REPORTED', 'REPORTED DATE', 'STATUS DATE']:
                    if c_rep in row_g and pd.notna(row_g[c_rep]):
                        v_r = str(row_g[c_rep]).strip()
                        if v_r and v_r.lower() != 'nan':
                            rep_raw = v_r
                            break

                # 1. Prioritas utama: jika kolom BULAN di Sheet sudah terisi nama bulan valid (misal "November")
                if raw_bulan_col in month_name_to_num:
                    month_idx = month_name_to_num[raw_bulan_col]
                    bulan_str = months_id_map[month_idx]
                elif rep_raw:
                    try:
                        if len(rep_raw) >= 10 and rep_raw[4] == '-' and rep_raw[7] == '-':
                            dt_obj = pd.to_datetime(rep_raw[:10], format='%Y-%m-%d')
                        else:
                            dt_obj = pd.to_datetime(rep_raw, format='mixed')
                        month_idx = dt_obj.month
                        bulan_str = months_id_map.get(month_idx, '-')
                    except Exception:
                        pass

                if rep_raw:
                    try:
                        if len(rep_raw) >= 10 and rep_raw[4] == '-' and rep_raw[7] == '-':
                            tgl_tiket_str = rep_raw[:10]
                        else:
                            tgl_tiket_str = str(rep_raw).split('.')[0]
                    except Exception:
                        tgl_tiket_str = str(rep_raw).split('.')[0]

                if not bulan_str or bulan_str.lower() == 'nan':
                    bulan_str = '-'

                # Nama Teknisi (Kolom CP di Sheet Gabungan)
                nama_tek = ''
                for c_cand in ['NAMA TEKNISI', 'CP (NAMA TEKNISI)', 'CP', 'TECHNICIAN', 'NAMA_TEKNISI']:
                    if c_cand in row_g and pd.notna(row_g[c_cand]):
                        val = str(row_g[c_cand]).strip()
                        if val and val.lower() not in ['nan', 'none', '-']:
                            nama_tek = val
                            break
                if not nama_tek and len(row_g) > 93:
                    try:
                        val_cp = str(row_g.iloc[93]).strip()
                        if val_cp and val_cp.lower() not in ['nan', 'none', '-']:
                            nama_tek = val_cp
                    except Exception:
                        pass
                if not nama_tek:
                    nama_tek = '-'
                if nama_tek.endswith('.0') and nama_tek[:-2].isdigit():
                    nama_tek = nama_tek[:-2]

                # Konversi NIK atau Nama Lengkap menjadi NAMA ALIAS
                nama_tek_clean = nama_tek.strip().upper()
                if nama_tek_clean in teknisi_alias_map:
                    nama_tek = teknisi_alias_map[nama_tek_clean]
                else:
                    nik_digits = ''.join(ch for ch in nama_tek_clean if ch.isdigit())
                    if nik_digits in teknisi_alias_map:
                        nama_tek = teknisi_alias_map[nik_digits]

                # Customer Type
                cust_type_raw = str(row_g.get('CUSTOMER TYPE', '-')).strip().upper().replace('_', ' ')
                if not cust_type_raw or cust_type_raw == 'NAN':
                    cust_type_raw = 'REGULER'

                # Incident
                inc_val = str(row_g.get('INCIDENT', '-')).strip()
                if not inc_val or inc_val.lower() == 'nan':
                    inc_val = '-'

                # Workzone & Customer Name
                wz_val = str(row_g.get('WORKZONE', '-')).strip()
                if not wz_val or wz_val.lower() == 'nan':
                    wz_val = '-'

                # Durasi Pelaporan Tiket
                dur_int = int(row_g.get('Durasi_Num', 0))
                dur_raw_txt = str(row_g.get('DURASI PELAPORAN TIKET', '')).strip().upper()
                if not dur_raw_txt or dur_raw_txt == 'NAN':
                    dur_raw_txt = f"{dur_int} HARI"

                gaul_records.append({
                    'NO': 0,
                    'BULAN TIKET': bulan_str,
                    'TGL TIKET': tgl_tiket_str,
                    'NAMA TEKNISI': nama_tek,
                    'CUSTOMER TYPE': cust_type_raw,
                    'WORKZONE': wz_val,
                    'INCIDENT': inc_val,
                    'NO INET': no_inet_disp,
                    'HASIL UKUR': hasil_ukur_final,
                    'ONU LINK STATUS': onu_status_final,
                    'PRIORITAS': prio_disp,
                    'KATEGORI UKUR': kat_ukur,
                    'DURASI': dur_raw_txt,
                    'DURASI PELAPORAN TIKET': dur_raw_txt,
                    'Durasi_Num': dur_int,
                    'Month_Index': month_idx
                })

            # --- TABEL MONITORING IBOOSTER ASGAR (SERUPA MONITORING FFG) ---
            st.markdown(f'''
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                <h3 style="color: #cbd5e1; font-weight: bold; margin: 0; font-size: 1.35rem; letter-spacing: 0.5px;">MONITORING IBOOSTER ASGAR (30 HARI)</h3>
                <div style="background-color: rgba(249, 115, 22, 0.15); border: 1px solid #ea580c; border-radius: 6px; padding: 4px 12px; color: #fb923c; font-size: 0.95rem; font-weight: 600; display: inline-flex; align-items: center; gap: 6px;">
                    ⏱️ Last Ibooster ASR: {ibooster_asr_sync_time}
                </div>
            </div>
            ''', unsafe_allow_html=True)

            total_gaul = len(gaul_records)

            if total_gaul == 0:
                st.info("Belum ada tiket Assurance berstatus CLOSE (durasi <= 30 hari) yang terindikasi UNSPEC (PRIO 1 / PRIO 2) atau LOS. Silakan klik tombol **'🚀 Tarik IBOOSTER ASGAR'** di sidebar untuk memperbarui hasil ukur.")

            if total_gaul > 0:
                df_disp_g = pd.DataFrame(gaul_records)

                def _status_rank_g(val):
                    v = str(val).upper()
                    if 'LOS' in v:
                        return 1
                    if 'ONLINE' in v:
                        return 2
                    return 3

                df_disp_g['Status_Rank'] = df_disp_g['ONU LINK STATUS'].apply(_status_rank_g)
                df_disp_g = df_disp_g.sort_values(by=['Durasi_Num', 'Status_Rank', 'PRIORITAS'], ascending=[True, True, True])

                df_disp_g['DURASI'] = df_disp_g['DURASI PELAPORAN TIKET']
                df_disp_g['NO'] = range(1, len(df_disp_g) + 1)

                table_cols_g = [
                    'NO', 'BULAN TIKET', 'NAMA TEKNISI', 'CUSTOMER TYPE',
                    'INCIDENT', 'NO INET', 'HASIL UKUR', 'ONU LINK STATUS',
                    'PRIORITAS', 'DURASI'
                ]
                df_disp_g = df_disp_g[table_cols_g].copy()
                df_disp_g['NO'] = range(1, len(df_disp_g) + 1)

                html_table_g = '<div style="width: 100%; min-height: 400px; overflow-x: auto; background-color: #0f172a; border-radius: 8px; border: 1px solid #334155;">'
                html_table_g += '<table style="width: 100%; border-collapse: collapse; color: white; font-size: 13px; font-family: sans-serif; text-align: center;">'
                html_table_g += '<thead><tr style="background: linear-gradient(180deg, #facc15 0%, #eab308 100%); color: #0f172a; font-weight: bold; border-bottom: 2.5px solid #a16207; font-size: 13.5px;">'

                for i, col in enumerate(df_disp_g.columns):
                    if col == 'NO':
                        html_table_g += (
                            '<th style="padding: 12px 6px; border: 1px solid #ca8a04; vertical-align: middle; '
                            'text-align: center; white-space: nowrap; width: 55px; background: linear-gradient(180deg, #facc15 0%, #eab308 100%);">'
                            '<span style="font-weight: 900; color: #0f172a; font-size: 13.5px; letter-spacing: 0.6px; text-transform: uppercase; '
                            'text-shadow: 0 1px 1px rgba(255, 255, 255, 0.7), 0 -1px 1px rgba(161, 98, 7, 0.4), 1px 0 1px rgba(202, 138, 4, 0.4), -1px 0 1px rgba(254, 240, 138, 0.6), 1px 1px 2px rgba(0, 0, 0, 0.25);">'
                            'NO</span></th>'
                        )
                        continue

                    unique_vals = sorted(df_disp_g[col].astype(str).unique())
                    checkboxes_html = ""
                    for val in unique_vals:
                        clean_val = regex.sub('<[^<]+>', '', val)
                        checkboxes_html += (
                            f'<label style="display: flex; align-items: center; gap: 8px; cursor: pointer; color: #cbd5e1; font-size: 12px; padding: 2px 0;">'
                            f'<input type="checkbox" class="gaul-filter-cb-{i}" value="{clean_val}" checked style="cursor: pointer; accent-color: #3b82f6; width: 14px; height: 14px;">'
                            f'<span class="gaul-filter-text-{i}">{clean_val}</span></label>'
                        )

                    html_table_g += (
                        f'<th style="padding: 12px 10px; border: 1px solid #ca8a04; vertical-align: middle; '
                        f'text-align: center; white-space: nowrap; position: relative; background: linear-gradient(180deg, #facc15 0%, #eab308 100%);">'
                        f'<div style="display: flex; justify-content: center; align-items: center; gap: 5px;">'
                        f'<span style="font-weight: 900; color: #0f172a; font-size: 13.5px; letter-spacing: 0.6px; text-transform: uppercase; '
                        f'text-shadow: 0 1px 1px rgba(255, 255, 255, 0.7), 0 -1px 1px rgba(161, 98, 7, 0.4), 1px 0 1px rgba(202, 138, 4, 0.4), -1px 0 1px rgba(254, 240, 138, 0.6), 1px 1px 2px rgba(0, 0, 0, 0.25);">{col}</span>'
                        f'<div class="gaul-filter-icon" data-colindex="{i}" title="Filter {col}" style="cursor: pointer; color: #713f12; font-size: 11px; padding: 2px 4px; border-radius: 4px; font-weight: bold;">&#9660;</div>'
                        f'</div>'
                        f'<div class="gaul-filter-menu" id="gaul-filter-menu-{i}" style="display: none; position: absolute; top: 100%; right: 50%; transform: translateX(50%); background-color: #1e293b; border: 1px solid #475569; border-radius: 8px; padding: 12px; z-index: 100; text-align: left; min-width: 220px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5); font-weight: normal;">'
                        f'<input type="text" class="gaul-filter-search" data-colindex="{i}" placeholder="Cari..." style="width: 100%; padding: 6px 10px; margin-bottom: 12px; background-color: #0f172a; color: white; border: 1px solid #334155; border-radius: 4px; box-sizing: border-box; font-size: 12px; outline: none;">'
                        f'<div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.7rem; color: #38bdf8; font-weight: bold; border-bottom: 1px solid #334155; padding-bottom: 8px;"><span class="gaul-filter-select-all" data-colindex="{i}" style="cursor: pointer;">Pilih Semua</span><span class="gaul-filter-clear-all" data-colindex="{i}" style="cursor: pointer;">Bersihkan</span></div>'
                        f'<div class="gaul-filter-options-container" style="max-height: 200px; overflow-y: auto; display: flex; flex-direction: column; gap: 4px; margin-bottom: 12px; padding-right: 5px;">{checkboxes_html}</div>'
                        f'<div style="text-align: right; border-top: 1px solid #334155; padding-top: 12px;"><button class="gaul-filter-apply-btn" style="background-color: #3b82f6; color: white; border: none; border-radius: 4px; padding: 6px 16px; font-size: 12px; font-weight: bold; cursor: pointer; width: 100%;">Terapkan</button></div>'
                        f'</div></th>'
                    )

                html_table_g += '</tr></thead><tbody id="gaul-tbody">'

                for _, row_d in df_disp_g.iterrows():
                    html_table_g += '<tr style="border-bottom: 1px solid #334155; font-size: 13px;">'
                    html_table_g += f'<td style="padding: 10px 6px; border-right: 1px solid #334155; text-align: center; color: #94a3b8; font-weight: 600; width: 55px;">{row_d["NO"]}</td>'
                    html_table_g += f'<td style="padding: 10px; border-right: 1px solid #334155;">{row_d["BULAN TIKET"]}</td>'
                    html_table_g += f'<td style="padding: 10px; border-right: 1px solid #334155; text-align: center;">{row_d["NAMA TEKNISI"]}</td>'

                    ct_val = str(row_d["CUSTOMER TYPE"]).strip().upper()
                    if "DIAMOND" in ct_val:
                        ct_bg = "background-color: #0c4a6e; color: #38bdf8; border-radius: 12px; padding: 4px 10px; text-align: center; display: inline-block; font-weight: bold; border: 1px solid #0284c7; font-size: 11px; letter-spacing: 0.5px;"
                    elif "PLATINUM" in ct_val:
                        ct_bg = "background-color: #3b0764; color: #e9d5ff; border-radius: 12px; padding: 4px 10px; text-align: center; display: inline-block; font-weight: bold; border: 1px solid #9333ea; font-size: 11px; letter-spacing: 0.5px;"
                    elif "GOLD" in ct_val:
                        ct_bg = "background-color: #713f12; color: #fde047; border-radius: 12px; padding: 4px 10px; text-align: center; display: inline-block; font-weight: bold; border: 1px solid #ca8a04; font-size: 11px; letter-spacing: 0.5px;"
                    else:
                        ct_bg = "background-color: #14532d; color: #86efac; border-radius: 12px; padding: 4px 10px; text-align: center; display: inline-block; font-weight: bold; border: 1px solid #16a34a; font-size: 11px; letter-spacing: 0.5px;"

                    html_table_g += f'<td style="padding: 10px; border-right: 1px solid #334155;"><span style="{ct_bg}">{row_d["CUSTOMER TYPE"]}</span></td>'
                    html_table_g += f'<td style="padding: 10px; border-right: 1px solid #334155; font-weight: bold; color: #38bdf8;">{row_d["INCIDENT"]}</td>'
                    html_table_g += f'<td style="padding: 10px; border-right: 1px solid #334155;">{row_d["NO INET"]}</td>'

                    ukur_c = str(row_d["HASIL UKUR"])
                    if ukur_c != "-":
                        ukur_c = f'<span style="background-color: #b91c1c; color: #ffffff; padding: 3px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #ef4444; font-size: 12.5px; display: inline-block;">{ukur_c}</span>'
                    html_table_g += f'<td style="padding: 10px; border-right: 1px solid #334155; text-align: center;">{ukur_c}</td>'

                    onu_raw = str(row_d["ONU LINK STATUS"]).strip().upper()
                    if onu_raw in ["ONLINE", "UP"]:
                        onu_c = '<span style="background-color: rgba(34, 197, 94, 0.15); color: #4ade80; padding: 3px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #22c55e; font-size: 12.5px; display: inline-block;">ONLINE</span>'
                    elif onu_raw == "LOS":
                        onu_c = '<span style="background-color: #b91c1c; color: #ffffff; padding: 3px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #ef4444; font-size: 12.5px; display: inline-block;">LOS</span>'
                    elif "DYING" in onu_raw:
                        onu_c = f'<span style="background-color: #ea580c; color: #ffffff; padding: 3px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #f97316; font-size: 12.5px; display: inline-block;">{row_d["ONU LINK STATUS"]}</span>'
                    elif onu_raw != "-":
                        onu_c = f'<span style="background-color: #475569; color: #f1f5f9; padding: 3px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #64748b; font-size: 12.5px; display: inline-block;">{row_d["ONU LINK STATUS"]}</span>'
                    else:
                        onu_c = '-'

                    html_table_g += f'<td style="padding: 10px; border-right: 1px solid #334155; text-align: center;">{onu_c}</td>'
                    html_table_g += f'<td style="padding: 10px; border-right: 1px solid #334155; font-weight: bold;">{row_d["PRIORITAS"]}</td>'
                    html_table_g += f'<td style="padding: 10px; font-weight: bold; color: #fbbf24;">{row_d["DURASI"]}</td>'
                    html_table_g += '</tr>'

                html_table_g += '</tbody></table></div>'
                st.markdown(html_table_g, unsafe_allow_html=True)

                js_gaul_filter = '''<script>
                const parentDoc = window.parent.document;
                function setupGaulFilters() {
                    const icons = parentDoc.querySelectorAll('.gaul-filter-icon');
                    if (icons.length === 0) return;

                    icons.forEach(icon => {
                        if (icon.dataset.listener) return;
                        icon.addEventListener('click', function(e) {
                            e.stopPropagation();
                            const colIdx = this.getAttribute('data-colindex');
                            const menu = parentDoc.getElementById('gaul-filter-menu-' + colIdx);
                            const isHidden = menu.style.display === 'none';
                            parentDoc.querySelectorAll('.gaul-filter-menu').forEach(m => m.style.display = 'none');
                            if (isHidden) {
                                menu.style.display = 'block';
                            }
                        });
                        icon.dataset.listener = 'true';
                    });

                    if (!parentDoc.body.dataset.gaulFilterClick) {
                        parentDoc.body.addEventListener('click', function(e) {
                            if (!e.target.closest('.gaul-filter-menu') && !e.target.closest('.gaul-filter-icon')) {
                                parentDoc.querySelectorAll('.gaul-filter-menu').forEach(m => m.style.display = 'none');
                            }
                        });
                        parentDoc.body.dataset.gaulFilterClick = 'true';
                    }

                    parentDoc.querySelectorAll('.gaul-filter-search').forEach(input => {
                        if (input.dataset.listener) return;
                        input.addEventListener('keyup', function() {
                            const term = this.value.toLowerCase();
                            const colIdx = this.getAttribute('data-colindex');
                            parentDoc.querySelectorAll('.gaul-filter-text-' + colIdx).forEach(label => {
                                const text = label.textContent.toLowerCase();
                                label.parentElement.style.display = text.includes(term) ? 'flex' : 'none';
                            });
                        });
                        input.dataset.listener = 'true';
                    });

                    parentDoc.querySelectorAll('.gaul-filter-select-all').forEach(btn => {
                        if (btn.dataset.listener) return;
                        btn.addEventListener('click', function() {
                            const colIdx = this.getAttribute('data-colindex');
                            parentDoc.querySelectorAll('.gaul-filter-cb-' + colIdx).forEach(cb => {
                                if (cb.parentElement.style.display !== 'none') cb.checked = true;
                            });
                        });
                        btn.dataset.listener = 'true';
                    });

                    parentDoc.querySelectorAll('.gaul-filter-clear-all').forEach(btn => {
                        if (btn.dataset.listener) return;
                        btn.addEventListener('click', function() {
                            const colIdx = this.getAttribute('data-colindex');
                            parentDoc.querySelectorAll('.gaul-filter-cb-' + colIdx).forEach(cb => {
                                if (cb.parentElement.style.display !== 'none') cb.checked = false;
                            });
                        });
                        btn.dataset.listener = 'true';
                    });

                    parentDoc.querySelectorAll('.gaul-filter-apply-btn').forEach(btn => {
                        if (btn.dataset.listener) return;
                        btn.addEventListener('click', function() {
                            parentDoc.querySelectorAll('.gaul-filter-menu').forEach(m => m.style.display = 'none');
                            applyGaulFilters();
                        });
                        btn.dataset.listener = 'true';
                    });
                }

                function applyGaulFilters() {
                    const tbody = parentDoc.getElementById('gaul-tbody');
                    if (!tbody) return;
                    const trs = tbody.getElementsByTagName('tr');

                    let filters = {};
                    parentDoc.querySelectorAll('.gaul-filter-menu').forEach(menu => {
                        const colIdx = menu.id.replace('gaul-filter-menu-', '');
                        const checkboxes = menu.querySelectorAll('.gaul-filter-cb-' + colIdx + ':checked');
                        filters[colIdx] = Array.from(checkboxes).map(cb => cb.value.toLowerCase().trim());
                    });

                    let visibleCount = 1;
                    for (let i = 0; i < trs.length; i++) {
                        let tr = trs[i];
                        let show = true;

                        for (let colIdx in filters) {
                            const allowedVals = filters[colIdx];
                            if (allowedVals.length === 0) {
                                show = false;
                                break;
                            }
                            const totalCbs = parentDoc.querySelectorAll('.gaul-filter-cb-' + colIdx).length;
                            if (allowedVals.length === totalCbs) continue;

                            let td = tr.getElementsByTagName('td')[colIdx];
                            if (td) {
                                let cellText = (td.textContent || td.innerText).toLowerCase().trim();
                                if (!allowedVals.includes(cellText)) {
                                    show = false;
                                    break;
                                }
                            }
                        }
                        tr.style.display = show ? "" : "none";
                        if (show) {
                            let td0 = tr.getElementsByTagName('td')[0];
                            if (td0) td0.innerHTML = visibleCount;
                            visibleCount++;
                        }
                    }
                }

                let gaulFilterInterval = setInterval(() => {
                    if (parentDoc.getElementById('gaul-tbody')) {
                        setupGaulFilters();
                        clearInterval(gaulFilterInterval);
                    }
                }, 500);
                </script>'''
                import streamlit.components.v1 as components
                components.html(js_gaul_filter, height=0, width=0)

    elif menu == "GRAFIK TIKET PERIODE":
        df_asr, asr_source = load_assurance_data(insera_time)
        df_proactive_raw, pro_source = load_proactive_data(insera_time)
        

        
        
        if df_asr.empty:
            st.warning("\u26A0\uFE0F **Data tiket Assurance belum berhasil dimuat.**")
            st.info("💡 **Petunjuk untuk Web Public (Streamlit Cloud):**\nPastikan spreadsheet **'SA ULIN - ANTIGRAVITY ASSURANCE'** sudah dibagikan dengan akses **'Siapa saja yang memiliki link: Pelihat'** agar server publik dapat membaca data secara otomatis. Di localhost, data juga dapat ditarik langsung melalui tombol **'🚀 Tarik INSERA ASR'** di sidebar.")
        else:
            # 1. Deteksi Kolom Tanggal Lapor
            date_col_asr = None
            for col in ['REPORTED DATE', 'REPORTED_DATE', 'TANGGAL TIKET', 'TANGGAL', 'STATUS DATE']:
                if col in df_asr.columns:
                    date_col_asr = col
                    break
                    
            if date_col_asr:
                df_asr['dt_parsed'] = pd.to_datetime(df_asr[date_col_asr], errors='coerce')
                df_asr['date_only'] = df_asr['dt_parsed'].dt.date
                df_asr['Jam'] = df_asr['dt_parsed'].dt.hour.apply(lambda h: f"{int(h):02d}:00" if pd.notna(h) else "00:00")
            else:
                df_asr['date_only'] = None
                df_asr['Jam'] = "00:00"

            # 2. Filter Berdasarkan Rentang Tanggal Sidebar
            if start_date and end_date and date_col_asr:
                df_filtered = df_asr[(df_asr['date_only'] >= start_date) & (df_asr['date_only'] <= end_date)].copy()
            else:
                df_filtered = df_asr.copy()

            # Fallback jika tanggal terpilih kosong
            if df_filtered.empty:
                avail_dates = df_asr['date_only'].dropna().unique()
                latest_avail = max(avail_dates) if len(avail_dates) > 0 else None
                st.warning(f"⚠️ Belum ada tiket masuk pada rentang tanggal terpilih: **{start_date} s/d {end_date}**.")
                if latest_avail:
                    st.info(f"💡 Data tiket terbaru yang tersedia di sistem adalah tanggal **{latest_avail}**. Anda dapat mengubah filter **'📅 KONTROL WAKTU'** di sidebar ke tanggal tersebut, atau klik tombol di bawah untuk langsung menampilkannya:")
                    if st.button(f"📅 Tampilkan Data Tiket Tanggal {latest_avail}", key="btn_show_latest_asr"):
                        st.session_state['force_asr_date'] = latest_avail
                        st.rerun()
                if 'force_asr_date' in st.session_state and st.session_state['force_asr_date']:
                    df_filtered = df_asr[df_asr['date_only'] == st.session_state['force_asr_date']].copy()

            if not df_filtered.empty:
                # 3. Deteksi Kolom STATUS TIKET & Normalisasi OPEN / CLOSE
                status_col_asr = None
                for c in ['STATUS TIKET', 'STATUS_TIKET', 'STATUS', 'TICKET STATUS', 'STATUS WO']:
                    if c in df_filtered.columns:
                        status_col_asr = c
                        break
                if status_col_asr:
                    is_closed = df_filtered[status_col_asr].astype(str).str.upper().str.contains('CLOSE', na=False)
                    df_filtered['Status_Kategori'] = np.where(is_closed, 'TIKET CLOSE', 'TIKET OPEN')
                else:
                    df_filtered['Status_Kategori'] = 'TIKET CLOSE'

                # 4. Deteksi Kolom CUSTOMER TYPE (REGULER, HVC_GOLD, HVC_DIAMOND, HVC_PLATINUM)
                cust_col_asr = None
                for c in ['CUSTOMER TYPE', 'CUSTOMER_TYPE', 'TIPE CUSTOMER', 'TIPE PELANGGAN']:
                    if c in df_filtered.columns:
                        cust_col_asr = c
                        break
                if cust_col_asr:
                    df_filtered['Cust_Clean'] = df_filtered[cust_col_asr].astype(str).str.upper().str.strip()
                else:
                    df_filtered['Cust_Clean'] = 'REGULER'

                # 5. Agregasi Jam 24 Jam (00:00 s/d 23:00)
                all_hours = pd.DataFrame({'Jam': [f"{i:02d}:00" for i in range(24)]})
                
                cust_targets = ['REGULER', 'HVC_GOLD', 'HVC_DIAMOND', 'HVC_PLATINUM']
                cust_frames = []
                for ct in cust_targets:
                    sub = df_filtered[df_filtered['Cust_Clean'] == ct]
                    cnt = pd.merge(all_hours, sub.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                    cnt['Kategori'] = ct
                    cust_frames.append(cnt)
                
                status_targets = ['TIKET OPEN', 'TIKET CLOSE']
                status_frames = []
                for st_name in status_targets:
                    sub = df_filtered[df_filtered['Status_Kategori'] == st_name]
                    cnt = pd.merge(all_hours, sub.groupby('Jam').size().reset_index(name='Jumlah'), on='Jam', how='left').fillna(0)
                    cnt['Kategori'] = st_name
                    status_frames.append(cnt)
                    
                chart_df_asr = pd.concat(cust_frames + status_frames, ignore_index=True)
                chart_df_asr['Text'] = chart_df_asr['Jumlah'].apply(lambda x: str(int(x)) if x > 0 else '')

                # 6. Kontrol View Layer Grafik
                main_chart_container = st.container()
                with main_chart_container:
                    st.markdown("<div class='custom-border-target'></div>", unsafe_allow_html=True)
                    st.markdown('<div class="section-title-wrap"><div class="section-title">📈 DISTRIBUSI JAM MASUK TIKET & STATUS PERIODE</div></div>', unsafe_allow_html=True)
                    
                    view_mode = st.radio(
                        "Layer Tampilan Grafik:",
                        options=["🌐 Tampilkan Semua (Customer Type & Status)", "👑 Khusus Customer Type (REGULER, GOLD, DIAMOND, PLATINUM)", "⚡ Khusus Status (OPEN vs CLOSE)"],
                        horizontal=True,
                        label_visibility="collapsed",
                        key="asr_layer_radio"
                    )

                if "Khusus Customer Type" in view_mode:
                    display_chart_df = chart_df_asr[chart_df_asr['Kategori'].isin(cust_targets)]
                elif "Khusus Status" in view_mode:
                    display_chart_df = chart_df_asr[chart_df_asr['Kategori'].isin(status_targets)]
                else:
                    display_chart_df = chart_df_asr

                ch_col1, ch_col2 = main_chart_container.columns([3, 1])

                with ch_col1:
                    fig_asr = px.line(
                        display_chart_df, x='Jam', y='Jumlah', color='Kategori', text='Text', markers=True,
                        color_discrete_map={
                            'HVC_GOLD': '#eab308',
                            'HVC_PLATINUM': '#a855f7',
                            'HVC_DIAMOND': '#06b6d4',
                            'REGULER': '#3b82f6',
                            'TIKET OPEN': '#ef4444',
                            'TIKET CLOSE': '#10b981'
                        }
                    )
                    fig_asr.update_traces(line=dict(width=3, shape='spline'), fill='tozeroy', marker=dict(size=7), textposition='top center', textfont=dict(color='#ffffff'))
                    
                    fill_colors_asr = {
                        'HVC_GOLD': 'rgba(234, 179, 8, 0.12)',
                        'HVC_PLATINUM': 'rgba(168, 85, 247, 0.12)',
                        'HVC_DIAMOND': 'rgba(6, 182, 212, 0.12)',
                        'REGULER': 'rgba(59, 130, 246, 0.12)',
                        'TIKET OPEN': 'rgba(239, 68, 68, 0.12)',
                        'TIKET CLOSE': 'rgba(16, 185, 129, 0.12)'
                    }
                    for trace in fig_asr.data:
                        raw_name = trace.name
                        if raw_name in fill_colors_asr:
                            trace.fillcolor = fill_colors_asr[raw_name]
                        trace.name = f'<b><span style="color:white; text-shadow:2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8);">{raw_name}</span></b>'
                        
                    fig_asr.add_vrect(x0="00:00", x1="07:00", fillcolor="rgba(160, 160, 160, 0.20)", layer="below", line_width=0)
                    fig_asr.add_vrect(x0="17:00", x1="23:00", fillcolor="rgba(160, 160, 160, 0.20)", layer="below", line_width=0)
                    
                    max_y_val = display_chart_df['Jumlah'].max() if not display_chart_df.empty else 5
                    fig_asr.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
                        font=dict(color='#cbd5e1'), xaxis_title="Waktu (Jam)", yaxis_title="Jumlah Tiket", 
                        margin=dict(t=10, b=40, l=50, r=10),
                        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title=""),
                        hovermode="x unified",
                        hoverlabel=dict(bgcolor='#1e293b', font=dict(color='#ffffff')),
                        xaxis=dict(fixedrange=True, dtick=2, range=[-0.5, 23.5], showgrid=True, gridwidth=1, gridcolor='#334155'),
                        yaxis=dict(fixedrange=True, showgrid=True, gridwidth=1, gridcolor='#334155', range=[0, max_y_val * 1.25 if max_y_val > 0 else 5])
                    )
                    fig_asr.update_xaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_asr.update_yaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_asr.update_traces(cliponaxis=False)
                    st.plotly_chart(fig_asr, use_container_width=True, config={'displayModeBar': False}, theme=None)

                # 7. Summary Card Sisi Kanan (Struktur Identik DETAIL RE PERIODE)
                with ch_col2:
                    tot_all_tkt = len(df_filtered)
                    tot_close = len(df_filtered[df_filtered['Status_Kategori'] == 'TIKET CLOSE'])
                    tot_open = len(df_filtered[df_filtered['Status_Kategori'] == 'TIKET OPEN'])
                    pct_close_val = (tot_close / tot_all_tkt * 100) if tot_all_tkt > 0 else 0
                    pct_close_color = "#10b981" if pct_close_val >= 80.0 else "#f59e0b"
                    
                    cnt_gold = len(df_filtered[df_filtered['Cust_Clean'] == 'HVC_GOLD'])
                    cnt_plat = len(df_filtered[df_filtered['Cust_Clean'] == 'HVC_PLATINUM'])
                    cnt_diam = len(df_filtered[df_filtered['Cust_Clean'] == 'HVC_DIAMOND'])
                    cnt_reg = len(df_filtered[df_filtered['Cust_Clean'] == 'REGULER'])
                    
                    pct_gold = f"{(cnt_gold/tot_all_tkt)*100:.1f}".rstrip('0').rstrip('.') if tot_all_tkt > 0 else "0"
                    pct_plat = f"{(cnt_plat/tot_all_tkt)*100:.1f}".rstrip('0').rstrip('.') if tot_all_tkt > 0 else "0"
                    pct_diam = f"{(cnt_diam/tot_all_tkt)*100:.1f}".rstrip('0').rstrip('.') if tot_all_tkt > 0 else "0"
                    pct_reg = f"{(cnt_reg/tot_all_tkt)*100:.1f}".rstrip('0').rstrip('.') if tot_all_tkt > 0 else "0"
                    
                    html_summary_asr = f'''
                    <div style="border: 1px solid #334155; border-radius: 8px; padding: 20px; text-align: center; background-color: #0f172a; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
                        <div style="font-size: 0.9rem; font-weight: bold; color: #cbd5e1; margin-bottom: 20px;">GRAND TOTAL TIKET ASSURANCE</div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px 10px; margin-bottom: 20px;">
                            <div><div style="font-size: 2.0rem; font-weight: bold; color: #38bdf8; line-height: 1;">{tot_all_tkt}</div><div style="font-size: 12px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">Total Tiket</div></div>
                            <div><div style="font-size: 2.0rem; font-weight: bold; color: #10b981; line-height: 1;">{tot_close}</div><div style="font-size: 12px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">Tiket Close</div></div>
                            <div><div style="font-size: 2.0rem; font-weight: bold; color: #ef4444; line-height: 1;">{tot_open}</div><div style="font-size: 12px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">Tiket Open</div></div>
                            <div><div style="font-size: 2.0rem; font-weight: bold; color: {pct_close_color}; line-height: 1;">{pct_close_val:.1f}%</div><div style="font-size: 12px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">% Selesai</div></div>
                        </div>
                        <div style="border-top: 1px dashed #334155; padding-top: 15px; margin-top: auto; font-size: 0.92rem; font-weight: bold; color: #94a3b8; text-align: left;">
                            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                                <span style="display:flex; align-items:center; gap:6px;"><span style="width:8px; height:8px; border-radius:50%; background:#eab308;"></span>HVC_GOLD</span>
                                <span style="color:white;">{cnt_gold} ({pct_gold}%)</span>
                            </div>
                            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                                <span style="display:flex; align-items:center; gap:6px;"><span style="width:8px; height:8px; border-radius:50%; background:#a855f7;"></span>HVC_PLATINUM</span>
                                <span style="color:white;">{cnt_plat} ({pct_plat}%)</span>
                            </div>
                            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                                <span style="display:flex; align-items:center; gap:6px;"><span style="width:8px; height:8px; border-radius:50%; background:#06b6d4;"></span>HVC_DIAMOND</span>
                                <span style="color:white;">{cnt_diam} ({pct_diam}%)</span>
                            </div>
                            <div style="display:flex; justify-content:space-between;">
                                <span style="display:flex; align-items:center; gap:6px;"><span style="width:8px; height:8px; border-radius:50%; background:#3b82f6;"></span>REGULER</span>
                                <span style="color:white;">{cnt_reg} ({pct_reg}%)</span>
                            </div>
                        </div>
                    </div>
                    '''
                    st.markdown(html_summary_asr, unsafe_allow_html=True)

                # 8. Mini-Charts (Small Multiples Grid 6 Kolom)
                st.markdown("<br>", unsafe_allow_html=True)
                mini_cols_asr = st.columns(6)
                
                mini_categories_asr = [
                    ('REGULER', '#3b82f6', 'rgba(59, 130, 246, 0.15)'),
                    ('HVC_GOLD', '#eab308', 'rgba(234, 179, 8, 0.15)'),
                    ('HVC_DIAMOND', '#06b6d4', 'rgba(6, 182, 212, 0.15)'),
                    ('HVC_PLATINUM', '#a855f7', 'rgba(168, 85, 247, 0.15)'),
                    ('TIKET OPEN', '#ef4444', 'rgba(239, 68, 68, 0.15)'),
                    ('TIKET CLOSE', '#10b981', 'rgba(16, 185, 129, 0.15)')
                ]
                
                for i, (cat, color, fill_color) in enumerate(mini_categories_asr):
                    df_cat = chart_df_asr[chart_df_asr['Kategori'] == cat]
                    max_y_mini = df_cat['Jumlah'].max() if not df_cat.empty else 5
                    
                    fig_mini_asr = px.line(df_cat, x='Jam', y='Jumlah', text='Text', markers=True)
                    fig_mini_asr.update_traces(
                        line=dict(width=2, color=color, shape='spline'),
                        fill='tozeroy', fillcolor=fill_color,
                        marker=dict(size=4, color=color), textposition='top center',
                        textfont=dict(color='#ffffff'), cliponaxis=False
                    )
                    fig_mini_asr.update_layout(
                        title=dict(text=cat, font=dict(color=color, size=12), x=0.5, xanchor='center'),
                        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='#0f172a',
                        margin=dict(t=40, b=45, l=45, r=10),
                        xaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, dtick=8, title="Waktu (Jam)"),
                        yaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, showticklabels=True, title="Tiket", range=[0, max_y_mini * 1.3 if max_y_mini > 0 else 1]),
                        hovermode="x unified",
                        hoverlabel=dict(bgcolor='#1e293b', font=dict(color='#ffffff')),
                        height=260
                    )
                    fig_mini_asr.update_xaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_mini_asr.update_yaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    
                    with mini_cols_asr[i]:
                        fig_mini_asr.update_traces(cliponaxis=False)
                        st.plotly_chart(fig_mini_asr, use_container_width=True, config={'displayModeBar': False}, theme=None)

                # 9. Analisa Peak Hours & Insight Box
                def get_asr_stats(df_data):
                    if df_data.empty: return 0, "-"
                    hours = pd.to_numeric(df_data['Jam'].astype(str).str[:2], errors='coerce').dropna().astype(int)
                    if hours.empty: return 0, "-"
                    total = len(hours)
                    val_counts = hours.value_counts()
                    peak_h = val_counts.idxmax()
                    peak_val = val_counts.max()
                    puncak = f"{peak_h:02d}:00 &rarr; {peak_val} Tiket"
                    return total, puncak
                    
                tot_rep, peak_rep = get_asr_stats(df_filtered)
                tot_cls, peak_cls = get_asr_stats(df_filtered[df_filtered['Status_Kategori'] == 'TIKET CLOSE'])
                
                top_cust = df_filtered['Cust_Clean'].value_counts()
                top_cust_name = top_cust.index[0] if len(top_cust) > 0 else "-"
                top_cust_cnt = top_cust.iloc[0] if len(top_cust) > 0 else 0
                top_cust_pct = f"{(top_cust_cnt / tot_all_tkt * 100):.1f}%" if tot_all_tkt > 0 else "0%"
                
                st.markdown(f'''
                <div style="background-color: #0f172a; padding: 22px; border-radius: 12px; border: 1px solid #1e293b; margin-top: 20px;">
                    <div style="font-size: 1.2rem; font-weight: 800; color: white; margin-bottom: 15px; display: flex; align-items: center; gap: 8px;">
                        <span>📊</span> ANALISA PEAK &amp; INSIGHT TIKET ASSURANCE
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px;">
                        <div style="background: rgba(56, 189, 248, 0.08); border-top: 3px solid #38bdf8; border-radius: 10px; padding: 14px; border: 1px solid #334155;">
                            <div style="color: #94a3b8; font-size: 0.8rem; font-weight: bold; text-transform: uppercase;">⏰ Jam Puncak Masuk</div>
                            <div style="font-size: 1.25rem; font-weight: bold; color: #38bdf8; margin-top: 6px;">{peak_rep}</div>
                            <div style="color: #cbd5e1; font-size: 0.78rem; margin-top: 4px;">Waktu pelaporan tiket tertinggi</div>
                        </div>
                        <div style="background: rgba(16, 185, 129, 0.08); border-top: 3px solid #10b981; border-radius: 10px; padding: 14px; border: 1px solid #334155;">
                            <div style="color: #94a3b8; font-size: 0.8rem; font-weight: bold; text-transform: uppercase;">✅ Jam Puncak Selesai</div>
                            <div style="font-size: 1.25rem; font-weight: bold; color: #10b981; margin-top: 6px;">{peak_cls}</div>
                            <div style="color: #cbd5e1; font-size: 0.78rem; margin-top: 4px;">Waktu penyelesaian (closing) terbanyak</div>
                        </div>
                        <div style="background: rgba(234, 179, 8, 0.08); border-top: 3px solid #eab308; border-radius: 10px; padding: 14px; border: 1px solid #334155;">
                            <div style="color: #94a3b8; font-size: 0.8rem; font-weight: bold; text-transform: uppercase;">👑 Segmen Pelanggan Terbanyak</div>
                            <div style="font-size: 1.25rem; font-weight: bold; color: #eab308; margin-top: 6px;">{top_cust_name} ({top_cust_cnt})</div>
                            <div style="color: #cbd5e1; font-size: 0.78rem; margin-top: 4px;">Porsi {top_cust_pct} dari seluruh volume</div>
                        </div>
                        <div style="background: rgba(168, 85, 247, 0.08); border-top: 3px solid #a855f7; border-radius: 10px; padding: 14px; border: 1px solid #334155;">
                            <div style="color: #94a3b8; font-size: 0.8rem; font-weight: bold; text-transform: uppercase;">⚡ Rasio Tiket Selesai</div>
                            <div style="font-size: 1.25rem; font-weight: bold; color: #a855f7; margin-top: 6px;">{tot_close} / {tot_all_tkt}</div>
                            <div style="color: #cbd5e1; font-size: 0.78rem; margin-top: 4px;">{pct_close_val:.1f}% tiket telah terselesaikan</div>
                        </div>
                    </div>
                </div>
                ''', unsafe_allow_html=True)

                # 10. Tabel Rincian Lengkap Tiket Periode (Permanent Card & Scrollable)
                st.markdown("<br>", unsafe_allow_html=True)
                
                # CSS khusus untuk tabel berdesain mewah & scrollbar horizontal/vertikal yang halus
                st.markdown('''
                <style>
                .asr-table-wrapper {
                    background-color: #0f172a;
                    padding: 22px;
                    border-radius: 12px;
                    border: 1px solid #1e293b;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.35);
                    margin-top: 15px;
                }
                .asr-scroll-container {
                    width: 100%;
                    overflow-x: auto !important;
                    overflow-y: auto !important;
                    max-height: 820px;
                    border: 1px solid #334155;
                    border-radius: 8px;
                    background-color: #0b1120;
                    margin-top: 12px;
                    scrollbar-width: thin;
                    scrollbar-color: #3b82f6 #0b1120;
                }
                .asr-scroll-container::-webkit-scrollbar {
                    height: 12px;
                    width: 10px;
                }
                .asr-scroll-container::-webkit-scrollbar-track {
                    background: #0b1120;
                    border-radius: 6px;
                }
                .asr-scroll-container::-webkit-scrollbar-thumb {
                    background: #1e40af;
                    border-radius: 6px;
                    border: 2px solid #0b1120;
                }
                .asr-scroll-container::-webkit-scrollbar-thumb:hover {
                    background: #2563eb;
                }
                .asr-table-custom {
                    width: 100%;
                    min-width: 1650px;
                    border-collapse: collapse;
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                    text-align: left;
                    font-size: 0.82rem;
                }
                .asr-table-custom thead th {
                    background: linear-gradient(180deg, #1e3a8a 0%, #172554 100%) !important;
                    position: sticky;
                    top: 0;
                    z-index: 10;
                    padding: 14px 12px;
                    border-bottom: 2px solid #2563eb;
                    color: #ffffff !important;
                    text-shadow: 1px 1px 2px #000, -1px -1px 2px #000, 1px -1px 2px #000, -1px 1px 2px #000, 0 0 4px #000;
                    font-weight: 800;
                    text-align: center !important;
                    text-transform: uppercase;
                    letter-spacing: 0.6px;
                    box-shadow: 0 3px 6px rgba(0,0,0,0.5);
                }
                .asr-table-custom tbody tr:hover {
                    background-color: #1e293b !important;
                }
                </style>
                ''', unsafe_allow_html=True)
                
                st.markdown('<div class="asr-table-wrapper">', unsafe_allow_html=True)
                
                # Header Card
                tbl_head_col1, tbl_head_col2 = st.columns([3, 1])
                with tbl_head_col1:
                    st.markdown('''
                    <div style="font-size: 1.18rem; font-weight: 800; color: white; display:flex; align-items:center; gap:8px;">
                        <span>📋</span> TABEL RINCIAN TIKET ASSURANCE PERIODE
                    </div>
                    <div style="color: #94a3b8; font-size: 0.78rem; margin-top: 4px;">
                        ↔️ <i>Tabel dapat di-scroll ke kanan &amp; kiri untuk membaca Summary lengkap. Header tetap terkunci di atas saat scroll ke bawah.</i>
                    </div>
                    ''', unsafe_allow_html=True)
                
                # Filter Section
                st.markdown("<div style='margin-top: 12px;'></div>", unsafe_allow_html=True)
                tf_c1, tf_c2, tf_c3 = st.columns([2, 2, 3])
                with tf_c1:
                    sel_cust = st.selectbox("Filter Tipe Pelanggan:", ["Semua"] + cust_targets, key="tb_filter_cust")
                with tf_c2:
                    sel_stat = st.selectbox("Filter Status:", ["Semua", "TIKET OPEN", "TIKET CLOSE"], key="tb_filter_stat")
                with tf_c3:
                    search_txt = st.text_input("🔍 Cari Tiket / Pelanggan / Summary:", key="tb_filter_search")
                    
                df_table = df_filtered.copy()
                if sel_cust != "Semua":
                    df_table = df_table[df_table['Cust_Clean'] == sel_cust]
                if sel_stat != "Semua":
                    df_table = df_table[df_table['Status_Kategori'] == sel_stat]
                if search_txt:
                    s_low = search_txt.lower()
                    match_m = (
                        df_table['INCIDENT'].astype(str).str.lower().str.contains(s_low, na=False) |
                        df_table['CUSTOMER NAME'].astype(str).str.lower().str.contains(s_low, na=False) |
                        df_table['SUMMARY'].astype(str).str.lower().str.contains(s_low, na=False)
                    )
                    df_table = df_table[match_m]

                with tbl_head_col2:
                    st.markdown(f'''
                    <div style="text-align: right; margin-top: 5px;">
                        <span style="font-size: 0.8rem; font-weight: 700; color: #38bdf8; background: rgba(56,189,248,0.12); padding: 5px 12px; border-radius: 20px; border: 1px solid #38bdf8; display: inline-block;">
                            {len(df_table):,} Tiket Ditampilkan
                        </span>
                    </div>
                    ''', unsafe_allow_html=True)

                if df_table.empty:
                    st.markdown('''
                    <div style="background: rgba(245,158,11,0.08); border: 1px solid #f59e0b; border-radius: 8px; padding: 18px; text-align: center; color: #fbbf24; margin-top: 15px;">
                        ⚠️ Tidak ada tiket yang sesuai dengan kriteria filter di atas.
                    </div>
                    ''', unsafe_allow_html=True)
                else:
                    status_badges = {
                        'CLOSED': '<span style="background: rgba(16,185,129,0.18); border: 1px solid #10b981; color: #34d399; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">CLOSED</span>',
                        'BACKEND': '<span style="background: rgba(245,158,11,0.18); border: 1px solid #f59e0b; color: #fbbf24; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">BACKEND</span>',
                        'SALAMSIM': '<span style="background: rgba(59,130,246,0.18); border: 1px solid #3b82f6; color: #60a5fa; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">SALAMSIM</span>',
                        'DRAFT': '<span style="background: rgba(148,163,184,0.18); border: 1px solid #64748b; color: #cbd5e1; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">DRAFT</span>'
                    }

                    cust_badges = {
                        'HVC_GOLD': '<span style="background: rgba(234,179,8,0.18); border: 1px solid #eab308; color: #facc15; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">👑 HVC_GOLD</span>',
                        'HVC_PLATINUM': '<span style="background: rgba(168,85,247,0.18); border: 1px solid #a855f7; color: #c084fc; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">💎 HVC_PLATINUM</span>',
                        'HVC_DIAMOND': '<span style="background: rgba(6,182,212,0.18); border: 1px solid #06b6d4; color: #22d3ee; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">✨ HVC_DIAMOND</span>',
                        'REGULER': '<span style="background: rgba(59,130,246,0.18); border: 1px solid #3b82f6; color: #60a5fa; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">👤 REGULER</span>'
                    }

                    import html as html_lib
                    
                    def compute_ttr_badge(ttr_val, cust_type_val, rep_val=None):
                        import math
                        elapsed_sec = None

                        # 1. Coba baca dari kolom TTR jika ada
                        if ttr_val is not None:
                            try:
                                if isinstance(ttr_val, (int, float)):
                                    if not math.isnan(ttr_val):
                                        if 0 < ttr_val < 10:
                                            elapsed_sec = float(ttr_val) * 86400
                                        else:
                                            elapsed_sec = float(ttr_val)
                                else:
                                    s_ttr = str(ttr_val).strip()
                                    if s_ttr and s_ttr.lower() not in ['nan', 'none', '-', '', '<na>', 'nat']:
                                        parts = s_ttr.split(':')
                                        if len(parts) == 3:
                                            elapsed_sec = float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
                                        elif len(parts) == 2:
                                            elapsed_sec = float(parts[0]) * 3600 + float(parts[1]) * 60
                                        else:
                                            val = float(parts[0])
                                            if not math.isnan(val):
                                                elapsed_sec = val * 3600
                            except Exception:
                                elapsed_sec = None

                        # 2. Fallback hitung otomatis dari selisih REPORTED DATE (WIB -> WITA +1 jam) ke saat ini
                        if elapsed_sec is None or math.isnan(elapsed_sec) or elapsed_sec < 0:
                            if rep_val:
                                try:
                                    dt_rep = pd.to_datetime(rep_val, errors='coerce')
                                    if pd.notna(dt_rep):
                                        from datetime import datetime as dt_cls
                                        now_dt = dt_cls.now()
                                        dt_rep_wita = dt_rep + pd.Timedelta(hours=1)
                                        diff = (now_dt - dt_rep_wita.to_pydatetime()).total_seconds()
                                        if diff >= 0:
                                            elapsed_sec = diff
                                except Exception:
                                    pass

                        if elapsed_sec is None or math.isnan(elapsed_sec) or elapsed_sec < 0:
                            elapsed_sec = 0.0

                        elapsed_sec = float(elapsed_sec)
                        c_up = str(cust_type_val).upper()
                        # Target SLA TTR:
                        # - HVC DIAMOND : 3 Jam
                        # - HVC PLATINUM: 6 Jam
                        # - HVC GOLD    : 12 Jam
                        # - REGULER : 24 Jam (dan default lainnya)
                        if 'DIAMOND' in c_up:
                            target_sec = 3 * 3600
                        elif 'PLATINUM' in c_up:
                            target_sec = 6 * 3600
                        elif 'GOLD' in c_up:
                            target_sec = 12 * 3600
                        else:
                            target_sec = 24 * 3600

                        remain_sec = target_sec - elapsed_sec
                        remain_pct = (remain_sec / target_sec) * 100

                        h = int(elapsed_sec // 3600)
                        m = int((elapsed_sec % 3600) // 60)
                        s = int(elapsed_sec % 60)
                        # Menghilangkan detik pada display teks agar seragam (hh:mm), detik tetap ada di tooltip
                        time_str = f"{h:02d}:{m:02d}"
                        time_str_full = f"{h:02d}:{m:02d}:{s:02d}"

                        if remain_pct >= 71.0:
                            # Hijau (100% sampai 71%)
                            bg = "rgba(16, 185, 129, 0.18)"
                            bd = "#10b981"
                            cl = "#34d399"
                            ic = "🟢"
                            lbl = f"({int(round(remain_pct))}%)"
                        elif remain_pct >= 41.0:
                            # Kuning (70% sampai 41%)
                            bg = "rgba(234, 179, 8, 0.18)"
                            bd = "#eab308"
                            cl = "#facc15"
                            ic = "🟡"
                            lbl = f"({int(round(remain_pct))}%)"
                        else:
                            # Merah (40% sampai 0% atau minus / OSLA)
                            bg = "rgba(239, 68, 68, 0.18)"
                            bd = "#ef4444"
                            cl = "#f87171"
                            ic = "🔴" if remain_pct >= 0 else "⚠️"
                            lbl = f"({int(round(max(0, remain_pct)))}%)" if remain_pct >= 0 else "(OSLA)"

                        target_hours = int(target_sec // 3600)
                        return (
                            f'<span style="background: {bg}; border: 1px solid {bd}; color: {cl}; '
                            f'font-size: 0.76rem; font-weight: 700; padding: 4px 10px; border-radius: 12px; '
                            f'display: inline-flex; align-items: center; justify-content: center; gap: 5px; white-space: nowrap;" '
                            f'title="TTR Berjalan: {time_str_full} | Sisa Waktu SLA: {lbl} (Target: {target_hours} Jam)">'
                            f'{ic} <span style="font-family: monospace; font-size: 0.82rem;">{time_str}</span> '
                            f'<span style="font-size: 0.69rem; opacity: 0.9;">{lbl}</span>'
                            f'</span>'
                        )
                    table_rows = []
                    # Tampilkan maksimal 300 tiket per tampilan agar browser tetap super ringan
                    display_limit = 300
                    df_view = df_table.head(display_limit)
                    
                    for idx, row in enumerate(df_view.to_dict('records')):
                        bg_tr = "#0f172a" if idx % 2 == 0 else "#0b1120"
                        
                        inc_val = html_lib.escape(str(row.get('INCIDENT', '-')))
                        rep_val = html_lib.escape(str(row.get('REPORTED DATE', '-')))
                        
                        raw_stat = str(row.get('STATUS', '-')).upper().strip()
                        stat_badge = status_badges.get(raw_stat, f'<span style="background: rgba(148,163,184,0.18); border: 1px solid #64748b; color: #cbd5e1; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">{html_lib.escape(raw_stat)}</span>')
                        
                        raw_cust = str(row.get('Cust_Clean', str(row.get('CUSTOMER TYPE', '-')))).upper().strip()
                        cust_badge = cust_badges.get(raw_cust, f'<span style="background: rgba(59,130,246,0.18); border: 1px solid #3b82f6; color: #60a5fa; font-size: 0.73rem; padding: 3px 8px; border-radius: 12px; font-weight: 700; display:inline-block;">{html_lib.escape(raw_cust)}</span>')
                        
                        ttr_val = row.get('TTR CUSTOMER', row.get('TTR_CUSTOMER', row.get('TTR BERJALAN', row.get('TTR', None))))
                        ttr_badge = compute_ttr_badge(ttr_val, raw_cust, row.get('REPORTED DATE'))

                        cname_val = html_lib.escape(str(row.get('CUSTOMER NAME', '-')))
                        stype_val = html_lib.escape(str(row.get('SERVICE TYPE', '-')))
                        wzone_val = html_lib.escape(str(row.get('WORKZONE', '-')))
                        summary_val = html_lib.escape(str(row.get('SUMMARY', '-')))

                        r_html = f'''<tr style="background-color: {bg_tr}; border-bottom: 1px solid #1e293b; transition: background 0.15s ease;">
                            <td style="padding: 12px 8px; text-align: center; color: #64748b; font-weight: 600;">{idx+1}</td>
                            <td style="padding: 12px 12px; text-align: center; font-family: monospace; font-size: 0.85rem; font-weight: 700; color: #38bdf8; white-space: nowrap;">{inc_val}</td>
                            <td style="padding: 12px 12px; text-align: center; color: #ffffff; font-weight: 700; white-space: nowrap;">{rep_val}</td>
                            <td style="padding: 12px 12px; text-align: center; white-space: nowrap;">{stat_badge}</td>
                            <td style="padding: 12px 12px; text-align: center; white-space: nowrap;">{cust_badge}</td>
                            <td style="padding: 12px 10px; text-align: center; white-space: nowrap;">{ttr_badge}</td>
                            <td style="padding: 12px 12px; text-align: center; color: #ffffff; font-weight: 600; white-space: nowrap;">{cname_val}</td>
                            <td style="padding: 12px 12px; text-align: center; color: #ffffff; font-weight: 700; white-space: nowrap;">{stype_val}</td>
                            <td style="padding: 12px 12px; text-align: center; font-weight: 700; color: #f8fafc; white-space: nowrap;">{wzone_val}</td>
                            <td style="padding: 12px 18px; min-width: 500px; max-width: 750px; line-height: 1.5; color: #cbd5e1; font-size: 0.80rem; white-space: normal; word-break: break-word; text-align: justify; text-justify: inter-word;">{summary_val}</td>
                        </tr>'''
                        table_rows.append(r_html)

                    table_body = "".join(table_rows)
                    
                    full_table_html = f'''
                    <div class="asr-scroll-container">
                        <table class="asr-table-custom">
                            <thead>
                                <tr>
                                    <th style="width: 50px; text-align: center;">NO</th>
                                    <th style="width: 145px; text-align: center;">INCIDENT</th>
                                    <th style="width: 165px; text-align: center;">REPORTED DATE</th>
                                    <th style="width: 130px; text-align: center;">STATUS</th>
                                    <th style="width: 155px; text-align: center;">CUSTOMER TYPE</th>
                                    <th style="width: 165px; text-align: center;">TTR CUSTOMER</th>
                                    <th style="width: 200px; text-align: center;">CUSTOMER NAME</th>
                                    <th style="width: 110px; text-align: center;">SERVICE</th>
                                    <th style="width: 100px; text-align: center;">WORKZONE</th>
                                    <th style="min-width: 500px; text-align: center;">SUMMARY TIKET</th>
                                </tr>
                            </thead>
                            <tbody>
                                {table_body}
                            </tbody>
                        </table>
                    </div>
                    '''
                    st.markdown(full_table_html, unsafe_allow_html=True)
                    
                    if len(df_table) > display_limit:
                        st.caption(f"⚡ Menampilkan {display_limit:,} dari total {len(df_table):,} tiket untuk kecepatan maksimal browser.")
                    else:
                        st.caption(f"Menampilkan seluruh {len(df_table):,} tiket.")
                
                st.markdown('</div>', unsafe_allow_html=True)

    elif menu == "PROGRESS ASSURANCE":
        st.markdown('<div class="section-title-wrap"><div class="section-title">📸 REKAP & GRAFIK HARIAN PROGRESS TEKNISI ASSURANCE</div></div>', unsafe_allow_html=True)

        @st.cache_data(ttl=60, show_spinner=False)
        def load_rekap_progress_asr():
            import urllib.parse
            sheet_id = "1bUXmomLo6DJYdk0CHGW9KCnoRgG8EqsUdOtALJ0_r7o"
            sheet_name = urllib.parse.quote("REKAP PROGRESS TEKNISI ASR")
            csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
            frames_a = []
            try:
                df_gs = pd.read_csv(csv_url)
                df_gs.columns = df_gs.columns.astype(str).str.strip().str.upper()
                if not df_gs.empty:
                    frames_a.append(df_gs)
            except Exception:
                pass
            local_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rekap_progress_asr.csv")
            if os.path.exists(local_csv):
                try:
                    df_loc = pd.read_csv(local_csv)
                    df_loc.columns = df_loc.columns.astype(str).str.strip().str.upper()
                    if not df_loc.empty:
                        frames_a.append(df_loc)
                except Exception:
                    pass
            if frames_a:
                df_a = pd.concat(frames_a, ignore_index=True)
                if 'TANGGAL' in df_a.columns and 'NOMER INCIDENT' in df_a.columns:
                    df_a['NOMER INCIDENT'] = df_a['NOMER INCIDENT'].astype(str).str.strip().str.upper()
                    df_a = df_a[df_a['NOMER INCIDENT'].ne('') & df_a['NOMER INCIDENT'].ne('NAN')]
                    df_a = df_a.drop_duplicates(subset=['TANGGAL', 'NOMER INCIDENT'], keep='first').reset_index(drop=True)
                return df_a
            return pd.DataFrame()

        try:
            df_asr_prog_raw = load_rekap_progress_asr()
        except Exception as e_asr_prog:
            st.error(f"Gagal memuat sheet REKAP PROGRESS TEKNISI ASR: {e_asr_prog}")
            df_asr_prog_raw = pd.DataFrame()

        if not df_asr_prog_raw.empty:
            tgl_col_a = next((c for c in df_asr_prog_raw.columns if 'TANGGAL' in c), None)
            jam_col_a = next((c for c in df_asr_prog_raw.columns if 'JAM' in c), None)
            tek_col_a = next((c for c in df_asr_prog_raw.columns if 'TEKNISI' in c), None)
            inc_col_a = next((c for c in df_asr_prog_raw.columns if 'INCIDENT' in c or 'TIKET' in c or 'WONUM' in c), None)
            notes_col_a = next((c for c in df_asr_prog_raw.columns if 'NOTE' in c), None)
            wita_col_a = next((c for c in df_asr_prog_raw.columns if 'WITA' in c), None)
            stat_col_a = next((c for c in df_asr_prog_raw.columns if 'STATUS' in c), None)

            if tgl_col_a and jam_col_a and inc_col_a:
                # Bersihkan baris kosong (seperti nomor urut 1..1000 tanpa data NOMER INCIDENT / TANGGAL)
                df_asr_p = df_asr_prog_raw[
                    df_asr_prog_raw[inc_col_a].notna() &
                    (df_asr_prog_raw[inc_col_a].astype(str).str.strip() != '') &
                    (df_asr_prog_raw[inc_col_a].astype(str).str.strip().str.upper() != 'NAN') &
                    df_asr_prog_raw[tgl_col_a].notna() &
                    (df_asr_prog_raw[tgl_col_a].astype(str).str.strip() != '') &
                    (df_asr_prog_raw[tgl_col_a].astype(str).str.strip().str.upper() != 'NAN')
                ].copy()

                # Parse tanggal dan filter sesuai periode di sidebar
                df_asr_p['Parsed_Date'] = pd.to_datetime(df_asr_p[tgl_col_a].astype(str).str.strip(), errors='coerce').dt.date
                df_asr_period = df_asr_p[
                    (df_asr_p['Parsed_Date'] >= start_date) &
                    (df_asr_p['Parsed_Date'] <= end_date)
                ].copy()

                # Parse Jam Kirim Progress (HH:MM:SS -> Hour 0..23 & label HH:00)
                def extract_hour_int_asr(val):
                    s = str(val).strip()
                    if ':' in s:
                        p = s.split(':')[0].strip()
                        if p.isdigit():
                            h = int(p)
                            if 0 <= h <= 23:
                                return h
                    return -1

                df_asr_period['Hour_Int'] = df_asr_period[jam_col_a].apply(extract_hour_int_asr)
                df_asr_period = df_asr_period[df_asr_period['Hour_Int'] >= 0].copy()
                df_asr_period['Jam'] = df_asr_period['Hour_Int'].apply(lambda h: f"{int(h):02d}:00")

                # Klasifikasi 4 Pembagian Progress:
                # - Progress Pagi  : 07:00 s/d 10:00 (Hour 7..10, termasuk <7 bila ada kiriman dini hari)
                # - Progress Siang : 11:00 s/d 14:00 (Hour 11..14)
                # - Progress Sore  : 15:00 s/d 18:00 (Hour 15..18)
                # - Progress Malam : 19:00 s/d 23:59 (Hour 19..23)
                def classify_sesi_progress_asr(h):
                    if 7 <= h <= 10 or h < 7:
                        return 'PROGRESS PAGI'
                    elif 11 <= h <= 14:
                        return 'PROGRESS SIANG'
                    elif 15 <= h <= 18:
                        return 'PROGRESS SORE'
                    else:
                        return 'PROGRESS MALAM'

                df_asr_period['Kategori_Sesi'] = df_asr_period['Hour_Int'].apply(classify_sesi_progress_asr)

                # Bersihkan nama teknisi (tanpa / ASR atau / A agar rapi di rekap)
                if tek_col_a:
                    df_asr_period['Teknisi_Clean'] = (
                        df_asr_period[tek_col_a].astype(str).str.strip()
                        .str.replace(r'(?i)\s*/\s*ASR.*$', '', regex=True)
                        .str.replace(r'(?i)\s*/\s*A\s*$', '', regex=True)
                        .str.strip().str.upper()
                    )
                else:
                    df_asr_period['Teknisi_Clean'] = 'UNKNOWN'

                tot_all_prog_a = len(df_asr_period)
                tot_uniq_inc_a = df_asr_period[inc_col_a].astype(str).str.strip().nunique() if not df_asr_period.empty else 0
                tot_active_tek_a = df_asr_period['Teknisi_Clean'].nunique() if not df_asr_period.empty else 0

                tot_pagi_a = int((df_asr_period['Kategori_Sesi'] == 'PROGRESS PAGI').sum())
                tot_siang_a = int((df_asr_period['Kategori_Sesi'] == 'PROGRESS SIANG').sum())
                tot_sore_a = int((df_asr_period['Kategori_Sesi'] == 'PROGRESS SORE').sum())
                tot_malam_a = int((df_asr_period['Kategori_Sesi'] == 'PROGRESS MALAM').sum())

                # Top Metric Cards
                mc_a1, mc_a2, mc_a3, mc_a4, mc_a5 = st.columns(5)
                with mc_a1:
                    st.markdown(f'<div class="metric-container mc-blue" style="margin-bottom: 18px;"><div class="mc-title">📸 TOTAL PROGRESS</div><div class="mc-value">{tot_all_prog_a} <span style="font-size:0.95rem; color:#94a3b8">FOTO ({tot_uniq_inc_a} TIKET)</span></div></div>', unsafe_allow_html=True)
                with mc_a2:
                    st.markdown(f'<div class="metric-container mc-blue" style="margin-bottom: 18px; border-left-color:#38bdf8;"><div class="mc-title">🌅 PROGRESS PAGI (07-10)</div><div class="mc-value" style="color:#38bdf8;">{tot_pagi_a} <span style="font-size:0.95rem; color:#94a3b8">PROGRESS</span></div></div>', unsafe_allow_html=True)
                with mc_a3:
                    st.markdown(f'<div class="metric-container mc-green" style="margin-bottom: 18px;"><div class="mc-title">☀️ PROGRESS SIANG (11-14)</div><div class="mc-value" style="color:#22c55e;">{tot_siang_a} <span style="font-size:0.95rem; color:#94a3b8">PROGRESS</span></div></div>', unsafe_allow_html=True)
                with mc_a4:
                    st.markdown(f'<div class="metric-container mc-orange" style="margin-bottom: 18px;"><div class="mc-title">🌇 PROGRESS SORE (15-18)</div><div class="mc-value" style="color:#f59e0b;">{tot_sore_a} <span style="font-size:0.95rem; color:#94a3b8">PROGRESS</span></div></div>', unsafe_allow_html=True)
                with mc_a5:
                    st.markdown(f'<div class="metric-container" style="margin-bottom: 18px; border-left: 4px solid #8b5cf6;"><div class="mc-title">🌙 PROGRESS MALAM (19-23)</div><div class="mc-value" style="color:#a78bfa;">{tot_malam_a} <span style="font-size:0.95rem; color:#94a3b8">PROGRESS</span></div></div>', unsafe_allow_html=True)

                # Container Grafik Utama (Identik dengan PROGRESS PROVI)
                asr_prog_chart_container = st.container()
                with asr_prog_chart_container:
                    st.markdown("<div class='custom-border-target'></div>", unsafe_allow_html=True)
                    st.markdown('<div class="section-title-wrap"><div class="section-title">📈 DISTRIBUSI JAM LAPORAN FOTO PROGRESS TEKNISI (PAGI / SIANG / SORE / MALAM)</div></div>', unsafe_allow_html=True)

                all_hours_asr_p = pd.DataFrame({'Jam': [f"{i:02d}:00" for i in range(24)]})
                sesi_list_a = ['PROGRESS PAGI', 'PROGRESS SIANG', 'PROGRESS SORE', 'PROGRESS MALAM']
                frames_asr_p = []
                for sesi_name_a in sesi_list_a:
                    df_sub_sesi_a = df_asr_period[df_asr_period['Kategori_Sesi'] == sesi_name_a]
                    cnt_df_a = pd.merge(
                        all_hours_asr_p,
                        df_sub_sesi_a.groupby('Jam').size().reset_index(name='Jumlah'),
                        on='Jam',
                        how='left'
                    ).fillna(0)
                    cnt_df_a['Kategori'] = sesi_name_a
                    frames_asr_p.append(cnt_df_a)

                chart_asr_prog_df = pd.concat(frames_asr_p, ignore_index=True)
                chart_asr_prog_df['Text'] = chart_asr_prog_df['Jumlah'].apply(lambda x: str(int(x)) if x > 0 else '')

                ch_a1, ch_a2 = asr_prog_chart_container.columns([3, 1])

                with ch_a1:
                    fig_asr_prog = px.line(
                        chart_asr_prog_df,
                        x='Jam',
                        y='Jumlah',
                        color='Kategori',
                        text='Text',
                        markers=True,
                        color_discrete_map={
                            'PROGRESS PAGI': '#3b82f6',
                            'PROGRESS SIANG': '#22c55e',
                            'PROGRESS SORE': '#f59e0b',
                            'PROGRESS MALAM': '#8b5cf6'
                        }
                    )
                    fig_asr_prog.update_traces(
                        line=dict(width=3, shape='spline'),
                        fill='tozeroy',
                        marker=dict(size=8),
                        textposition='top center',
                        textfont=dict(color='#ffffff')
                    )

                    fill_colors_asr_p = {
                        'PROGRESS PAGI': 'rgba(59, 130, 246, 0.16)',
                        'PROGRESS SIANG': 'rgba(34, 197, 94, 0.16)',
                        'PROGRESS SORE': 'rgba(245, 158, 11, 0.16)',
                        'PROGRESS MALAM': 'rgba(139, 92, 246, 0.16)'
                    }
                    for trace in fig_asr_prog.data:
                        if trace.name in fill_colors_asr_p:
                            trace.fillcolor = fill_colors_asr_p[trace.name]
                        trace.name = f'<b><span style="color:white; text-shadow:2px 2px 4px rgba(0,0,0,0.9), -1px -1px 2px rgba(0,0,0,0.8);">{trace.name}</span></b>'

                    fig_asr_prog.add_vrect(x0="00:00", x1="07:00", fillcolor="rgba(160, 160, 160, 0.25)", layer="below", line_width=0)
                    fig_asr_prog.add_vrect(x0="18:00", x1="23:00", fillcolor="rgba(160, 160, 160, 0.25)", layer="below", line_width=0)

                    max_y_asr_p = chart_asr_prog_df['Jumlah'].max() if not chart_asr_prog_df.empty else 5
                    fig_asr_prog.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(color='#cbd5e1'),
                        xaxis_title="Waktu (Jam)",
                        yaxis_title="Jumlah Progress",
                        margin=dict(t=10, b=40, l=50, r=10),
                        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title=""),
                        hovermode="x unified",
                        hoverlabel=dict(bgcolor='#1e293b', font=dict(color='#ffffff')),
                        xaxis=dict(fixedrange=True, dtick=2, range=[-0.5, 23.5], showgrid=True, gridwidth=1, gridcolor='#334155'),
                        yaxis=dict(fixedrange=True, showgrid=True, gridwidth=1, gridcolor='#334155', range=[0, max(max_y_asr_p * 1.22, 4)])
                    )
                    fig_asr_prog.update_xaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_asr_prog.update_yaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_asr_prog.update_traces(cliponaxis=False)
                    st.plotly_chart(fig_asr_prog, use_container_width=True, config={'displayModeBar': False}, theme=None)

                with ch_a2:
                    pct_pagi_a = f"{(tot_pagi_a / tot_all_prog_a) * 100:.1f}".rstrip('0').rstrip('.') if tot_all_prog_a > 0 else "0"
                    pct_siang_a = f"{(tot_siang_a / tot_all_prog_a) * 100:.1f}".rstrip('0').rstrip('.') if tot_all_prog_a > 0 else "0"
                    pct_sore_a = f"{(tot_sore_a / tot_all_prog_a) * 100:.1f}".rstrip('0').rstrip('.') if tot_all_prog_a > 0 else "0"
                    pct_malam_a = f"{(tot_malam_a / tot_all_prog_a) * 100:.1f}".rstrip('0').rstrip('.') if tot_all_prog_a > 0 else "0"

                    html_summary_asr_prog = (
                        '<div style="border: 1px solid #334155; border-radius: 8px; padding: 20px; text-align: center; background-color: #0f172a; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">'
                        '<div style="font-size: 0.9rem; font-weight: bold; color: #cbd5e1; margin-bottom: 18px; letter-spacing: 0.5px;">GRAND TOTAL PROGRESS ASSURANCE</div>'
                        '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 22px 10px; margin-bottom: 18px;">'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #3b82f6; line-height: 1;">{tot_pagi_a}</div><div style="font-size: 11px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">PAGI (07-10)</div><div style="font-size: 11px; color: #94a3b8;">{pct_pagi_a}%</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #22c55e; line-height: 1;">{tot_siang_a}</div><div style="font-size: 11px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">SIANG (11-14)</div><div style="font-size: 11px; color: #94a3b8;">{pct_siang_a}%</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #f59e0b; line-height: 1;">{tot_sore_a}</div><div style="font-size: 11px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">SORE (15-18)</div><div style="font-size: 11px; color: #94a3b8;">{pct_sore_a}%</div></div>'
                        f'<div><div style="font-size: 2.0rem; font-weight: bold; color: #8b5cf6; line-height: 1;">{tot_malam_a}</div><div style="font-size: 11px; color: white; font-weight: bold; text-transform: uppercase; margin-top:8px;">MALAM (19-23)</div><div style="font-size: 11px; color: #94a3b8;">{pct_malam_a}%</div></div>'
                        '</div>'
                        f'<div style="border-top: 1px dashed #334155; padding-top: 16px; margin-top: auto; font-size: 0.92rem; font-weight: bold; color: #94a3b8; text-align: left;">'
                        f'<div style="display:flex; justify-content:space-between; margin-bottom:8px;"><span>TOTAL PROGRESS</span> <span style="color:#38bdf8;">{tot_all_prog_a} FOTO</span></div>'
                        f'<div style="display:flex; justify-content:space-between; margin-bottom:8px;"><span>TIKET UNIK</span> <span style="color:#22c55e;">{tot_uniq_inc_a} TIKET</span></div>'
                        f'<div style="display:flex; justify-content:space-between;"><span>TEKNISI AKTIF</span> <span style="color:white;">{tot_active_tek_a} TIM</span></div>'
                        '</div>'
                        '</div>'
                    )
                    st.markdown(html_summary_asr_prog, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                # --- 4 MINI SPARKLINE CHARTS (PAGI, SIANG, SORE, MALAM) ---
                mini_a_cols = st.columns(4)
                asr_prog_categories_meta = [
                    ('PROGRESS PAGI', 'PROGRESS PAGI (07:00 - 10:00)', '#3b82f6', 'rgba(59, 130, 246, 0.16)'),
                    ('PROGRESS SIANG', 'PROGRESS SIANG (11:00 - 14:00)', '#22c55e', 'rgba(34, 197, 94, 0.16)'),
                    ('PROGRESS SORE', 'PROGRESS SORE (15:00 - 18:00)', '#f59e0b', 'rgba(245, 158, 11, 0.16)'),
                    ('PROGRESS MALAM', 'PROGRESS MALAM (19:00 - 23:59)', '#8b5cf6', 'rgba(139, 92, 246, 0.16)')
                ]
                for idx_ma, (cat_key_a, cat_title_a, cat_color_a, cat_fill_a) in enumerate(asr_prog_categories_meta):
                    df_cat_a = chart_asr_prog_df[chart_asr_prog_df['Kategori'] == cat_key_a]
                    max_y_ma = df_cat_a['Jumlah'].max() if not df_cat_a.empty else 4
                    fig_m_asr = px.line(df_cat_a, x='Jam', y='Jumlah', text='Text', markers=True)
                    fig_m_asr.update_traces(
                        line=dict(width=2.2, color=cat_color_a, shape='spline'),
                        fill='tozeroy',
                        fillcolor=cat_fill_a,
                        marker=dict(size=5, color=cat_color_a),
                        textposition='top center',
                        textfont=dict(color='#ffffff'),
                        cliponaxis=False
                    )
                    fig_m_asr.update_layout(
                        title=dict(text=cat_title_a, font=dict(color=cat_color_a, size=12), x=0.5, xanchor='center'),
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='#0f172a',
                        margin=dict(t=40, b=45, l=45, r=10),
                        xaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, dtick=6, title="Waktu (Jam)"),
                        yaxis=dict(showgrid=True, gridcolor='#334155', fixedrange=True, showticklabels=True, title="Progress", range=[0, max(max_y_ma * 1.28, 2)]),
                        hovermode="x unified",
                        hoverlabel=dict(bgcolor='#1e293b', font=dict(color='#ffffff')),
                        height=260
                    )
                    fig_m_asr.update_xaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    fig_m_asr.update_yaxes(showline=True, linewidth=1, linecolor='#334155', mirror=True)
                    with mini_a_cols[idx_ma]:
                        st.plotly_chart(fig_m_asr, use_container_width=True, config={'displayModeBar': False}, theme=None)

                st.markdown("<br>", unsafe_allow_html=True)

                # --- TABEL REKAP PER TEKNISI (ATAS) & DETAIL PROGRESS (BAWAH) ---
                st.markdown('<div class="section-title-wrap"><div class="section-title" style="font-size: 1.15rem;">👷 REKAP PROGRESS PER TEKNISI</div></div>', unsafe_allow_html=True)
                if not df_asr_period.empty:
                    piv_tek_a = (
                        df_asr_period.groupby(['Teknisi_Clean', 'Kategori_Sesi'])
                        .size()
                        .unstack(fill_value=0)
                        .reset_index()
                    )
                    for s_col_a in ['PROGRESS PAGI', 'PROGRESS SIANG', 'PROGRESS SORE', 'PROGRESS MALAM']:
                        if s_col_a not in piv_tek_a.columns:
                            piv_tek_a[s_col_a] = 0
                    piv_tek_a['TOTAL'] = (
                        piv_tek_a['PROGRESS PAGI'] +
                        piv_tek_a['PROGRESS SIANG'] +
                        piv_tek_a['PROGRESS SORE'] +
                        piv_tek_a['PROGRESS MALAM']
                    )
                    piv_tek_a = piv_tek_a.sort_values(by=['TOTAL', 'Teknisi_Clean'], ascending=[False, True]).reset_index(drop=True)

                    rows_tek_a_html = ""
                    for idx_ta, r_ta in piv_tek_a.iterrows():
                        rows_tek_a_html += (
                            f'<tr style="border-bottom: 1px solid #1e293b;">'
                            f'<td style="padding: 12px 12px; text-align:center; color:#ffffff; font-weight:bold; font-size:1.05rem;">{idx_ta + 1}</td>'
                            f'<td style="padding: 12px 16px; text-align:left; color:#ffffff; font-weight:800; font-size:1.05rem;">{r_ta["Teknisi_Clean"]}</td>'
                            f'<td style="padding: 12px 12px; text-align:center; color:#38bdf8; font-weight:800; font-size:1.1rem;">{int(r_ta["PROGRESS PAGI"])}</td>'
                            f'<td style="padding: 12px 12px; text-align:center; color:#22c55e; font-weight:800; font-size:1.1rem;">{int(r_ta["PROGRESS SIANG"])}</td>'
                            f'<td style="padding: 12px 12px; text-align:center; color:#f59e0b; font-weight:800; font-size:1.1rem;">{int(r_ta["PROGRESS SORE"])}</td>'
                            f'<td style="padding: 12px 12px; text-align:center; color:#a78bfa; font-weight:800; font-size:1.1rem;">{int(r_ta["PROGRESS MALAM"])}</td>'
                            f'<td style="padding: 12px 14px; text-align:center;"><span style="background:rgba(59,130,246,0.2); color:#ffffff; border:1px solid #3b82f6; padding:4px 15px; border-radius:999px; font-weight:800; font-size:1.05rem;">{int(r_ta["TOTAL"])}</span></td>'
                            f'</tr>'
                        )

                    gt_pagi_a = int(piv_tek_a["PROGRESS PAGI"].sum())
                    gt_siang_a = int(piv_tek_a["PROGRESS SIANG"].sum())
                    gt_sore_a = int(piv_tek_a["PROGRESS SORE"].sum())
                    gt_malam_a = int(piv_tek_a["PROGRESS MALAM"].sum())
                    gt_total_a = int(piv_tek_a["TOTAL"].sum())

                    rows_tek_a_html += (
                        f'<tr style="background: #1e293b; border-top: 2px solid #eab308;">'
                        f'<td colspan="2" style="padding: 14px 16px; text-align:center; color:#ffffff; font-weight:900; font-size:1.1rem; letter-spacing:1px;">GRAND TOTAL</td>'
                        f'<td style="padding: 14px 12px; text-align:center; color:#38bdf8; font-weight:900; font-size:1.15rem;">{gt_pagi_a}</td>'
                        f'<td style="padding: 14px 12px; text-align:center; color:#22c55e; font-weight:900; font-size:1.15rem;">{gt_siang_a}</td>'
                        f'<td style="padding: 14px 12px; text-align:center; color:#f59e0b; font-weight:900; font-size:1.15rem;">{gt_sore_a}</td>'
                        f'<td style="padding: 14px 12px; text-align:center; color:#a78bfa; font-weight:900; font-size:1.15rem;">{gt_malam_a}</td>'
                        f'<td style="padding: 14px 14px; text-align:center;"><span style="background:rgba(234,179,8,0.25); color:#ffffff; border:1.5px solid #eab308; padding:4px 16px; border-radius:999px; font-weight:900; font-size:1.1rem;">{gt_total_a}</span></td>'
                        f'</tr>'
                    )

                    tek_a_table_html = (
                        '<div style="border: 1px solid #334155; border-radius: 10px; overflow: hidden; background: #0f172a; margin-bottom: 28px;">'
                        '<table style="width: 100%; border-collapse: collapse; font-size: 1.05rem;">'
                        '<thead>'
                        '<tr style="background: #1e293b; color: #ffffff; text-transform: uppercase; font-size: 0.96rem;">'
                        '<th style="padding: 14px 12px; text-align:center; width: 70px; color:#ffffff;">NO</th>'
                        '<th style="padding: 14px 16px; text-align:center; color:#ffffff;">TEKNISI</th>'
                        '<th style="padding: 14px 12px; text-align:center; color:#38bdf8;">PAGI<br><span style="font-size:12.5px;color:#ffffff;">07:00 - 10:00</span></th>'
                        '<th style="padding: 14px 12px; text-align:center; color:#22c55e;">SIANG<br><span style="font-size:12.5px;color:#ffffff;">11:00 - 14:00</span></th>'
                        '<th style="padding: 14px 12px; text-align:center; color:#f59e0b;">SORE<br><span style="font-size:12.5px;color:#ffffff;">15:00 - 18:00</span></th>'
                        '<th style="padding: 14px 12px; text-align:center; color:#a78bfa;">MALAM<br><span style="font-size:12.5px;color:#ffffff;">19:00 - 23:59</span></th>'
                        '<th style="padding: 14px 14px; text-align:center; color:#ffffff;">TOTAL</th>'
                        '</tr>'
                        '</thead>'
                        f'<tbody>{rows_tek_a_html}</tbody>'
                        '</table>'
                        '</div>'
                    )
                    st.markdown(tek_a_table_html, unsafe_allow_html=True)
                else:
                    st.info("Belum ada data teknisi Assurance yang melapor pada periode tanggal ini.")

                st.markdown('<div class="section-title-wrap"><div class="section-title">📋 DETAIL LOG FOTO PROGRESS TEKNISI</div></div>', unsafe_allow_html=True)
                search_prog_qa = st.text_input("🔍 Cari Teknisi / Incident / Notes / Status Insera / Sesi Waktu:", "", key="search_prog_asr_detail", placeholder="Ketik nama teknisi, INC..., notes, CLOSED, BACKEND, PAGI, SIANG...")
                if not df_asr_period.empty:
                    df_det_a = df_asr_period.sort_values(by=['Parsed_Date', 'Hour_Int', jam_col_a], ascending=[False, False, False]).copy()
                    if search_prog_qa.strip():
                        q_low_a = search_prog_qa.strip().lower()
                        mask_qa = (
                            df_det_a['Teknisi_Clean'].astype(str).str.lower().str.contains(q_low_a, na=False) |
                            df_det_a[inc_col_a].astype(str).str.lower().str.contains(q_low_a, na=False) |
                            df_det_a['Kategori_Sesi'].astype(str).str.lower().str.contains(q_low_a, na=False) |
                            (df_det_a[notes_col_a].astype(str).str.lower().str.contains(q_low_a, na=False) if notes_col_a else False) |
                            (df_det_a[stat_col_a].astype(str).str.lower().str.contains(q_low_a, na=False) if stat_col_a else False)
                        )
                        df_det_a = df_det_a[mask_qa]

                    sesi_badge_map_a = {
                        'PROGRESS PAGI': ('#38bdf8', 'rgba(56,189,248,0.15)', 'PAGI (07-10)'),
                        'PROGRESS SIANG': ('#22c55e', 'rgba(34,197,94,0.15)', 'SIANG (11-14)'),
                        'PROGRESS SORE': ('#f59e0b', 'rgba(245,158,11,0.15)', 'SORE (15-18)'),
                        'PROGRESS MALAM': ('#a78bfa', 'rgba(167,139,250,0.15)', 'MALAM (19-23)')
                    }

                    rows_det_a_html = ""
                    for idx_da, (_, r_da) in enumerate(df_det_a.iterrows(), 1):
                        tgl_va = str(r_da.get(tgl_col_a, '-')).strip()
                        jam_va = str(r_da.get(jam_col_a, '-')).strip()
                        tek_va = str(r_da.get('Teknisi_Clean', '-')).strip()
                        inc_va = str(r_da.get(inc_col_a, '-')).strip()
                        note_va = str(r_da.get(notes_col_a, '-')).strip() if notes_col_a and pd.notna(r_da.get(notes_col_a)) else '-'
                        wita_va = str(r_da.get(wita_col_a, '-')).strip() if wita_col_a and pd.notna(r_da.get(wita_col_a)) else '-'
                        stat_va = str(r_da.get(stat_col_a, '-')).strip() if stat_col_a and pd.notna(r_da.get(stat_col_a)) else '-'
                        sesi_va = str(r_da.get('Kategori_Sesi', 'PROGRESS PAGI'))
                        b_col_a, b_bg_a, b_lbl_a = sesi_badge_map_a.get(sesi_va, ('#38bdf8', 'rgba(56,189,248,0.15)', sesi_va))

                        stat_up_a = stat_va.upper()
                        stat_color_a = '#22c55e' if 'CLOSE' in stat_up_a or 'RESOLV' in stat_up_a else ('#f59e0b' if 'BACKEND' in stat_up_a or 'PENDING' in stat_up_a else '#38bdf8')

                        rows_det_a_html += (
                            f'<tr style="border-bottom: 1px solid #1e293b;">'
                            f'<td style="padding: 10px 8px; text-align:center; color:#94a3b8; font-weight:bold;">{idx_da}</td>'
                            f'<td style="padding: 10px 10px; text-align:center; color:#e2e8f0; white-space:nowrap;">{tgl_va} &bull; <span style="color:#38bdf8; font-weight:700;">{jam_va}</span></td>'
                            f'<td style="padding: 10px 10px; text-align:center;"><span style="background:{b_bg_a}; color:{b_col_a}; border:1px solid {b_col_a}; padding:3px 10px; border-radius:6px; font-size:0.74rem; font-weight:700; white-space:nowrap;">{b_lbl_a}</span></td>'
                            f'<td style="padding: 10px 12px; text-align:left; color:#f8fafc; font-weight:700; white-space:nowrap;">{tek_va}</td>'
                            f'<td style="padding: 10px 12px; text-align:left; color:#fbbf24; font-family:monospace; font-size:0.84rem; white-space:nowrap;">{inc_va}</td>'
                            f'<td style="padding: 10px 12px; text-align:left; color:#cbd5e1;">{note_va}</td>'
                            f'<td style="padding: 10px 10px; text-align:center; color:#94a3b8; white-space:nowrap;">{wita_va}</td>'
                            f'<td style="padding: 10px 10px; text-align:center;"><span style="color:{stat_color_a}; font-weight:700; font-size:0.78rem;">{stat_va}</span></td>'
                            f'</tr>'
                        )

                    det_a_table_html = (
                        '<div style="border: 1px solid #334155; border-radius: 10px; overflow: hidden; background: #0f172a; max-height: 550px; overflow-y: auto;">'
                        '<table style="width: 100%; border-collapse: collapse; font-size: 0.83rem;">'
                        '<thead>'
                        '<tr style="background: #1e293b; color: #cbd5e1; text-transform: uppercase; font-size: 0.76rem; position: sticky; top: 0; z-index: 2;">'
                        '<th style="padding: 12px 8px; text-align:center; width: 55px;">NO</th>'
                        '<th style="padding: 12px 10px; text-align:center;">TANGGAL & JAM KIRIM</th>'
                        '<th style="padding: 12px 10px; text-align:center;">SESI PROGRESS</th>'
                        '<th style="padding: 12px 12px; text-align:left;">TEKNISI</th>'
                        '<th style="padding: 12px 12px; text-align:left;">NOMER INCIDENT</th>'
                        '<th style="padding: 12px 12px; text-align:left;">NOTES</th>'
                        '<th style="padding: 12px 10px; text-align:center;">DATE MODIFIED WITA</th>'
                        '<th style="padding: 12px 10px; text-align:center;">STATUS INSERA</th>'
                        '</tr>'
                        '</thead>'
                        f'<tbody>{rows_det_a_html}</tbody>'
                        '</table>'
                        '</div>'
                    )
                    st.markdown(det_a_table_html, unsafe_allow_html=True)
                else:
                    st.info("Tidak ada detail log foto progress Assurance pada rentang tanggal yang dipilih.")
            else:
                st.warning("Kolom TANGGAL, JAM KIRIM PROGRESS, atau NOMER INCIDENT tidak ditemukan pada sheet REKAP PROGRESS TEKNISI ASR.")
        else:
            st.info("Data REKAP PROGRESS TEKNISI ASR belum tersedia atau kosong.")

else:
    st.warning("⚠️ **Data satelit belum dapat ditampilkan atau terjadi pembatasan jam ekspor oleh Google Sheets.**")
    st.info("💡 Catatan: Google Sheets membatasi ekspor data antara pukul 06:00 - 23:00 WIB (07:00 - 24:00 WITA).")
    if st.button("🔄 Muat Ulang Data (Clear Cache)"):
        st.cache_data.clear()
        st.rerun()

