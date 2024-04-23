import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd

# Set page configuration
st.set_page_config(
    layout="wide"
)

# Define the file path with regular spaces
path_to_html = "Logistic_regression.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Logistic Regression]")
    st.markdown(""" Hi guys. Welcome back. Till now we have understood how can one predict a value in future
    from a current value in the dataset. But what if we have a situation where we have to predict a class 
    from a current value in the dataset? Is it possible to classify an entity based on the current data? The 
    answer to all these questions lies in our next algorithm 'Logistic regression'. Before starting with 
    the algorithm, I would request you to download 'adult_new' dataset by clicking on the button 'Download CSV'
    below. That being said, let us start with Logistic Regression.""")
    
    df = pd.read_csv("adult_new.csv")
    
    def download_csv():
        df.to_csv("adult_new.csv", index=False)
        with open("adult_new.csv", "rb") as f:
            data = f.read()
        return data

    # Create a download button
    button_label = ":violet[Download CSV]"
    button_download = st.download_button(label=button_label, data=download_csv(), file_name='adult_new.csv', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    

    st.write("---")
    st.components.v1.html(html_data, width=800, height=27000)

    def download_notebook():
        with open("Logistic_Regression.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Logistic Regression' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Logistic_Regression.ipynb", mime='application/x-ipynb+json')
    
    

