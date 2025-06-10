import json
# https://ghe.hedgeserv.net/DevOps/Config/blob/master/aws/aws_stop_exclusions.json

# Load JSON file
with open('execution_list.json', 'r') as file:
    data = json.load(file)

# Read and print each hostname
for hostname in data.get("execution_list", []):
    print(hostname)
  
