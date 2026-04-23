import streamlit as st

st.title("🛠 Skills")

st.subheader("Programming")
st.write("Python")
st.progress(80)

st.write("Java")
st.progress(70)

st.write("HTML/CSS")
st.progress(75)

st.subheader("Tools")
st.write("- GitHub")
st.write("- VS Code")
st.write("- Streamlit")

skill = st.selectbox("Choose skill to improve", ["Python", "Java", "Design"])
st.success(f"Improve {skill} 🚀")