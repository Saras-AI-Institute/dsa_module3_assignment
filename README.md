# Module 3 Assignment: LogiRoute (Fulfillment & Dispatch Engine)

## Context
You are optimizing the core backend engine for **LogiRoute**, an automated supply chain platform. The system handles thousands of delivery packages daily. To prevent delayed shipments and minimize fuel costs, you must implement highly optimized algorithms for three critical microservices:

1. **Inventory Lookup:** Finding packages instantly in a sorted high-density warehouse matrix.
2. **Delivery Drone Scheduling:** Maximizing the number of delivery windows a single drone can fulfill without overlaps.
3. **Fulfillment Route Optimization:** Finding the absolute shortest paths through a complex network of delivery hubs.

---

## Core Tasks to Complete

### Task 1: Canonical Search — Inventory Tracking (`dispatch_engine.py`)
* **Topic Focus:** *Binary Search ($O(\log n)$)*
* **Challenge:** Given a strictly sorted list of package IDs (`Package` objects), implement a modified **Binary Search** to locate a target package's index. If the package does not exist, return the insertion index where it *should* be placed to maintain order. 
* **Constraint:** A linear scan ($O(n)$) will cause the validation tests to time out.

### Task 2: Resource Scheduling — Drone Window Maximization (`dispatch_engine.py`)
* **Topic Focus:** *Scheduling Problems & Greedy Design Patterns*
* **Challenge:** You are given a list of requested delivery slots, each with a `(start_time, end_time)`. A single delivery drone can only perform one delivery at a time. Implement an algorithm to find the **maximum number of non-overlapping delivery windows** the drone can complete.
* **Algorithmic Secret:** You will need to sort the intervals first. Think critically: Should you sort by start time, duration, or end time to achieve the optimal greedy choice?

### Task 3: Route Optimization — Shortest Path Hub Network (`router_engine.py`)
* **Topic Focus:** *Graph Problem & Route Optimization Analysis*
* **Challenge:** Hubs and roads are modeled as a weighted graph. Implement a shortest-path graph algorithm (such as Dijkstra's) to find the minimum distance from a central distribution center to a target delivery node.

---

## Section 4: Critical Thinking & Written Algorithm Analysis
*Open README.md and append your answers to these two architectural questions at the bottom of the file.*

1. **Scheduling Trade-offs:** In Task 2, if you chose a greedy approach based on sorting by *start time* vs *end time*, explain with a small counter-example why one fails to yield the maximum number of intervals while the other succeeds.
2. **Graph Scaling Analysis:** If the delivery network expands from 100 hubs to 100,000 hubs, how does the time complexity of your shortest-path algorithm change relative to the number of Vertices ($V$) and Edges ($E$)? Which internal data structure would you introduce to prevent performance degradation?
