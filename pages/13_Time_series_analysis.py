import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd
import xlwt

# Set page configuration
st.set_page_config(
    layout="wide"
)

# Define the file path with regular spaces
path_to_html = "C:/Users/ninad/Eclipse/Time_series_analysis.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Time Series Analysis using Exponential Smoothing & ARIMA]")
    st.markdown("""Hi guys. Welcome to the session. Today we are going to learn Time Series Analysis
                    using Exponential Smoothing & ARIMA model. I would request you to download the 
                    dataset of 'Sample Superstore' and start working with me.
                    Also in the notebook I have read '.xls' file since the original dataset was in 
                    '.xls' extension. So while reading use the syntax
                      **df = pd.read_excel(r"Sample_Superstore.xlsx",header = 0)**""")
    
   
   

# Read the xls file
df = pd.read_excel("Sample_Superstore.xlsx")

# Define a function to download the Excel file
def download_excel():
    # Write the DataFrame to an Excel file using xlwt
    df.to_excel("Sample_Superstore.xlsx", index=False)
    # Read the Excel file as binary data
    with open("Sample_Superstore.xlsx", "rb") as f:
        data = f.read()
    return data

# Create a download button
button_label = ":violet[Download xlsx]"
button_download = st.download_button(label=button_label, data=download_excel(), file_name='Sample_Superstore.xlsx', mime='application/vnd.ms-excel')



st.write("---")
st.components.v1.html(html_data, width=800, height=27570)

def download_notebook():
        with open("Time_series_analysis.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
st.write("----")
st.write("To download 'Time series analysis' Jupyter notebook click on the button below.")
button_label = ":violet[Download Jupyter Notebook]"
button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Time_series_analysis.ipynb", mime='application/x-ipynb+json')
