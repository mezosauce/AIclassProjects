
class Map:
    def __init__(self):
        # Format: city -> [(neighbor, distance), (neighbor, distance), ...]
        self.graph = {
            'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
            'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
            'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
            'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
            'Eforie': [('Hirsova', 86)],
            'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
            'Giurgiu': [('Bucharest', 90)],
            'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
            'Iasi': [('Vaslui', 92), ('Neamt', 87)],
            'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
            'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
            'Neamt': [('Iasi', 87)],
            'Oradea': [('Zerind', 71), ('Sibiu', 151)],
            'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
            'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
            'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
            'Timisoara': [('Arad', 118), ('Lugoj', 111)],
            'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
            'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
            'Zerind': [('Arad', 75), ('Oradea', 71)]
        }
        
        self.sld_to_bucharest = {
            "Arad": 366,
            "Bucharest": 0,
            "Craiova": 160,
            "Drobeta": 242,
            "Eforie": 161,
            "Fagaras": 176,  # NOTE: The lecture slides have this as 178
            "Giurgiu": 77,
            "Hirsova": 151,
            "Iasi": 226,
            "Lugoj": 244,
            "Mehadia": 241,
            "Neamt": 234,
            "Oradea": 380,
            "Pitesti": 100,  # NOTE: The lecture slides have this as 98
            "Rimnicu Vilcea": 193,
            "Sibiu": 253,
            "Timisoara": 329,
            "Urziceni": 80,
            "Vaslui": 199,
            "Zerind": 374,
        }
        
        self.cities = list(self.graph.keys())
    
    def get_neighbors(self, city):
        return self.graph.get(city, [])
    
    def get_distance(self, city1, city2):
        for neighbor, distance in self.graph.get(city1, []):
            if neighbor == city2:
                return distance
        return None
    
    def get_sld_to_bucharest(self, city):

        return self.sld_to_bucharest.get(city, float('inf'))
    

    # |SLD(A→B) - SLD(C→B)| ≤ SLD(A→C) ≤ SLD(A→B) + SLD(C→B)

    # Hueristic Search
    
    # Method 1 Hueristic Search (Lower Bound)

    def estimate_lower_bound(self, city1, city2):
        if city1 == 'Bucharest' or city2 == 'Bucharest':
            return self.get_sld_to_bucharest(city1 if city2 == 'Bucharest' else city2)

        sld1 = self.get_sld_to_bucharest(city1)
        sld2 = self.get_sld_to_bucharest(city2)
        return abs(sld1 - sld2)
    
    
    # Method 2 Hueristic Search (Upper Bound)
    
    def estimate_upper_bound(self, city1, city2):
        if city1 == 'Bucharest' or city2 == 'Bucharest':
            return self.get_sld_to_bucharest(city1 if city2 == 'Bucharest' else city2)
        sld1 = self.get_sld_to_bucharest(city1)
        sld2 = self.get_sld_to_bucharest(city2)
        return sld1 + sld2
    


    def __str__(self):
        result = "Romanian Road Map:\n"
        result += f"Total cities: {len(self.cities)}\n"
        result += f"Cities: {', '.join(sorted(self.cities))}\n"
        return result



if __name__ == "__main__":
    romania = Map()

    print("Testing the estimate_upper_bound method:")
    print(f"Upper bound estimate from Arad to Bucharest: {romania.estimate_upper_bound('Arad', 'Bucharest')}")
    print(f"Upper bound estimate from Sibiu to Mehadia: {romania.estimate_upper_bound('Sibiu', 'Mehadia')}")
    print ("NOW TESTING THE LOWER BOUND METHOD:")
    print(f"Lower bound estimate from Arad to Bucharest: {romania.estimate_lower_bound('Arad', 'Bucharest')}")
    print(f"Lower bound estimate from Sibiu to Mehadia: {romania.estimate_lower_bound('Sibiu', 'Mehadia')}")

    print("Calculating average of upper and lower bound estimates between all city pairs:")
    print("AVERAGE CALCULATED FOR SIBIU TO MEHADIA:")
    lower_bound = romania.estimate_lower_bound('Sibiu', 'Mehadia')
    upper_bound = romania.estimate_upper_bound('Sibiu', 'Mehadia')
    average = (lower_bound + upper_bound) / 2
    print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}, Average: {average}")


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
