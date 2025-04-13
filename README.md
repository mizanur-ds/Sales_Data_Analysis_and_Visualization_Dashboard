# 📊 Sales_Data_Analysis_and_Visualization_Dashboard
***A Data Analysis Project with Streamlit Web App***
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
<img src="https://github.com/user-attachments/assets/501fb005-2c75-4b06-b0a6-88741f898aaa" alt="Image Description" width="500" height="350"/>


### 📊 4. Sales Analysis by Groupings
- **Sales by Region**: Compared average and total sales.
- **Sales by Category**: Highlighted performance of product categories.
- **Sales by Sub-Category**: Identified high and low performers.
<img src="https://github.com/user-attachments/assets/42a6a0c0-c76a-4ec2-b33a-2cd00f89ab04" alt="Image Description" width="1000" height="350"/>
<img src="https://github.com/user-attachments/assets/f9951876-51cd-4421-b987-f667941d8644" alt="Image Description" width="1000" height="350"/>

### 🏆 5. Top Products Analysis
- Identified **Top 10 Products Total Sales**.
<img src="https://github.com/user-attachments/assets/14a1f723-25e3-4c36-97e2-47bff23001a7" alt="Image Description" width="1000" height="350"/>

### 👥 6. Customer Segmentation
- Analyzed the distribution of customer Segments.
<img src="https://github.com/user-attachments/assets/66eae895-9e95-46f9-b823-946ce1587dbc" alt="Image Description" width="500" height="350"/>

### 🌍 7. Regional Sales Trends Over Time
- Grouped sales by **Region** and time (monthly/yearly).
- Plotted:
  - Total Sales over Time by Region
  - Average Sales over Time by Region
<img src="https://github.com/user-attachments/assets/96783ef3-0a96-4a08-bd9a-43bf6386423f" alt="Image Description" width="1000" height="350"/>
<img src="https://github.com/user-attachments/assets/659e5b1f-969c-4a7b-b257-be73df5d7728" alt="Image Description" width="1000" height="350"/>

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
- **Technology** dominate in volume and frequency.
- **West Region** leads in overall sales.
- **Phones**, **Chair** and **Binders** are top-selling sub-categories.
- **Consumers** are the dominant customer segment.
---
## ✍️ Author
**Mizanur Rahman** – [GitHub](https://github.com/mizanur-ds) [Linkedin](https://www.linkedin.com/in/mizanur-rahman-953b2b217/)
