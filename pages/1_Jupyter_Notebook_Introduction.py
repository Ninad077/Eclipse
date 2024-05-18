import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd

# Set page configuration
st.set_page_config(
    layout="wide"
)

# Define the file path with regular spaces
path_to_html = "Jupyter_Intro.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Getting familar with Jupyter notebook]")
    st.markdown("""Hi guys, welcome to your very first session. I am very excited to walk you through all the modules starting from
                    Preprocessing in Python to Supervised Machine Learning, Unsupervised Machine Learning, Reinforcement Machine Learning and
                    Deep Learning. The modules are well curated for anyone who is starting Machine Learning or even programming for the first
                    time. So rest assured it would be a fun ride. :)
                    To begin with, the entire course is designed to work on Jupyter notebook environment. So it is important for you to first
                    understand what Jupter notebook is and how does one code on Jupyter notebook.
                    The coding on Jupyter notebook is done in cell wise fashion unlike VS code. Vs code is another famous interpretor whereas 
                    one can code as well.
                    Let us understand some basic features of Jupyter notebook first.""")
    st.write("---")
    st.components.v1.html(html_data, width=800, height=18700)

    def download_notebook():
        with open("Jupyter_Intro.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Jupyter introduction' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Jupyter_Intro.ipynb", mime='application/x-ipynb+json')
    
