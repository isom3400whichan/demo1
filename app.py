import streamlit as st
import pandas as pd
import os

st.title("Retail Business Dashboard")

st.header("Manager Input Section")

st.write("Please enter the monthly sales target and select the region.")

st.number_input("Enter Monthly Sales Target (in USD):",
                min_value = 0,
                max_value = 100000000
                value =50000)

st.selectbox("Select Region:", 
             ["North", "South", "East", "West"]

if st.button("Submit"):
              st.button("Submitted!")

st.success("Dashboard updated successfully!")
