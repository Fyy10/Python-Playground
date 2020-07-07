import numpy as np
import matplotlib.pyplot as plt
from PCA import PCA
from DataLoader import read_CIFAR10
from DataLoader import read_DomainNet
import argparse
import os
from PIL import Image
# import tkinter as tk

base_dir = './data/'

# top = tk.Tk()
# top.mainloop()

parser = argparse.ArgumentParser(description='Image Searching using PCA')
# image file name
parser.add_argument('--filename', type=str, help='想要进行检索的图片名')
# set dataset
parser.add_argument('--dataset', type=str, help='选择查询的数据集（CIFAR10或DomainNet），默认情况下读取images文件夹中的所有图片作为数据集')
# number of image to search for (row)
parser.add_argument('--num_row', type=int, metavar='N', default=2, help='展示相似图片的行数，默认为2')
# number of image to search for (column)
parser.add_argument('--num_col', type=int, metavar='N', default=5, help='展示相似图片的列数，默认为5')
# number of dimension to reserve
parser.add_argument('--num_dim', type=int, metavar='D', default=100, help='使用PCA保留的维数，默认为100')

args = parser.parse_args()


def main(args):
    print('Searching for images similar to', args.filename)

    # 读取用于搜索的图片
    img = Image.open('./' + args.filename)
    # img: [height, width, RGB], numpy array

    # read dataset to variable data
    if args.dataset is None:
        print('Dataset not set, reading image files from default directory...')
        image_dir = './images/'
        image_list = os.listdir(image_dir)
        data = []
        data_raw = []
        for image in image_list:
            img_arr = Image.open(image_dir + image)
            img_arr = img_arr.resize((50, 50))
            img_arr = np.array(img_arr)
            data.append(img_arr)
        data = np.array(data)
        # data: [n, 50, 50, 3]
        data_raw = data

        # resize用于搜索的图片，注意在PIL的resize中，先width再height
        img = img.resize((50, 50))
        print('Done!')

    elif args.dataset == 'CIFAR10':
        data = read_CIFAR10.load_batch(base_dir)
        # data: [2000, 32, 32, 3]
        # raw data for display
        data_raw = data

        # resize用于搜索的图片，注意在PIL的resize中，先width再height
        img = img.resize((32, 32))

    elif args.dataset == 'DomainNet':
        data = read_DomainNet.load_small_batch(base_dir)
        # data: [3450, 40, 60, 3]
        # raw data for display
        # data_raw = read_DomainNet.load_batch(base_dir)
        data_raw = data

        # resize用于搜索的图片，注意在PIL的resize中，先width再height
        img = img.resize((60, 40))

    print('Computing...')
    img = np.array(img)

    # 分别对 3 个 channel 进行处理
    # channel R
    data_R = data[:, :, :, 0]
    img_R = img[:, :, 0]
    data_R = data_R.reshape(data_R.shape[0], -1)
    # data_R: [n, height * width]
    img_R = img_R.reshape(1, -1)
    # img_R: [1, height * width]
    z_R = PCA(data_R, args.num_dim, img_R)
    # z_R: [n+1, num_dim]

    # channel G
    data_G = data[:, :, :, 1]
    img_G = img[:, :, 1]
    data_G = data_G.reshape(data_G.shape[0], -1)
    # data_G: [n, height * width]
    img_G = img_G.reshape(1, -1)
    # img_G: [1, height * width]
    z_G = PCA(data_G, args.num_dim, img_G)
    # z_G: [n+1, num_dim]

    # channel B
    data_B = data[:, :, :, 2]
    img_B = img[:, :, 2]
    data_B = data_B.reshape(data_B.shape[0], -1)
    # data_B: [n, height * width]
    img_B = img_B.reshape(1, -1)
    # img_B: [1, height * width]
    z_B = PCA(data_B, args.num_dim, img_B)
    # z_B: [n+1, num_dim]

    # 取 3 个 channel 的均值
    z = (z_R + z_G + z_B) / 3
    # 将用于检索的图像拆分出来（z的最后一个）
    z_img = z[-1, :]
    z = z[:-1, :]

    # 计算欧式距离
    dist = np.square(z - z_img).sum(1)
    # dist: [n,]
    idx = np.argsort(dist)
    # 截取距离最小的前 args.num_row * args.num_col 个图像
    idx = idx[:args.num_row * args.num_col]

    # select raw data for display
    data = data[idx, :, :, :]
    print('Done!')

    # display image
    plt.figure(args.filename)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    # display similar images
    plt.figure('Similar images')
    for i in range(args.num_row * args.num_col):
        plt.subplot(args.num_row, args.num_col, i+1)
        plt.imshow(data[i])
        plt.axis('off')
    plt.show()


if __name__ == '__main__':
    if args.filename is None:
        raise TypeError('Please choose an image file using \'--filename FILENAME\'')
    main(args)
