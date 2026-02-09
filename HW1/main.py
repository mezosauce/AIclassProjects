import time
import csv
from layout import Map
from breadthfirst import bfs_shortest_path
from depthfirst import depth_first_search
from greedysearch import greedy_search
from A_star import a_star_search

def calculate_path_cost(map_obj, path):
    if not path:
        return 0
    cost = 0
    for i in range(len(path) - 1):
        dist = map_obj.get_distance(path[i], path[i+1])
        if dist is not None:
            cost += dist
    return cost

def run_experiment():
    romania_map = Map()
    
    # Test cases
    test_cases = [
        ("Arad", "Bucharest"),
        ("Sibiu", "Mehadia"),
        ("Timisoara", "Bucharest"),
        ("Oradea", "Eforie"),
        ("Timisoara", "Giurgiu"),
        ("Neamt", "Drobeta")
    ]
    
    # Algorithms configuration
    # (Name, Function, Args wrapper, Is_Heuristic)
    algorithms = [
        ("BFS", bfs_shortest_path, lambda m, s, g: bfs_shortest_path(m.graph, s, g), False),
        ("DFS", depth_first_search, lambda m, s, g: depth_first_search(m, s, g), False),
        ("Greedy (Lower)", greedy_search, lambda m, s, g: greedy_search(m, s, g, "lower"), True),
        ("Greedy (Upper)", greedy_search, lambda m, s, g: greedy_search(m, s, g, "upper"), True),
        ("A* (Lower)", a_star_search, lambda m, s, g: a_star_search(m, s, g, "lower"), True),
        ("A* (Upper)", a_star_search, lambda m, s, g: a_star_search(m, s, g, "upper"), True),
    ]
    
    results = []
    
    print(f"{'Test Case':<25} {'Algorithm':<20} {'Success':<8} {'Cost':<6} {'Nodes':<6} {'Time(ms)':<10} {'Path'}")
    print("-" * 120)
    
    for start, goal in test_cases:
        test_case_name = f"{start} -> {goal}"
        
        for algo_name, func, wrapper, is_heuristic in algorithms:
            # 1. Correctness and Metrics run
            path, nodes_expanded = wrapper(romania_map, start, goal)
            
            success = "Yes" if path else "No"
            cost = calculate_path_cost(romania_map, path) if path else 0
            
            # 2. Timing run (1000 loops for better precision on small graphs)
            start_time = time.perf_counter()
            loops = 1000
            for _ in range(loops):
                wrapper(romania_map, start, goal)
            end_time = time.perf_counter()
            avg_time_ms = ((end_time - start_time) / loops) * 1000
            
            path_str = " -> ".join(path) if path else ""
            if len(path_str) > 40:
                path_str = path_str[:37] + "..."
                
            print(f"{test_case_name:<25} {algo_name:<20} {success:<8} {cost:<6} {nodes_expanded:<6} {avg_time_ms:<10.4f} {path_str}")
            
            results.append({
                "test_case": test_case_name,
                "algorithm": algo_name,
                "success": success,
                "cost": cost,
                "nodes_expanded": nodes_expanded,
                "time_ms": avg_time_ms,
                "path": " -> ".join(path) if path else ""
            })
            
    # Write results to CSV
    csv_file = "results.csv"
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["test_case", "algorithm", "success", "cost", "nodes_expanded", "time_ms", "path"])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"\nResults saved to {csv_file}")

if __name__ == "__main__":
    run_experiment()
