import pandas as pd
import json

csv_path1 = 'corenodes1.csv'
json_path1 = 'corenodes1.json'

csv_path2 = 'link1.csv'
json_path2 = 'keylink1.json'

df = pd.read_csv(csv_path1,header=None)
# df.columns = ['id','name','category','industry']
df.columns = ['id','name','category','industry','value']

df.to_json(json_path1,orient='records')

df = pd.read_csv(csv_path2,header=None)
df.columns = ['relation','source','target','importance','jumps']
df.to_json(json_path2,orient='records')

# # further transfer
# f1 = open(json_path1,'r')
# f2 = open(json_path2,'r')
# node_json = json.load(f1)
# edge_json = json.load(f2)
# # print(node_json)
# id_data = []
# name_data = []
# category = []
# industry = []

# source = []
# target = []
# relation = []

# for node in node_json:
#     id_data.append(node['id'])
#     name_data.append(node['name'])
#     category.append(node['category'])
#     industry.append(node['industry'])

# for edge in edge_json:
#     source.append(edge['source'])
#     target.append(edge['target'])
#     relation.append(edge['relation'])

# node = {
#     "id":id_data,
#     "name": name_data,
#     "category": category,
#     "industry": industry,
# }

# edge = {
#     "source": source,
#     "target": target,
#     "relation": relation,
# }
# f3 = open(json_path1,'w')
# f4 = open(json_path2,'w')
# json.dump(node,f3)
# json.dump(edge,f4)
