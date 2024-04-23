import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd
import zipfile

# Set page configuration
st.set_page_config(
    layout="wide"
)

# Define the file path with regular spaces
path_to_html = "CNN.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Convolutional Neural Networks (CNN)]")
    st.markdown("""Hi guys. Welcome to the 2nd lecture of Deep Learning series. Today we are going to study one of the most
                    widely used Deep Learning algorithm named 'Convolutional Neural Networks' aka 'CNN'. CNN is an alogirthm 
                    which has multiple real-time applications like Facial recognition, Healthcare analysis, Drug discovery,
                    Image Classification to name a few. Today, we are going to create a CNN model for Image classification 
                    and test our model on a gradio interface. Before starting with the session, I would request you to 
                    download the zip file 'dataset' on which we are going to train our CNN model. The dataset file contains
                    Images from 3 classes: Forest, Sea & Buildings. Our aim today is to build a model using CNN that would
                    correctly classify an uploaded image into it's respective category. So nuf' said, let's get started. """)
    
    
    
    def create_zip():
        with zipfile.ZipFile('dataset.zip', 'w') as zipf:
            for root, dirs, files in os.walk('dataset'):
                for file in files:
                    zipf.write(os.path.join(root, file), file)
        with open("dataset.zip", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the zip file
    button_label_zip = "Download dataset Zip"
    button_download_zip = st.download_button(label=button_label_zip, data=create_zip(), file_name='dataset.zip', mime='application/zip')
    


    st.write("---")
    st.components.v1.html(html_data, width=800, height=19750)

    def download_notebook():
        with open("CNN.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Convolutional Neural Networks' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="CNN.ipynb", mime='application/x-ipynb+json')
    