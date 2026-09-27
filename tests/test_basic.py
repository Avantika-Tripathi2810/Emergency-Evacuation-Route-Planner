import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.graph import build_graph
from src.pathfinder import dijkstra

data = {
    "nodes": [
        {"node_id": "A", "name": "A", "x": 0, "y": 0, "node_type": "building"},
        {"node_id": "B", "name": "B", "x": 1, "y": 0, "node_type": "intersection"},
        {"node_id": "C", "name": "C", "x": 2, "y": 0, "node_type": "safe_zone", "capacity": 10}
    ],
    "edges": [
        {"edge_id": "E1", "from_id": "A", "to_id": "B", "distance": 5},
        {"edge_id": "E2", "from_id": "B", "to_id": "C", "distance": 5},
        {"edge_id": "E3", "from_id": "A", "to_id": "C", "distance": 20}
    ]
}

nodes, edges, adjacency = build_graph(data)

path, cost = dijkstra(nodes, edges, adjacency, "A", "C")
assert path == ["A", "B", "C"]
assert cost == 10

edges["E1"]["blocked"] = True
path, cost = dijkstra(nodes, edges, adjacency, "A", "C")
assert path == ["A", "C"]
assert cost == 20

print("all tests passed")
