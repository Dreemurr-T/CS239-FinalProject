import pandas as pd
csv_path = 'childnode1.csv'
json_path = 'childnode1.json'

# csv_path = 'childpic1.csv'
# json_path = 'childpic1.json'

df = pd.read_csv(csv_path,header=None)
df.columns = ['id','name','category','industry']
# df.columns = ['relation','source','target']
print(df)

df.to_json(json_path,orient='records')