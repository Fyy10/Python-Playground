import numpy as np
from NN import DoubleLayerNN


def load_data():
    file_train = './data/Iris-train.txt'
    file_test = './data/Iris-test.txt'

    data_train = []
    label_train = []
    data_test = []
    label_test = []

    f = open(file_train)
    for line in f:
        data_list = line.split()
        data_train.append(data_list[:-1])
        label_train.append(data_list[-1])
    f.close()
    data_train = np.array(data_train).astype(np.float)
    label_train = np.array(label_train).astype(np.int)

    f = open(file_test)
    for line in f:
        data_list = line.split()
        data_test.append(data_list[:-1])
        label_test.append(data_list[-1])
    f.close()
    data_test = np.array(data_test).astype(np.float)
    label_test = np.array(label_test).astype(np.int)

    return data_train, label_train, data_test, label_test


def main():
    data_train, label_train, data_test, label_test = load_data()
    # print(data_train.shape)
    # print(label_train.shape)
    # print(data_test.shape)
    # print(label_test.shape)

    test_num = 10
    acc = 0
    tmp_acc = 0
    for i in range(test_num):
        model = DoubleLayerNN(in_feat=4, hidden_feat=10, out_feat=3)
        model.train(data_train, label_train, lr=4e-3, batch_size=50, num_batch=2000, verbose=False)
        tmp_acc = model.test_acc(data_test, label_test)
        print('Test {}, accuracy: {:4f}'.format(i, tmp_acc))
        acc += tmp_acc / test_num

    print('Average test accuracy: {:4f}'.format(acc))


if __name__ == '__main__':
    main()
