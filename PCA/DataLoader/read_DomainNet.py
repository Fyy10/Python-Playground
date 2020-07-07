import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from tqdm import tqdm


# load DomainNet Dataset
def load_batch(base_dir):
    """
    :param base_dir: path of data
    :return: a numpy array of shape [n, 200, 300, 3]
    """
    data_dir = base_dir + 'DomainNet/'
    data_list = []
    # 记录当前到达第几个class了
    cnt_class = 0
    # 记录当前到达某个class中的第几张图片了
    cnt_num = 0

    print('Loading DomainNet...')
    for line in tqdm(open(data_dir + 'real_train.txt')):
        # 读取文件名和类标签
        line_split = line.split(' ')
        img_filename = line_split[0]
        img_label = line_split[1]

        # 跳过，直到下一个类
        if int(img_label) == cnt_class - 1:
            continue

        # load image
        img = Image.open(data_dir + img_filename)
        # img = plt.imread(data_dir + img_filename)
        # img: [height, width, RGB], numpy array

        # resize to 200 x 300 x 3 注意PIL的resize函数中width在前面，height在后面
        img = img.resize((300, 200))
        # from PIL to numpy array
        img = np.array(img)
        # from numpy to PIL
        # img = Image.fromarray(np.uint8(img))

        # display image
        # plt.imshow(img)
        # plt.show()
        # print(img_filename, int(img_label), 'loaded')

        # append to data list
        data_list.append(img)

        # image loaded
        cnt_num += 1
        # load 10 images per class
        if cnt_num == 10:
            cnt_class += 1
            cnt_num = 0

    data_arr = np.array(data_list)
    # data_arr: [n, 200, 300, 3]
    print('Done!')
    return data_arr


# load DomainNet Dataset (small batch)
def load_small_batch(base_dir):
    """
    :param base_dir: path of data
    :return: a numpy array of shape [n, 40, 60, 3]
    """
    data_dir = base_dir + 'DomainNet/'
    data_list = []
    # 记录当前到达第几个class了
    cnt_class = 0
    # 记录当前到达某个class中的第几张图片了
    cnt_num = 0

    print('Loading DomainNet (small)...')
    for line in tqdm(open(data_dir + 'real_train.txt')):
        # 读取文件名和类标签
        line_split = line.split(' ')
        img_filename = line_split[0]
        img_label = line_split[1]

        # 跳过，直到下一个类
        if int(img_label) == cnt_class - 1:
            continue

        # load image
        img = Image.open(data_dir + img_filename)
        # img = plt.imread(data_dir + img_filename)
        # img: [height, width, RGB], numpy array

        # resize to 40 x 60 x 3 注意PIL的resize函数中width在前面，height在后面
        img = img.resize((60, 40))
        # from PIL to numpy array
        img = np.array(img)
        # from numpy to PIL
        # img = Image.fromarray(np.uint8(img))

        # display image
        # plt.imshow(img)
        # plt.show()
        # print(img_filename, int(img_label), 'loaded')

        # append to data list
        data_list.append(img)

        # image loaded
        cnt_num += 1
        # load 10 images per class
        if cnt_num == 10:
            cnt_class += 1
            cnt_num = 0

    data_arr = np.array(data_list)
    # data_arr: [n, 40, 60, 3]
    print('Done!')
    return data_arr
