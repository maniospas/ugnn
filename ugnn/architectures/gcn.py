import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv


class GCN(torch.nn.Module):
    def __init__(self, feats, classes, hidden):
        super().__init__()
        self.conv1 = GCNConv(feats, hidden)
        self.conv2 = GCNConv(hidden, classes)

    def forward(self, data):
        x, edges = data.x, data.edges
        x = F.dropout(x, training=self.training)
        x = F.relu(self.conv1(x, edges))
        x = F.dropout(x, training=self.training)
        x = self.conv2(x, edges)
        return x