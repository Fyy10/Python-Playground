import numpy as np
from DataLoader import DataLoader


class DoubleLayerNN(object):
    def __init__(self, in_feat=4, hidden_feat=10, out_feat=3, std=1e-1):
        # initialize weights
        self.W1 = std * np.random.randn(in_feat, hidden_feat)
        self.b1 = np.zeros(hidden_feat)
        self.W2 = std * np.random.randn(hidden_feat, out_feat)
        self.b2 = np.zeros(out_feat)

    def forward(self, x):
        # x: [N, in_feat]
        W1, b1 = self.W1, self.b1
        W2, b2 = self.W2, self.b2
        # FC 1
        out1 = x.dot(W1) + b1
        # out1: [N, hidden_feat]
        # ReLU (hidden layer)
        outh = np.maximum(0, out1)
        # FC 2
        out2 = outh.dot(W2) + b2
        return out2, outh

    def backward(self, dW1, db1, dW2, db2, lr=1e-3):
        # update model parameters
        # SGD optimizer
        self.W1 -= lr * dW1
        self.b1 -= lr * db1
        self.W2 -= lr * dW2
        self.b2 -= lr * db2

    def cross_entropy_loss(self, x, y):
        # with softmax
        # x: [N, in_feat]
        # y: [out_feat,]
        N = x.shape[0]

        # loss
        scores, h_out = self.forward(x)
        # scores(out2): [N, out_feat]
        # h_out: [N, hidden_feat]
        # normalization (regard max as a constant)
        shifted_scores = scores - np.max(scores, axis=1).reshape(-1, 1)
        # shifted_scores: [N, out_feat]
        softmax_out = np.exp(shifted_scores) / np.sum(np.exp(shifted_scores), axis=1).reshape(-1, 1)
        loss = -np.sum(np.log(softmax_out[range(N), list(y)]))
        loss /= N

        # grads
        # loss = 1/N * sum(-scores_i + log(sum(exp(scores_j))))
        dscores = softmax_out.copy()
        dscores[range(N), list(y)] -= 1
        dscores /= N

        # scores(out2) = h_out * W2 + b2
        dW2 = np.dot(h_out.T, dscores)
        db2 = np.sum(dscores, axis=0)
        dh_out = dscores.dot(self.W2.T)  # (N, H)

        # h_out = ReLU(out1)
        dout1 = (h_out > 0) * dh_out
        # out1 = x * W1 + b1
        dW1 = np.dot(x.T, dout1)
        db1 = np.sum(dout1, axis=0)
        return loss, dW1, db1, dW2, db2

    def train_step(self, x, y, lr=1e-3):
        # x: [N, in_feat]
        # y: [out_feat,]
        loss, dW1, db1, dW2, db2 = self.cross_entropy_loss(x, y)
        self.backward(dW1, db1, dW2, db2, lr)
        return loss

    def train(self, train_data, train_label, lr=1e-3, batch_size=20, num_batch=20, verbose=False):
        data_loader = DataLoader(train_data, train_label, batch_size)
        for i in range(num_batch):
            data, label = data_loader.get_batch()
            batch_loss = self.train_step(data, label, lr)
            if verbose:
                print('Batch: {} Loss: {}'.format(i, batch_loss))

    def predict(self, x):
        pred = self.forward(x)[0]
        # pred: [N, out_feat]
        labels = np.argmax(pred, axis=1)
        # labels: [N,]
        return labels

    def test_acc(self, x, y):
        predict_label = self.predict(x)
        accuracy = np.sum(predict_label == y).sum() / x.shape[0]
        return accuracy
