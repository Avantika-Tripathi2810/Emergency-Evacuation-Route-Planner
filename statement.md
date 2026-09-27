# Problem Statement — Evacuation Route Simulator

**Author:** Avantika Tripathi
**Registration Number:** 26BAI10170
**Course:** B.Tech CSE (AI & ML)
**Faculty:** J. Manikandan
**Date:** 28/09/2026

## Problem Statement

During emergencies like fires, floods, or building collapses, people near the affected area often don't know which routes are still safe to use, and manual coordination of who should go where quickly breaks down once more than a handful of people are involved. Static maps and pre-planned evacuation routes don't account for the fact that hazards move, spread, and block specific roads dynamically — a route that was safe five minutes ago might now run straight through the danger zone.

This project addresses a smaller, well-scoped version of that problem: given a city represented as a network of buildings, road junctions, and designated safe zones, how do we (a) find the least-risky route between any two points, (b) make that route automatically update as new hazards appear or clear, and (c) handle evacuating *many* people at once without overloading any single safe zone's capacity?

## Scope of the Project

**In scope:**
- Representing a small city as a graph (nodes = locations, edges = roads with distance + hazard state).
- Adding/removing hazards at runtime, with a severity-based radius that affects nearby roads.
- Finding the cheapest route between two nodes using Dijkstra's algorithm, where "cost" factors in hazard risk, not just distance.
- Automatically finding the nearest safe zone that still has free capacity.
- Simulating evacuation of multiple buildings at once, respecting each safe zone's remaining capacity.
- Visualizing the map, hazards, and routes with matplotlib.
- Exporting simulation results to CSV.

**Out of scope (for this version):**
- Real-world map data / GPS integration.
- Persistent storage across sessions (a database).
- A graphical or web-based user interface — this is a CLI tool.
- Multi-hazard interaction modelling beyond simple radius-based severity (e.g., hazard spread over time).

## Target Users

- Emergency-response planners or students studying disaster management, who want a lightweight tool to test "what if a hazard blocks this road" scenarios on a sample map.
- Anyone learning graph algorithms (Dijkstra specifically) who wants to see the algorithm applied to a concrete, visual problem rather than an abstract array of numbers.
- Academically: this doubles as a demonstration of applying core Python + data structures + algorithms concepts (graphs, priority queues, greedy allocation) to a real-world-flavoured scenario, per the CSE1021 project brief.

## High-Level Features

1. **Interactive map viewer** — list all locations and currently active hazards.
2. **Hazard management** — add a hazard (center point, radius, severity) or clear one, with road costs recalculated immediately.
3. **Single-route pathfinding** — Dijkstra's algorithm between any two nodes, or automatically to the nearest safe zone with space.
4. **Bulk evacuation simulation** — assign multiple source buildings (with population counts) to their nearest available safe zone, largest groups first, respecting capacity limits.
5. **Visualization** — save a PNG of the map showing roads (color-coded by hazard level), hazard radii, and the planned route.
6. **CSV export** — save the results of the last simulation (source, destination, people moved, route taken) for later analysis.
