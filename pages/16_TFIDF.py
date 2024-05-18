import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd

# Set page configuration
st.set_page_config(
    layout="wide"
)

# Define the file path with regular spaces
path_to_html = "NLP_Tfidf.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[NLP - Term Frequency Inverse Document Frequency (TFIDF) model]")
    st.markdown("""Hi guys. Now that you have finished knowing the fundamentals of neural networks, let us understand one of the most
                    important domain of Deep Learning which has recently shot to a meteoric fame, courtesy to Chatgpt. For those who don't 
                    know, Chatgpt is fundamentally built on the concept of NLP, which is an abbreviation for 'Natural Language Processing'. What 
                    is this NLP? What are it's components? How does it help fetch answers to almost any input text? What all models it uses to 
                    generate an output? Let us try to understand it as much as we can. To be frank with you guys, Deep learning, Computer Vision, 
                    NLP are very big fields and one may take years to understand it out and out. However, hear me out, all big things started with
                    one step at a time, so let us make sure we understand the basics correctly. Rest assured, I will help you with that. For now, let us 
                   start with the session.
                """)
    


    st.write("---")
    st.components.v1.html(html_data, width=800, height=10800)

    def download_notebook():
        with open("NLP_Tfidf.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'NLP-TFIDF' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="NLP_Tfidf.ipynb", mime='application/x-ipynb+json')
    