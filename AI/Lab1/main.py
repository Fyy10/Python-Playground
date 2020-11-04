import numpy as np
from DecisionTree import DecisionTree
from sklearn import tree
import matplotlib.pyplot as plt


def load_data():
    file_train = './data/traindata.txt'
    file_test = './data/testdata.txt'

    data_train = []
    label_train = []
    data_test = []
    label_test = []

    # load train data
    f = open(file_train)
    for line in f:
        data = line.split('\t')
        # not a data sample
        if len(data) == 1:
            continue

        # remove '\n'
        data[-1] = data[-1][:-1]

        # convert
        for i in range(len(data) - 1):
            data[i] = float(data[i])
        data[-1] = int(data[-1])

        # append
        data_train.append(data[:-1])
        label_train.append(data[-1])

    # load test data
    f = open(file_test)
    for line in f:
        data = line.split('\t')
        # not a data sample
        if len(data) == 1:
            continue

        # remove '\n'
        data[-1] = data[-1][:-1]

        # convert
        for i in range(len(data) - 1):
            data[i] = float(data[i])
        data[-1] = int(data[-1])

        # append
        data_test.append(data[:-1])
        label_test.append(data[-1])

    # numpy array
    data_train = np.array(data_train)
    label_train = np.array(label_train)
    data_test = np.array(data_test)
    label_test = np.array(label_test)

    return data_train, label_train, data_test, label_test


def main():
    eps = 1e-6

    # load data
    data_train, label_train, data_test, label_test = load_data()
    # (75, 4), (75,), (75, 4), (75,)
    # print(data_train.shape, label_train.shape, data_test.shape, label_test.shape)
    dt = DecisionTree()
    dt.train(data_train, label_train)
    dt.display(dt.root)
    prediction = dt.predict(data_test)
    # print('myxxxx', prediction)

    # accuracy
    acc = (prediction == label_test).sum() / prediction.shape[0]
    print('Accuracy: {:.4f}'.format(acc))

    # test (calculate accuracy)
    acc_test = test(data_train, label_train, data_test, label_test)

    assert np.abs(acc - acc_test) <= eps


def test(data_train, label_train, data_test, label_test):
    dt = tree.DecisionTreeClassifier(criterion='entropy')
    dt.fit(data_train, label_train)
    labels = dt.predict(data_test)
    # print('oracle', labels)
    accuracy = (labels == label_test).sum() / labels.shape[0]
    # tree.plot_tree(dt)
    # plt.show()
    return accuracy


if __name__ == '__main__':
    main()
