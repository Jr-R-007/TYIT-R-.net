import heapq
def uniform_cost_search(graph, start, goal):
   
    priority_queue = [(0,start,[start])]
    visited = set()
   
    while priority_queue:
        cost,current_node,path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == goal:
            return cost,path
        for neighbor, weight in graph.get(current_node,{}).items():
             if neighbor not in visited:
                    total_cost = cost + weight
                    heapq.heappush(priority_queue,(total_cost,neighbor,path+[neighbor]))
    return float('inf'), []
            
romania_map = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118},
    'Sibiu': {'Fagaras': 99, 'Rimnicu Vilcea':80,'Arad': 140 },
    'Timisoara': {'Arad': 118},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, }
        }

custom_map={
            "Node_A": {"Node_B": 5, "Node_C": 2},
            "Node_B": {"Node_D": 4},
            "Node_C": {"Node_B": 1, "Node_D": 9},
            "Node_D": {}
          
        }

if __name__ == "__main__":
    print("\n--Running Uniform Cost Search on Romania Map (Arad to Bucharest)--")
    cost,path=uniform_cost_search(romania_map, 'Arad', 'Bucharest')
    print(f"Minimum path cost : {cost}")
    print(f"Optimal Path: {'->'.join(path)}")
    print("\n--Running Uniform Cost Search on alternative graph(Node A to Node D)--")
    alt_cost,alt_path=uniform_cost_search(custom_map,'Node_A','Node_D')
    print(f"Minimum path cost : {alt_cost}")
    print(f"Optimal Path: {'->'.join(alt_path)}")


   