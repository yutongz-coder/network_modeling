# 介数：用于衡量节点在网络中的作用和影响力，介数分为节点介数和边介数
# 一个图的k-核是指反复（比如k=1的情况，反复的意思是去掉度为1的节点之后，又出现原本度大于1但是现在度等于1的节点，那也要去掉）去掉度值小于等于k的节点及其连线后所剩余的子图，该子图的节点数就是该核的大小
# 若一个节点属于k-核，而不属于(k+1)-核，则此节点的核度为k
# 节点核度的最大值叫做网络的核度
# 节点的核度可以说明节点在核中的深度，核度的最大值对应着网络结构中最中心的位置。k-核解析可用来描述度分布所不能描述的网络特征，揭示源于系统特殊结构的结构和层次性质
# 网络密度：指一个网络中各节点之间联络的紧密程度，d(G)=2M/[N(N-1)],其中M为网络中实际拥有的连接数，N为网络节点数
# 实际网络中能够发现的最大密度值为0.5
# 度中心性分为节点度中心性和网络度中心性
# 节点度中心性（局部）指节点在其与之直接相连的邻居节点当中的中心程度：C_D(v_i)=k_i/(N-1)
# 网络度中心性（全局）侧重节点在整个网络的中心程度，体现整个网络的集中程度
import networkx as nx
import matplotlib.pyplot as plt

BA = nx.barabasi_albert_graph(20, 2)
# 节点介数
bc = nx.betweenness_centrality(BA)
# 结果以字典形式输出
print("节点介数：", bc)

# 获取介数最大的节点标签
max_id = max(bc, key=bc.get)
print("介数最大的节点标签：", max_id)
# 绘制网络
nx.draw(BA, node_size=500, with_labels=True)
plt.show()

# 边介数
ebc = nx.edge_betweenness_centrality(BA)
print("边介数：", ebc)

# 核度
ks = nx.core_number(BA)
print("BA核度：", ks)

# 换一个网络
kcg = nx.karate_club_graph()
ks = nx.core_number(kcg)
print("kcg核度：", ks)
# 获取核度最大的节点的标签
max_id = max(ks, key=ks.get)
print("核度最大的节点的标签:", max_id)
nx.draw(kcg, node_size=500, with_labels=True)
plt.show()

# 几种常用的中心性指标
# 分别生成ER和BA无标度网络，节点数设定为N=100
GER = nx.erdos_renyi_graph(100, 0.08)
GBA = nx.barabasi_albert_graph(100, 4)
# 度中心性
dc1 = nx.degree_centrality(GER)
dc2 = nx.degree_centrality(GBA)
# 介数中心性
bc1 = nx.betweenness_centrality(GER)
bc2 = nx.betweenness_centrality(GBA)
# 接近度中心性
cc1 = nx.closeness_centrality(GER)
cc2 = nx.closeness_centrality(GBA)
# 特征向量中心性
ec1 = nx.eigenvector_centrality(GER)
ec2 = nx.eigenvector_centrality(GBA)

# 绘图比较
plt.figure(figsize=(10, 10))
plt.subplot(221)
plt.plot(dc1.keys(), dc1.values(), 'ro', label='ER')
plt.plot(dc2.keys(), dc2.values(), 'b--', label='BA')
plt.legend(loc=0)
plt.xlabel("node label")
plt.ylabel("dc")
plt.title("degree_centrality")

plt.subplot(222)
plt.plot(bc1.keys(), bc1.values(), 'ro', label='ER')
plt.plot(bc2.keys(), bc2.values(), 'b--', label='BA')
plt.legend(loc=0)
plt.xlabel("node label")
plt.ylabel("bc")
plt.title("betweenness_centrality")

plt.subplot(223)
plt.plot(cc1.keys(), cc1.values(), 'ro', label='ER')
plt.plot(cc2.keys(), cc2.values(), 'b--', label='BA')
plt.legend(loc=0)
plt.xlabel("node label")
plt.ylabel("cc")
plt.title("closeness_centrality")

plt.subplot(224)
plt.plot(ec1.keys(), ec1.values(), 'ro', label='ER')
plt.plot(ec2.keys(), ec2.values(), 'b--', label='BA')
plt.legend(loc=0)
plt.xlabel("node label")
plt.ylabel("ec")
plt.title("eigenvector_centrality")
plt.show()

