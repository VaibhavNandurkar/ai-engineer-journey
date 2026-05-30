with open('notes.txt', 'w') as f:
    f.write('Python is powerful\n')
    f.write('File I/O is essential\n')
    f.write('Practice makes perfect\n')

with open('notes.txt', 'r') as f:
    print(f.read())    

with open('notes.txt', 'r') as f:
    for i, line in enumerate(f, start =1):
        print(f'{i}: {line.strip()}')

with open('notes.txt', 'a') as f:
    f.write('Day 5 complete!\n')   
    
with open('notes.txt', 'r') as f:
    print(f.read())     