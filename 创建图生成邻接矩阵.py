import geopandas as gpd
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
# 获取图的邻接矩阵
As = nx.adjacency_matrix(G)
print(As)
# 转化成二维数组形式的矩阵
A = As.todense()
print(A)
# 判断连通性，无向网络中，如果任意一对节点i和节点j之间至少存在一条路径，则网络是连通的；如果不存在路径，则网络是不连通的。
print(nx.is_connected(G))
# 集聚系数用以捕获给定节点的邻居节点之间的连接程度。对于一个度为k_i的节点i，局部集聚系数被定义为C_i = 2L_i/[k_i(k_i-1)]，L_i是邻居节点真实的连接数量。
print("节点1的局部集聚系数", nx.clustering(G, 1))
# 平均集聚系数<C>=1/N * [\Sigma^N (C_i)]
print("平均集聚系数", nx.average_clustering(G))
# 全局集聚系数 C=3*三角形的个数/连通三元组的个数
print("全局集聚系数", nx.transitivity(G))
# 整个网络的平均距离
print("平均距离", nx.average_shortest_path_length(G))
print("节点1，2最短距离", nx.shortest_path_length(G, 1, 2))

# 创建一个无向加权网络
WG = nx.Graph()
WG.add_nodes_from([1, 2, 3, 4])
WG.add_weighted_edges_from([(1, 2, 3), (1, 3, 1), (2, 4, 4)])
# 对于每条边 e，通过 WG[e[0]][e[1]]['weight'] 来获取边的权重。这里 e[0] 和 e[1] 分别对应边的两个端点节点标识
w = [WG[e[0]][e[1]]['weight'] for e in WG.edges()]
nx.draw(WG, node_size=500, width=w, with_labels=True)
# 获取网络节点的加权度（即点权）
nw = nx.degree(WG, weight='weight')
print("网络节点加权度：", nw)
# 获取每条边的权重
for e in WG.edges():
    print(WG[e[0]][e[1]]['weight'])
plt.show()


