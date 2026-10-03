import sqlite3
import pandas as pd

print("Loading 50,000 record dataset into SQLite Database...")

# 1. Load dataset
df = pd.read_csv("cleaned_customer_churn.csv")

# 2. Store dataset into SQLite DB
conn = sqlite3.connect("churn_db.db")
df.to_sql("customers", conn, if_exists="replace", index=False)

print("Database updated! Executing SQL Analytics...\n")

# Query 1: MRR Breakdown and Revenue Loss by Customer Segment
q1 = """
SELECT 
    Customer_Segment,
    COUNT(*) AS Total_Customers,
    ROUND(SUM(MRR), 2) AS Total_MRR,
    ROUND(SUM(CASE WHEN Churn = 1 THEN MRR ELSE 0 END), 2) AS Lost_MRR,
    ROUND((SUM(CASE WHEN Churn = 1 THEN MRR ELSE 0 END) * 100.0 / SUM(MRR)), 2) AS Revenue_Loss_Pct
FROM customers
GROUP BY Customer_Segment;
"""
print("--- 1. Monthly Recurring Revenue (MRR) Loss Analysis ---")
print(pd.read_sql_query(q1, conn))
print("\n" + "="*65 + "\n")

# Query 2: Churn Metrics by Contract Type
q2 = """
SELECT 
    Contract_Type,
    COUNT(*) AS Total_Customers,
    SUM(Churn) AS Total_Churned,
    ROUND((SUM(Churn) * 100.0 / COUNT(*)), 2) AS Churn_Rate_Pct
FROM customers
GROUP BY Contract_Type
ORDER BY Churn_Rate_Pct DESC;
"""
print("--- 2. Churn Metrics by Contract Type ---")
print(pd.read_sql_query(q2, conn))

conn.close()