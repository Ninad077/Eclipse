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
path_to_html = "Decision_Tree.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Decision Tree]")
    st.markdown("""Hi guys. Today we are going to learn about Decision Tree algorithm. For those who could relate, I can simply describe the logic of Decision Tree
                   as that of 'Nested If' statement. Similar to Nested If, here as well we check for each and every attribute one by one starting from the most important 
                   condition first followed by other conditions in the decreasing order of importance. For those who are unaware about Nested If concept, it is completely 
                   fine. I would walk you through the concept of Decision trees, the leaf nodes,the root nodes & the decision nodes step by step so that you could understand the 
                   algorithm much better. For now just try to remember Decision Tree as an algorithm which checks the columns selectively giving more preference to a column
                   having a higher importance (importance gain) followed by checking the less important columns in the decreasing order of importance. Before we dive into 
                   understanding Decision Trees, I would request you to please donwload  'cars_data' zip file which has 'cars_train' and 'cars_test' data on which we are going 
                   to apply Decision Trees. The dataset is about different features of cars and classes in which these cars are categorised. Our job is to find out what columns 
                   are contributing in going ahead and deciding which class the car belongs to. So without wasting any more time, let's get started.""")
    
    
    
    def create_zip():
        with zipfile.ZipFile('cars_data.zip', 'w') as zipf:
            for root, dirs, files in os.walk('cars_data'):
                for file in files:
                    zipf.write(os.path.join(root, file), file)
        with open("cars_data.zip", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the zip file
    button_label_zip = ":violet[Download cars_data Zip]"
    button_download_zip = st.download_button(label=button_label_zip, data=create_zip(), file_name='cars_data.zip', mime='application/zip')
    


    st.write("---")
    st.components.v1.html(html_data, width=800, height=9700)

    def download_notebook():
        with open("Decision_Tree.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Decision Tree' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Decision_Tree.ipynb", mime='application/x-ipynb+json')
    
   