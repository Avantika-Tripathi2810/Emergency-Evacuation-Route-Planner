import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

NODE_COLORS = {
    "safe_zone": "green",
    "building": "blue",
    "intersection": "gray"
}

NODE_MARKERS = {
    "safe_zone": "s",
    "building": "o",
    "intersection": "o"
}


def get_edge_color(edge):
    if edge["blocked"]:
        return "darkred"
    if edge["hazard"] >= 0.6:
        return "red"
    if edge["hazard"] >= 0.3:
        return "orange"
    return "lightgray"


def draw_hazards(ax, hazards, nodes):
    for hazard_id in hazards:
        h = hazards[hazard_id]
        center = nodes[h["center"]]
        outer = Circle((center["x"], center["y"]), h["radius"],
                        color="red", alpha=0.12, linestyle="--", fill=True)
        inner = Circle((center["x"], center["y"]), h["critical_radius"],
                        color="red", alpha=0.25, fill=True)
        ax.add_patch(outer)
        ax.add_patch(inner)
        ax.annotate(hazard_id, (center["x"], center["y"]), color="darkred",
                    fontsize=9, ha="center", va="center", weight="bold")


def plot_map(nodes, edges, route=None, hazards=None, title="Evacuation Map", save_path="map.png"):
    fig, ax = plt.subplots(figsize=(10, 8))

    if hazards:
        draw_hazards(ax, hazards, nodes)

    for edge_id in edges:
        edge = edges[edge_id]
        a = nodes[edge["from"]]
        b = nodes[edge["to"]]
        style = "--" if edge["blocked"] else "-"
        ax.plot([a["x"], b["x"]], [a["y"], b["y"]], style, color=get_edge_color(edge), linewidth=2)

    if route:
        for i in range(len(route) - 1):
            a = nodes[route[i]]
            b = nodes[route[i + 1]]
            ax.plot([a["x"], b["x"]], [a["y"], b["y"]], color="blue", linewidth=4, alpha=0.8)

    for node_id in nodes:
        node = nodes[node_id]
        color = NODE_COLORS.get(node["type"], "black")
        marker = NODE_MARKERS.get(node["type"], "o")
        ax.scatter(node["x"], node["y"], color=color, s=220, marker=marker,
                   edgecolors="black", linewidths=1, zorder=3)
        ax.annotate(node["name"], (node["x"], node["y"]), textcoords="offset points",
                    xytext=(8, 8), fontsize=9)

    legend_items = [
        Line2D([0], [0], marker='o', color='w', label='Intersection',
               markerfacecolor=NODE_COLORS["intersection"], markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Building',
               markerfacecolor=NODE_COLORS["building"], markersize=10),
        Line2D([0], [0], marker='s', color='w', label='Safe zone',
               markerfacecolor=NODE_COLORS["safe_zone"], markersize=10),
        Line2D([0], [0], color="blue", lw=3, label='Planned route'),
        Line2D([0], [0], color="darkred", lw=2, ls='--', label='Blocked road'),
        Line2D([0], [0], color="red", lw=2, label='Hazard zone')
    ]
    ax.legend(handles=legend_items, loc="upper left", fontsize=8)
    ax.set_aspect("equal", adjustable="datalim")

    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle=":", alpha=0.4)

    fig.savefig(save_path, dpi=150)
    plt.close(fig)

    return save_path
