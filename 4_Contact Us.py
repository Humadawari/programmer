import streamlit as st


st.header("I am Huma Dawari. I will teach you some programing languages so that you can design a Website or application etc")
st.subheader("You can contact me here👇")
st.divider()



st.header("if you have any questions, you can email me📧")
st.subheader("humadawari@gmail.com")

st.header("You can find me here on Linkedin📱")
st.subheader("https://www.linkedin.com/in/huma-dawari-3b35292a4?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")


st.divider()
st.sidebar.header('ABOUT')
st.sidebar.text('''Hi I am Huma Dawari. I will teach you some programing 
languages so that you can design a Website or application etc.''')


linkedin = st.text_input('Enter your linkedin ID:')
if 'https://www.linkedin.com/in' in linkedin:
    st.write(f"confirm your linkedin ID is {linkedin}")






