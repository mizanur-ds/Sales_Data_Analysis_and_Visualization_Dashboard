# 📊 Sales_Data_Analysis_and_Visualization_Dashboard
### A Data Analysis Project with Streamlit Web App
This repository contains a Jupyter Notebook for data analysis and machine learning, along with a [Streamlit App](https://sales-data-analysis-and-visualisation.streamlit.app/) that provides an interactive user interface for the project.

## 📁 Contents
- Project.ipynb – Main notebook containing data loading, preprocessing, analysis, and modeling.

- project_streamlit.py – Streamlit app for user interaction (assumed filename; update if needed).

- requirements.txt – List of required Python packages (you can generate this).

- README.md – Project overview and instructions.

## 🚀 [Streamlit App](https://sales-data-analysis-and-visualisation.streamlit.app/)
The Streamlit web app allows users to interact with the project in a simple and intuitive way. It features:

- Data visualization and summary
- Model prediction or simulation
- User input for dynamic interaction

Running the Streamlit App Locally
   ```bash
   pip install -r requirements.txt
   Streamlit run project_streamlit.py
```

## 📘 Notebook Overview

This notebook provides a comprehensive analysis of sales data from a retail dataset. The main goals of the notebook include:

### 🔍 1. Data Loading & Initial Exploration
- Imported essential libraries: `pandas`, `numpy`, `matplotlib` and `seaborn`.
- Loaded the dataset using `pd.read_csv()`.
- Performed initial inspection using `head()`, `info()`, and `describe()` to understand structure, data types, and summary statistics.
- Reviewed column distributions such as:
  - Segment
  - Region
  - Category
  - Sub-Category
 
### 📅 2. Date Handling & Feature Engineering
- Converted `Order Date` and `Ship Date` to datetime format.
- Sorted the data based on `Order Date`.
- Extracted **Month** and **Year** from `Order Date` to enable temporal analysis.

### 📈 3. Time Series Analysis
- Created a time-indexed DataFrame to resample sales data.
- **Monthly Sales Trend** plotted using a line chart.
- Identified sales fluctuations and seasonal patterns across years.

### 📊 4. Sales Analysis by Groupings
- **Sales by Region**: Compared average and total sales.
- **Sales by Category**: Highlighted performance of product categories.
- **Sales by Sub-Category**: Identified high and low performers.
- Visualized using horizontal bar plots

### 🏆 5. Top Products Analysis
- Identified **Top 10 Products by Average Sales**.
- Visualized results using a colorful horizontal bar chart.


### 🌍 7. Regional Sales Trends Over Time
- Grouped sales by **Region** and time (monthly/yearly).
- Plotted:
  - Total Sales over Time by Region
  - Average Sales over Time by Region
- Used `seaborn.lineplot` for multi-line regional trends.

### 🧩 8. Interactive Dashboard with Widgets
- Built an interactive dashboard using `ipywidgets`.
- Users can filter data by:
  - Category
  - Region
  - Sub-Category
  - Segment
  - Date Range
- Dynamic plotting includes:
  - Sales trends over time
  - Total sales by various dimensions

---

### ✅ Key Insights
- Sales trend shows peaks during specific months (possible seasonality).
- **Office Supplies** dominate in volume and frequency.
- **West Region** leads in overall sales.
- **Binders**, **Paper**, and **Phones** are top-selling sub-categories.
- **Consumers** are the dominant customer segment.
