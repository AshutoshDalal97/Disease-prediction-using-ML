🩺 Disease Prediction System using Machine Learning
📌 Overview

This project builds a machine learning-based disease prediction system that predicts the most probable disease based on user-selected symptoms.

The system:

Collects disease–symptom data from Wikipedia
Cleans and processes the data
Converts symptoms into a structured feature matrix
Trains ML models
Predicts diseases with probability scores (descending order)
🎯 Objective

To create a system that:

Takes symptoms as input
Predicts possible diseases
Outputs probabilities for each disease
Helps in early-stage diagnostic assistance

📊 Dataset Creation

🔹 Source
Data collected from https://medlineplus.gov website

🔹 Steps Involved

Disease Selection
Started with common human diseases 

Web Scraping

Extracted symptoms using requests + BeautifulSoup

Data Cleaning

Converted text to lowercase
Split symptoms using delimiters (,, and, ;)
Normalization
Also some manual corrections in csv file


Data Augmentation

Since the dataset had:

❌ Only one row per disease

We applied augmentation:

Randomly removed symptoms
Generated multiple samples per disease

👉 This simulates real-world variability


# Model Training
Models Tested:
Logistic Regression
Support Vector Machine (SVM)
Random Forest
Decision Tree
Extensive Tree
Gradient Boosting
XGB

Best Model: SVM


Model Evaluation

Train-test split (80/20)
Stratified sampling
Accuracy and classification metrics
Cross-validation

⚠️ Limitations
Dataset is synthetic + scraped
Not medically validated
Predictions are approximate
Not suitable for real clinical use

🛠️ Tech Stack
Python
Pandas
NumPy
Scikit-learn
BeautifulSoup
Requests

📂 Project Structure
├── data/
│   └── disease_dataset.csv
├── notebooks/
│   └── model_training.ipynb
├── src/
│   ├── scraper.py
│   ├── preprocessing.py
│   ├── model.py
│   └── predict.py
├── README.md

👨‍💻 Author

Ashutosh Dalal