import json

config = {
    'app_name': 'AI Journey Tracker',
    'version': '1.0',
    'days_completed': 5,
    'topics': ['Python', 'SQL', 'Pandas', 'Matplotlib']
}

with open('config.json', 'w') as f:
    json.dump(config, f, indent =4)

with open('config.json', 'r') as f:
    loaded_config = json.load(f) 

print(loaded_config['app_name'])
print(loaded_config['topics'])

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return(f.read())
    except FileNotFoundError:
        return 'Error: file not found'

print(read_file('notes.txt'))
print(read_file('ghost.txt'))        