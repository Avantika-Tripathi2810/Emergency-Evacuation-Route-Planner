# Problem Statement — Evacuation Route Simulator

**Author:** Avantika Tripathi
**Registration Number:** 26BAI10170
**Course:** B.Tech CSE (AI & ML)
**Faculty:** J. Manikandan
**Date:** 28/09/2026

## Problem Statement

During emergencies like fires, floods, or building collapses, people near the affected area often don't know which routes are safe to use and manual coordination of who should go where quickly fails. Static maps and pre-planned evacuation routes do not consider hazard spreading and block specific roads, suddenly a route that was safe five minutes ago might now run straight through the danger zone.

This project aims to solve a smaller, well-defined part of the larger problem: a city is represented as a network of buildings, road junctions, and designated safe zones, how do we (a) find the least-risky route between any two points, (b) make that route automatically update as new hazards appear or clear, and (c) evacuate a bunch of people without having to worry about having all of them arrive at one safe zone at once.


## Scope of the Project

**In scope:**

- A city of small size represented as a graph (nodes = locations, edges = roads with distance + hazard state).
- Adding/removing hazards at runtime, with a radius that is based on severity and that impacts nearby roads.
- Pathfinding with Dijkstra's algorithm between two nodes which use the cheapest path, including the risk of a hazard.
- Automatic location of the nearest safe area with room.
- Simultaneous evacuation of several buildings, taking into account the remaining capacity of each safe zone.
- Plotting maps, hazards, and routes in matplotlib.Using matplotlib to plot maps, hazards, and routes.
- Exporting simulation results to CSV file.

**Out of scope (for this version):**
- Real-world map data / GPS integration.
- Keeping data across sessions (a database).
- A graphical or web-based user interface — this is a CLI tool.
- Modelling the interactions between multiple hazards.

## Target Users

- Those interested in emergency response planning or in disaster management courses, who wish to have a lightweight tool to test the "what if a hazard blocks this road" scenarios using a sample map.
- Anyone learning graph algorithms (Dijkstra specifically) who wants to see the algorithm applied to a concrete, visual problem rather than an abstract array of numbers.
- Academically: this doubles as a demonstration of applying core Python + data structures + algorithms concepts (graphs, priority queues, greedy allocation) to a real-world-flavoured scenario, per the CSE1021 project brief.

## High-Level Features

1. **Interactive map viewer** — list all locations and currently active hazards.
2. **Hazard management** — add a hazard (center point, radius, severity) or clear one, with road costs recalculated immediately.
3. **Single-route pathfinding** — Dijkstra's algorithm between any two nodes, or automatically to the nearest safe zone with space.
4. **Bulk evacuation simulation** — assign multiple source buildings (with population counts) to their nearest available safe zone, largest groups first, respecting capacity limits.
5. **Visualization** — save a PNG of the map showing roads (color-coded by hazard level), hazard radii, and the planned route.
6. **CSV export** — save the results of the last simulation (source, destination, people moved, route taken) for later analysis.
