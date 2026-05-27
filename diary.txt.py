f = open('notes.txt', 'w')
f.write("Python is fun\n")
f.write("I am learning File IO\n")
f.write("Day 2 of my AI journey\n")
f.close()

with open('notes.txt', 'r') as f:
    lines  = f.readlines()

for line in lines:   
    print(line.strip()) 

with open('log.txt', 'w') as f:
    f.write('Session started\n')
    f.write('Topic: File IO\n')
    f.write('Status: In progress\n')

with open('log.txt', 'r') as f:
    print(f.read())

with open('log.txt', 'a') as f:
    f.write("Checkpoint 4 done\n")
    f.write("Append mode works!\n")
with open('log.txt', 'r') as f:
    lines = f.readlines() 
for i, line in enumerate(lines, start=1):
    print(f"{i}: {line.strip()}") 

try:
    with open('missing.txt', 'r') as f:
        content = f.read()
        print(content)    
except FileNotFoundError as e:
    print("File Not Found: {e}")
except Exception as e:
    print (f"Unexpected error: {e}")    
finally:
    print("Done.")    
    
def safe_read(filename):
    try:
        with open('filename', 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
            return []
    except Exception:
        return None
print("notes.txt:", safe_read('notes.txt')) 
print("ghost.txt:", safe_read('ghost.txt'))              