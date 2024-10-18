import streamlit as st
import json
from model import process_data

# Page 1: Upload Data
st.title("Data Upload Page")

uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    data = json.load(uploaded_file)

    result = process_data(data)
    st.session_state.result = result

    if st.button("Submit"):
        st.success("Data processed successfully! Go to Page 2 to see the results.")

# Page 2: Display Results
if "result" in st.session_state:
    st.title("Results:")

    flags = st.session_state.result["flags"]
    formatted_results = (
        f"**Rule 1:** TOTAL_REVENUE_5CR_FLAG: {flags['TOTAL_REVENUE_5CR_FLAG']}\n\n"
        f"**Rule 2:** BORROWING_TO_REVENUE_FLAG: {flags['BORROWING_TO_REVENUE_FLAG']}\n\n"
        f"**Rule 3:** ISCR_FLAG: {flags['ISCR_FLAG']}"
    )

    st.markdown(formatted_results)
else:
    st.warning("Please upload a JSON file on Page 1 first.")
