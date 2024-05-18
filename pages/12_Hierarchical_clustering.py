import streamlit as st
import streamlit.components.v1 as components
import os  # Import the os module
import pandas as pd

# Set page configuration
st.set_page_config(
    layout="wide"
)

# Define the file path with regular spaces
path_to_html = "Hierarchical_clustering.html"

# Check if the HTML file exists
if not os.path.exists(path_to_html):
    st.error("HTML file not found!")
else:
    # Read HTML content
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    # Show HTML content
    st.header(":violet[Hierarchical clustering]")
    st.markdown("""Hi guys. Let us proceed with the Unsupervised Machine learning algorithms. Today we are going to learn another clustering algorithm
                   which goes by the name 'Hierarchical clustering'. The concept of Hierarchical clustering is sightly different but the purpose of 'customer 
                   segmentation' is same here. In contrast to K-means, where we make use of 'elbow method' to compute optimal clusters, here we make use of a
                   'dendrogram'. We are going to understand one of the types of Hierarchical clustering named 'Agglomerative Hierarchical clustering' a little 
                    more elaborately. I would like you to imagine this algorithm as the concept of 'nuclear fusion' where two atoms combine together due to 
                    electronic affinity to form one single nucleus, likewise in Agglomerative clustering different clusters combine to form a unified cluster. 
                    The electronic affinity here would be the 'Euclidean' distance which is used to combine two different clusters. Smaller distances would form 
                    clusters first. Still unclear? Let me explain it concept by concept. Before that, as a ritual please do not forget to download 'google_review_ratings' 
                    dataset on which we are going to perform Hierarchical clustering. Enough of beating around the bush, let's get started.""")
    
    df = pd.read_csv("google_review_ratings.csv")
    
    def download_csv():
        df.to_csv("google_review_ratings.csv", index=False)
        with open("google_review_ratings.csv", "rb") as f:
            data = f.read()
        return data

    # Create a download button
    button_label = ":violet[Download CSV]"
    button_download = st.download_button(label=button_label, data=download_csv(), file_name='google_review_ratings.csv', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    st.write("---")
    st.components.v1.html(html_data, width=800, height=16370)

    def download_notebook():
        with open("Hierarchical_clustering.ipynb", "rb") as f:
            data = f.read()
        return data

    # Create a download button for the notebook
    st.write("----")
    st.write("To download 'Hierarchical clustering' Jupyter notebook click on the button below.")
    button_label = ":violet[Download Jupyter Notebook]"
    button_download = st.download_button(label=button_label, data=download_notebook(), file_name="Hierarchical_clustering.ipynb", mime='application/x-ipynb+json')
    