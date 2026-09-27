import json
import csv
import os


def load_map(filename):
    if not os.path.exists(filename):
        print("Map file not found:", filename)
        return None

    with open(filename, "r") as f:
        data = json.load(f)

    return data


def save_results_csv(results, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["source", "safe_zone", "people", "route"])
        for source in results:
            info = results[source]
            route_str = " -> ".join(info["route"])
            writer.writerow([source, info["safe_zone"], info["people"], route_str])
