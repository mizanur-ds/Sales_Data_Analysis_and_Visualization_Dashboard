import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Load data
df = pd.read_csv(r"E:\Self Project\data set\train.csv")

# Data Preparation
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)
df = df.sort_values(by='Order Date', ascending=True)

df['Month'] = df['Order Date'].dt.strftime('%B')
df['Year'] = df['Order Date'].dt.year

# Sidebar Filters
st.sidebar.header('Filters')
category = st.sidebar.selectbox('Category', ['All'] + list(df['Category'].unique()))
region = st.sidebar.selectbox('Region', ['All'] + list(df['Region'].unique()))
sub_category = st.sidebar.selectbox('Sub-Category', ['All'] + list(df['Sub-Category'].unique()))
segment = st.sidebar.selectbox('Segment', ['All'] + list(df['Segment'].unique()))
start_date = st.sidebar.date_input('Start Date', df['Order Date'].min().date())
end_date = st.sidebar.date_input('End Date', df['Order Date'].max().date())
time_interval = st.sidebar.selectbox('Time Interval',['Week','Month','Year'])

# Filter Data
def filter_data():
    filtered_data = df.copy()
    if category != 'All':
        filtered_data = filtered_data[filtered_data['Category'] == category]
    if region != 'All':
        filtered_data = filtered_data[filtered_data['Region'] == region]
    if sub_category != 'All':
        filtered_data = filtered_data[filtered_data['Sub-Category'] == sub_category]
    if segment != 'All':
        filtered_data = filtered_data[filtered_data['Segment'] == segment]
    filtered_data = filtered_data[
        (filtered_data['Order Date'] >= pd.to_datetime(start_date)) &
        (filtered_data['Order Date'] <= pd.to_datetime(end_date))
    ]
    return filtered_data

filtered_data = filter_data()

# Dataset Overview
st.header('Dataset Overview')
st.write(df.head())

# Sales Trend Plot
st.header('Sales Trend')
period = 'M' if time_interval == 'Month' else 'Y' if time_interval == 'Year' else 'W'
sales_trend = filtered_data.groupby(filtered_data['Order Date'].dt.to_period(period))['Sales'].sum().reset_index()
sales_trend['Order Date'] = sales_trend['Order Date'].dt.to_timestamp()
plt.figure(figsize=(10, 5))
sns.lineplot(data=sales_trend, x='Order Date', y='Sales')
plt.title(f'Sales Trend (Category: {category}, Region: {region})')
plt.xticks(rotation=45)
plt.grid(True)
st.pyplot(plt)

# Sales Breakdown
st.header('Sales Breakdown')
fig, axes = plt.subplots(4, 1, figsize=(8, 12))

for group, values in filtered_data.groupby('Region'):
    axes[0].barh(group, values['Sales'].sum())
    axes[0].set_title('Total Sales by Region')

for group, values in filtered_data.groupby('Category'):
    axes[1].barh(group, values['Sales'].sum())
    axes[1].set_title('Total Sales by Category')

for group, values in filtered_data.groupby('Sub-Category'):
    axes[2].barh(group, values['Sales'].sum())
    axes[2].set_title('Total Sales by Sub-Category')

count_segment = filtered_data['Segment'].value_counts()
axes[3].bar(count_segment.index, count_segment.values)
axes[3].set_title("Segment Distribution")

plt.tight_layout()
st.pyplot(fig)

