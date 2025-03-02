# 规则网络：每个节点具有相同的度，所以其度分布集中在一个单一尖峰上
# 完全随机网络：度分布具有Poisson分布的形式，每一条边的出现概率是相等的，大多数节点的度是基本相同的，并接近于网络平均度<k>，远离峰值<k>，度分布则按指数形式急剧下降，把这类网络称为均匀网络
# 无标度网络：具有幂指数形式的度分布，所谓无标度是指一个概率分布函数F(x)对于任意给定常数a存在常数b使得F(x)满足F(ax)=bF(x)
# 幂律分布是唯一满足无标度条件的概率分布函数，绝大多数节点的度相对很低，也存在少量度值相对很高的节点，把这类网络称为非均匀网络（异质网络）

import networkx as nx
import matplotlib.pyplot as plt

# 泊松分布，以ER随机网络为例
# 创建一个ER随机网络
n = 10000  # 节点个数
p = 0.001  # 连边概率
ER = nx.erdos_renyi_graph(n, p)

# 获取平均度
d = dict(nx.degree(ER))
print("平均度为：", sum(d.values())/len(ER.nodes))

# 获取所有可能的度值对应的概率
x = list(range(max(d.values())+1))
# 遍历 nx.degree_histogram(ER) 返回的列表中的每个元素 i（也就是每个度值对应的节点数量）
y = [i/n for i in nx.degree_histogram(ER)]
# 绘制度分布
# r 表示线条和标记的颜色为红色
# o 表示绘制的数据点标记形状为圆形（可以使用其他字符来表示不同形状，比如 s 表示方形，^ 表示三角形等）
# - 表示用连线将数据点连接起来，形成连续的线条，如果只想绘制散点图，不显示连线，可以去掉这个字符
plt.plot(x, y, "ro-")
plt.xlabel("$k$")
plt.ylabel("$p_k$")
plt.show()

# 幂律分布：以BA无标度网络为例子
m = 3
BA = nx.barabasi_albert_graph(n, m)
# 获取平均度
d = dict(nx.degree(BA))
print("平均度为：", sum(d.values())/len(BA.nodes))
# 获取所有可能的度值对应的概率
x = list(range(max(d.values())+1))
# 遍历 nx.degree_histogram(ER) 返回的列表中的每个元素 i（也就是每个度值对应的节点数量）
y = [i/n for i in nx.degree_histogram(BA)]
plt.plot(x, y, "bo-")
plt.xlabel("$k$")
plt.ylabel("$p_k$")
plt.show()
# 在双对数坐标轴下显示
plt.plot(x, y, "yo-")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("$k$")
plt.ylabel("$p_k$")
plt.show()
# 在双对数坐标下要把横坐标的0值排除掉
new_x = []
new_y = []
for i in range(len(x)):
    if y[i] != 0:
        new_x.append(x[i])
        new_y.append(y[i])
plt.plot(new_x, new_y, "yo-")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("$k$")
plt.ylabel("$p_k$")
plt.show()
