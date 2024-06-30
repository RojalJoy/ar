import streamlit as st
import os

# Function to read HTML file
def get_html_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# Set the title of the Streamlit app
st.title("AR Session in Streamlit")

# Embed the HTML content
st.components.v1.html(get_html_file("ar.html"), height=600, width=800)
