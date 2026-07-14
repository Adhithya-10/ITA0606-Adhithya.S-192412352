import pandas as pd

# Load Dataset
data = pd.read_csv("loan_approval.csv")

# Separate attributes and target
concepts = data.iloc[:, :-1].values
target = data.iloc[:, -1].values

# Initialize Specific Hypothesis
S = concepts[0].copy()

# Initialize General Hypothesis
G = [["?" for _ in range(len(S))] for _ in range(len(S))]

print("Initial Specific Hypothesis:")
print(S)

print("\nInitial General Hypothesis:")
for g in G:
    print(g)

# Candidate Elimination Algorithm
for i, h in enumerate(concepts):

    if target[i].lower() == "yes":
        # Positive Example
        for x in range(len(S)):
            if h[x] != S[x]:
                S[x] = "?"
                G[x][x] = "?"

    else:
        # Negative Example
        for x in range(len(S)):
            if h[x] != S[x]:
                G[x][x] = S[x]
            else:
                G[x][x] = "?"

    print(f"\nAfter Training Example {i+1}:")
    print("Specific Hypothesis:")
    print(S)

    print("General Hypothesis:")
    for g in G:
        print(g)

# Remove overly general hypotheses
final_G = [g for g in G if g != ["?" for _ in range(len(S))]]

print("\n==========================")
print("Final Specific Hypothesis:")
print(S)

print("\nFinal General Hypothesis:")
for g in final_G:
    print(g)

print("Name   : ADHITHYA S")
print("Reg No : 192412352")