import json

with open('./sample.json') as f:
    jsn = json.load(f)

print(jsn)

for jsn_key in jsn:
    print(jsn_key)


for jsn_val in jsn.values():
    print(jsn_val)

