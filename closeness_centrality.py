import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_excel("LinkedIn_Connexions.xlsx")

G = nx.from_pandas_edgelist(df, source='Source', target='Target')

closeness_centrality = nx.closeness_centrality(G)

print("Closeness Centrality Değerleri:")
for node, centrality in closeness_centrality.items():
    print(f"{node}: {centrality}")

pos = nx.spring_layout(G, seed=42)

node_sizes = [closeness_centrality[node] * 3000 for node in G.nodes()]

node_colors = [closeness_centrality[node] for node in G.nodes()]

plt.figure(figsize=(12, 8))
nx.draw_networkx_edges(G, pos, alpha=0.5)
nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.viridis, alpha=0.8)
nx.draw_networkx_labels(G, pos, font_size=10)

plt.title("Closeness Centrality ile Görselleştirilmiş Ağ")
plt.axis('off')
plt.colorbar(nodes, label="Closeness Centrality")
plt.show()

target_node = 'Su Yılmaz'

ego_G = nx.ego_graph(G, target_node, radius=1)

pos = nx.spring_layout(ego_G, seed=42)

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(ego_G, pos, node_color='skyblue', node_size=500, alpha=0.7)
nx.draw_networkx_edges(ego_G, pos, alpha=0.5)
nx.draw_networkx_labels(ego_G, pos, font_size=10)
plt.title(f"Ego Graph: {target_node} ve Komşuları")
plt.axis('off')
plt.show()