import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd

# Set page configuration
st.set_page_config(
    layout="wide"
)

# Define the file path with regular spaces
path_to_html = "NLP_RASA.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[NLP - RASA]")
    st.markdown("""Hi guys. I know it is too boring to study algorithms after algorithms. So for today's session I am not going 
                   to teach you any algorithm. Yes, you heard it right! For a change we are going to do something really interesting.
                   We are going to talk with a RASA assistant. Now what is RASA and what does an assitant mean?..... all these questions 
                   I will address in a minute, but before that let me tell you how important it is to know frameworks when it comes to NLP. 
                   When one applies for a NLP/AI/Deep Learning job, it is necessary that we know at least one NLP framework well. RASA is one 
                   of the widely known frameworks that help in building custom chatbots. Assitant is basically a chatbot that responds 
                   to human questions by generating answers. So for those interested, I would recommend you to learn more about RASA frameworks 
                   from their official videos on Youtube and try to understand the framework. For now, I will just brief you out on how to 
                   create your first RASA assistant.""")
    
    
    st.write("---")
    st.components.v1.html(html_data, width=800, height=10700)

    def download_notebook():
        with open("NLP_RASA.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'NLP - RASA' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="NLP_RASA.ipynb", mime='application/x-ipynb+json')
    