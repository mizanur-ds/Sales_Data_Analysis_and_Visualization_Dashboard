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

## 📘 Notebook Overview

This notebook provides a comprehensive analysis of sales data from a retail dataset. The main goals of the notebook include:

### 🔍 1. Data Loading & Initial Exploration
- Imported essential libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, and `warnings`.
- Loaded the dataset using `pd.read_csv()`.
- Performed initial inspection using `head()`, `info()`, and `describe()` to understand structure, data types, and summary statistics.
- Reviewed column distributions such as:
  - Segment
  - Region
  - Category
  - Sub-Category
