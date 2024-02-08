from mglearn.plots import plot_linear_regression_wave
from mglearn.datasets import make_wave
from mglearn.datasets import load_extended_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
import numpy as np
import matplotlib.pyplot as plt
import mglearn
import matplotlib


matplotlib.use('MacOSX')

def main():
    # Your code here
    print("Hello, world!")



def example_1():
    """
    线性回归，普通最小二乘法
    """
    X, y = mglearn.datasets.make_wave(n_samples=60)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    lr = LinearRegression().fit(X_train, y_train)
    print("lr.coef_: {}".format(lr.coef_))
    print("lr.interept_: {}".format(lr.intercept_))

    print("Training set score: {:.2f}".format(lr.score(X_train, y_train)))
    print("Test set score: {:.2f}".format(lr.score(X_test, y_test)))


def example_2():
    """
    波士顿房价数据集
    """
    X, y = mglearn.datasets.load_extended_boston()

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    lr = LinearRegression().fit(X_train, y_train)
    print("Training set score: {:.2f}".format(lr.score(X_train, y_train)))
    print("Test set score: {:.2f}".format(lr.score(X_test, y_test)))


def example_3():
    """
    岭回归 ridge regression
    """
    X, y = mglearn.datasets.load_extended_boston()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    ridge = Ridge().fit(X_train, y_train)
    print("Training set score: {:.2f}".format(ridge.score(X_train, y_train)))
    print("Test set score: {:.2f}".format(ridge.score(X_test, y_test)))


def example_4():
    """
    不同岭回归与线性回归的系数比较
    """        
    X, y = mglearn.datasets.load_extended_boston()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    lr = LinearRegression().fit(X_train, y_train)
    ridge1 = Ridge().fit(X_train, y_train)
    ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)
    ridge10 = Ridge(alpha=10).fit(X_train, y_train)
    plt.plot(ridge1.coef_, 's', label="Ridge alpha=1")
    plt.plot(ridge01.coef_, '^', label="Ridge alpha=0.1")
    plt.plot(ridge10.coef_, 'v', label="Ridge alpha=10")

    plt.plot(lr.coef_, 'o', label='Linear Regression')
    plt.xlabel("Coefficient index")
    plt.xlabel("Coefficient magnitude")
    plt.hlines(0, 0, len(lr.coef_))
    plt.ylim(-25, 25)
    plt.legend()
    plt.show()


def example_5():
    """
    来自 chatgpt 对 alpha 的解释：
    在线性拟合或线性回归分析中，alpha 值通常指的是正则化参数。这里有两种常见的情景，可能涉及到 alpha 值：

岭回归（Ridge Regression）：

在岭回归中，alpha 是一个正则化项（L2 正则化），它添加到损失函数中以防止模型过拟合。这个参数控制着正则化的强度。
较大的 alpha 值增加了对模型复杂度的惩罚，倾向于使得回归系数更小，降低了模型的复杂度，但可能导致欠拟合。
较小的 alpha 值减少了对模型复杂度的惩罚，使得模型更接近于普通的最小二乘法，但可能导致过拟合。
Lasso 回归（Least Absolute Shrinkage and Selection Operator）：

在 Lasso 回归中，alpha 代表 L1 正则化项，它同样是为了防止过拟合而引入的。
与岭回归类似，alpha 的值决定了正则化的强度。不同的是，Lasso 回归倾向于产生稀疏参数；即，它可以将某些回归系数完全压缩至零，从而实现特征选择。
在这两种方法中，alpha 的选择是非常关键的，因为它直接影响模型的复杂性和拟合能力。通常，alpha 的最佳值通过交叉验证等方法确定。这些方法在不同的 alpha 值下评估模型性能，以找到最佳平衡点，既不过拟合也不欠拟合。

在其他上下文中，alpha 的含义可能有所不同，但在线性拟合或回归分析中，它通常与正则化相关。
    """
    X, y = mglearn.datasets.load_extended_boston()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    lasso = Lasso().fit(X_train, y_train)
    print("Training set score: {:.2f}".format(lasso.score(X_train, y_train)))
    print("Test set score: {:.2f}".format(lasso.score(X_test, y_test)))
    print("Number of features used: {}".format(np.sum(lasso.coef_ != 0)))

    # 降低欠拟合，减小 alpha 值，增加 max_iter
    lasso001 = Lasso(alpha=0.01, max_iter=100000).fit(X_train, y_train)
    print("Training set score: {:.2f}".format(lasso001.score(X_train, y_train)))
    print("Test set score: {:.2f}".format(lasso001.score(X_test, y_test)))
    print("Number of features used: {}".format(np.sum(lasso001.coef_ != 0)))

    # 如果 alpha 值太小，会消除正则化的效果，过拟合
    lasso00001 = Lasso(alpha=0.0001, max_iter=100000).fit(X_train, y_train)
    print("Training set score: {:.2f}".format(lasso00001.score(X_train, y_train)))
    print("Test set score: {:.2f}".format(lasso00001.score(X_test, y_test)))
    print("Number of features used: {}".format(np.sum(lasso00001.coef_ != 0)))


def example_6():
    X, y = mglearn.datasets.make_forge()
    fig, axes = plt.subplots(1, 2, figsize=(10, 3))

    for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
        clf = model.fit(X, y)
        mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5, ax=ax, alpha=.7)
        mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
        ax.set_title("{}".format(clf.__class__.__name__))
        ax.set_xlabel("Feature 0")
        ax.set_ylabel("Feature 1")
    axes[0].legend()
    plt.show()
    

if __name__ == '__main__':
    main()
    # example_1()
    # example_2()
    # example_3()
    # example_4()
    # mglearn.plots.plot_ridge_n_samples()
    # plt.show()
    # example_5()
    example_6()

    