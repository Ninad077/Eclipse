import streamlit as st
import webbrowser as web
import streamlit.components.v1 as components
from st_pages import Page, Section, show_pages, add_page_title
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title=":violet[Eclipse]",layout="wide"
)

st.subheader(":violet[Select a section to study:]")


selected_page = option_menu(
                                menu_title="",
                                options=["Preprocessing","Supervised ML","Unsupervised ML",
                                         "Reinforcement ML","Deep Learning"],
                                orientation= "horizontal",
                        
                            )


if selected_page == "Preprocessing":
       show_pages(
               [
        Page("app.py", "Eclipse",""),

        # Preprocessing Section
        Page("pages/0_Jupyter_Notebook_Installation.py","Jupyter Notebook Installation", icon="🐍"),
        Page("pages/1_Jupyter_Notebook_Introduction.py","Jupyter notebook Introduction", icon="🐍"),
        Page("pages/2_Python_basics.py","Python basics", icon="🐍"),
        Page("pages/3_Null_value_treatment.py","Null value treatment", icon="🐍"),
        Page("pages/4_EDA.py","Exploratory Data Analysis", icon="🐍"),
        Page("pages/5_Outliers_and_Correlation.py","Outliers & Correlation", icon="🐍"),


        Page("pages/Contact_me.py", in_section=False),
    ]
)

elif selected_page == "Supervised ML":
      show_pages(
    [
        Page("app.py", "Eclipse",""),

        # Supervised ML section
        Page("pages/6_Linear_Regression.py","Linear Regression", icon="📈"),
        Page("pages/7_Logistic_Regression.py","Logistic Regression", icon="📈"),
        Page("pages/8_KNN.py","KNN", icon="📈"),
        Page("pages/9_Support_Vector_Machine.py","Support Vector Machine", icon="📈"),
        Page("pages/10_Decision_Tree.py","Decision Tree", icon="📈"),

        Page("pages/Contact_me.py", in_section=False),
    ]
)
elif selected_page == "Unsupervised ML":
        show_pages(
    [
        Page("app.py", "Eclipse",""),

         # Unupervised ML section
        Page("pages/11_K_means_clustering.py","K means clustering", icon="🧿"),
        Page("pages/12_Hierarchical_clustering.py","Hierarchical clustering", icon="🧿"),

        Page("pages/Contact_me.py", in_section=False),
    ]
)
elif selected_page == "Reinforcement ML":
        show_pages(
    [
        Page("app.py", "Eclipse",""),

         # Unupervised ML section
        Page("pages/13_Time_series_analysis.py","Time Series Analysis", icon="🧿"),

        Page("pages/Contact_me.py", in_section=False),
    ]
)
elif selected_page == "Deep Learning":
        show_pages(
    [
        Page("app.py", "Eclipse",""),

        # Deep Learning section
        Page("pages/14_Artificial_Neural_Networks.py","Artificial Neural Networks", icon="🧠"),
        Page("pages/15_CNN.py","Convolutional Neural Networks", icon="🧠"),

        Page("pages/Contact_me.py", in_section=False),
    ]
)

# Either this or add_indentation() MUST be called on each page in your
# app to add indendation in the sidebar
add_page_title()


# Title and image
st.image("Eclipse_logo.png")
st.write("---")
st.markdown("""Hi, Ninad here. Eclipse is an open source web application designed by me to teach 
Machine Learning. It spans through core Python, Preprocessing & Machine Learning models step
by step in a way that even a layman would understand. Rest assured,I have tried to break down 
complex concepts with simple examples so that the user gets a clear picture of everything. 
I would recommend the user to start following the course from the first session and follow
it religiously till the last one. To make things easy for the user I have divided the lecture
series into multiple sections namely Preprocessing, Supervised ML, Unsupervised ML, Deep Learning.
            
I have enclosed the essential datasets and Jupyter notebooks in every session so that people can
refer and practice on their own comfort at home. We would be using Jupyter notebooks to code and 
the language used is Python. I would walk you through Jupyter notebook installation and make 
you familiar with Jupyter notebook environment on Anaconda navigator. For now, I would just like 
you to have 2 prerequisites. Funny enough,those two prerequisites have nothing to do with 
technology and they are: **Passion & curiosity**. Be passionate & be curious about the things to 
learn. Don't be intimidated if you don't understand something. Machine learning requires practice 
and with time you would be proficient. My only advice is to make your foundations about the core 
concepts very clear which would prepare you to learn more advanced concepts in future with ease.
I have kept this application open source because in the era of MOOCs which do charge subscription,
I  don't want to make money an impediment for someone who has the zeal within him or her to learn 
something new. 

For any query related to Machine Learning feel free to text me in the Query box below. 
To get started, select a Section from the navigation bar above and follow the lecture series
listed in the sidebar (extreme left of your screen).
            
Hope you will have fun!
            
Happy Learning :)""")
st.write("---")
st.subheader(":mailbox: :violet[Query box]") 
contact_form = """<form action="https://formsubmit.co/ninadmandavkar28@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder= "Your name" required>
    <input type="email" name="email" placeholder= "Your email" required>
    <textarea name="message" placeholder="Your message"></textarea>
    <button type=":submit">Send</button>
    </form>"""

st.markdown(contact_form,unsafe_allow_html=True)

def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css.txt")
components.html("""<div><a href="https://github.com/Ninad077" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" target="_blank"></a>
                        <a href="https://www.linkedin.com/in/ninad-s-mandavkar-12328715b" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
                        <a href="https://medium.com/@ninadmandavkar28" target="blank"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="35" fill="currentColor" class="bi bi-medium" viewBox="0 0 16 16"><path d="M9.025 8c0 
                        2.485-2.02 4.5-4.513 4.5A4.506 4.506 0 0 1 0 8c0-2.486 2.02-4.5 4.512-4.5A4.506 4.506 0 0 1 9.025 8m4.95 0c0 2.34-1.01 4.236-2.256 4.236S9.463 10.339 9.463 8c0-2.34 1.01-4.236 2.256-4.236S13.975 5.661 13.975 
                        8M16 8c0 2.096-.355 3.795-.794 3.795-.438 0-.793-1.7-.793-3.795 0-2.096.355-3.795.794-3.795.438 0 .793 1.699.793 3.795"/></svg></div>""")
