                              #Loads & Dumps
import json

api_response = '''
{
  "name": "Vaibhav",
  "semester": 6,
  "subjects": ["IC Engines", "Robotics", "Machine Design"]
}
'''
student = json.loads(api_response)
student["grade"] = "A"

formatted = json.dumps(student, indent=2)
print(formatted)

                                #Reading & Writing files

import json

students = [
    {"name": "Arjun",  "score": 88},
    {"name": "Priya",  "score": 94},
    {"name": "Rohit",  "score": 76}
]

with open("students.json", "w") as f:
    json.dump(students, f, indent =2)
print("Saved to students.json")

with open("students.json", "r") as f:
    loaded = json.load(f)
for s in loaded:
    print(f"{s['name']}: {s['score']}")
                             
                                  #Nested JSON & Filtering

import json

products_json = '''
[
  {"name": "Laptop",  "price": 75000, "specs": {"brand": "Dell",     "in_stock": true}},
  {"name": "Mouse",   "price": 850,   "specs": {"brand": "Logitech", "in_stock": false}},
  {"name": "Monitor", "price": 18000, "specs": {"brand": "LG",       "in_stock": true}},
  {"name": "Webcam",  "price": 3200,  "specs": {"brand": "HP",       "in_stock": false}}
]
'''
products = json.loads(products_json)
in_stock = [p for p in products if p["specs"]["in_stock"]]

for product in in_stock:
    print(f"{product['name']}: - ₹{product['price']}")