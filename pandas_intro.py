import pandas as pd
marks = [88, 72, 95, 60, 78]
s = pd.Series(marks)
print(s)
print(s[0])
print(s.mean())
print(s.max)

data = {
    'name':   ['Vaibhav', 'Riya', 'Arjun', 'Sneha', 'Karan'],
    'marks':  [88, 72, 95, 60, 78],
    'grade':  ['A', 'B', 'A+', 'C', 'B'],
    'passed': [True, True, True, False, True]
}

df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.dtypes)
print(df.head(3))
print(df['name'] )
print(df[['name', 'marks']])
print(df.iloc[0])
print(df.iloc[2:4])
print(df.loc[0, 'name'])
print(df[df['marks'] > 75])
print(df[df['passed'] == True])
print(df[(df['marks'] >= 70) & (df['marks'] <= 90)])
print(df[df['passed'] == False])
print(df.sort_values('marks', ascending=False))
print(df.sort_values('name'))
print(df.describe())
print(df['marks'].mean())
print(df['marks'].min())
print(df['marks'].max())
print(df.groupby('subject')['marks'].mean())
print(df.groupby('subject')['marks'].max())
print(df.groupby('subject')['passed'].sum())
print(df.groupby('subject')['marks'].agg(['mean', 'min', 'max']))
