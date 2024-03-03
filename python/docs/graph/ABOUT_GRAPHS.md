# About Graph Data Structures

## 1. Initializing an Empty Graph

The `Graph` class initializes with an empty dictionary `_adjacency_list` to hold the vertices and their edges.

**Diagram for an Empty Graph:**

- Imagine a blank canvas, as there are no nodes (vertices) or edges to display.

## 2. Adding Two Nodes and Three Edges

To add two nodes and three edges, we follow these steps:

1. **Adding Nodes:** The `add_node` method creates a `Vertex` instance for each value provided and adds it to the graph's `_adjacency_list` with an empty list to hold its edges.
2. **Adding Edges:** The `add_edge` method links two vertices together with an optional weight. If both vertices exist in the graph, an `Edge` instance is created and appended to the list of edges for the starting vertex.

**Diagram for Adding Two Nodes and Three Edges:**

- Assume we add nodes `A` and `B`.
- Then, we add three edges.
  - Since it's a simple graph, we'll demonstrate by adding edges in a manner that might include self-loops or multiple edges to the same node for illustration, as the specific edges weren't defined.
  - Edge 1: From `A` to `B`.
  - Edge 2: From `B` to `A`.
  - Edge 3: Another edge from `A` to `B` or a self-loop from `A` to `A` or `B` to `B`.

## 3. Checking if a Path Exists Between Two Nodes

The function `direct_flights` checks if a direct path exists between two nodes (cities) based on the provided city names. It:
    - iterates through the names,
    - finds the corresponding vertices,
    - then checks if there is a direct edge connecting them.
If a direct connection exists for each pair of cities in the sequence, it returns `True` along with the total cost. Otherwise, it returns `False` and `0`.

**Diagram for Checking Path Between Two Nodes:**

- This would illustrate a sequence of nodes connected by directed edges, highlighting the path checked by the `direct_flights` function.

The diagram illustrates the three stages of working with a simple graph data structure as described:

1. **An Empty Graph:** Represented as a blank canvas, indicating the initial state of the graph before any nodes or edges have been added.
2. **Adding Nodes and Edges:** Shows two nodes labeled 'A' and 'B', with three edges demonstrating the addition of connections between these nodes.
   - The edges illustrate possible connections including a direct link from 'A' to 'B', 'B' to 'A', and an optional third edge that could represent another connection between 'A' and 'B' or a self-loop.
3. **Checking Path Between Nodes:** Highlights a path check between two nodes, indicating the process of determining if a direct path (flight) exists between them, as would be done by the `direct_flights` function in the provided code.

![alt text](image.png)
