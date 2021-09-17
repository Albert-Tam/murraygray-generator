import streamlit as st
import requests

API_URL = "https://murraygray-server.herokuapp.com/"


def course_name(description):
    my_data = {"description": description}
    response = requests.post(API_URL + "course-name", json=my_data).json()
    return response["answer"]


st.title("Course Name Generator")
st.markdown("""### Transform descriptions into course names with the power of AI.""")
with st.form(key='course_name_from'):
    description = st.text_area(label="Course description.")
    submit = st.form_submit_button(label='Submit')
    if submit:
        output = course_name(description)
        st.markdown(output)



