import pandas as pd

result={
    "Name":["Ali","Ibrahim","Hassan"],
    "Math":[90,80,70],
    "English":[85,75,65],
    "Science":[88,78,68]
}
df=pd.DataFrame(result)
df.to_csv("StudentMarks.csv",index=False)
print("Dataset Created Successfully")