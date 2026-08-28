import pandas as pd

# Load student performance dataset
df = pd.read_csv("data/student-mat[1].csv", sep=";")

# Display basic information
print("Original dataset shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
for column in df.select_dtypes(include="number").columns:
    df[column] = df[column].fillna(df[column].median())

for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# Convert categorical columns into numerical values
df_encoded = pd.get_dummies(df, drop_first=True)

print("Preprocessed dataset shape:", df_encoded.shape)
print("\nFirst 5 rows:")
print(df_encoded.head())

# Save the preprocessed dataset
df_encoded.to_csv("results/preprocessed_student_data.csv", index=False)

print("\nPreprocessed dataset saved successfully.")