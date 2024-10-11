import streamlit as st

# Title
st.title("Hello GeeksForGeeks !!!")

number = st.slider("Pick a number", 0, 100)

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

st.write("You selected:", genre)

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"))

st.write("You selected:", option)

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

on = st.toggle("Activate feature")

if on:
    st.write("Feature activated!")

# Spuštěšní aplikace streamlit
# streamlit run c:/VisualStudio/Python/Streamlit/Program.py 

# Ceta kde je progrma
# c:\Users\HHH594\AppData\Roaming\Python\Python39\Scripts\

# Funguje spuštění s celou cestou
# c:\Users\HHH594\AppData\Roaming\Python\Python39\Scripts\streamlit run c:/VisualStudio/Python/Streamlit/Program.py 
# c:\Users\HHH594\AppData\Roaming\Python\Python39\Scripts\streamlit run c:/VisualStudio/Python/Streamlit/Program.py --server.port 80
# c:\Users\HHH594\AppData\Roaming\Python\Python39\Scripts\streamlit run c:/VisualStudio/Python/Streamlit/Program.py --server.port 80
# KONEC WEBU
# CTRL + C

#
#pip install PyPDF2
#pip install argparse