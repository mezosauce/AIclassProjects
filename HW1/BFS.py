from collections import deque
import time

def bfs_shortest_path(graph, start, goal):
    # Corner case: Start is the goal
    if start == goal:
        return [start]
    
    # 1. Initialize Queue with start node
    # Storing path directly in queue for simplicity: (current_node, [path_so_far])
    queue = deque([ (start, [start]) ])
    
    # 2. Keep track of visited nodes to avoid cycles
    visited = set()
    visited.add(start)
    
    nodes_visited_count = 0
    
    while queue:
        current_city, path = queue.popleft() # Dequeue from front
        nodes_visited_count += 1
        
        # Check neighbors
        if current_city in graph:
            for neighbor in graph[current_city]:
                if neighbor not in visited:
                    # check if goal reached
                    if neighbor == goal:
                        return path + [neighbor]
                    
                    # Add to visited and enqueue
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor])) # Enqueue at back
                    
    return [] # Return empty if no path found