import heapq
from .graph import get_neighbors, edge_cost, get_safe_zones


def dijkstra(nodes, edges, adjacency, start, goal):
    dist = {}
    prev = {}
    for node_id in nodes:
        dist[node_id] = float("inf")
        prev[node_id] = None
    dist[start] = 0

    visited = set()
    queue = [(0, start)]

    while queue:
        d, current = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for neighbor, edge_id in get_neighbors(current, edges, adjacency):
            cost = edge_cost(edges[edge_id])
            if cost is None:
                continue
            new_dist = d + cost
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current
                heapq.heappush(queue, (new_dist, neighbor))

    if dist[goal] == float("inf"):
        return None, None

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()

    return path, dist[goal]


def find_nearest_safe_zone(nodes, edges, adjacency, start):
    best_path = None
    best_cost = None
    best_zone = None

    for zone_id in get_safe_zones(nodes):
        remaining = nodes[zone_id]["capacity"] - nodes[zone_id]["load"]
        if remaining <= 0:
            continue

        path, cost = dijkstra(nodes, edges, adjacency, start, zone_id)
        if path is None:
            continue

        if best_cost is None or cost < best_cost:
            best_path = path
            best_cost = cost
            best_zone = zone_id

    return best_path, best_cost, best_zone
