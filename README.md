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
Data collected from Wikipedia disease pages
Symptoms extracted from infobox ("Symptoms")
🔹 Steps Involved
Disease Selection
Started with common human diseases (20–50)
Expanded using curated lists
Web Scraping
Extracted symptoms using requests + BeautifulSoup
Data Cleaning
Removed references [1], [2]
Converted text to lowercase
Split symptoms using delimiters (,, and, ;)
Normalization

Converted symptoms into standard format:

"high fever" → "high_fever"
Noise Removal

Removed words like:

may, can, often, usually


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

Best Model: Random Forest

Why?

Handles binary features well
Works with small datasets
Captures non-linear relationships

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