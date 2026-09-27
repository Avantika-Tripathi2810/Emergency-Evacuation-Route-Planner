import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def apply_hazard(hazard, nodes, edges):
    center = nodes[hazard["center"]]

    for edge_id in edges:
        edge = edges[edge_id]
        a = nodes[edge["from"]]
        b = nodes[edge["to"]]
        mid_x = (a["x"] + b["x"]) / 2
        mid_y = (a["y"] + b["y"]) / 2
        d = distance(mid_x, mid_y, center["x"], center["y"])

        if d <= hazard["critical_radius"]:
            edge["blocked"] = True
            edge["hazard"] = 1.0
        elif d <= hazard["radius"]:
            level = hazard["severity"] * (1 - d / hazard["radius"])
            if level > edge["hazard"]:
                edge["hazard"] = level


def add_hazard(hazards, nodes, edges, hazard_id, center_id, radius, severity):
    if center_id not in nodes:
        print("No such node:", center_id)
        return False

    if severity < 0 or severity > 1:
        print("Severity must be between 0 and 1")
        return False

    hazards[hazard_id] = {
        "center": center_id,
        "radius": radius,
        "severity": severity,
        "critical_radius": radius * 0.3
    }

    apply_hazard(hazards[hazard_id], nodes, edges)
    return True


def remove_hazard(hazards, nodes, edges, hazard_id):
    if hazard_id not in hazards:
        print("No hazard called", hazard_id)
        return False

    del hazards[hazard_id]

    for edge_id in edges:
        edges[edge_id]["blocked"] = False
        edges[edge_id]["hazard"] = 0.0

    for hazard in hazards.values():
        apply_hazard(hazard, nodes, edges)

    return True
