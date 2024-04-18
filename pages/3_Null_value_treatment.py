import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd
import zipfile

import streamlit as st

# Define the file path with regular spaces
path_to_html = "C:/Users/ninad/MLapp_UI/Day1_Python_basics (1).html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header("Introduction to the Libraries & Null Value Treatment")
    st.markdown("""Happy to see you guys back! Now that you have fundamental knowledge about core Python functions
                    let us try to dive in a little deeper. Before jumping on any Machine Learning algorithm, it is 
                    important to learn 'Preprocessing'. The first step of Preprocessing is Installing & importing the
                    libraries & Null value treatment. Since I would be working on multiple CSV files, I would appreciate
                    if you guys download these files first to start working on it.
                 """)
    df = pd.read_csv("advertising.csv")
    
def create_zip():
        with zipfile.ZipFile('Null.zip', 'w') as zipf:
            for root, dirs, files in os.walk('Null'):
                for file in files:
                    zipf.write(os.path.join(root, file), file)
        with open("Null.zip", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the zip file
button_label_zip = "Download Excel Files Zip"
button_download_zip = st.download_button(label=button_label_zip, data=create_zip(), file_name='Null.zip', mime='application/zip')
st.components.v1.html(html_data, width=800, height=13780)

def download_notebook():
        with open("Day1_Python_basics.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
st.write("----")
st.write("To download 'Python basics' Jupyter notebook click on the button below.")
button_label = "Download Jupyter Notebook"
button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Day1_Python_basics.ipynb", mime='application/x-ipynb+json')
