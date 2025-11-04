import pandas as pd

df=pd.read_csv("StudentMarks.csv")
df["Average_Score"]=df[["Math","English","Science"]].mean(axis=1)
print("Average score of each student:", df[["Name", "Average_Score"]].values.tolist())
highest_avg_student=df.loc[df["Average_Score"].idxmax()]["Name"]
print("Student with highest average score:", highest_avg_student)