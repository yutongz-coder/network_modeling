# 度-度相关性描述了网络中度大的节点和度小的节点之间的关系。若度大的节点倾向于和度大的节点连接，则网络是度-度正相关的；反之，若度大的节点倾向于和度小的节点连接，则网络是度-度负相关的
# # 节点v_i的最近平均度值定义为k_{nn,i}=[\Sigma_j a_ij * k_j]/k_i
# # 所有度值为k的节点的最近邻平均度值的平均值k_{nn}(k)=(\Sigma_i k_{nn,i})/[N*P(k)],N为节点个数，P(k)为度分布函数
# # 如果k_{nn}(k)是随着k上升的增函数，则说明度值大的节点倾向于和度值大的节点连接，网络具有正相关特性，称之为同配网络；反之网络具有负相关特性，称之为异配网络
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# 加载三个真实数据集
# 创建无向网络是nx.Graph(), 创建有向网络是nx.DiGraph()
# 1.科学合作网络
df1 = pd.read_csv("数据/citation.csv")
G1 = nx.from_pandas_edgelist(df1, 'source', 'target', create_using=nx.Graph())
# 2.电网
df2 = pd.read_csv("数据/power.csv")
G2 = nx.from_pandas_edgelist(df2, 'source', 'target', create_using=nx.Graph())
# 3.代谢网络
df3 = pd.read_csv("数据/celegans_metabolic.csv")
G3 = nx.from_pandas_edgelist(df3, 'source', 'target', create_using=nx.Graph())

# 定义求最近邻平均度的函数
def average_nearest_neighbor_degree(G):
    k = set([G.degree(i) for i in G.nodes()])  # 获取所有可能的度值，集合可以去重，对不同度值计算最近邻平均度
    sorted_k = sorted(k)

    k_nn_k = []   # 这个列表将用于存储每个度值对应的最近邻平均度
    for ki in sorted_k:
        c = 0   # c 变量用于记录当前度值 ki 的节点个数
        k_nn_i = 0   # k_nn_i 变量用于累计当前度值 ki 的所有节点的邻居节点度值总和（后续会除以对应节点个数来得到平均度）
        for i in G.nodes():
            if G.degree(i) == ki:
                k_nn_i += sum([G.degree(j) for j in list(nx.all_neighbors(G, i))])/ki   # 将这个总和除以当前节点 i 的度值 ki（这样做的原因是要计算平均邻居度值，需要考虑每个节点自身连接的边数情况）
                c += 1
        k_nn_k.append(k_nn_i/c)
    return sorted_k, k_nn_k


sorted_k, k_nn_k = average_nearest_neighbor_degree(G1)
# 打印结果（可以根据实际需求进行更复杂的后续处理）
print("所有不同的度值:", sorted_k)
print("对应的最近邻平均度值:", k_nn_k)

# 基于Pearson相关系数的度-度相关性
# 如果r的值接近 1，这个网络具有较强的正度 - 度相关性；如果接近 -1，则是较强负相关性；接近 0 就表示度之间相关性较弱，连接相对随机
# r大于 0，表示图 G 是正相关的，即度大的节点更倾向于连接度大的节点，度小的节点更倾向于连接度小的节点，这种网络结构也被称为同配网络（assortative network）；r小于0称为异配网络
r1 = nx.degree_assortativity_coefficient(G1)
# d1 = nx.average_shortest_path_length(G1)
print(f"r1:{r1}")
r2 = nx.degree_assortativity_coefficient(G2)

print(f"r2:{r2}")
r3 = nx.degree_assortativity_coefficient(G3)

print(f"r3:{r3}")
#  nx.degree_assortativity_coefficient用于计算给定图 G1 的度 - 度相关性系数。这个系数通常是基于 Pearson 相关系数来计算的

# r2 = nx.degree_pearson_correlation_coefficient(G2)
# print("r2:", r2)

# 画度值和最近邻平均度的关系
x1, y1 = average_nearest_neighbor_degree(G1)
x2, y2 = average_nearest_neighbor_degree(G2)
x3, y3 = average_nearest_neighbor_degree(G3)

plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.plot(x1, y1, 'ro', label='r='+'%.4f' % r1)
plt.legend(loc=0)
plt.xlabel("$k$")
plt.ylabel("$k_{nn}(k)$")
plt.xscale("log")
plt.yscale("log")
plt.title("citation")
plt.ylim([1, 100])

plt.subplot(132)
plt.plot(x2, y2, 'bo', label='r='+'%.4f' % r2)
plt.legend(loc=0)
plt.xlabel("$k$")
plt.ylabel("$k_{nn}(k)$")
plt.xscale("log")
plt.yscale("log")
plt.title("power")
plt.ylim([1, 100])

# plt.subplot() 函数用于在一个图形窗口中创建子图布局。它接受三个参数，这里传入的 133 表示将整个图形窗口划分为 1 行 3 列（共 3 个子图的布局），最后的数字 3 表示当前操作的是第 3 个子图
plt.subplot(133)
plt.plot(x3, y3, 'go', label='r='+'%.4f' % r3)
plt.legend(loc=0)
plt.xlabel("$k$")
plt.ylabel("$k_{nn}(k)$")
plt.xscale("log")
plt.yscale("log")
plt.title("celegans_metabolic")
plt.ylim([1, 100])

plt.tight_layout()
plt.show()
# 图1递增：正关联的图。



