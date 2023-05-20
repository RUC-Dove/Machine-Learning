---
description: 来源：https://wizardforcel.gitbooks.io/dm-algo-top10/content/svm-3.html
---

# 支持向量机（SVM)-3.最优间隔分类器

对于前文提出的问题，现在我们终于可以开始解决了！

## 1.问题的转化

我们要解决的问题是：$$min$$$$\frac{1}{2}|w|^2,s.t.y_i(w^T x_i+b)\geqslant1$$\
我们将约束条件改为：$$min$$$$\frac{1}{2}|w|^2,s.t.-y_i(w^T x_i+b)\leqslant1$$\
即：约束函数为$$g_i(w)=-y_i(w^T x_i+b)\leqslant1$$\
考察下图所示的情况：

<figure><img src="../.gitbook/assets/image (11).png" alt="" width="217"><figcaption></figcaption></figure>

实线表示最大间隔超平面，假设 **x** 号是正例，**o** 号是负例。在实线两边的虚线上的三个称作支持向量。

## 2.问题的求解

构造$$Lagrange$$函数如下：

$$L(w,b,\alpha)=\frac{1}{2}\|w\|^2 - \sum_{i=1}^{m} \alpha_i[y_i(w^T x_i+b)-1]$$

对$$w,b$$分别求偏导：

$$\frac{\partial}{\partial w}L(w,b,\alpha)=w-\sum_{i=1}^{m}\alpha_i y_i x_i=0$$\
$$\frac{\partial}{\partial b}L(w,b,\alpha)=\sum_{i=1}^{m}\alpha_i y_i =0$$

将$$w=\sum_{i=1}^{m}\alpha_i y_i x_i$$带入$$Lagrange$$函数得到：

$$L(w,b,\alpha)=\sum_{i=1}^{m}\alpha_i-\frac{1}{2}\sum_{i,j=1}^{m}y_i y_j \alpha_i \alpha_j x_i^T x_j -b\sum_{i=1}^{m}\alpha_iy_i$$

再由于$$\frac{\partial}{\partial b}L(w,b,\alpha)=\sum_{i=1}^{m}\alpha_i y_i =0$$\
我们可以将求解函数简化为$$L(w,b,\alpha)=\sum_{i=1}{m}\alpha_i - \frac{1}{2} \sum_{i,j=1}^{m}y_i y_j \alpha_i \alpha_j x_i^T x_j$$

现在我们联合$$\alpha_i$$这个参数，我们进而得到了如下的二元优化约束条件：

$$\underset{\alpha}{max}$$ $$W(\alpha)=\sum_{i=1}^{m}\alpha_i - \frac{1}{2}\sum_{i,j=1}^{m}y_i y_j \alpha_i \alpha_j x_i^T x_j$$\
$$s.t.$$ $$\alpha_i\geqslant0,i=1,...,m$$\
&#x20;       $$\sum_{i=1}^{m} \alpha_i y_i=0$$

由 2.Lagrange对偶问题的解决过程，当我们求解出对偶问题的解$$\alpha^*$$，根据$$w=\sum_{i=1}^{m}\alpha_i y_i x_i$$即可求出$$w$$（即$$w^*$$)，然后由于$$b^*=-\frac{\underset{i:y_i=-1}{max} w^{*T}x_i+\underset{i:y_i=-1}{min}w^{*T}x_i}{2}$$\
求出$$b$$：距离超平面最近的正的函数间隔等于离超平面最近的负的函数间隔。

