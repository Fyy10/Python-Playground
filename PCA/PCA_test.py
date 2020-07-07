from sklearn import decomposition
import numpy as np
import matplotlib.pyplot as plt
from PCA import PCA
from DataLoader import read_CIFAR10
from DataLoader import read_DomainNet
from tqdm import tqdm

base_dir = './data/'


# test pca algorithm
def test_pca(n, m):
    # n: num of row
    # m: num of column
    for i in tqdm(range(n * m)):
        # make some toy data for random test
        test_data = np.random.rand(10, 100)
        # test_data: [10, 100]
        # set pca
        pca = decomposition.PCA(n_components=2)
        new_data = pca.fit_transform(test_data)
        # new_data: [10, 2]
        new_data_homemade = PCA(test_data, 2)
        # new_data_homemade: [10, 2]
        plt.subplot(n, m, i+1)
        plt.scatter(new_data[:, 0], new_data[:, 1], c='blue')
        plt.scatter(new_data_homemade[:, 0], new_data_homemade[:, 1], c='red')
    plt.show()


def display_cifar10():
    test_data_raw = read_CIFAR10.load_batch(base_dir)
    # test_data_raw: [n, 32, 32, 3]
    # pick a channel
    test_data = test_data_raw[:, :, :, 0]
    test_data = test_data.reshape(-1, 32 * 32)
    # test_data: [n, 32 * 32]
    # set pca
    pca = decomposition.PCA(n_components=2)
    new_data = pca.fit_transform(test_data)
    # new_data: [n, 2]
    # plt.scatter(new_data[:, 0], new_data[:, 1], c='blue')
    # plt.xlim(-4000, 4000)
    # plt.ylim(-3000, 3000)
    # display images
    for i in tqdm(range(test_data.shape[0])):
        img = test_data_raw[i, :, :, :]
        # [left, bottom, width, height]
        plt.axes(((new_data[i, 0]+4000) / 8000, (new_data[i, 1]+3000) / 6000, 0.05, 0.05))
        plt.axis('off')
        plt.imshow(img)
    plt.show()


def display_DomainNet():
    # display DomainNet images in one figure
    test_data_raw = read_DomainNet.load_batch(base_dir)
    # test_data_raw: [3450, 200, 300, 3]
    # 选取一个通道
    test_data = test_data_raw[:, :, :, 0]
    test_data = test_data.reshape(-1, 200 * 300)
    # test_data: [3450, 200 * 300]
    # set pca
    pca = decomposition.PCA(n_components=2)
    new_data = pca.fit_transform(test_data)
    # new_data: [3450, 2]
    # plt.scatter(new_data[:, 0], new_data[:, 1], c='blue')
    # plt.xlim(-30000, 40000)
    # plt.ylim(-30000, 30000)
    # display images
    for i in tqdm(range(test_data.shape[0])):
        img = test_data_raw[i, :, :, :]
        # [left, bottom, width, height]
        plt.axes(((new_data[i, 0]+30000) / 70000, (new_data[i, 1]+30000) / 60000, 0.05, 0.05))
        plt.axis('off')
        plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    test_pca(2, 5)
    # display_cifar10()
    # display_DomainNet()
