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
path_to_html = "Support_Vector_Machine_(SVM).html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Support Vector Machine (SVM)]")
    st.markdown("""Hi guys. Today we are going to learn about 'Support Vector Machine' algorithm. SVM is a special kind of an algorithm which can be used to solve both classification & regression problems.
                   Today however, we are going to see how it goes ahead and does classification on a bank loan data. The bank loan zip dataset contains both risk train & risk test data. The data here is 
                   split already into train & test data, so we are not going to perform 'Train-test split' in today's session. The limitation of KNN is the fact that it works only on linearly separable data.
                   However, if we want to work on non-linearly separable data, by this I mean data which is distributed/scattered in such a way that it cannot be separated using a straight line then we make 
                   use of SVM. SVM operates well on sporadic/concentric data as it can properly separate data by using a hyperplane. Similar to KNN, we have hyperparameters here as well (namely kernel, C & gamma)
                   which can help us tune the model to achieve even better results. For now, I would request you to please download the 'risk_analytics' zip datatset that contains both the training and testing data 
                   on which we are going to perform SVM. Let's get started.""")
    
    def create_zip():
        with zipfile.ZipFile('risk_analytics.zip', 'w') as zipf:
            for root, dirs, files in os.walk('risk_analytics'):
                for file in files:
                    zipf.write(os.path.join(root, file), file)
        with open("risk_analytics.zip", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the zip file
    button_label_zip = ":violet[Download risk analytics dataset Zip]"
    button_download_zip = st.download_button(label=button_label_zip, data=create_zip(), file_name='risk_analytics.zip', mime='application/zip')

    st.write("---")
    st.components.v1.html(html_data, width=800, height=12500)

    def download_notebook():
        with open("Support_Vector_Machine_(SVM).ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Support Vector Machine (SVM)' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Support_Vector_Machine_(SVM).ipynb", mime='application/x-ipynb+json')
    