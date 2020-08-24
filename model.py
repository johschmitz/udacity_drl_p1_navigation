import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        inner_width = [128, 64]
        self.l1 = nn.Linear(state_size, inner_width[0])
        self.l2 = nn.Linear(inner_width[0], inner_width[1])
        self.l3 = nn.Linear(inner_width[1], action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = F.relu(self.l1(state))
        x = F.relu(self.l2(x))
        return self.l3(x)
