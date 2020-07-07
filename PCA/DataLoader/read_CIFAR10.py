import pickle
import numpy as np
import matplotlib.pyplot as plt


def load_batch(base_dir):
    """
    :param base_dir: path of data
    :return: a numpy array of shape [n, 32, 32, 3]
    """
    print('Loading CIFAR10...')
    data_dir = base_dir + 'CIFAR10/data_batch_1'
    with open(data_dir, 'rb') as batch:
        data_dict = pickle.load(batch, encoding='bytes')
    # data: 10000 x 3072 numpy array (uint8), 每一行表示一个 32 x 32 的彩色图片（1024R 1024G 1024B）
    # labels: a list of 10000 numbers，表示第 i 张图片的类别
    data = data_dict[b'data']
    data = data.reshape(-1, 3, 32, 32)
    data = data.transpose(0, 2, 3, 1)
    # use the first 2k images
    data = data[:2000, :, :, :]
    # data: [n, 32, 32, 3]
    print('Done!')
    return data
