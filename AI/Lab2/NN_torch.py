from torch import nn


class TorchDoubleLayerNN(nn.Module):
    def __init__(self, in_dim=4, hidden_dim=10, out_dim=3):
        super(TorchDoubleLayerNN, self).__init__()
        self.fc1 = nn.Linear(in_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, out_dim)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(x)
        out = self.fc2(x)
        return out
