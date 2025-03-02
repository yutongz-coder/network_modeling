"""
节点的度就是该节点的邻边数量。平均度就是所有节点的度的平均值。度分布描述了节点度的分布情况，通常可以用一个直方图来表示。
"""

import networkx as nx
import matplotlib.pyplot as plt
# 创建空图
G = nx.Graph()
# 添加节点
G.add_nodes_from([1, 2, 3, 4])
# 添加边
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])
# 获取网络G的度
d = nx.degree(G)
# 创建字典，最终得到的字典 d ，它的键（key）就是图 G 中的节点，值（value）就是对应节点的度
d = dict(nx.degree(G))
print(d)
# 平均度就是节点的度总和/节点个数
print("平均度为：", sum(d.values())/len(G.nodes))

# 获取度分布，度分布p(k)是度为k的节点个数在整个网络节点数目中所占的比例。

dd = nx.degree_histogram(G)   # 返回所有位于区间[0,max]的度值的频数列表
print("度分布为：", dd)
# 绘制度分布直方图
x = list(range(max(d.values())+1))
y = [i/len(G.nodes) for i in nx.degree_histogram(G)]
print(x)
print(y)
plt.bar(x, y, width=0.5, color="red")
plt.xlabel("k")
plt.ylabel("$p_k$")
plt.xlim([0, 4])
plt.show()



