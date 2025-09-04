📊 Data Analysis with Pandas & Visualization with Matplotlib
📌 Project Overview

This project demonstrates how to analyze and visualize data using Pandas, Matplotlib, and Seaborn in Python.
The Iris dataset is used as an example, but the workflow can be applied to any CSV dataset.

The analysis covers:

Loading and exploring the dataset

Handling missing data

Performing descriptive statistics and grouping

Creating different visualizations (line chart, bar chart, histogram, scatter plot)

Observing insights from the analysis

📂 Project Structure
├── data_analysis.ipynb   # Jupyter Notebook containing the full analysis
├── data_analysis.py      # Python script version (optional)
├── README.md             # Project documentation

⚙️ Requirements

Make sure you have Python 3 installed with the following libraries:

pip install pandas matplotlib seaborn scikit-learn

🚀 How to Run
Option 1: Run Jupyter Notebook

Open the notebook:

jupyter notebook data_analysis.ipynb


Run each cell step by step.

Option 2: Run Python Script

Execute the script directly:

python data_analysis.py

📊 Tasks Completed
Task 1: Load and Explore the Dataset

Loaded the Iris dataset using sklearn.datasets.

Displayed the first rows (.head()).

Checked data types and missing values.

Dataset was clean (no missing values).

Task 2: Basic Data Analysis

Computed descriptive statistics with .describe().

Grouped data by species and calculated mean values.

Found key differences among Setosa, Versicolor, and Virginica.

Task 3: Data Visualization

Line Chart – Petal length trend across samples.

Bar Chart – Average petal length per species.

Histogram – Distribution of sepal length.

Scatter Plot – Relationship between sepal length and petal length.

📌 Findings & Observations

Setosa has much smaller petal length and width compared to other species.

Virginica generally has the largest flower dimensions.

Sepal length and petal length are strongly correlated.

The dataset was already clean, but real-world data often requires handling missing values.

🛠 Error Handling

Implemented error handling for missing files (try/except FileNotFoundError).

✅ Submission Checklist

 Data loading & cleaning

 Summary statistics

 Grouped analysis

 Four different types of plots

 Error handling

 Findings & insights
