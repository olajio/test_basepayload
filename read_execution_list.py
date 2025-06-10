import json

# Load JSON file
with open('execution_list.json', 'r') as file:
    data = json.load(file)

# Read and print each hostname
for hostname in data.get("execution_list", []):
    print(hostname)
  
