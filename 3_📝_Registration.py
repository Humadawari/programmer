import streamlit as st


st.title("You can register in this registration section📝")
st.divider()



st.markdown("<h1 style='text-slign: center;'>User Registration</h1>", unsafe_allow_html=True)
with st.form("Form 2"):
    col1,col2=st.columns(2)
    f_name=col1.text_input("First Name")
    l_name=col2.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day,month,year=st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state=st.form_submit_button("Submit")
    if s_state:
        if f_name == "" and l_name =="":
            st.warning("Please fill above fields")
            slse:()
            st.success("Submitted Successfully")


st.divider()
occupation = st.selectbox('What is your major?',
                          ['', 'Engineer', 'Health', 'Art', 'Biochemistry', 'Computer Engineering', 'Businss',
                           'Social Science', 'Social Engineering', 'Natural Science', 'Computer Science',
                           'Communications', 'Architecture', 'Mathematics and Statistics', 'Environmental Science',
                           'Software Engineering', 'programmer', 'Teacher', 'doctor'])
st.write('you are a', occupation)

location = st.multiselect('Where did you live', (
'Afghanistan', 'Germany', 'United states', 'Ireland', 'Italy', 'Spain', 'Sweden', 'United Kingdom', 'Russia', 'Japan',
'Switzerland', 'Belgium', 'China', 'Australia', 'india'))
st.write('you selected', len(location), 'location')


st.divider()
classdata = st.selectbox("Enter your class :", (1, 2, 3, 4, 5, 6))

button = st.button("Done")
if button:
    st.markdown(f"""
    class : {classdata}""")




st.sidebar.header('ABOUT')
st.sidebar.text('''Hi I am Huma Dawari. I will teach you some programing 
languages so that you can design a Website or application etc.''')



