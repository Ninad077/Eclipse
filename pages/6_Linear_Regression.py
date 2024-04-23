import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd

# Set page configuration
st.set_page_config(
    layout="wide"
)

# Define the file path with regular spaces
path_to_html = "Linear_Regression.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Linear Regression]")
    st.markdown(""" Hi guys. I hope you are excited to finally start with Machine Learning. Today marks our first day to learn
                    Machine Learning and I am thrilled to present you the first ML algorithm which goes by the name 'Linear Regression'. 
                    I would request you to  download the excel file 'advertising.csv' by clicking on the download button below. I would 
                    also appreciate if you code along with me by keeping your Jupyter notebook open as well. Follow the session from start 
                    to end diligently to understand the concepts better. At the end of each session, I would anyways allow you to download
                    the Jupyter notebooks I created for every topic. You could find a button at the bottom of every session page that says 
                    'Download jupyter notebook'.
                    Assuming that you are ready, let us start with Machine Learning.""")
    
    df = pd.read_csv("advertising.csv")
    
    def download_csv():
        df.to_csv("advertising.csv", index=False)
        with open("advertising.csv", "rb") as f:
            data = f.read()
        return data

    # Create a download button
    button_label = ":violet[Download CSV]"
    button_download = st.download_button(label=button_label, data=download_csv(), file_name='advertising.csv', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    

    st.write("---")
    st.components.v1.html(html_data, width=800, height=16500)

    def download_notebook():
        with open("Linear_Regression.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Linear Regression' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Linear_Regression.ipynb", mime='application/x-ipynb+json')
    
    st.markdown("""I have created an app which predicts Sales using Linear Regression.
                   Click on the link below to check it out.""")
    st.write("[Visit the app >](https://sales-prediction-app.onrender.com/)")

