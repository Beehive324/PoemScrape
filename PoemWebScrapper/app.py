import streamlit as st
from main import get_poem
from threading import Thread
import time
import os
from datetime import datetime

# Function to read the poem from the file
def read_poem(file_path):
    with open(file_path, 'r') as file:
        poem = file.read()
    return poem

# Get today's date in the format the file is saved
today = datetime.today().strftime('%Y-%m-%d')
file_path = f"{today}"

st.title("Poem of the Day")

button = st.sidebar.button("Get Poem of the day")

if button:
    t = Thread(target=get_poem, args=())
    t.start()
    # Wait for the file to be created
    while not os.path.exists(file_path):
        time.sleep(0.1)

poem_text = read_poem(file_path)

with st.expander(f"{file_path}"):
    st.markdown(f"### Poem of the Day\n\n{poem_text}")
