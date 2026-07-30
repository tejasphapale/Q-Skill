import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

print("="*50)
print("STUDENT DATA")
print("="*50)

print(df)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

average_marks = df["Marks"].mean()

print("\nAverage Marks =", average_marks)

highest = df["Marks"].max()

print("Highest Marks =", highest)

lowest = df["Marks"].min()

print("Lowest Marks =", lowest)

avg_hours = df["StudyHours"].mean()

print("Average Study Hours =", avg_hours)

avg_attendance = df["Attendance"].mean()

print("Average Attendance =", avg_attendance)

department_marks = df.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department")

print(department_marks)



plt.figure(figsize=(8,5))

plt.bar(
    department_marks.index,
    department_marks.values
)

plt.title("Average Marks by Department")

plt.xlabel("Department")

plt.ylabel("Average Marks")

plt.grid(axis='y')

plt.show()



plt.figure(figsize=(8,5))

plt.scatter(
    df["StudyHours"],
    df["Marks"]
)

plt.title("Study Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.grid(True)

plt.show()


correlation = df.corr(numeric_only=True)

plt.figure(figsize=(6,5))

plt.imshow(
    correlation,
    cmap='coolwarm',
    interpolation='nearest'
)

plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.show()

print("\nProgram Executed Successfully")