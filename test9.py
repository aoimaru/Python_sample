import json
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

with open("./laradock_tree.json") as file:
    data_dict = json.load(file)


def create_json_tree(next_key,next_value):
    data_name = next_key
    next_data_name_list = [item for item in next_value if item == "dependencies"]
    print(next_data_name_list)
    

    for next_name in next_data_name_list:
        G.add_edge(data_name,next_name)
    
    if not next_data_name_list:
        return data_name
    else:
        return data_name + str(
            [create_json_tree(key,value) for key,value in next_value.items() if key in next_data_name_list]
            )


for keys,values in data_dict.items():
    if keys == "dependencies":
        for key,value in values.items():
            answear = create_json_tree(key,value)
            print(answear)
        

print(nx.pagerank(G))

plt.figure(figsize=(10, 10))
    
pos = nx.spring_layout(G, k=1.2)
    
#PageRankの追加
pr = nx.pagerank(G)
    
nx.draw_networkx_edges(G, pos, edge_color='y')
    
#node_sizeにPageRankの値を組み込む
nx.draw_networkx_nodes(G, pos, node_color='r', alpha=0.5, node_size=[8000*v for v in pr.values()])
nx.draw_networkx_labels(G, pos, font_size=8)
    
plt.axis('off')
plt.show()





