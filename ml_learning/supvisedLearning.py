import matplotlib
import mglearn
import os
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
from deprecated import deprecated

matplotlib.use('MacOSX')


def main():
    os.system('export DISPLAY=:1')


def example_2():
    """
    forge数据集的散点图
    """
    x, y = mglearn.datasets.make_forge()
    mglearn.discrete_scatter(x[:, 0], x[:, 1], y)
    plt.legend(["Class 0", "Class 1"], loc=4)
    plt.xlabel("First feature")
    plt.ylabel("Second feature")
    plt.show()
    print("x.shape: {}".format(x.shape))


def example_3():
    """
    wave数据集的图像， x轴表示特征，y轴表示回归目标
    """
    x,y = mglearn.datasets.make_wave(n_samples=40)
    plt.plot(x, y, 'o')
    plt.ylim(-3, 3) 
    plt.xlabel("Feature")
    plt.ylabel("Target")
    plt.show()


def example_4():
    """
    威斯康星州乳腺癌数据集
    """
    cancer = load_breast_cancer()
    print("cancer.keys(): \n{}".format(cancer.keys()))
    print("Shape of cancer data: {}".format(cancer.data.shape))
    print("Sample counts per class:\n{}".format(
        {n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))
    print("Feature names:\n{}".format(cancer.feature_names))


@deprecated
def example_5():
    """
    `load_boston` has been removed from scikit-learn since version 1.2.
    波士顿房价数据集    
    removed
    """
    # boston = load_boston()
    # print("Data shape: {}".format(boston.data.shape))
    # X, y = mglearn.datasets.load_extended_boston()
    # print("X.shape: {}".format(X.shape))


def example_6():
    """
    knn算法 - K近邻分类法
    """
    # mglearn.plots.plot_knn_classification(n_neighbors=1)
    mglearn.plots.plot_knn_classification(n_neighbors=3)
    plt.show()


def example_7():
    """
    评估make_forge的泛化能力
    """    
    X, y = mglearn.datasets.make_forge()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_train, y_train)
    print("Test set predictions: {}".format(clf.predict(X_test)))
    print("Test set accuracy: {:.2f}".format(clf.score(X_test, y_test)))


def example_8():
    """
    决策边界
    """
    X, y = mglearn.datasets.make_forge()
    fig, axes = plt.subplots(1, 3, figsize=(10, 3))
    for n_neighbors, ax in zip([1, 3, 9], axes):
        # fit方法返回对象本身，所以我们可以将实例化和你和拟合放在一行代码中
        clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
        mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
        mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
        ax.set_title("{} neighbor(s)".format(n_neighbors))
        ax.set_xlabel("feature 0")
        ax.set_ylabel("feature 1")
    axes[0].legend(loc=3)
    plt.show()


def example_9():
    """
    """
    cancer = load_breast_cancer()
    # print("cancer data: {}".format(cancer.target))
    X_train, X_test, y_train, y_test = train_test_split(
        cancer.data, cancer.target, stratify=cancer.target, random_state=66)
    training_accuracy = []
    test_accuracy = []
    # n_neighbours取值从1到10
    neighbors_settings = range(1, 11)
    for n_neighbors in neighbors_settings:
        # 构建模型
        clf = KNeighborsClassifier(n_neighbors=n_neighbors)
        clf.fit(X_train, y_train)
        # 记录训练集精度
        training_accuracy.append(clf.score(X_train, y_train))
        # 记录泛化精度
        test_accuracy.append(clf.score(X_test, y_test))
    plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
    plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("n_neighbors")
    plt.legend()
    plt.show()


def example_10():
    """
    k近邻回归
    """
    # mglearn.plots.plot_knn_regression(n_neighbors=1)
    # mglearn.plots.plot_knn_regression(n_neighbors=3)
    # plt.show()
    X, y = mglearn.datasets.make_wave(n_samples=40)

    # 将wave数据集分为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    # 模型实例化，并将邻居个数设为3
    reg = KNeighborsRegressor(n_neighbors=3)
    # 利用训练数据和训练目标值来拟合模型
    print("{}".format(X_train))
    print("{}".format(y_train))
    reg.fit(X_train, y_train)
    # print("Test set predictions:\n{}".format(reg.predict(X_test)))
    print("Test set R^2: {:.2f}".format(reg.score(X_test, y_test)))


def example_11():
    """
    分析KNeighborsRegressor
    """
    X, y = mglearn.datasets.make_wave(n_samples=40)

    # 将wave数据集分为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    # 创建1000个数据点，在-3和3之间均匀分布
    line = np.linspace(-3, 3, 1000).reshape(-1, 1)
    for n_neighbors, ax, in zip([1, 3, 9], axes):
        # 利用1个、3个或9个邻居分别进行预测
        reg = KNeighborsRegressor(n_neighbors=n_neighbors)
        reg.fit(X_train, y_train)
        ax.plot(line, reg.predict(line))
        ax.plot(X_train, y_train, '^', c=mglearn.cm2(0), markersize=8)
        ax.plot(X_test, y_test, 'v', c=mglearn.cm2(1), markersize=8)
        ax.set_title(
            "{} neighbor(s)\n train score: {:.2f} test score: {:.2f}".format(
                n_neighbors, reg.score(X_train, y_train),
                reg.score(X_test, y_test)))
        ax.set_xlabel("Feature")
        ax.set_ylabel("Target")
    axes[0].legend(["Model predictions", "Training data/target",
                    "Test data/target"], loc="best")
    plt.show()

if __name__ == '__main__':
    main()
    # example_2()
    # example_3()
    # example_4()
    # example_6()
    # example_7()
    # example_8()
    # example_9()
    # example_10()
    example_11()
