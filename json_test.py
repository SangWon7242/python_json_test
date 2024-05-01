import json

with open('demo.json', 'r', encoding='UTF8') as f:
  data = json.load(f)

first_data = data['data'][0]    
second_data = data['data'][1]    

for key, val in first_data.items():
  print(f"{key} : {val}")
  