---
description: 来源：https://wizardforcel.gitbooks.io/dm-algo-top10/content/svm-2.html
---

# 支持向量机（SVM）-2.Lagrange对偶问题

本节为求解第一节问题的过渡章节

## 1.求解函数的转换

考察约束函数如下：$$\underset{w}{min} f(w)$$ $$s.t.$$ $$g_i(w)\leqslant0,i=1,...,k$$\
&#x20;                                                         $$h_i(w)=0,i=1,...,l$$

根据上述式子的两个约束条件，定义**一般化的拉格朗日公式**为：

$$L(w,\alpha,\beta)=f(w)+\sum_{i=1}^{k} \alpha_i g_i(w)+ \sum_{i=1}^{l} \beta_i h_i(w)$$

上式中的$$\alpha_i$$和$$\beta_i$$称为**拉格朗日算子**

我们记$$\theta_p(w)=\underset{\alpha,\beta:\alpha_i\geqslant0}{max} L(w,\alpha,\beta)$$

显然，对于两个约束条件（primal constraints）：

$$g_i(w)\leqslant0,i=1,...,k$$\
$$h_i(w)=0,i=1,...,l$$

如果这两个条件不全部满足的话，总存在充分大的$$\alpha_i$$和$$\beta_i$$，使得：$$\theta_p(w)$$趋向于正无穷。所以，我们得到以下式子：

$$\theta_p(w)=f(w)$$ $$if$$ $$w$$ $$satisfies$$ $$primal$$ $$constraints$$.

由此，我们原来要求的$$\underset{w}{min}f(w)$$就转换为求：$$\underset{w}{min}\theta_p(w)$$

## 2.拉格朗日对偶问题的求解

我们定义：

$$\theta_D(\alpha,\beta)=\underset{w}{min}L(w,\alpha,\beta)$$

借由$$\theta_D(\alpha,\beta)$$，提出原拉格朗日式子的对偶问题，即先求拉格朗日式关于$$w$$的最小值（将$$\alpha,\beta$$看作常量），再求最大值。这样，相较于原问题更换了$$min$$和$$max$$的顺序：

$$\underset{\alpha,\beta:\alpha_i\geqslant0}{max}\theta_D(\alpha,\beta)$$$$=$$$$\underset{\alpha,\beta:\alpha_i\geqslant0}{max}\underset{w}{min}L(w,\alpha,\beta)$$

&#x20;一般情况下：我们有

$$d^*$$$$=$$$$\underset{\alpha,\beta:\alpha_i\geqslant0}{max}\underset{w}{min}L(w,\alpha,\beta)$$$$\leqslant$$$$\underset{w}{min}\underset{\alpha,\beta:\alpha_i\geqslant0}L(w,\alpha,\beta)$$$$=$$$$p^*$$

可以证明，当$$f,g$$都是凸函数，$$h$$是仿射的（即存在$$a_i,b_i$$使得$$h_i(w)=a_i^T w+b_i)$$，且存在$$w$$使得对于所有的$$i$$都有：$$g_i(w)<0$$时，一定存在$$w^*$$是原问题的解，$$\alpha^*,\beta^*$$是对偶问题的解，同时满足$$p^*$$=$$d^*$$=$$L(w^*,\alpha^*,\beta^*)$$，而且$$w^*,\alpha^*,\beta^*$$还满足$$Karush-Kuhn-Tucker(KKT)$$条件：

![](<../.gitbook/assets/image (13).png>)

我们从第三个式子和第四个式子可以得到：如果$$\alpha_i^*>0$$，那么$$g_i(w^*)=0$$，这也就是说，如果$$g_i(w^*)=0$$，$$w$$处于可行域的边界上，这才是真正起作用的约束条件，而其他位于可行域内部（即$$g_i(w^*)<0$$）都是不起作用的约束。
