# Customer Churn & MRR Loss Analytics Pipeline

An end-to-end data engineering and machine learning pipeline designed to process customer subscription data, analyze Monthly Recurring Revenue (MRR) loss, and predict churn risk using a calibrated Random Forest classifier.

## Key Features & Metrics

* **ETL Pipeline**: Processes 50,000 customer records, generating clean feature structures for analysis.
* **SQL Analytics**: Evaluates revenue vulnerability, contract-type churn distribution, and high-value customer loss using SQLite queries.
* **Machine Learning Model**: Implements a Random Forest Classifier with dynamic probability thresholding (0.4960) to optimize the retention budget.
* **Performance Metrics**:
  * **Precision**: 86.00% (Minimizes false positive discounts for loyal customers)
  * **Recall**: 75.00% (Captures high-risk churners effectively)
  * **Overall Accuracy**: 83.00%

## Tech Stack

* **Language**: Python 3.10+
* **Data Processing**: Pandas, NumPy
* **Machine Learning**: Scikit-Learn
* **Database**: SQLite3, SQL
* **Version Control**: Git, GitHub

## Repository Structure

```text
customer-churn-pipeline/
├── .gitignore               # Excludes database and cached files
├── etl_pipeline.py          # Generates and cleans 50,000 customer records
├── sql_queries.py          # SQLite connection and MRR analytical queries
├── train_model.py          # Random forest classifier with threshold tuning
└── README.md                # Project documentation