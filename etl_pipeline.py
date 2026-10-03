import pandas as pd
import numpy as np

print("Generating 50,000 Cleaned Customer Records...")
np.random.seed(42)
n_samples = 50000

tenure = np.random.randint(1, 72, n_samples)
monthly_charges = np.round(np.random.uniform(20.0, 120.0, n_samples), 2)
contract = np.random.choice(['Month-to-Month', 'One Year', 'Two Year'], n_samples, p=[0.5, 0.3, 0.2])

# Calibrated signal for high signal-to-noise ratio
score = (
    (contract == 'Month-to-Month') * 3.6 +
    (monthly_charges > 68) * 2.65 +
    (tenure < 15) * 3.15 -
    (contract == 'Two Year') * 3.6
)
prob = 1 / (1 + np.exp(-(score - 3.6)))
churn = np.random.binomial(1, prob)

data = {
    'CustomerID': [f'CUST-{10000+i}' for i in range(n_samples)],
    'Gender': np.random.choice(['Male', 'Female'], n_samples),
    'Tenure_Months': tenure,
    'Contract_Type': contract,
    'Payment_Method': np.random.choice(['Electronic Check', 'Credit Card', 'Bank Transfer'], n_samples),
    'Monthly_Charges': monthly_charges,
    'MRR': monthly_charges,
    'Total_Charges': np.round(tenure * monthly_charges, 2),
    'Churn': churn,
    'Customer_Segment': np.where(monthly_charges > 80, 'High Value', 'Standard')
}

df = pd.DataFrame(data)
df.to_csv("cleaned_customer_churn.csv", index=False)
print("Success: Generated 'cleaned_customer_churn.csv' with 50,000 rows.")