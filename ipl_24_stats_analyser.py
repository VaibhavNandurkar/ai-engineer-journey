import pandas as pd

data = {
    'Player':  ['Virat Kohli','Rohit Sharma','MS Dhoni','Hardik Pandya','Jasprit Bumrah'],
    'Team':    ['RCB','MI','CSK','MI','MI'],
    'Runs':    [450, 380, 210, 420, 30],
    'Wickets': [0, 0, 0, 8, 20],
    'SR':      [145.2, 132.5, 168.3, 155.8, 75.0]
}

df = pd.DataFrame(data)
print(df)
print("\nShape:", df.shape)
print("\nDType:", df.dtypes)
runs_series = df['Runs']
print("Type:", type(runs_series))
print("Mean:", runs_series.mean())
print("Max:", runs_series.max())
print("Min:", runs_series.min())

my_series = pd.Series([10, 20, 30])
print("\nStandalone Series:\n", my_series)


                                                #Read CSV loading real data

import pandas as pd
from io import StringIO

csv_data = """Player,Team,Runs,Wickets,SR
Virat Kohli,RCB,450,0,145.2
Rohit Sharma,MI,380,0,132.5
MS Dhoni,CSK,210,0,168.3
Hardik Pandya,MI,420,8,155.8
Jasprit Bumrah,MI,30,20,75.0"""

df = pd.read_csv(StringIO(csv_data))
print(df)
print("Shape:", df.shape)
print("Columns:", df.columns)
print("\n First 2 rows:", df.head(2))

                                                #Head & Tail - peeking at data

import pandas as pd

data = {
    'Player':  ['Virat Kohli','Rohit Sharma','MS Dhoni','Hardik Pandya','Jasprit Bumrah'],
    'Team':    ['RCB','MI','CSK','MI','MI'],
    'Runs':    [450, 380, 210, 420, 30],
    'Wickets': [0, 0, 0, 8, 20],
    'SR':      [145.2, 132.5, 168.3, 155.8, 75.0]
}
df = pd.DataFrame(data)

print("--- First 3 ---")
print(df.head(3))
print("--- Last 2 ---")
print(df.tail(2))

                                                #loc - label based selection

import pandas as pd

data = {
    'Player':  ['Virat Kohli','Rohit Sharma','MS Dhoni','Hardik Pandya','Jasprit Bumrah'],
    'Team':    ['RCB','MI','CSK','MI','MI'],
    'Runs':    [450, 380, 210, 420, 30],
    'Wickets': [0, 0, 0, 8, 20],
    'SR':      [145.2, 132.5, 168.3, 155.8, 75.0]
}
df = pd.DataFrame(data)

print("Task 1 - specific rows + columns")
print(df.loc[[0,3], ['Player','Runs']])
print("\nTask 2 - all rows, 2 columns")
print(df.loc[:, ['Team','SR']])
print("\nTask 3 - Slice rows 1 to 3")
print(df.loc[1:3])

                                            #iloc - position based selection

import pandas as pd

data = {
    'Player':  ['Virat Kohli','Rohit Sharma','MS Dhoni','Hardik Pandya','Jasprit Bumrah'],
    'Team':    ['RCB','MI','CSK','MI','MI'],
    'Runs':    [450, 380, 210, 420, 30],
    'Wickets': [0, 0, 0, 8, 20],
    'SR':      [145.2, 132.5, 168.3, 155.8, 75.0]
}
df = pd.DataFrame(data)

print("Task 1 - First 3 rows, last 2 cols:")
print(df.iloc[:3,-2:])
print("\nTask 2 - Row at position 2, all cols:")
print(df.iloc[2])
print("\nTask 3 - Every other row(0,2,4) - cols at position 0 to 2")
print(df.iloc[::2, [0, 2]])

                                            #Boolean filtering

import pandas as pd

data = {
    'Player':  ['Virat Kohli','Rohit Sharma','MS Dhoni','Hardik Pandya','Jasprit Bumrah'],
    'Team':    ['RCB','MI','CSK','MI','MI'],
    'Runs':    [450, 380, 210, 420, 30],
    'Wickets': [0, 0, 0, 8, 20],
    'SR':      [145.2, 132.5, 168.3, 155.8, 75.0]
}
df = pd.DataFrame(data)
f1 = df[df['Runs'] > 350]
print(f"Filter 1 - Runs > 350 (len{f1} rows):")
print(f1)
f2 = df[(df['Team'] == 'MI') & (df['Runs'] > 300)]
print(f"\nFilter 2 - Team MI and Runs > 300 (len{f2} rows):")
print(f2)
f3 = df[(df['SR'] > 150) | (df['Wickets'] > 10)]
print(f"\nFilter 3 - SR > 150 or Wickets > 10 (len{f3} rows):")
print(f3)

                                            #Sort Values

import pandas as pd

data = {
    'Player':  ['Virat Kohli','Rohit Sharma','MS Dhoni','Hardik Pandya','Jasprit Bumrah'],
    'Team':    ['RCB','MI','CSK','MI','MI'],
    'Runs':    [450, 380, 210, 420, 30],
    'Wickets': [0, 0, 0, 8, 20],
    'SR':      [145.2, 132.5, 168.3, 155.8, 75.0]
}
df = pd.DataFrame(data)

print("Sort 1 - Runs descending:")
print(df.sort_values('Runs', ascending=False))

print("\nSort 2 - Wickets descending:")
print(df.sort_values('Wickets', ascending=False))

print("\nSort 3 - Team asc, SR desc:")
print(df.sort_values(by=['Team', 'SR'], ascending=[True, False])[['Player','Team','SR']])

                                          # describe & groupby

import pandas as pd

data = {
    'Player':  ['Virat Kohli','Rohit Sharma','MS Dhoni','Hardik Pandya','Jasprit Bumrah'],
    'Team':    ['RCB','MI','CSK','MI','MI'],
    'Runs':    [450, 380, 210, 420, 30],
    'Wickets': [0, 0, 0, 8, 20],
    'SR':      [145.2, 132.5, 168.3, 155.8, 75.0]
}
df = pd.DataFrame(data)

print("Describe():")
print(df.describe())

avg_runs = df.groupby('Team')['Runs'].mean()
print("\nAverage Runs by Team:")
print(avg_runs)

total_wkts = df.groupby('Team')['Wickets'].sum()
print("\nTotal Wickets by Team:")
print(total_wkts)

        