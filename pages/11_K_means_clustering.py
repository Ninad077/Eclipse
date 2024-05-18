import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd

# Set page configuration
st.set_page_config(
    layout="wide"
)

# Define the file path with regular spaces
path_to_html = "K_means.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[K-means clustering]")
    st.markdown("""Hi guys. Today we are going to learn the second type of Machine Learning algorithms which are called as Unsupervised algorithms. Unsupervised algorithms 
                   are those which work on unlabelled data. As in, we do not have 'y'(dependent column), we have only 'x' (independent columns) in the dataset. K-means 
                    clustering is the first unsupervised ML algorithm we are going to study. In this algorithm, we group the data into clusters one by one starting from k=1 
                    and go on computing a WCSS value. As we proceed further, we reach a point after which the value of WCSS almost saturates. This point is called as an 'elbow point' 
                    and the value of 'k' at elbow point gives us the optimal clusters. K-Means clustering is generally used for Customer segmentation/Customer clustering.          
                    Clustering is basically grouping of data into chunks. I know, I have used a lot of technical terms in the intro itself. Let me break down the concepts one by one 
                    in this session. Before that, I would request you to please download the 'Mall_Customers' data file on which we are going to perform k-means clustering. Having said 
                    that, let's get started.""")
    
    df = pd.read_csv("Mall_Customers.csv")
    
    def download_csv():
        df.to_csv("Mall_Customers.csv", index=False)
        with open("Mall_Customers.csv", "rb") as f:
            data = f.read()
        return data

    # Create a download button
    button_label = ":violet[Download CSV]"
    button_download = st.download_button(label=button_label, data=download_csv(), file_name='Mall_Customers.csv', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    st.write("---")
    st.components.v1.html(html_data, width=800, height=13600)

    def download_notebook():
        with open("K_means.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'K-means clustering' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="K_means.ipynb", mime='application/x-ipynb+json')
    