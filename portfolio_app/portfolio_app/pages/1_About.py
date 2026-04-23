import streamlit as st

st.title("🧑‍💻 About Me")

col1, col2 = st.columns([1,2])

with col1:
    st.image("https://via.placeholder.com/200")

with col2:
    st.write("I am a BSCS student passionate about programming and technology.")

st.divider()

st.subheader("🎓 Education")
st.write("BS Computer Science")

st.subheader("🎯 Goals")
st.write("- Become a Full Stack Developer")
st.write("- Build useful apps")

level = st.slider("My Motivation Level", 0, 100, 90)
st.progress(level)