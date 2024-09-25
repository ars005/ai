import heapq

class Node:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.g = float('inf')  
        self.h = float('inf') 
        self.f = float('inf')  
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node1, node2):
    return abs(node1.position[0] - node2.position[0]) + abs(node1.position[1] - node2.position[1])

def astar(start_node, goal_node, graph):
    open_set = []
    closed_set = set()
    
    start_node.g = 0
    start_node.h = heuristic(start_node, goal_node)
    start_node.f = start_node.h
    heapq.heappush(open_set, start_node)
    
    while open_set:
        current_node = heapq.heappop(open_set)
        
        if current_node == goal_node:
            return reconstruct_path(current_node)
        
        closed_set.add(current_node)
        
        for neighbor, weight in graph.get(current_node.name, []):
            if neighbor in closed_set:
                continue
            
            tentative_g = current_node.g + weight
            
            if tentative_g < neighbor.g:
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, goal_node)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current_node
                
                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)
    return None

def reconstruct_path(goal_node):
    path = []
    current_node = goal_node
    while current_node:
        path.append(current_node.name)
        current_node = current_node.parent
    return path[::-1]

def main():
    nodes = {
        'A': Node('A', (0, 0)),
        'B': Node('B', (1, 0)),
        'C': Node('C', (2, 0)),
        'D': Node('D', (1, 1)),
        'E': Node('E', (2, 1)),
        'F': Node('F', (2, 2))
    }

    graph = {
        'A': [(nodes['B'], 1), (nodes['D'], 1)],
        'B': [(nodes['C'], 1), (nodes['D'], 2)],
        'C': [(nodes['E'], 1)],
        'D': [(nodes['E'], 1)],
        'E': [(nodes['F'], 1)],
        'F': []
    }

    start = nodes['A']
    goal = nodes['F']
    path = astar(start, goal, graph)
    
    if path:
        print(f"Path found: {' -> '.join(path)}")
    else:
        print("No path found")

if __name__ == "__main__":
    main()