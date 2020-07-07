import numpy as np
import matplotlib.pyplot as plt


def PCA(x, m=2, pic=None):
    """
    :param x: data of shape [N, F]
    :param m: 需要保留的维度个数
    :param pic: 需要根据 x 进行 PCA 降维的图片 shape [1, F]
    :return: 降维后的数据 shape [N, m]，如果 pic 不是 None 的话，则在原始的输出上添加一个 pic，shape 变为 [N+1, m]
    """
    # 当需要保留的维数 m 大于所有维数 F 时，保留所有维数
    if m > x.shape[1]:
        m = x.shape[1]
    mean = x.mean(0)
    x = x - mean
    # x: (N, F)
    # S = np.cov(x.T) = cov(x, x)
    S = np.matmul(x.T, x)
    # S: (F, F)
    # eig value (v) and eig vector (W)
    v, W = np.linalg.eigh(S)
    # v: (F,) W: (F, F)

    # select top m values
    idx = np.argsort(-v)
    # W 中每一列是一个 eig vector
    # 选取前 m 个 eig value 对应的 eig vector
    W = W[:, idx[:m]]
    # W: [F, m]
    # x: (N, F)
    z = np.matmul(x, W)
    # z: (N, m)

    if pic is not None:
        # pic: [1, F]
        pic = pic - mean
        z_pic = np.matmul(pic, W)
        # z_pic: [1, m]
        z = np.append(z, z_pic)
        z = z.reshape(-1, m)
        # z: [n+1, m]
    return z
