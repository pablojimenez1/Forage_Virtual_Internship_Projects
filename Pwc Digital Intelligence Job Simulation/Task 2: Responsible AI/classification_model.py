import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

# Load a sample dataset
np.random.seed(42)
data_size = 500
df = pd.DataFrame({
    'Feature_1' : np.random.rand(data_size) * 10,
    'Feature_2' : np.random.randint(1, 100, data_size),
    'Feature_3' : np.random.choice([0, 1], data_size),
    'Feature_4' : np.random.normal(50, 15, data_size),
    'Feature_5' : np.random.randint(1, 5, data_size),
    'Target' : np.random.choice([0, 1], data_size)
})

# Split into training and testing sets
X = df.drop(columns=['Target'])
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a RandomForest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Model evaluation
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Display classification report and accuracy
accuracy, report

# Use RandomForest's built-in feature importance method
feature_importance_rf = model.feature_importances_

# Store results in a DataFrame
rf_feature_importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': feature_importance_rf
}).sort_values(by='Importance', ascending=False)

# Print feature importance
print(rf_feature_importance_df)

# Plot Feature Importance
plt.figure(figsize=(8, 5))
sns.barplot(x=rf_feature_importance_df['Importance'], y=rf_feature_importance_df['Feature'])
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.title("Feature Importance (Random Forest)")
plt.show()
