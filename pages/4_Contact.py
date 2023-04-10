import os.path
import streamlit as st
import  base64
import webbrowser
import urllib3

def page():
    return st.set_page_config(
         page_title="My First Web App",
         page_icon=":shark:",
         layout="wide",
         initial_sidebar_state="expanded",
         menu_items={
             'Get Help': 'https://www.extremelycoolapp.com/help',
             'Report a bug': "https://www.extremelycoolapp.com/bug",
             'About': "# This is a header. This is an *extremely* cool app!"

         }
     )

page()


with st.sidebar:
    select = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )

with st.container():

    def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="820" height="680" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)


    st.markdown("<h1 style='text-align: center; '> My Certificates </h1>",
                unsafe_allow_html=True)

    st.write("#")
    st.write("#")


    with st.expander("Python Zero to Mastery Certificate - Udemy"):

        st.balloons()
        st.write('''
        More information about the certification. 
        ''')
        col3, col1, col2 = st.columns([1, 4, 1])
        with col1:
            show_pdf(os.path.join('Certificates','python_ztm.pdf'))

        '---'
        with col2:
            if st.button('Validate this Certificate! ',key='ztm'):
                webbrowser.open_new_tab(url='https://www.udemy.com/certificate/UC-90653b4c-a49d-40f2-80d2-b43b3e14c563/')
            else:
                pass


    '---'

    with st.expander("Python and SQL for Data Science - Scaler"):
        st.balloons()
        st.write('''
        More information about the certification. 
        ''')
        '---'
        col3, col1, col2 = st.columns([1, 4, 1])
        with col1:
            show_pdf(os.path.join('Certificates','python_scaler.pdf'))

        '---'
        with col2:
            if st.button('Validate this Certificate! ',key='scaler'):
                webbrowser.open_new_tab(url='https://moonshot.scaler.com/s/sl/QQZTt-z4He')
            else:
                pass

    google = 'https://google.com'

    if st.button('Google ',key='google'):
        webbrowser.open_new_tab(url=google)
    else:
        pass

    st.markdown(f'''
    <a href={google}><button style="background-color:GreenYellow;">Stackoverflow</button></a>
    ''',
                unsafe_allow_html=True)