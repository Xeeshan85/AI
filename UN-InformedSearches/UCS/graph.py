# Using a Fragment map of Romania from the book of Classical Searches fro Modern Problem Solving
# Implemented UCS algorithm also known as Dijkstra algorithm in Computer Science
# Main Element Priority Queue
# Helps a Traveler find the shortest path to reach his Destination

class Node:
    def __init__(self, state, parent, cost=0):
        self.state=state
        self.parent=parent
        self.cost=cost
    
    def __lt__(self, other):
        return self.cost < other.cost
    
class PriorityQueue:
    def __init__(self):
        self.frontier=[]
    
    def add(self, node):
        self.frontier.append(node)
        self.frontier.sort()
    
    def contains_state(self, state):
        return any(node.state==state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            return self.frontier.pop(0)
    

class UCS:
    def get_neighbours(self, city):
        return romania[city]

    def print_path(self, path):
        print('CITY(Distance to reach there)')
        path_str = ' -> '.join([f'{state}({cost})' for state, cost in path])
        print(f'Shortest Path: {path_str}')

    def solve_ucs(self, romania, start_city, goal):
        explored_states = set()
        num_explored = 0

        start = Node(state=start_city, parent=None, cost=0)
        frontier = PriorityQueue()
        frontier.add(start)

        while True:
            if frontier.empty():
                raise Exception("No Solution.")
            
            current_node = frontier.remove()
            num_explored += 1
            
            if current_node.state == goal:
                path = []
                while current_node:
                    path.append((current_node.state, current_node.cost))
                    current_node = current_node.parent
                path.reverse()
                self.print_path(path)
                return
            
            if current_node.state in explored_states:
                continue

            explored_states.add(current_node.state)

            for neighbour, cost in self.get_neighbours(current_node.state):
                if not frontier.contains_state(neighbour) and neighbour not in explored_states:
                    new_node = Node(neighbour, current_node, cost + current_node.cost)
                    frontier.add(new_node)


romania = {
    'sibiu': [('fagaras', 99), ('rimnicu vilcea', 80)],
    'fagaras': [('bucharest', 211)],
    'rimnicu vilcea': [('pitesti', 97)],
    'pitesti': [('bucharest', 101)]
}

start = 'sibiu'
destination = 'bucharest'

findPath = UCS()
findPath.solve_ucs(romania, start, destination)