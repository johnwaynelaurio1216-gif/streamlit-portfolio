import streamlit as st

st.title("📂 Projects")

projects = [
    ("E-Attendance", "Tracks attendance"),
    ("Portfolio App", "My personal website"),
    ("Banking System", "Handles transactions")
]

for title, desc in projects:
    st.markdown(f"""
    <div style="background:#1e293b;padding:15px;border-radius:10px;margin-bottom:10px;">
        <h3>{title}</h3>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

rating = st.slider("Rate my projects", 1, 5)
st.write(f"Rating: {rating} ⭐")