import sqlite3
import csv
from datetime import datetime

# 1. Database Setup
conn = sqlite3.connect('experiments.db')
cursor = conn.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS runs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT,
            learning_rate REAL,
            accuracy  REAL,
            timestamp  TEXT
        )
""")
conn.commit()
conn.close()
print("experiments.db ready!")

# 2. Generate Dummy Config 
with open('config.txt', 'w') as f:
    f.write("LinearRegression,0.01,0.82\nRandomForest,0.001,0.91\nNeuralNet,0.0001,0.95\n")

# 3. Parse Config
def parse_config(filepath):
    experiments = []
    with open(filepath, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            experiments.append((parts[0], float(parts[1]), float(parts[2])))
    return experiments

# 4. Log runs to DB
def log_runs(experiments):
    conn = sqlite3.connect('experiments.db')
    cursor = conn.cursor()
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    rows = [(m, lr, acc, ts) for m, lr, acc in experiments]
    cursor.executemany(
        'INSERT INTO runs (model_name, learning_rate, accuracy, timestamp) VALUES (?,?,?,?)',
        rows
    )
    conn.commit()
    conn.close()
    print(f"Logged {len(rows)} runs.")

#5. Query & Export to CSV
def export_summary(db='experiments.db', out='summary.csv'):
    conn = sqlite3.connect(db)
    cursor = conn.cursor() 
    cursor.execute('SELECT * FROM runs ORDER BY accuracy DESC')
    rows = cursor.fetchall()
    conn.close()
    
    with open(out, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id','model_name','learning_rate','accuracy','timestamp'])
        writer.writerows(rows)
    print("summary.csv exported!")    

# 6. Full Pipeline
def run_pipeline(config_path='config.txt'):
    experiments = parse_config(config_path)
    log_runs(experiments)
    export_summary()
    
    with open('summary.csv', 'r') as f:
        reader = csv.DictReader(f)
        best = next(reader)
        print(f"\nBest: {best['model_name']} | Accuracy: {best['accuracy']}")


run_pipeline()