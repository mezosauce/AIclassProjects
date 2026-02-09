from collections import deque
import time


def bfs_shortest_path(graph, start, goal):
    # Corner case: Start is the goal
    if start == goal:
        return [start], 0

    # 1. Initialize Queue with start node
    # Storing path directly in queue for simplicity: (current_node, [path_so_far])
    queue = deque([(start, [start])])

    # 2. Keep track of visited nodes to avoid cycles
    visited = set()
    visited.add(start)

    nodes_expanded = 0

    while queue:
        current_city, path = queue.popleft()  # Dequeue from front
        nodes_expanded += 1

        # Check neighbors
        if current_city in graph:
            for neighbor, _ in graph[current_city]:
                if neighbor not in visited:
                    # check if goal reached
                    if neighbor == goal:
                        return path + [neighbor], nodes_expanded

                    # Add to visited and enqueue
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))  # Enqueue at back

    return [], nodes_expanded  # Return empty if no path found


if __name__ == "__main__":
    from layout import Map

    romania_map = Map()

    # Store results for table
    results = []

    test_cases = [
        ("Arad", "Bucharest"),
        ("Sibiu", "Mehadia"),
        ("Oradea", "Eforie"),
        ("Timisoara", "Giurgiu"),
        ("Neamt", "Drobeta")
    ]

    print("--- Breadth First Search Testing ---")

    for start_city, goal_city in test_cases:
        path, nodes = bfs_shortest_path(romania_map.graph, start_city, goal_city)

        # Calculate path cost
        cost = 0
        if path:
            for i in range(len(path) - 1):
                distance = romania_map.get_distance(path[i], path[i + 1])
                if distance:
                    cost += distance

        results.append(
            {
                "test_case": f"{start_city} → {goal_city}",
                "path": " → ".join(path) if path else "No path",
                "cost": cost,
                "nodes": nodes,
            }
        )

    # Print results table
    print("\n" + "=" * 100)
    print("BREADTH FIRST SEARCH RESULTS SUMMARY")
    print("=" * 100)
    print(f"{'Test Case':<25} {'Path Cost':<12} {'Nodes Expanded':<18} {'Path'}")
    print("-" * 100)

    for result in results:
        print(
            f"{result['test_case']:<25} {result['cost']:<12} {result['nodes']:<18} {result['path']}"
        )

    print("=" * 100)