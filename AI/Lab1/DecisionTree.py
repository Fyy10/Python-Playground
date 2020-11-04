import numpy as np


class Node(object):
    def __init__(self):
        # category
        self.value = None
        # direct (attribute_id, mid_value)
        self.judge = None
        # left child
        self.l_child = None
        # right child
        self.r_child = None
        # entropy
        self.entropy = None


class DecisionTree(object):
    def __init__(self):
        self.root = Node()
        self.eps = 1e-6

    def entropy(self, p):
        """
        :param p: a list of probability, shape: (num_label,)
        :return: self entropy of p
        """
        return np.sum(-p * np.log2(p + self.eps/100))

    def cross_entropy(self, p, q):
        """
        :param p: a list of probability, shape: (num_label,)
        :param q: a list of probability, shape: (num_label,)
        :return: cross entropy of p and q
        """
        return np.sum(-p * np.log2(q + self.eps/100))

    def condition_entropy(self, feature, label):
        """
        :param feature: features of a specific attribute, shape: (num_sample,)
        :param label: labels, shape: (num_sample,)
        :return: the minimum condition entropy, corresponding mid value, corresponding index
        """
        idx = np.argsort(feature)
        feature_sorted = feature[idx]
        label_sorted = label[idx]
        min_condition_entropy = np.inf
        min_mid = 0
        min_idx = 0
        for i in range(1, len(feature)):
            left_feature = feature_sorted[:i]
            right_feature = feature_sorted[i:]
            left_label = label_sorted[:i]
            right_label = label_sorted[i:]
            mid = (left_feature[-1] + right_feature[0]) / 2
            p_left = self.get_p(left_label)
            p_right = self.get_p(right_label)
            entropy_left = self.entropy(p_left)
            entropy_right = self.entropy(p_right)
            condition_entropy = len(left_feature) / len(feature) * entropy_left + \
                                len(right_feature) / len(feature) * entropy_right
            if condition_entropy < min_condition_entropy:
                min_condition_entropy = condition_entropy
                min_mid = mid
                min_idx = i

        return min_condition_entropy, min_mid, min_idx

    # calculate p from label (numpy array)
    def get_p(self, label):
        """
        :param label: labels, shape: (num_sample,)
        :return: probabilities, shape: (num_label,)
        """
        num_label = np.max(label)
        num_sample = label.shape[0]
        p_array = np.zeros(num_label)

        for i in range(num_label):
            cnt = (label == (i + 1)).sum()
            p_array[i] = cnt / num_sample

        return p_array

    # calculate information gain of a specific attribute
    def gain(self, feature, label):
        """
        :param feature: features of a specific attribute, shape: (num_sample,)
        :param label: labels, shape: (num_sample,)
        :return: information gain, min_mid, min_idx
        """
        p = self.get_p(label)
        condition_entropy, min_mid, min_idx = self.condition_entropy(feature, label)
        return self.entropy(p) - condition_entropy, min_mid, min_idx

    def train(self, data, label):
        """
        :param data: train data, shape: (num_sample, num_attribute)
        :param label: train label, shape: (num_label,)
        """
        num_attribute = data.shape[1]
        attr_arr = np.array(range(num_attribute))
        self.build(self.root, data, label, attr_arr)

    def predict(self, data: np.ndarray):
        """
        :param data: test data, shape: (num_sample, num_attribute)
        :return: predicted labels, shape: (num_sample,)
        """
        num_sample = data.shape[0]
        labels = np.zeros(num_sample).astype(np.int)
        for i in range(num_sample):
            labels[i] = self.search(self.root, data[i, :])
        return labels

    # build decision tree
    def build(self, node: Node, data, label, attr_arr):
        """
        :param node: the base node of building tree
        :param data: shape (num_sample, num_attribute)
        :param label: shape (num_sample,)
        :param attr_arr: numpy array, shape (num_attribute,), available attribute indexes, -1 for used attributes
        """
        data = data.copy()
        label = label.copy()
        attr_arr = attr_arr.copy()
        p = self.get_p(label)
        node.entropy = self.entropy(p)
        # print(node.entropy)
        if np.abs(node.entropy) < self.eps:
            node.value = label[0]
            return

        available_flag = 0
        for i in attr_arr:
            if i != -1:
                available_flag = 1

        if not available_flag:
            counts = np.bincount(label)
            node.value = np.argmax(counts)
            return

        max_gain = -np.inf
        max_gain_attr_id = 0
        max_gain_mid = 0
        max_gain_sample_idx = 0
        for i in attr_arr:
            if i == -1:
                continue

            gain, min_mid, min_idx = self.gain(data[:, i], label)
            if gain >= max_gain:
                max_gain = gain
                max_gain_attr_id = i
                max_gain_mid = min_mid
                max_gain_sample_idx = min_idx

        # print('max gain', max_gain)
        # print('max gain attr id', max_gain_attr_id)
        # print('max gain mid', max_gain_mid)
        # print('max gain sample idx', max_gain_sample_idx)

        node.judge = (max_gain_attr_id, max_gain_mid)
        attr_arr[max_gain_attr_id] = -1

        sort_idx = data[:, max_gain_attr_id].argsort()
        # sort_idx = np.argsort(data, max_gain_attr_id)
        data_sorted = data[sort_idx]
        label_sorted = label[sort_idx]

        # print('data sorted', data_sorted.shape)
        # print('label sorted', label_sorted.shape)
        # print('attr arr', attr_arr)

        node.l_child = Node()
        self.build(node.l_child, data_sorted[:max_gain_sample_idx, :], label_sorted[:max_gain_sample_idx], attr_arr)

        node.r_child = Node()
        self.build(node.r_child, data_sorted[max_gain_sample_idx:, :], label_sorted[max_gain_sample_idx:], attr_arr)

    # search on decision tree
    def search(self, node: Node, attribute):
        """
        :param node: root
        :param attribute: numpy array, attribute of a specific sample, shape: (num_attribute,)
        :return: predicted label, int
        """
        if node.value is not None:
            return int(node.value)

        if np.abs(node.entropy) < self.eps:
            return int(node.value)

        if attribute[node.judge[0]] <= node.judge[1]:
            return self.search(node.l_child, attribute)
        else:
            return self.search(node.r_child, attribute)

    def display(self, node):
        if node.value is not None:
            print('label', node.value)
            return

        print('idx threshold (<=):', node.judge)

        self.display(node.l_child)
        self.display(node.r_child)
