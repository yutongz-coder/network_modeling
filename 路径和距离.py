"""
路径就是沿着网络的链接运行的路，路径的长度表示路径包含的链接数。在网络科学中，更多的是关注两个节点i和节点j之间的最短路径长度，最短路径长度称为它们之间的距离。
"""

import networkx as nx
import matplotlib.pyplot as plt
# 创建一个空图
G = nx.Graph()   # 无向图
# 无向图
# G = nx.DiGraph()
# 添加节点
G.add_nodes_from([1, 2, 3, 4])
# 添加边
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])
# 可视化
nx.draw(G, node_size=500, with_labels=True)
plt.show()
# 最短路径,source 的值被设为 1，它用于指定路径的起始节点， target 的值设为 4，用于指定路径的目标节点
short_road = nx.shortest_path(G, source=1, target=4)
print("short_road:", short_road)
# 从1到4的所有简单路径
all_list = list(nx.all_simple_paths(G, source=1, target=4))
print("all_list:", all_list)
# 两个节点之间所有最短距离
short_list = list(nx.all_shortest_paths(G, source=1, target=4))
print("short_list:", short_list)
# 求两个节点之间最短路径长度（距离）
short_distance = nx.shortest_path_length(G, source=1, target=4)
print("short_distance:", short_distance)
# 求整个网络的平均距离
ave_distance = nx.average_shortest_path_length(G)
print("ave_distance:", ave_distance)



