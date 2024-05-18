import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd

# Set page configuration
st.set_page_config(
    layout="wide"
)

# Define the file path with regular spaces
path_to_html = "Sentiment_Analysis.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[NLP - Sentiment Analysis]")
    st.markdown("""Hi guys. Now that you know how TFIDF (Term Frequency Inverse Document Frequency) algorithm works, it is about time for you to
                   understand how to perform 'sentiment analysis'. For those who are guessing, yes it is exactly as it sounds. In Sentiment analysis,
                   we are trying to interpret the mood or the sentiment of a sentence. The most common usecase of sentiment anaylsis would be product 
                   review portals on the websites where consumers post their feedbacks. These feedbacks are generally high in volume and hence to process
                   and interpret each one of them backend developers generally use 'sentiment analysis'. The core working principle relies heavily on Tfidf 
                   and Logistic Regression in pipleine. Let us start working straight away to understand the concept much better. Don't forget to 
                   download 'train.csv' dataset below.""")
    
    df = pd.read_csv("train.csv")
    
    def download_csv():
        df.to_csv("train.csv", index=False)
        with open("train.csv", "rb") as f:
            data = f.read()
        return data

    # Create a download button
    button_label = ":violet[Download CSV]"
    button_download = st.download_button(label=button_label, data=download_csv(), file_name='train.csv', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    st.write("---")
    st.components.v1.html(html_data, width=800, height=8500)

    def download_notebook():
        with open("Sentiment_analysis.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Sentiment Analysis' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Sentiment_analysis.ipynb", mime='application/x-ipynb+json')
    