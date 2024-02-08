import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
# import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import mglearn
from pandas.plotting import scatter_matrix

if __name__ == '__main__':
    iris_dataset = load_iris()
    print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))
    print(iris_dataset['DESCR'][:] + "\n...")
    print("Target names: {}".format(iris_dataset['target_names']))
    print("Feature names: \n{}".format(iris_dataset['feature_names']))
    print("Type of data: {}".format(type(iris_dataset['data'])))
    print("Shape of data: {}".format(iris_dataset['data'].shape))
    print("First five rows of data:\n{}".format(iris_dataset['data'][:5]))
    print("Target:\n{}".format(iris_dataset['target']))

    # X_train, X_test, y_train, y_test = train_test_split(
    #     iris_dataset['data'], iris_dataset['target'], random_state=0)

    # iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
    # # create a scatter matrix from the dataframe, color by y_train
    # matplotlib.use('MacOSX')
    # grr = scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
    #                      hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
    # plt.show()

