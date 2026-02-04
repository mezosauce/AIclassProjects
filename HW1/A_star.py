import heapq

from layout import Map


class Node:
    def __init__(self, city, parent=None, g=0, h=0):
        self.city = city
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        # Comparison for priority queue (min-heap based on f cost)
        if self.f == other.f:
            # Tie-breaker: prefer lower h (closer to goal)
            return self.h < other.h
        return self.f < other.f


def a_star_search(map_obj, start, goal, heuristic_method="lower"):
    # Priority Queue
    open_list = []

    # Determine heuristic function
    if heuristic_method == "upper":
        h_start = map_obj.estimate_upper_bound(start, goal)
    else:
        h_start = map_obj.estimate_lower_bound(start, goal)

    start_node = Node(start, None, 0, h_start)
    heapq.heappush(open_list, start_node)

    # Keep track of visited cities to avoid cycles and redundant work
    visited = set()

    # Keep track of best g-score to allow re-discovery of better paths if necessary
    # (Though with consistent heuristics, the first expansion is optimal)
    g_scores = {start: 0}

    nodes_expanded = 0

    while open_list:
        current_node = heapq.heappop(open_list)

        # If we've already processed this node with a better or equal g, skip
        if current_node.city in visited:
            continue

        nodes_expanded += 1
        visited.add(current_node.city)

        # Check goal
        if current_node.city == goal:
            path = []
            while current_node:
                path.append(current_node.city)
                current_node = current_node.parent
            return path[::-1], nodes_expanded

        # Expand neighbors
        neighbors = map_obj.get_neighbors(current_node.city)
        for neighbor_city, distance in neighbors:
            tentative_g = current_node.g + distance

            # If we found a shorter path to neighbor, or haven't seen it yet
            if neighbor_city not in g_scores or tentative_g < g_scores[neighbor_city]:
                g_scores[neighbor_city] = tentative_g

                if heuristic_method == "upper":
                    h = map_obj.estimate_upper_bound(neighbor_city, goal)
                else:
                    h = map_obj.estimate_lower_bound(neighbor_city, goal)

                new_node = Node(neighbor_city, current_node, tentative_g, h)
                heapq.heappush(open_list, new_node)

    return None, nodes_expanded


if __name__ == "__main__":
    romania_map = Map()

    # Test Case 1: Arad to Bucharest (Standard Textbook Example)
    print("--- Test Case 1: Arad to Bucharest ---")
    start_city = "Arad"
    goal_city = "Bucharest"

    # Method 1: Lower Bound (Admissible)
    path_lower, count_lower = a_star_search(romania_map, start_city, goal_city, "lower")
    print("Lower Bound Heuristic:")
    print(f"  Path: {path_lower}")
    print(f"  Nodes Expanded: {count_lower}")

    # Method 2: Upper Bound (Likely Inadmissible)
    path_upper, count_upper = a_star_search(romania_map, start_city, goal_city, "upper")
    print("Upper Bound Heuristic:")
    print(f"  Path: {path_upper}")
    print(f"  Nodes Expanded: {count_upper}")

    # Test Case 2: Sibiu to Mehadia (Goal != Bucharest)
    print("\n--- Test Case 2: Sibiu to Mehadia ---")
    start_city = "Sibiu"
    goal_city = "Mehadia"

    path_lower, count_lower = a_star_search(romania_map, start_city, goal_city, "lower")
    print("Lower Bound Heuristic:")
    print(f"  Path: {path_lower}")
    print(f"  Nodes Expanded: {count_lower}")

    path_upper, count_upper = a_star_search(romania_map, start_city, goal_city, "upper")
    print("Upper Bound Heuristic:")
    print(f"  Path: {path_upper}")
    print(f"  Nodes Expanded: {count_upper}")
