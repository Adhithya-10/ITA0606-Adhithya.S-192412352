import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text

# Read CSV
df = pd.read_csv("play_tennis.csv")

# Encode categorical columns
label_encoders = {}
for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features and target
X = df.drop("Play", axis=1)
y = df["Play"]

# Train ID3 Decision Tree
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

# Print the tree
print(export_text(model, feature_names=list(X.columns)))

# Predict a new sample
new = pd.DataFrame({
    "Outlook": ["Sunny"],
    "Temperature": ["Mild"],
    "Humidity": ["Normal"],
    "Wind": ["Weak"]
})

for col in new.columns:
    new[col] = label_encoders[col].transform(new[col])

prediction = model.predict(new)
print("Prediction:", label_encoders["Play"].inverse_transform(prediction)[0])