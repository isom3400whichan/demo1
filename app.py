import streamlit as st
import time

# 1. Dashboard Title and Objective
# TODO: Add title and description
st.title("Business Performance Dashboard")
st.write("Description blah blah blah")

# 2. Columns Layout
# TODO: Display Q1, Q2, Q3 revenue in columns
col1, col2, col3 = st.columns(3)
with col1: 
  st.header("Q1 2024")
  st.write("Revenue: $1.2M")

with col2: 
  st.header("Q2 2024")
  st.write("Revenue: $1.5M")

with col3: 
  st.header("Q3 2024")
  st.write("Revenue: $1.3M")
  
# 3. Tabs
# TODO: Create tabs for Sales Data, Customer Insights, Market Trends
tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])
with tab1:
  st.write("Sales Data")
  sales_data = {
    'Q1 2024': "$1.2M",
    'Q2 2024': "$1.5M",
    'Q3 2024': "$1.3M",
    'Q4 2024': "TBC"
    }
  for quarters, revenue in sales_data.items():
    st.write(f'{quarters}, {revenue}')

# 4. Expander
# TODO: Add expander for additional info
st.expander("More Information")
st.write("Info on data collection")

# 5. Dynamic Loading
# TODO: Simulate loading and display insights
placeholder = st.empty()

for i in range(5):
  placeholder.write(f"Loading data... {100/(5-i)}% complete")
  time.sleep(1)

placeholder.write("Loading completed")


# 6. Interactivity
# TODO: Add selectbox and slider for revenue adjustment

# 7. Bonus
# TODO: Add bar chart and motivational button
