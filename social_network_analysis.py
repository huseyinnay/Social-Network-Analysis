import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain
from networkx.algorithms.community import girvan_newman

df = pd.read_excel("LinkedIn_Connexions.xlsx")

G = nx.from_pandas_edgelist(df, source='Source', target='Target')

degree_dict = dict(G.degree())

max_node = max(degree_dict, key=degree_dict.get)
print("En çok bağlantıya sahip düğüm:", max_node)
print("Bağlantı sayısı:", degree_dict[max_node])

density = nx.density(G)
avg_clustering = nx.average_clustering(G)
try:
    avg_shortest_path = nx.average_shortest_path_length(G)
except nx.NetworkXError:
    avg_shortest_path = "Ağ bağlı değil, hesaplanamadı."

print("Ağ Yoğunluğu:", density)
print("Ortalama Kümeleşme Katsayısı:", avg_clustering)
print("Ortalama En Kısa Yol Uzunluğu:", avg_shortest_path)

if nx.is_connected(G):
    avg_path_length = nx.average_shortest_path_length(G)
    print("Ortalama Yol Uzunluğu:", avg_path_length)
else:
    largest_cc = max(nx.connected_components(G), key=len)
    G_lcc = G.subgraph(largest_cc)
    avg_path_length = nx.average_shortest_path_length(G_lcc)
    print("Ağ bağlı olmadığı için en büyük bileşen için Ortalama Yol Uzunluğu:", avg_path_length)

plt.figure(figsize=(12,8))
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=50)
nx.draw_networkx_edges(G, pos, alpha=0.3)
plt.title("LinkedIn Bağlantıları Sosyal Ağı")
plt.show()

louvain_partition = community_louvain.best_partition(G)
num_louvain_communities = len(set(louvain_partition.values()))
print("Louvain Algoritması ile Toplam Topluluk Sayısı:", num_louvain_communities)

for comm_id in set(louvain_partition.values()):
    nodes_in_comm = [node for node, cid in louvain_partition.items() if cid == comm_id]
    print(f"Topluluk {comm_id}: {nodes_in_comm[:5]} ...")

girvan_newman_generator = girvan_newman(G)
first_level_communities = next(girvan_newman_generator)
first_level_communities = sorted(map(sorted, first_level_communities))
print("\nGirvan-Newman Algoritması ile İlk Seviye Topluluklar:")
for comm in first_level_communities:
    print(comm)

communities = {}
for node, comm_id in louvain_partition.items():
    communities.setdefault(comm_id, []).append(node)

colors = plt.get_cmap("viridis")(range(len(communities)))
for color, (comm_id, nodes) in zip(colors, communities.items()):
    nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=[color],
                           label=f"Topluluk {comm_id}", node_size=50)

nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.title("Louvain Algoritması ile Topluluk Tespiti")
plt.legend()
plt.show()