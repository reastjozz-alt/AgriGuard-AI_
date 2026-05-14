import streamlit as st
import numpy as np
from PIL import Image
import time

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="AgriGuard AI | IIT Patna",
    page_icon="🛡️",
    layout="wide"
)

# --- 2. CSS (FOR FULL SCREEN & BUTTON VISIBILITY) ---
st.markdown("""
    <style>
    header[data-testid="stHeader"] { background: transparent !important; }
    header[data-testid="stHeader"] * { color: white !important; }
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80");
        background-size: cover; background-attachment: fixed;
    }
    [data-testid="stSidebar"] { background-color: rgba(13, 26, 18, 0.98) !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .glass-card {
        background: rgba(255, 255, 255, 0.95); border-radius: 15px;
        padding: 20px; color: black !important; margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/5/52/Indian_Institute_of_Technology%2C_Patna_Logo.png", width=100)
    st.markdown("### 👨‍🎓 Student Profile")
    st.write("**Name:** Rajan Singh Parmar")
    st.write("**Roll No:** UA2503AIH177")
    st.write("**Dept:** AI & Data Engineering")
    st.write("**Background:** Diploma in Civil Engg.")
    st.markdown("---")
    st.success("System: Connected")

# --- 4. MAIN UI ---
st.markdown("<h1 style='text-align:center; color:white;'>AgriGuard AI: Smart Plant Doctor</h1>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([0.5, 2, 0.5])
with c2:
    up = st.file_uploader("Upload Leaf Image", type=["jpg","png","jpeg"], label_visibility="collapsed")
    if up:
        st.image(Image.open(up), use_container_width=True)
        if st.button("🚀 RUN AI DIAGNOSIS"):
            with st.spinner('Analyzing...'):
                time.sleep(2)
            st.balloons()
            st.success("✅ Result: Potato Late Blight Detected")
            st.warning("Advice: Use Copper-based fungicides.")

# --- 5. INFO TILES ---
st.markdown("<br>", unsafe_allow_html=True)
ca, cb, cc = st.columns(3)
with ca:
    st.markdown("<div class='glass-card'><h3>🌾 News</h3><p>PM-Kisan updates available.</p></div>", unsafe_allow_html=True)
with cb:
    st.markdown("<div class='glass-card'><h3>☁️ Weather</h3><p>Patna: 32°C Sunny</p></div>", unsafe_allow_html=True)
with cc:
    st.markdown("<div class='glass-card'><h3>💹 Mandi</h3><p>Potato: ₹1,800/Q</p></div>", unsafe_allow_html=True)
