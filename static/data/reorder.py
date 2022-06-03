import json


node_path1 = 'corenodes10.json'
node_path2 = 'allnodes10.json'

edge_path = 'keylinks10.json'

nodes1 = json.load(open(node_path1))
nodes2 = json.load(open(node_path2))
edges1 = json.load(open(edge_path))

new_node = []

for node in nodes2:
    in_num = 0
    out_num = 0
    for edge in edges1:
        if edge['source'] == node['id']:
            out_num += 1
        elif edge['target'] == node['id']:
            in_num += 1
    if (in_num >= 1 and out_num >= 1) or out_num >= 2 or in_num >= 2:
        flag = 1
        for check in nodes1:
            if node['id'] == check['id']:
                flag = 0
        if flag:
            nodes1.append({
                "id": node['id'],
                "name": node['name'],
                "category": node['category'],
                "industry": node['industry'],
                "symbolSize": 1,
            })

print(nodes1)
save_file = open('corenode10.json','w')
json.dump(nodes1,save_file)
# json.dump(new_node,save_file)
