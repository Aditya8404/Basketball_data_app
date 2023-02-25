import streamlit as st

st.set_page_config(page_title="My Data App", layout="wide")

# header
st.header("Hi, I'm Aditya Punia :wave:")
st.title("Data science intern at Innomatics Research Labs")

st.write("---")

# about me
st.subheader("About Me")
st.text("Hello")
st.text("I am Aditya Punia.")
st.text("Creative, hardworking computer science student anticipating graduation in 2025.")
st.text("Having skills in python, C++, Front-end development and Machine Learning")
st.text("Looking to apply my skills and knowledge in a challenging and dynamic entry-level role.")

# connect
st.write("---")
st.subheader("Let's connect =>")

st.text("LinkedIn -")
if st.button("click here to connect with me on LinkedIn"):
    st.write("https://www.linkedin.com/in/aditya-punia-0340ba239/")
    st.balloons()

st.text("GitHub -")
if st.button("click here to connect with me on GitHub"):
    st.write("https://github.com/Aditya8404")
    st.balloons()