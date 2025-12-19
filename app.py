import streamlit as st
from summarize import summarize

st.title("📄 RAG Document Search & Summary")

query = st.text_input("Enter query")
length = st.selectbox("Summary length", ["short", "medium", "detailed"])

if st.button("Search"):
    st.write(summarize(query, length))
