import torch
from torch import nn, optim
import numpy as np
from DataLoader import DataLoader


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

    data_train = torch.tensor(data_train).float()
    label_train = torch.tensor(label_train).long()
    data_test = torch.tensor(data_test).float()
    label_test = torch.tensor(label_test).long()

    return data_train, label_train, data_test, label_test


def main():
    model = nn.Sequential(
        nn.Linear(4, 10),
        nn.ReLU(),
        nn.Linear(10, 3)
    )
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=4e-3)

    data_train, label_train, data_test, label_test = load_data()
    data_loader = DataLoader(data_train, label_train, batch_size=50)

    for i in range(1000):
        data, label = data_loader.get_batch()
        optimizer.zero_grad()
        model_out = model(data)
        loss = criterion(model_out, label)
        loss.backward()
        optimizer.step()
        # print('Batch: {} Loss: {}'.format(i, loss.item()))

    pred = model(data_test)
    labels = torch.argmax(pred, dim=1)

    acc = (labels == label_test).sum().float() / labels.size(0)

    print('Accuracy: {:4f}'.format(acc.item()))


if __name__ == '__main__':
    main()
