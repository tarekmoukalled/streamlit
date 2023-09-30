#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data  # Use st.cache_data instead of @st.cache
def load_data():
    df = pd.read_csv("Global-Superstore.csv", encoding='latin1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

df = load_data()

# Create a Streamlit app
st.title("Interactive Data Exploration")

# Sidebar for user interaction
st.sidebar.header("Filter Data")

# Filter by Category
selected_category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter by Sub-Category based on the selected category
sub_categories = df[df["Category"] == selected_category]["Sub-Category"].unique()
selected_sub_category = st.sidebar.selectbox("Select Sub-Category", sub_categories)

# Filter by Region
selected_region = st.sidebar.selectbox("Select Region", df["Region"].unique())

# Filter the data based on user selections
filtered_data = df[(df["Category"] == selected_category) &
                   (df["Sub-Category"] == selected_sub_category) &
                   (df["Region"] == selected_region)]

# Display filtered data in a table
st.write(f"Showing data for Category: {selected_category}, Sub-Category: {selected_sub_category}, Region: {selected_region}")
st.write(filtered_data)

# Create an interactive bar chart for Sales by City
st.subheader("Sales by City")
city_sales_data = filtered_data.groupby("City")["Sales"].sum().sort_values(ascending=False)
st.bar_chart(city_sales_data)

# Create a line plot to visualize sales over time
st.subheader("Sales Trend Over Time")
monthly_sales = filtered_data.resample('M', on='Order Date')['Sales'].sum().reset_index()

# Convert columns to NumPy arrays before indexing
ax.plot(monthly_sales['Order Date'].values, monthly_sales['Sales'].values, marker='o', linestyle='-')

ax.set_xlabel('Date')
ax.set_ylabel('Total Sales')
ax.set_title('Sales Trend Over Time')
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)

# Create a histogram for Shipping Cost
st.subheader("Shipping Cost Distribution")
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(filtered_data["Shipping Cost"], bins=20, edgecolor="k")
ax.set_xlabel("Shipping Cost")
ax.set_ylabel("Frequency")
ax.set_title("Shipping Cost Distribution")
st.pyplot(fig)
