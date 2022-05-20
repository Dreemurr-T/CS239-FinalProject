import json

with open('childnode1.json','r') as f:
    tmp = json.loads(f.read())
    print(tmp[0])