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
path_to_html = "Time_series_analysis.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Time Series Analysis using Exponential Smoothing & ARIMA]")
    st.markdown("""Hi guys. Welcome to the session. Today we are going to learn 3rd type of Machine Learning algorithm which is Reinforcement Machine Learning or populary known as 'Time Series Analysis'.
                    This Time Series Analysis is going to be done using Exponential Smoothing & ARIMA model. Time Series analysis is generally used on continuous data. This analysis is mostly 
                    used for forecasting a value. There's a thin difference between prediction & forecasting. Prediction is a strong hypothesis one does using independent columns, whereas 
                    forecast is a mere weak prediction on dependent column. Here we use a previous value of the dependent column itself to forecast it's value in the future. So Time series analysis 
                    is generally used to forecast the values of weather or stock prices or mostly continuous data. For now, I would request you to please download the dataset of 'Sample Superstore' 
                    and start working with me. Also in the notebook I have read '.xls' file since the original dataset was in '.xls' extension. So while reading please use the syntax:  
                  **df = pd.read_excel(r"Sample_Superstore.xlsx",header = 0)**. Time series analysis is a big file, so the webpage might take a while to load. 
                    Please have patience :)""")
    
   
   

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
