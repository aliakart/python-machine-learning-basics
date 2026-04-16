# Python Data Analysis & Machine Learning

This repository contains a collection of Python scripts demonstrating foundational data analysis and machine learning techniques. The projects progress from basic exploratory data analysis (EDA) to unsupervised and supervised machine learning algorithms using Pandas, Matplotlib, and Scikit-Learn.

## Projects Overview

### Task 1: Structure and Correlation Analysis
Located in `task1-analysis/`
- Performs Exploratory Data Analysis (EDA) on the dataset.
- Calculates descriptive statistics (mean, median, standard deviation, quartiles).
- Visualizes data distributions using histograms and boxplots.
- Analyzes feature correlations using scatter plots and linear regression fitting (calculating Pearson correlation coefficients).

### Task 2: Clustering (Unsupervised Learning)
Located in `task2-clustering/`
- Implements the K-Means clustering algorithm to group unlabeled data.
- Standardizes features using `StandardScaler` for distance-based accuracy.
- Utilizes the Elbow Method (WCSS calculation) to determine the optimal number of clusters (k).
- Visualizes the resulting clusters and their centroids across different feature dimensions.

### Task 3: Classification (Supervised Learning)
Located in `task3-classification/`
- Implements the K-Nearest Neighbors (KNN) algorithm for multi-class classification.
- Evaluates model accuracy across different values of 'k' to find the optimal hyperparameter.
- Generates Confusion Matrices to analyze the true vs. predicted class distributions.
- Compares classification performance using the full 4D feature space versus 2D subsets.

## Technologies Used
- **Language:** Python
- **Data Manipulation:** NumPy, Pandas
- **Machine Learning:** Scikit-Learn
- **Data Visualization:** Matplotlib

## How to Run

1. Clone the repository.
2. Ensure you have the required libraries installed:
   pip install numpy pandas matplotlib scikit-learn
3. Navigate to the respective task directory and run the script:
   python main.py

## License
This project is for educational purposes.
