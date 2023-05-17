# TODO: Add docstrings and comments

import streamlit as st

import ncbi

st.title("Neglected Diagnostics: Perform Genetic Testing At Scale!")

datasource = st.selectbox("Select the datasource to search", ("NCBI", "BOLD"))

if datasource == "NCBI":
    database = st.selectbox("Select the database to search", ("gene", "nucleotide"))
    operation = st.selectbox("Select the operation to perform", ("Search", "Fetch"))
    term = st.text_input(
        label="Enter the search term",
        placeholder="Example: human[organism] AND topoisomerase[protein name]",
    )

    if st.button('Perform Operation'):
        data = ncbi.get(operation, database, term)
        st.write(data)

else:
    st.write("Selected BOLD")
