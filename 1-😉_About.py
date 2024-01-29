import streamlit as st


st.title("HELLO👋")
st.header("I am Huma Dawari. I will teach you some programing languages so that you can design a Website or application etc")
st.divider()
st.subheader("Here you can find information about the programming languages that can be used for coding (build some thing by programming languages)")
st.subheader("And you can copy the streamlit installing code from this website, and get the youtube video links that have the best information, you can also get more information from the youtube links that I have shared, Tank you😊")

st.sidebar.header('ABOUT')
st.sidebar.text('''Hi I am Huma Dawari. I will teach you some programing 
languages so that you can design a Website or application etc.''')

st.divider()
# video
vid = open('Untitled 22_1080p.mp4', 'rb').read()
st.video(vid)

st.divider()
st.markdown(
    "The choice for the word language wasn't made by accident, either: just like in human languages, programming languages have internal rules that keep it all from going off the rails.")
st.markdown(
    "A programming language will have a syntax, a set of rules concerning word order and word use, just like in a human language. For example, in English you can say Gary gave Fred a book. In this sentence, you know exactly who gave what and to whom; change the words around and you get a different sentence: Fred gave Gary a book That still makes sense, but if you say a book to Gary Fred gave we have a problem on our hands.")

st.markdown(
    "Roughly speaking, programming languages fall into two categories: low-level and high-level languages. Low-level languages are called that because they are closs to the machine, they can speak to it directly. This includes machine language and assembly languages, which are programming languages that are only a little removed from binary.")
st.markdown(
    "High-level languages are a step above low-level languages. They're further away from the machine, but are readable by humans. Readable in this case means that if you know the language in question you can look at a few lines of code and figure out what's going on. This also works the other way around: you can type up commands which will then be executed by the machine")
