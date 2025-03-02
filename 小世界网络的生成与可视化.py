# K-近邻规则网络的生成与可视化
import networkx as nx
import matplotlib.pyplot as plt


# 写一个规则网络的生成算法
def regular_graph(n, k):
    G = nx.Graph()
    nodes = list(range(n))  # 节点标签设置为0到n-1
    # 每个节点与周围k/2个邻近节点连接
    for j in range(1, k//2 + 1):  # //是取整，返回商的整数部分
        targets = nodes[j:] + nodes[0:j]
        # nodes[j:] 就是从j取到最后，nodes[0:j] 就是从0到j-1元素，targets = nodes[j:] + nodes[0:j] 得到的 targets 列表就是组合起来
        G.add_edges_from(zip(nodes, targets))  # zip() 函数用于将多个可迭代对象（这里是 nodes 和 targets 两个列表）中对应的元素一一配对，组合成一个个元组
    return G


n = 20  # 网络节点总数
k = 4  # 近邻节点数
color_list = ['red', 'gray']

G = regular_graph(n, k)
pos = nx.circular_layout(G)
nx.draw(G, pos, node_size=100, node_color=color_list[0], edge_color=color_list[1])
plt.title("K-regular", fontsize=20)
plt.show()


# WS小世界网络模型
plt.figure(figsize=(15, 4))
# 绘制规则网络
p = 0
G1 = nx.watts_strogatz_graph(n, k, p)
plt.subplot(131)
pos1 = nx.circular_layout(G1)
nx.draw(G1, pos1, node_size=100, node_color=color_list[0], edge_color=color_list[1])
plt.title("regular", fontsize=20)

# 绘制WS小世界
p = 0.2
G2 = nx.watts_strogatz_graph(n, k, p)
plt.subplot(132)
pos2 = nx.circular_layout(G2)
nx.draw(G2, pos2, node_size=100, node_color=color_list[0], edge_color=color_list[1])
plt.title("small-world", fontsize=20)

# 绘制随机网络
p = 1
G3 = nx.watts_strogatz_graph(n, k, p)
plt.subplot(133)
pos3 = nx.circular_layout(G3)
nx.draw(G3, pos3, node_size=100, node_color=color_list[0], edge_color=color_list[1])
plt.title("random", fontsize=20)

plt.show()




