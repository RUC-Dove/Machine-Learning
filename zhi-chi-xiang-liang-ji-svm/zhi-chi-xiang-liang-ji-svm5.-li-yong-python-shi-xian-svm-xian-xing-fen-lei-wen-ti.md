---
description: 来源：https://blog.csdn.net/Recursions/article/details/124367464
---

# 支持向量机（SVM）-5.利用Python实现SVM线性分类问题

{% file src="../.gitbook/assets/SVM解决线性分类问题.py" %}

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

## 输出结果：

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

## 源代码：

import numpy as np import pylab as pl # 绘图功能 from sklearn import svm

np.random.seed(0) # 让每次运行程序生成的随机样本点不变

Y = \[0] \* 20 + \[1] \* 20&#x20;

clf = svm.SVC(kernel='linear') clf.fit(X, Y)

w = clf.coef\_\[0] # w 是一个二维数据，coef 就是 w = \[w0,w1] a = -w\[0] / w\[1] # 斜率 xx = np.linspace(-5, 5) # 从 -5 到 5 产生一些连续的值（随机的）

yy = a \* xx - (clf.intercept\_\[0]) / w\[1] # 带入 x 的值，获得直线方程

b = clf.support\_vectors\_\[0] # 取出第一个支持向量点 yy\_down = a \* xx + (b\[1] - a \* b\[0]) b = clf.support\_vectors\_\[-1] # 取出最后一个支持向量点 yy\_up = a \* xx + (b\[1] - a \* b\[0])

print("w: ", w) print("a: ", a) print("support\_vectors\_: ", clf.support\_vectors\_) print("clf.coef\_: ", clf.coef\_)

pl.plot(xx, yy, 'k-') pl.plot(xx, yy\_down, 'k--') pl.plot(xx, yy\_up, 'k--')

pl.scatter(clf.support\_vectors\_\[:, 0], clf.support\_vectors\_\[:, 1], s=80, facecolors='none') pl.scatter(X\[:, 0], X\[:, 1], c=Y, cmap=pl.cm.Paired)

pl.axis('tight') pl.show()

