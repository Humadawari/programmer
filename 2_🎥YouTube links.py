import streamlit as st


st.title("Hello you can find YouTube links of programming languages here🎥")
st.divider()

st.markdown(
    "The choice for the word language wasn't made by accident, either: just like in human languages, programming languages have internal rules that keep it all from going off the rails.")
st.divider()

st.subheader("PYTHON PROGRAMMING LANGUAGE")
st.markdown("https://youtube.com/playlist?list=PLsyeobzWx|7poL9JTVyndKe62ieoN-MZ3&si=3L6WE00kapjKzrNQ")
st.divider()
st.subheader("JAVASCRIPT PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/W6NZfCO5SIk?si=TMFTtLJyBxV9RebM")
st.divider()
st.subheader("C++ PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/ZzaPdXTrSb8?si=XuuYInARv-GajSkm")
st.divider()
st.subheader("JAVA PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/eIrMbAQSU34?si=jTQr8JCZTInWBv0-")
st.divider()
st.subheader("C PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/KJgsSFOSQv0?si=ilZY__mb2-YMdGE-")
st.divider()
st.subheader("RUBY PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/t_ispmWmdjY?si=EFw4MAdJnr-eGd7G")
st.divider()
st.subheader("C# PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/gfkTfcpWqAY?si=sWxboAp00HMRBOmj")
st.divider()
st.markdown(
    "In short, a programming language is the way in which a computer programmer talks to a device. If you know how to speak one of these languages and there are hundreds you can create a program that can perform tasks. These can range from the very simple, like a script that moves a file from one place to another, to the very complex, like rendering a 3D world in a video game.")

st.divider()
message = st.text_area('Give your Experience about Coding')


st.divider()
status = st.radio('What is your status', ('Active', 'Inactive'))
if status is 'Active':
    st.success('Active')
else:
    st.warning('you are Inactive')

st.sidebar.header('ABOUT')
st.sidebar.text('''Hi I am Huma Dawari. I will teach you some programing 
languages so that you can design a Website or application etc.''')






st.divider()
# video
vid = open('Untitled 22_1080p.mp4', 'rb').read()
st.video(vid)

st.markdown("A computer programmer,sometimes referred to as a software developer,"
        " a software engineer, a programmer or a coder, "
        "is a person who creates computer programs.")
st.markdown(
    "A programming language will have a syntax, a set of rules concerning word order and word use, just like in a human language. For example, in English you can say Gary gave Fred a book. In this sentence, you know exactly who gave what and to whom; change the words around and you get a different sentence: Fred gave Gary a book That still makes sense, but if you say a book to Gary Fred gave we have a problem on our hands.")




st.markdown(
    "Roughly speaking, programming languages fall into two categories: low-level and high-level languages. Low-level languages are called that because they are closs to the machine, they can speak to it directly. This includes machine language and assembly languages, which are programming languages that are only a little removed from binary.")
st.markdown(
    "High-level languages are a step above low-level languages. They're further away from the machine, but are readable by humans. Readable in this case means that if you know the language in question you can look at a few lines of code and figure out what's going on. This also works the other way around: you can type up commands which will then be executed by the machine")




