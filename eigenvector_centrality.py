import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_excel("LinkedIn_Connexions.xlsx")

G = nx.from_pandas_edgelist(df, source='Source', target='Target')

if not nx.is_connected(G):
    print("Grafik bağlantılı değil; en büyük bağlantılı bileşen seçiliyor.")
    largest_cc = max(nx.connected_components(G), key=len)
    G = G.subgraph(largest_cc).copy()

eigenvector_centrality = nx.eigenvector_centrality_numpy(G)

print("Eigenvector Centrality Değerleri:")
for node, centrality in eigenvector_centrality.items():
    print(f"{node}: {centrality}")

pos = nx.spring_layout(G, seed=42)

node_sizes = [5000 * eigenvector_centrality[node] for node in G.nodes()]

node_colors = [eigenvector_centrality[node] for node in G.nodes()]

plt.figure(figsize=(12, 8))
nx.draw_networkx_edges(G, pos, alpha=0.3)
nodes = nx.draw_networkx_nodes(
    G, pos, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.viridis, alpha=0.9
)
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title("Eigenvector Centrality ile Görselleştirilmiş Ağ")
plt.colorbar(nodes, label="Eigenvector Centrality")
plt.axis('off')
plt.show()

target_node = 'Su Yılmaz'
if target_node not in G.nodes():
    print(f"{target_node} grafikte bulunamadı. Lütfen başka bir düğüm seçin.")
else:
    ego_G = nx.ego_graph(G, target_node, radius=1)

    ego_centrality = {node: eigenvector_centrality[node] for node in ego_G.nodes()}

    pos = nx.spring_layout(ego_G, seed=42)

    node_sizes = [3000 * ego_centrality[node] for node in ego_G.nodes()]
    node_colors = [ego_centrality[node] for node in ego_G.nodes()]

    plt.figure(figsize=(8, 6))
    nx.draw_networkx_edges(ego_G, pos, alpha=0.5)
    nodes = nx.draw_networkx_nodes(
        ego_G, pos, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.viridis, alpha=0.9
    )
    nx.draw_networkx_labels(ego_G, pos, font_size=10)

    plt.title(f"Ego Graph: {target_node} ve Komşuları (Eigenvector Centrality)")
    plt.axis('off')
    plt.colorbar(nodes, label="Eigenvector Centrality")
    plt.show()