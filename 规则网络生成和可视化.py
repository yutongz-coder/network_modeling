import networkx as nx
import matplotlib.pyplot as plt

n = 10
# 创建孤立节点图
G1 = nx.Graph()
G1.add_nodes_from(list(range(n)))
# 将创建的图形对象（画布）的宽度和高度都设置为 4 英寸
plt.figure(figsize=(4, 4))
nx.draw(G1, pos=nx.circular_layout(G1), node_size=500, node_color="red", with_labels=True)
# plt.savefig("孤立图.pdf")
plt.show()

# 创建完全图
G2 = nx.complete_graph(n)
plt.figure(figsize=(4, 4))
nx.draw(G2, pos=nx.circular_layout(G2), node_size=500, node_color="red", with_labels=True)
plt.show()

# 创建一维环状图
G3 = nx.cycle_graph(n)
plt.figure(figsize=(4, 4))
nx.draw(G3, pos=nx.circular_layout(G3), node_size=500, node_color="red", with_labels=True)
plt.show()

# K近邻规则（耦合）图
# 4，意味着每个节点一开始会和另外的 4 个节点形成边连接
# 当 p = 0 时，表示不进行随机重连操作，此时生成的网络结构相对比较规则、有序，呈现出类似环状且节点与固定数量近邻相连的状态；随着 p 值的增大（取值范围是从 0 到 1），网络的随机性逐渐增强，结构也会变得越来越无序
G4 = nx.watts_strogatz_graph(n, 4, 0.7)
plt.figure(figsize=(4, 4))
nx.draw(G4, pos=nx.circular_layout(G4), node_size=500, node_color="red", with_labels=True)
plt.show()

# 二维方格图
G5 = nx.grid_graph((6, 6), periodic=False)
plt.figure(figsize=(4, 4))
nx.draw(G5, node_size=500, node_color="red", with_labels=True)
plt.show()


