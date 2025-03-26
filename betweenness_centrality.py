import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_excel("LinkedIn_Connexions.xlsx", engine='openpyxl')

G = nx.from_pandas_edgelist(df, source='Source', target='Target')

betweenness = nx.betweenness_centrality(G)

print("Betweenness Centrality:")
for node, centrality in betweenness.items():
    print(f"{node}: {centrality}")

node_sizes = [1000 * betweenness[node] for node in G.nodes()]

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='skyblue', alpha=0.7)
nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=10)

plt.title("Network Graph with Betweenness Centrality")
plt.axis('off')
plt.show()

threshold = 0.05
selected_nodes = [node for node, cent in betweenness.items() if cent > threshold]

subG = G.subgraph(selected_nodes)

pos = nx.spring_layout(subG, seed=42)

node_sizes = [1000 * betweenness[node] for node in subG.nodes()]

plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(subG, pos, node_size=node_sizes, node_color='lightgreen', alpha=0.7)
nx.draw_networkx_edges(subG, pos, alpha=0.5)
nx.draw_networkx_labels(subG, pos, font_size=10)
plt.title("Subgraph Visualization with Betweenness Centrality > Threshold")
plt.axis('off')
plt.show()

target_node = 'Su Yılmaz'
ego_G = nx.ego_graph(G, target_node, radius=1)

pos = nx.spring_layout(ego_G, seed=42)

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(ego_G, pos, node_color='skyblue', node_size=500, alpha=0.7)
nx.draw_networkx_edges(ego_G, pos, alpha=0.5)
nx.draw_networkx_labels(ego_G, pos, font_size=10)
plt.title(f"Ego Graph for Node {target_node}")
plt.axis('off')
plt.show()

subgraph_nodes = list(G.nodes())[:50]
subgraph = G.subgraph(subgraph_nodes)

subgraph_betweenness_centrality = nx.betweenness_centrality(subgraph)
subgraph_node_color = [subgraph_betweenness_centrality[node] for node in subgraph.nodes()]

fig, ax = plt.subplots(figsize=(12, 12))


subgraph_pos = nx.spring_layout(subgraph, seed=42)
nx.draw_networkx_nodes(subgraph, subgraph_pos, node_color=subgraph_node_color,
                         cmap=plt.cm.viridis, node_size=500, ax=ax)
nx.draw_networkx_edges(subgraph, subgraph_pos, alpha=0.5, ax=ax)
nx.draw_networkx_labels(subgraph, subgraph_pos, font_size=10, ax=ax)


sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis,
                           norm=plt.Normalize(vmin=min(subgraph_node_color),
                                              vmax=max(subgraph_node_color)))
sm.set_array([])
plt.colorbar(sm, label='Betweenness Centrality', ax=ax)

ax.set_title("Graph Visualization with Betweenness Centrality (Subset)")
plt.show()