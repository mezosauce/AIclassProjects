import heapq
from layout import Map

from A_star import Node


def greedy_search(graph, start, goal, heuristic_fn="lower"):

    open_list = []

    if heuristic_fn == "upper":
        start_h = graph.estimate_upper_bound(start, goal)
    else:
        start_h = graph.estimate_lower_bound(start, goal)

    start_node = Node(start, None, 0, start_h)

    heapq.heappush(open_list, start_node)
    visted = set()

    # Keep track of best g-score to allow re-discovery of better paths if necessary
    g_scores = {start: 0}
    
    nodes_expanded = 0

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.city in visted:
            continue

        nodes_expanded += 1
        visted.add(current_node.city)

        if current_node.city == goal:
            path = []
            while current_node:
                path.append(current_node.city)
                current_node = current_node.parent
            return path[::-1], nodes_expanded

        for neighbor, distance in graph.get_neighbors(current_node.city):
            g = current_node.g + distance

            if neighbor in g_scores and g >= g_scores[neighbor]:
                continue

            g_scores[neighbor] = g

            if heuristic_fn == "upper":
                h = graph.estimate_upper_bound(neighbor, goal)
            else:
                h = graph.estimate_lower_bound(neighbor, goal)

            neighbor_node = Node(neighbor, current_node, g, h)
            heapq.heappush(open_list, neighbor_node)
                                          
    return None, nodes_expanded
    

if __name__ == "__main__":

    romania_map = Map()

    #Test Case 1: Arad to Bucharest:
    print("A--- Test Case 1: Arad to Bucharest ---")
    start_city = "Arad"
    goal_city = "Bucharest"

    # Method 1: Lower Bound (Admissible):
    print("Method 1: Lower Bound (Admissible):")
    path, nodes_expanded = greedy_search(romania_map, start_city, goal_city, heuristic_fn="lower")
    print(f"Paths: {path}")
    print(f"Nodes expanded: {nodes_expanded}")

    # Method 2: Upper Bound (Non-Admissible):
    print("Method 2: Upper Bound (Non-Admissible):")
    path, nodes_expanded = greedy_search(romania_map, start_city, goal_city, heuristic_fn="upper")
    print(f"Paths: {path}")
    print(f"Nodes expanded: {nodes_expanded}")

     # Test Case 2: Sibiu to Mehadia (Goal != Bucharest)
    print("\n--- Test Case 2: Sibiu to Mehadia ---")
    start_city = "Sibiu"
    goal_city = "Mehadia"

    # Method 1: Lower Bound (Admissible):
    print("Method 1: Lower Bound (Admissible):")
    path, nodes_expanded = greedy_search(romania_map, start_city, goal_city, heuristic_fn="lower")
    print(f"Paths: {path}")
    print(f"Nodes expanded: {nodes_expanded}")

    # Method 2: Upper Bound (Non-Admissible):
    print("Method 2: Upper Bound (Non-Admissible):")
    path, nodes_expanded = greedy_search(romania_map, start_city, goal_city, heuristic_fn="upper")
    print(f"Paths: {path}")
    print(f"Nodes expanded: {nodes_expanded}")