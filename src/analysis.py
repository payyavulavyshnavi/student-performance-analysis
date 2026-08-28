import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/preprocessed_student_data.csv")

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

if "G3" in df.columns:
    print("\nCorrelation with final grade:")
    print(df.corr(numeric_only=True)["G3"].sort_values(ascending=False))

    plt.figure(figsize=(8, 5))
    plt.hist(df["G3"], bins=10)
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Final Grades")
    plt.tight_layout()
    plt.savefig("results/final_grade_distribution.png")
    plt.show()

print("\nAnalysis completed successfully.")