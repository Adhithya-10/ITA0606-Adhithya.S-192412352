import pandas as pd

# Read the CSV file
df = pd.read_csv("loan_approval.csv")

print("Training Data:\n")
print(df)

# Separate attributes and target
concepts = df.iloc[:, :-1].values
target = df.iloc[:, -1].values

# Initialize hypothesis with the first positive example
for i in range(len(target)):
    if target[i] == "Yes":
        hypothesis = concepts[i].copy()
        break

print("\nInitial Hypothesis:")
print(hypothesis)

# Find-S Algorithm
for i in range(len(concepts)):
    if target[i] == "Yes":
        for j in range(len(hypothesis)):
            if hypothesis[j] != concepts[i][j]:
                hypothesis[j] = '?'

        print(f"\nAfter Positive Example {i+1}:")
        print(hypothesis)

# Final Hypothesis
print("\nFinal Hypothesis:")
print(hypothesis)

print("Name   : ADHITHYA S")
print("Reg No : 192412352")