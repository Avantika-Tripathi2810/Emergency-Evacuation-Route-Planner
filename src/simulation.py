from .pathfinder import find_nearest_safe_zone


def run_simulation(nodes, edges, adjacency, sources):
    results = {}
    unassigned = []

    source_list = list(sources.items())
    source_list.sort(key=lambda pair: pair[1], reverse=True)

    for source_id, people in source_list:
        path, cost, zone_id = find_nearest_safe_zone(nodes, edges, adjacency, source_id)
        if path is None:
            unassigned.append(source_id)
            continue

        zone = nodes[zone_id]
        space_left = zone["capacity"] - zone["load"]
        people_sent = min(people, space_left)
        zone["load"] += people_sent

        results[source_id] = {
            "safe_zone": zone_id,
            "people": people_sent,
            "route": path,
            "cost": cost
        }

    return results, unassigned


def print_summary(results, unassigned):
    print("=== Evacuation Summary ===")
    for source in results:
        info = results[source]
        route_str = " -> ".join(info["route"])
        print(" ", source, "->", info["safe_zone"], ":", info["people"], "people via", route_str)
    if unassigned:
        print("Could not evacuate:", ", ".join(unassigned))
