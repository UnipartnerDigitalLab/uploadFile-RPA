import streamlit as st
import pandas as pd
from io import StringIO

def main():
    st.title("Receive file")
    menu=["Home","Login","Signup"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader("Home")
    elif choice=="Login":
        st.subheader("Login Section")
        username=st.sidebar.text_input("Username")
        password=st.sidebar.text_input("Password",type='password')
        loginBox=st.sidebar.checkbox("Login")
        if loginBox:
            if password == '12345' and username=='admin':
                if st.sidebar.button("Logout!"):
                    username = ""
                st.success("Logged in as {}".format(username))
                task = st.selectbox("Task",["Another Task","Upload File"])
                if task=="Another Task":
                    st.subheader("Another Task")
                elif task=="Upload File":
                    st.subheader("Upload your file")
                    uploaded_file = st.file_uploader("Choose a file")
                    if uploaded_file is not None:
                        # To read file as bytes:
                        bytes_data = uploaded_file.getvalue()
                        st.write("Success")
            else:
                st.warning("Incorrect login data")

    elif choice=="Signup":
        st.subheader("Create New Account")

if __name__=='__main__':
    main()