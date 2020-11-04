import numpy as np


class DataLoader(object):
    def __init__(self, data, label, batch_size, seed=0):
        self.data = data
        self.label = label
        self.batch_size = batch_size
        self.N_sample = self.data.shape[0]
        np.random.seed(seed)

    def get_batch(self):
        # get a random batch of data
        batch_sample_idx = np.random.randint(self.N_sample, size=self.batch_size)
        # batch_sample_idx: [batch_size,]
        batch_data = self.data[batch_sample_idx, :]
        batch_label = self.label[batch_sample_idx]
        return batch_data, batch_label
