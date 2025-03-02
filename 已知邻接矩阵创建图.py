import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

A = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
G = nx.from_numpy_array(A)
# 加权图的邻接边有权重
G.add_weighted_edges_from([(0, 1, 3), (1, 2, 7.5), (0, 2, 1.5)])
As = nx.adjacency_matrix(G)
print(As.todense())
# 画出创建的图
nx.draw(G, node_size=500, with_labels=True)
plt.show()
