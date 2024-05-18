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
path_to_html = "KNN.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[K-Nearest Neighbours (KNN)]")
    st.markdown("""Hi guys. As of now, we have studied one classification algorithm 'Logistic Regression', which was capable enough to classify the data into 2 classes (i.e. binary classification),
                   but what if we want to classify the data into more than 2 classes? Is there an algorithm which is capable to perform 'multi-class classification'? The answer to this question lies
                   in our next algorithm which goes by the name 'K-Nearest Neighbours' or popularly known as 'KNN'. To give a brief introduction about KNN, it basically uses the metric Euclidean distance 
                   of the k nearest neighbours to classify co-ordinates into classes. 'k' here is a hyperparameter and it can be controlled manually. For now I would request you to 
                   download the 'fish_dataset_updated' zip file. It has 2 csv files. 'Fish_dataset' is the one we use for Underfitting problem, whereas 'fish_dataset_updated' file is for the Overfitting problem.
                   Underfitting & Overfitting is one of the most important concepts in Machine Learning and hence I would request you guys to go through this session thoroughly. There have been ample of definitions 
                   of Underfitting & Overfitting on Internet that might confuse you, but let me define it as a funny example so that you guys could remember it for a lifetime. So, Underfitting I would define as a
                   student who does not study well in the exam and hence fails miserably in the test, whereas Overfitting is a student who studies on the same exam pattern so much so that when an exam paper is set with
                   a different pattern and questions he/she fails to perform on the test. To give you the technical definitions, "**Underfitting is performing poor on training data & hence on testing data as well, whereas 
                   Overfitting means performing too much on training data that it cannot handle variations and hence poor performance on testing data.**" So data should  neither be 'Overfitted nor 'Underfitted' it
                   should be 'optimally fitted'. Just like the way a student should neither give up on preparation nor he/she should mug up the concepts, he/she should always understand the concepts and try to express them 
                   in their own words in the test. I guess I preached too much. Enough of the talks, let's start with the session.""")
    
    
    
    def create_zip():
        with zipfile.ZipFile('fish_dataset_updated.zip', 'w') as zipf:
            for root, dirs, files in os.walk('fish_dataset_updated'):
                for file in files:
                    zipf.write(os.path.join(root, file), file)
        with open("fish_dataset_updated.zip", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the zip file
    button_label_zip = ":violet[Download fish dataset Zip]"
    button_download_zip = st.download_button(label=button_label_zip, data=create_zip(), file_name='fish_dataset_updated.zip', mime='application/zip')
    


    st.write("---")
    st.components.v1.html(html_data, width=800, height=25500)

    def download_notebook():
        with open("KNN.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'K Nearest Neighbours' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="KNN.ipynb", mime='application/x-ipynb+json')
    
  