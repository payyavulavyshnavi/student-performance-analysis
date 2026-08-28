import pandas as pd
import matplotlib.pyplot as plt

# Load student performance dataset
df = pd.read_csv("data/student-mat[1].csv", sep=";")

print("Dataset shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

# Final grade correlation
print("\nCorrelation with final grade:")
print(df.corr(numeric_only=True)["G3"].sort_values(ascending=False))

# Final grade distribution
plt.figure(figsize=(8, 5))
plt.hist(df["G3"], bins=10)
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.title("Distribution of Final Grades")
plt.tight_layout()
plt.savefig("results/final_grade_distribution.png")
plt.show()

# Attendance vs Final Marks
plt.figure(figsize=(8, 5))
plt.scatter(df["absences"], df["G3"], alpha=0.7)

plt.title("Attendance vs Final Marks")
plt.xlabel("Absences (lower = better attendance)")
plt.ylabel("Final Exam Marks (G3)")

plt.tight_layout()
plt.savefig("results/attendance_vs_final_marks.png")
plt.show()

print("\nAttendance vs final marks visualization saved successfully.")
print("Analysis completed successfully.")