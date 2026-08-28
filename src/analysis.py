import pandas as pd
import matplotlib.pyplot as plt

# Load the student performance dataset
data = pd.read_csv("data/student-mat.csv", sep=";")

# Display basic information
print("First 5 rows:")
print(data.head())

print("\nDataset shape:")
print(data.shape)

print("\nAverage marks:")
print("G1:", data["G1"].mean())
print("G2:", data["G2"].mean())
print("G3:", data["G3"].mean())

# Study time vs final grade
study_performance = data.groupby("studytime")["G3"].mean()

print("\nAverage final grade by study time:")
print(study_performance)

# Attendance/absence analysis
print("\nAverage absences:", data["absences"].mean())

# Plot study time vs final grade
study_performance.plot(kind="bar")
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Average Final Grade")
plt.tight_layout()
plt.savefig("results/study_time_vs_final_grade.png")
plt.show()
