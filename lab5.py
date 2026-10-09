import pandas as pd
import numpy as np

print("="*50)
print("PART 1: DATA MANIPULATION (Slide 1)")
print("="*50)

# 1. Load the dataset
print("\n--- Loading students.csv ---")
students_df = pd.read_csv("students.csv")
print("Dataset loaded successfully.")

# 2. Display first five rows
print("\n--- First five rows ---")
print(students_df.head())

# 3. Find number of rows and columns
print("\n--- Number of rows and columns ---")
rows, cols = students_df.shape
print(f"Rows: {rows}, Columns: {cols}")

# 4. Select name and GPA
print("\n--- Select name and GPA (first 5 rows) ---")
name_gpa_df = students_df[['name', 'GPA']]
print(name_gpa_df.head())

# 5. Find students with GPA >= 3.5
print("\n--- Students with GPA >= 3.5 ---")
high_gpa_students = students_df[students_df['GPA'] >= 3.5]
print(high_gpa_students)

# 6. Sort students by GPA
print("\n--- Sort students by GPA (Descending) ---")
sorted_students = students_df.sort_values(by='GPA', ascending=False)
print(sorted_students.head(10)) # display top 10 for brevity

# 7. Find average GPA by major
print("\n--- Average GPA by major ---")
avg_gpa_by_major = students_df.groupby('major')['GPA'].mean()
print(avg_gpa_by_major)


print("\n\n" + "="*50)
print("PART 2: FROM RAW DATA TO USEFUL INFO (Slide 2)")
print("="*50)

# 1. Load both files
print("\n--- Loading both datasets ---")
df_students = pd.read_csv("students.csv")
df_scores = pd.read_csv("scores.csv")
print("students.csv and scores.csv loaded.")

# 2. Check missing values
print("\n--- Missing values in students.csv ---")
print(df_students.isnull().sum())
print("\n--- Missing values in scores.csv ---")
print(df_scores.isnull().sum())

# 3. Fill or remove missing data appropriately
print("\n--- Handling missing data ---")
# For students: Fill missing age with median, missing GPA with median
df_students['age'] = df_students['age'].fillna(df_students['age'].median())
df_students['GPA'] = df_students['GPA'].fillna(df_students['GPA'].median())
print("Missing values in students after fill:")
print(df_students.isnull().sum())

# For scores: Fill missing subject scores with median of that subject
df_scores['python'] = df_scores['python'].fillna(df_scores['python'].median())
df_scores['math'] = df_scores['math'].fillna(df_scores['math'].median())
df_scores['database'] = df_scores['database'].fillna(df_scores['database'].median())
print("\nMissing values in scores after fill:")
print(df_scores.isnull().sum())

# 4. Merge the two datasets
print("\n--- Merging the two datasets ---")
merged_df = pd.merge(df_students, df_scores, on='student_id')
print(merged_df.head())

# 5. Calculate each student's average score
print("\n--- Calculating each student's average score ---")
# Average of python, math, and database
merged_df['average_score'] = merged_df[['python', 'math', 'database']].mean(axis=1)
print(merged_df[['student_id', 'name', 'average_score']].head())

# 6. Find the top 5 students (based on average score)
print("\n--- Top 5 students by average score ---")
top_5_students = merged_df.sort_values(by='average_score', ascending=False).head(5)
print(top_5_students[['student_id', 'name', 'major', 'average_score']])

# 7. Compute average score by major
print("\n--- Average score by major ---")
avg_score_by_major = merged_df.groupby('major')['average_score'].mean()
print(avg_score_by_major)
