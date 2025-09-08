# ========================================================
# Assignment: Analyzing Data with Pandas & Visualizing Results with Matplotlib
# ========================================================

# Task 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ------------------------------
# Task 1: Load and Explore Dataset
# ------------------------------

try:
    # Load Iris dataset
    iris = load_iris(as_frame=True)
    df = iris.frame

    # Display first rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Dataset info
    print("\nDataset Information:")
    print(df.info())

    # Check for missing values
    print("\nMissing Values Check:")
    print(df.isnull().sum())

    # If there were missing values, handle them (example: drop missing values)
    df = df.dropna()

except FileNotFoundError:
    print("Error: Dataset file not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")

# ------------------------------
# Task 2: Basic Data Analysis
# ------------------------------

# Compute descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Add categorical labels for species
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

# Grouping by species and computing mean values
grouped = df.groupby("species").mean()
print("\nMean of numerical features grouped by species:")
print(grouped)

# Findings:
# - Setosa has the smallest petal length and width.
# - Virginica has the largest dimensions overall.
# - Sepal and petal length appear correlated.

# ------------------------------
# Task 3: Data Visualization
# ------------------------------

# 1. Line Chart - Trend of Petal Lengths Across Samples
plt.figure(figsize=(8, 5))
plt.plot(sorted(df["petal length (cm)"].values))
plt.title("Trend of Petal Lengths Across Samples")
plt.xlabel("Sample Index (sorted)")
plt.ylabel("Petal Length (cm)")
plt.grid(True)
plt.show()

# 2. Bar Chart - Average Petal Length by Species
plt.figure(figsize=(8, 5))
df.groupby("species")["petal length (cm)"].mean().plot(
    kind="bar", color=["#4daf4a", "#377eb8", "#e41a1c"]
)
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram - Distribution of Sepal Length
plt.figure(figsize=(8, 5))
plt.hist(df["sepal length (cm)"], bins=20, edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="sepal length (cm)",
    y="petal length (cm)",
    hue="species",
    palette="deep",
    s=70
)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# ------------------------------
# Findings & Observations
# ------------------------------
print("\nFindings & Observations:")
print("- Setosa species has significantly smaller petal dimensions.")
print("- Virginica has the largest petal and sepal measurements.")
print("- Sepal length and petal length are positively correlated.")
print("- Dataset is clean (no missing values).")
