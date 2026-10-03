# Customer Churn & MRR Loss Analytics Pipeline

An end-to-end data engineering, machine learning, and business intelligence pipeline designed to process customer subscription data, analyze Monthly Recurring Revenue (MRR) loss, and predict churn risk using a calibrated Random Forest classifier.

---

##  Interactive Power BI Dashboard

![Customer Churn Dashboard](./Screenshot%202026-10-04%20024147.png)

### Core Executive Metrics
* **Total Churned**: 24K Customers
* **Churn Rate**: 47.51%
* **MRR Loss**: $1.84M

### Key Business Insights
* **Primary Risk Driver**: Month-to-Month contracts account for the majority of overall churn (~77.8%), compared to <3% for Two-Year contracts.
* **Payment Behavior**: Revenue loss is evenly distributed across payment methods (~33% each for Electronic Check, Bank Transfer, and Credit Card).
* **Segment Distribution**: Churn affects High Value (12.1K) and Standard (11.7K) customer tiers equally, proving that contract terms—rather than customer tier—are the primary root cause.

---

##  Key Features & Pipeline Components

- **ETL Pipeline**: Processes 50,000 customer records, generating clean feature structures for analysis.
- **SQL Analytics**: Evaluates revenue vulnerability, contract-type churn distribution, and high-value customer loss using SQLite queries.
- **Machine Learning Model**: Implements a Random Forest Classifier with dynamic probability thresholding (0.4960) to optimize the retention budget.
- **Power BI Reporting**: Interactive executive report formatted in a balanced 3-column layout for fast decision-making.

---

##  ML Model Performance Metrics

- **Precision**: 86.00% (Minimizes false positive discounts for loyal customers)
- **Recall**: 75.00% (Captures high-risk churners effectively)
- **Overall Accuracy**: 83.00%

---

##  Tech Stack

- **Language**: Python 3.10+
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn
- **Database**: SQLite3, SQL
- **Visualization**: Power BI Desktop
- **Version Control**: Git, GitHub

---

## Repository Structure

```text
customer-churn-pipeline/
├── .gitignore                          # Excludes database and cached files
├── Customer_Churn_Analysis_Dashboard.pbix # Interactive Power BI report
├── Screenshot 2026-10-04 024147.png    # Preview image for README documentation
├── etl_pipeline.py                     # Generates and cleans 50,000 customer records
├── sql_queries.py                     # SQLite connection and MRR analytical queries
├── train_model.py                     # Random forest classifier with threshold tuning
└── README.md                          # Comprehensive project documentation
