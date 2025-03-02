# 网络中的两节点v_i和v_j之间经历边数最少的一条简单路径（经历的边各不相同），称为测地线
# 测地线的边数d_ij称为两节点v_i和v_j之间的距离（或叫测地线距离）
# 1/d_ij 称为节点v_i和v_j之间的效率，记为epsilon_ij，效率用来度量节点间的信息传递速度
# 网络的全局效率：图中所有节点对效率的平均值
# 局部效率是基于节点的邻居节点所构成的子图的全局效率来定义
# 网络的直径D定义为所有距离d_ij中的最大值
# 平均距离：（特征路径长度）L定义为所有节点对之间的连接程度，它描述了网络中节点间的平均分离程度
# L=(1/N^2) * \Sigma^N_{j=1} * \Sigma^N_{i=1}d_ij
# 对于无向简单图来说，d_ij=d_ji, d_ii=0, 上式简化为L=2/N(N-1) * \Sigma^N_{i=1} * \Sigma^N_{j=i+1}d_ij
# 很多实际网络虽然节点数巨大，但是平均距离小得惊人，就是所谓的小世界效应
# 集聚系数C用以捕获给定节点的邻居节点之间的连接程度，C=0，所有节点都是孤立节点，C=1，节点两两之间都有边连接的完全图
# 节点v_i的最近平均度值定义为k_{nn,i}=[\Sigma_j a_ij * k_j]/k_i
# 所有度值为k的节点的最近邻平均度值的平均值k_{nn}(k)=(\Sigma_i k_{nn,i})/[N*P(k)],N为节点综述，P(k)为度分布函数
# 如果k_{nn}(k)是随着k上升的增函数，则说明度值大的节点倾向于和度值大的节点连接，网络具有正相关特性，称之为同配网络；反之网络具有负相关特性，称之为异配网络
# Newman利用边两端节点的度Pearson相关系数r来描述网络的度-度相关性，r<0:网络负相关；r=0:网络不相关；r>0:网络正相关

import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.barabasi_albert_graph(1000, 3)
print("网络的直径为：", nx.diameter(G1))
# 计算节点对i,j之间的效率，前提是这两个节点之间有路径可达
print(nx.efficiency(G1, 1, 5))
print(nx.shortest_path_length(G1, 1, 5))
# 局部效率
print("局部效率", nx.local_efficiency(G1))
# 全局效率
print("全局效率", nx.global_efficiency(G1))
# 整个网络的平均距离
print("平均距离", nx.average_shortest_path_length(G1))
# 1000个节点，但是平均距离只有3.几，距离是两节点之间最短路径长度

# 平均集聚系数
print("平均集聚系数:", nx.average_clustering(G1))
# 全局集聚系数
print("全局集聚系数", nx.transitivity(G1))
