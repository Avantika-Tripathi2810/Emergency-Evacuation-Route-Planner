def build_graph(data):
    nodes = {}
    edges = {}
    adjacency = {}

    for n in data["nodes"]:
        nodes[n["node_id"]] = {
            "name": n["name"],
            "x": n["x"],
            "y": n["y"],
            "type": n.get("node_type", "intersection"),
            "capacity": n.get("capacity", 0),
            "load": 0
        }
        adjacency[n["node_id"]] = []

    for e in data["edges"]:
        edges[e["edge_id"]] = {
            "from": e["from_id"],
            "to": e["to_id"],
            "distance": e["distance"],
            "blocked": e.get("blocked", False),
            "hazard": e.get("hazard_level", 0.0)
        }
        adjacency[e["from_id"]].append(e["edge_id"])
        adjacency[e["to_id"]].append(e["edge_id"])

    return nodes, edges, adjacency


def get_neighbors(node_id, edges, adjacency):
    result = []
    for edge_id in adjacency[node_id]:
        edge = edges[edge_id]
        if edge["from"] == node_id:
            other = edge["to"]
        else:
            other = edge["from"]
        result.append((other, edge_id))
    return result


def edge_cost(edge):
    if edge["blocked"]:
        return None
    return edge["distance"] * (1 + 5 * edge["hazard"])


def get_safe_zones(nodes):
    zones = []
    for node_id in nodes:
        if nodes[node_id]["type"] == "safe_zone":
            zones.append(node_id)
    return zones
