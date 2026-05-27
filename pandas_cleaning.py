import pandas as pd

data = {
    'name':  ['Vaibhav', 'Rohit', None,    'Priya', 'Rohit',  'Sneha'],
    'age':   [21,        22,      20,       21,      22,       23],
    'marks': [88,        None,    75,       None,    None,     91],
    'city':  ['Pune',    'Mumbai','Nagpur', 'Pune',  'Mumbai', 'Nashik']
}

df = pd.DataFrame(data)
print(df)
print("Shape", df.shape)
print("Null grid:")
print(df.isnull)
print("\nMissing per column:")
print(df.isnull().sum())
df_dropped = df.dropna()
print("After dropna:")
print(df_dropped)
print("Shape:", df_dropped.shape)
df_filled = df.copy()
df_filled['marks'] = df_filled['marks'].fillna(df_filled['marks'].mean())
df_filled['name']  = df_filled['name'].fillna('Unknown')
print(df_filled)
df_clean = df_filled.drop_duplicates()
print(df_clean)
print("Before:", df_filled.shape, "→After", df_clean.shape)
df.to_csv('dirty_students.csv', index=False)
df2 = pd.read_csv('dirty_students.csv')
df2['marks'] = df2['marks'].fillna(df2['marks'].mean())
df2['name'] = df2['name'].fillna('Unknown')
df2 = df2.drop_duplicates()
print(df2)
df2.to_csv('clean_students.csv', index = False)
print("Saved to clean_students.csv")