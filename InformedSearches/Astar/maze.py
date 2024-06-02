from queue import PriorityQueue
import math

class Maze():
    def __init__(self, filename):
        
        with open(filename) as f:
            contents = f.read()
        
        if contents.count("A") != 1:
            raise Exception("MAZE should have only one start")
        if contents.count("B") != 1:
            raise Exception ("MAZE should have only one Goal")
        
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            cells = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        cells.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        cells.append(False)
                    elif contents[i][j] == " ":
                        cells.append(False)
                    else:
                        cells.append(True)
                except IndexError:
                    cells.append(False)
            self.walls.append(cells)
        self.solution = None

    def print(self):
        solution = self.solution if self.solution is not None else None
        print()
        for i, rows in enumerate(self.walls):
            for j, col in enumerate(rows):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end = "")
                elif (i, j) == self.goal:
                    print("B", end = "")
                elif solution is not None and (i, j) in solution:
                    print("*", end = "")
                else:
                    print(" ", end = "")
            print()
        print()

    def neighbours(self, state):
        row, col = state
        # Directions  (up,      down,   left,    right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # Identifying valid Neighbouring moves
        result = []
        for (r, c) in directions:
            r = r + row
            c = c + col
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((r, c))
        return result
    
    def euclidean(self, state, goal):
        if len(state) != len(goal):
            raise Exception('Dimensions Mismatch.')
        distance = 0
        for i in range(len(state)):
            distance += (state[i] - goal[i])**2
        return math.sqrt(distance)

    def heuristic(self, state):
        if state == self.goal:
            return 0
        return self.euclidean(state, self.goal)

    def solve(self):
        self.numExplored = 0 # To keep track of number of moves taken

        Frontier = PriorityQueue()
        Frontier.put((self.heuristic(self.start), 0.0, self.start, None))

        self.explored = set()
        while Frontier:
            
            _, cost, node, parent = Frontier.get()
            
            if node == self.goal: # Backtrack to find solution
                cell = []
                while parent is not None:
                    cell.append(node)
                    node, parent = parent
                cell.reverse()
                self.solution = cell
                return
            
            self.explored.add(node) # Keep track of explored nodes to avoid exploring them again
            self.numExplored += 1

            for neighbor in self.neighbours(node):
                new_cost = cost+1
                if neighbor not in self.explored and neighbor not in [n[2] for n in Frontier.queue]:
                    Frontier.put((self.heuristic(neighbor), new_cost, neighbor, (node, parent)))




m = Maze("C:/Users/Zeeshan/Desktop/AIassign/AI/UN-InformedSearches/maze1.txt")
print("Initial Maze: ")
m.print()
m.solve()
print("Solved Maze(Astar): ")
m.print()
print(f"Number of States explored: {m.numExplored}")