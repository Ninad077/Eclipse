import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd

# Set page configuration
st.set_page_config(
    layout="wide"
)

# Define the file path with regular spaces
path_to_html = "Python_basics.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Python basics]")
    st.markdown("""Hi guys. Now that you are familiar with Jupyter notebook, let us start with Python. The entire
                   Machine Learning we are going study is implemented using Python. So , it is essential for us to 
                   understand some core Python basics to get started. You can download the Jupyter notebook
                   at the end of this session. I have enclosed it at the bottom of this page. 
                    For now, let's get started with Python.""")
    st.write("---")
    st.components.v1.html(html_data, width=800, height=13900)

    def download_notebook():
        with open("Python_basics.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Python basics' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Python_basics.ipynb", mime='application/x-ipynb+json')
