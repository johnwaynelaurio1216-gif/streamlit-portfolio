import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

# ---- CUSTOM STYLE ----
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# ---- HERO SECTION ----
col1, col2 = st.columns([2,1])

with col1:
    st.title("👋 Hi, I'm John Wayne")
    st.subheader("BSCS Student | Aspiring Developer")
    st.write("I create simple and clean web applications.")

st.divider()

# ---- SERVICES ----
st.subheader("🚀 What I Do")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h3>💻 Development</h3><p>Build apps using Python.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>🎨 UI Design</h3><p>Clean and simple designs.</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h3>⚙️ Problem Solving</h3><p>Fix real-world problems.</p></div>', unsafe_allow_html=True)

st.info("Use the sidebar to explore my portfolio.")