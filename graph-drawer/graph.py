import json
import torch
import torch_geometric.data
from torch_geometric.utils import from_networkx
import networkx as nx
import matplotlib.pyplot as plt

# pip install torch torchvision torchaudio
# pip install torch-scatter -f https://data.pyg.org/whl/torch-1.11.0+cpu.html
# pip install torch-sparse -f https://data.pyg.org/whl/torch-1.11.0+cpu.html
# pip install torch-cluster -f https://data.pyg.org/whl/torch-1.11.0+cpu.html
# pip install torch-spline-conv -f https://data.pyg.org/whl/torch-1.11.0+cpu.html
# pip install torch-geometric



# Load the JSON dataset
with open('User-Videogame-Dataset.json', 'r') as f:
    users_data = json.load(f)

# Create a graph
G = nx.Graph()

# Add nodes with user ID as node feature
for user in users_data:
    G.add_node(user['UserID'], username=user['Username'])

# Add edges based on the Friends property
for user in users_data:
    user_id = user['UserID']
    for friend_id in user['Friends']:
        G.add_edge(user_id, friend_id)

# Convert the networkx graph to a PyTorch Geometric Data object
data = from_networkx(G)

# Since we need to keep the graph small-scale, let's set a simple feature
# Here, we'll just set the node feature to be an index
data.x = torch.arange(data.num_nodes, dtype=torch.float).view(-1, 1)

print(data)

# Draw the graph using networkx and matplotlib
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)  # positions for all nodes

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=50)

# Draw edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title('User Friendship Graph')
plt.show()
