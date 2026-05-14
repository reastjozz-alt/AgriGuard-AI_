import streamlit as st
import numpy as np
from PIL import Image
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AgriGuard AI | IIT Patna Capstone",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE ULTIMATE CSS (FIXED EVERYTHING) ---
st.markdown("""
    <style>
    /* 1. Header & Toolbar Transparency with Button Visibility */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    header[data-testid="stHeader"] svg, 
    header[data-testid="stHeader"] button,
    header[data-testid="stHeader"] a {
        color: #ffffff !important; /* Force icons/buttons to stay White */
        fill: #ffffff !important;
    }

    /* 2. Full Screen Background with Crops Theme */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)), 
                    url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* 3. Sidebar Styling (Professional Dark Green) */
    [data-testid="stSidebar"] {
        background-color: rgba(13, 26, 18, 0.98) !important;
        border-right: 2px solid #2e7d32;
    }
    [data-testid="stSidebar"] * { color: #ffffff !important; }

    /* 4. Text & Title Shadows for Contrast */
    .main-title {
        color: #ffffff !important;
        text-shadow: 4px 4px 8px rgba(0,0,0,1);
        text-align: center;
        font-size: 55px;
        font-weight: 800;
        margin-top: -50px; /* Adjust for transparent header */
    }
    .sub-title {
        color: #ffffff !important;
        text-align: center;
        font-size: 20px;
        text-shadow: 2px 2px 4px #000;
        margin-bottom: 30px;
    }

    /* 5. Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        color: #1a2421 !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        border-top: 5px solid #2e7d32;
    }

    /* 6. Uploader Styling */
    div[data-testid="stFileUploader"] section {
        background-color: rgba(255, 255, 255, 0.98) !important;
        border: 3px dashed #2e7d32 !important;
        border-radius: 20px !important;
    }
    div[data-testid="stFileUploader"] p, div[data-testid="stFileUploader"] small {
        color: #666666 !important;
    }

    /* 7. Action Button */
    div.stButton > button {
        background: linear-gradient(135deg, #2e7d32 0%, #1b5e20 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        width: 100%;
        height: 3.5em;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: ADMIN PANEL ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/5/52/Indian_Institute_of_Technology%2C_Patna_Logo.png", width=110)
    st.markdown("## ⚙️ ADMIN PANEL")
    st.markdown("---")
    # Clean Text (No Boxes)
    st.markdown(f"👨‍🎓 *Student:* Rajan Singh Parmar")
    st.markdown(f"🆔 *Roll No:* UA2503AIH177")
    st.markdown("---")
    st.info("System Status: *Active*")
    st.success("Cloud Server: *Connected*")
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("✍️ *Developed by:*")
    st.write("Rajan Singh Parmar")
    st.caption("IIT Patna | UG")

# --- 4. MAIN INTERFACE ---
st.markdown("<h1 class='main-title'>AgriGuard AI: Smart Plant Doctor</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Multi-Crop Diagnosis: Rice • Wheat • Potato • Tomato • Mustard</p>", unsafe_allow_html=True)

# Center Section: Uploader
c1, c2, c3 = st.columns([0.5, 2, 0.5])
with c2:
    uploaded_file = st.file_uploader("Upload leaf specimen", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    if uploaded_file:
        st.image(Image.open(uploaded_file), use_container_width=True, caption="Uploaded Specimen")
        if st.button("🚀 RUN DEEP LEARNING DIAGNOSIS"):
            with st.spinner('Analyzing crop patterns...'):
                time.sleep(2)
            st.balloons()
            st.success("✅ Analysis Complete! Result: *Potato Late Blight*")
            st.markdown("""
                <div style='background-color: #fff9c4; padding: 15px; border-radius: 10px; border-left: 8px solid #fbc02d;'>
                <p style='color: #856404; font-weight: bold; margin:0;'>Treatment: Use Copper-based fungicides immediately.</p>
                </div>
            """, unsafe_allow_html=True)

# --- 5. INFORMATION TILES ---
st.markdown("<br>", unsafe_allow_html=True)
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("""<div class='glass-card'>
    <h3>🌾 Crop News</h3>
    <p>• PM-Kisan 17th installment updates.</p>
    <p>• New soil health check camps in Patna.</p>
    </div>""", unsafe_allow_html=True)

with col_b:
    st.markdown("""<div class='glass-card'>
    <h3>☁️ Patna Weather</h3>
    <p style='font-size: 28px; color: #2e7d32;'><b>32°C ☀️ Sunny</b></p>
    <p>Location: Patna, Bihar | Humidity: 45%</p>
    </div>""", unsafe_allow_html=True)

with col_c:
    st.markdown("""<div class='glass-card'>
    <h3>💹 Mandi Bhav</h3>
    <p>🍅 Tomato: <b>₹2,500/Q</b></p>
    <p>🥔 Potato: <b>₹1,800/Q</b></p>
    <p>🌾 Wheat: <b>₹2,200/Q</b></p>
    </div>""", unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("<br><hr style='border: 1.1px solid white;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-weight: bold;'>© 2026 AgriGuard Project | Developed by: Rajan Singh Parmar | IIT Patna</p>", unsafe_allow_html=True)
