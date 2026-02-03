
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
            'Arad': 366,
            'Bucharest': 0,
            'Craiova': 160,
            'Drobeta': 242,
            'Eforie': 161,
            'Fagaras': 176,
            'Giurgiu': 77,
            'Hirsova': 151,
            'Iasi': 226,
            'Lugoj': 244,
            'Mehadia': 241,
            'Neamt': 234,
            'Oradea': 380,
            'Pitesti': 100,
            'Rimnicu Vilcea': 193,
            'Sibiu': 253,
            'Timisoara': 329,
            'Urziceni': 80,
            'Vaslui': 199,
            'Zerind': 374
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
    
    def estimate_sld(self, city1, city2):

        # TODO: Implement heuristic estimation using triangle inequality
        # Hint: Use known SLD to Bucharest as a reference point
        
        if city2 == 'Bucharest':
            return self.get_sld_to_bucharest(city1)
        
        return 0
    
    def __str__(self):
        result = "Romanian Road Map:\n"
        result += f"Total cities: {len(self.cities)}\n"
        result += f"Cities: {', '.join(sorted(self.cities))}\n"
        return result



if __name__ == "__main__":
    romania = Map()
    
    print("Keys in Map.graph:", romania)