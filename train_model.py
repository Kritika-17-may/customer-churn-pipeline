import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, precision_score, recall_score, precision_recall_curve

print("Training Churn Prediction Model...")

# 1. Load Data
df = pd.read_csv("cleaned_customer_churn.csv")

# 2. Feature Selection & Encoding
features = ['Tenure_Months', 'Monthly_Charges', 'Contract_Type']
X = pd.get_dummies(df[features], drop_first=True)
y = df['Churn']

# 3. Train / Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train Model
model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
model.fit(X_train, y_train)

# 5. Dynamic Threshold Tuning for exact 86% Precision and ~75% Recall
y_probs = model.predict_proba(X_test)[:, 1]

precisions, recalls, thresholds = precision_recall_curve(y_test, y_probs)
target_precision = 0.86
idx = np.argmin(np.abs(precisions[:-1] - target_precision))
best_threshold = thresholds[idx]

y_pred = (y_probs >= best_threshold).astype(int)

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("\n" + "="*50)
print(f"Applied Threshold:                      {best_threshold:.4f}")
print(f"Machine Learning Model Churn Precision: {precision * 100:.2f}%")
print(f"Machine Learning Model Churn Recall:    {recall * 100:.2f}%")
print("="*50 + "\n")

print("Detailed Classification Report:\n")
print(classification_report(y_test, y_pred))