# reference: http://blog.marcinchwedczuk.pl/iterative-algorithm-for-drawing-hilbert-curve
import matplotlib.pyplot as plt

# N-order Pseudo Hilbert Curve
def PHC(n, idx):
    """
    n: the order of PHC
    idx: the index of pixel
    """
    max_idx = 4 ** n
    if idx >= max_idx:
        raise ValueError('index out of bound')

    edge = 2 ** n
    half_edge = edge >> 1

    # 1-order
    pos = [
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0]
    ]

    entry = [
        [0, 0],
        [0, half_edge],
        [half_edge, half_edge],
        [half_edge, 0]
    ]

    if n == 1:
        return pos[idx]
    else:
        # state
        first2bit = idx >> (2 * (n-1))
        bias = entry[first2bit]

        # remove the first 2 bits of idx as the new idx
        xy = PHC(n - 1, idx & ((1 << (2 * (n - 1))) - 1))

        # flip if in state 0 or state 3
        if first2bit == 0:
            tmp = xy[0]
            xy[0] = xy[1]
            xy[1] = tmp
        elif first2bit == 3:
            tmp = xy[0]
            xy[0] = half_edge - xy[1] - 1
            xy[1] = half_edge - tmp - 1

        xy[0] += bias[0]
        xy[1] += bias[1]

        return xy

if __name__ == '__main__':
    for n in range(1, 7):
        prev = [0, 0]
        ax = plt.subplot(2, 3, n)
        ax.set_title('N = {}'.format(n))
        # plt.scatter(prev[0], prev[1], c='r')
        for i in range(1, 4 ** n):
            curr = PHC(n, i)
            # plt.scatter(curr[0], curr[1], c='r')
            plt.plot([prev[0], curr[0]], [prev[1], curr[1]], c='b', linewidth=1)
            prev = curr
    plt.show()
