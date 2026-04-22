import streamlit as st

st.title("📞 Contact Me")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Send"):
    if name and email and message:
        st.success("Message sent! ✅")
    else:
        st.error("Fill all fields")

st.write("GitHub: https://github.com/johnwaynelaurio1216-gif/streamlit-portfolio")