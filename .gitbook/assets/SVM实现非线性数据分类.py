# 导入相关的包
import numpy as np
import pylab as plt  # 绘图功能
from matplotlib.colors import ListedColormap
from sklearn import svm
def plot_decision_regions(x,y,model,resolution=0.02):
    #定义标记符
    markers = ('s','x','o','^','v')
    #定义颜色
    colors = ('red','blue','lightgreen','gray','cyan')
    #ListedColormap方法是将标记符和颜色进行对应
    #在绘图的时候红色表示正方形而蓝色表示叉
    cmap = ListedColormap(colors[:len(np.unique(y))])
    #获取第一个特征中最大值加1和最小值减1
    x1_min,x1_max = x[:,0].min() - 1,x[:,0].max() + 1
    #获取第二个特征中最大值加1和最小值减1
    x2_min,x2_max = x[:,1].min() - 1,x[:,1].max() + 1
    #根据特上面获取到特征的最大最小值构建一个网格坐标
    #通过模拟足够多的数据，来绘制出决策边界
    #resolution表示网格的大小
    '''
    如一个2*2的网格坐标,网格大小为1，网格坐标点如下
    (0,0),(0,1),(0,2)
    (1,0),(1,1),(1,2)
    (2,0),(2,1),(2,2)
    '''
    xx1,xx2 = np.meshgrid(np.arange(x1_min,x1_max,resolution),
                          np.arange(x2_min,x2_max,resolution))
    z = model.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    #绘制边界
    plt.contourf(xx1,xx2,z,alpha=0.4,cmap=cmap)
    #设置坐标的长度
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())
    for idx,cl in enumerate(np.unique(y)):
        #绘点
        plt.scatter(x=x[y == cl,0],y=x[y == cl,1],
                    alpha=0.8,c=cmap(idx),
                    marker=markers[idx],label=cl)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.show()
if __name__ == "__main__":
    #随机生成200个点
    x_xor = np.random.randn(200,2)
    #将数据集变成一个异或的数据集
    #都满足或者都不满足条件返回False，否则返回True
    y_xor = np.logical_xor(x_xor[:,0] > 0,x_xor[:,1] > 0)
    #三元运算符，为True返回1或者返回-1
    y_xor = np.where(y_xor,1,-1)
    svm = svm.SVC(kernel="rbf", random_state=0, gamma=1, C=1.0)
    svm.fit(x_xor, y_xor)
    plot_decision_regions(x_xor, y_xor, svm)