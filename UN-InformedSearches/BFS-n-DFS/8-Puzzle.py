from collections import deque
import copy

# 8-puzzle has 9!/2 = 181,440 unique states reachable in a BFS/DFS due to parity
# On average it takes at least 3 mins to find the BFS solution for current problem exploring at least 24k unique states
# and 17 mins in case of DFS, exploring at least 55k unique states

class Puzzle():
    def __init__(self, initialState, goalState, algorithm):
        self.BFS = False
        self.DFS = False
        if algorithm == 'BFS':
            self.BFS = True
        elif algorithm == 'DFS':
            self.DFS = True
        else:
            raise Exception('Invalid Algorithm Parameter. Use BFS or DFS.')
        
        self.start = initialState
        self.goal = goalState
        self.height = len(initialState)
        self.width = len(initialState[0])
        
        self.solution = None
        

    def printSolution(self):
        solution = self.solution if self.solution is not None else None
        print()
        print("solution is: ")
        self.print(self.start)
        print()
        for sol in solution:
            self.print(sol)
            print()
    
    def print(self, node):
        for row in node:
            print(row)

    def neighbours(self, node):
        row, col = self.findEmptySlide(node)
        # Directions  (up,      down,   left,    right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        result = []
        for (r, c) in directions:
            r = r + row
            c = c + col
            if 0 <= r < self.height and 0 <= c < self.width:
                neighbour = copy.deepcopy(node)
                neighbour[row][col], neighbour[r][c] = neighbour[r][c], neighbour[row][col]
                result.append(neighbour)
        return result
    
    def findEmptySlide(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    return (i, j)
        return None
    
    def solve(self):
        self.numExplored = 0

        Frontier = deque()
        Frontier.append((self.start, None))

        self.explored = []
        while True:
            if not Frontier:
                raise Exception("Empty Frontier")
            
            node, parent = None, None
            if self.BFS:
                node, parent = Frontier.popleft()
            elif self.DFS:
                node, parent = Frontier.pop()
            
            
            if node == self.goal:
                cell = []
                while parent is not None:
                    cell.append(node)
                    node, parent = parent
                cell.reverse()
                self.solution = cell
                return
            
            self.explored.append(node)
            self.numExplored += 1

            for neighbor in self.neighbours(node):
                if neighbor not in self.explored and neighbor not in [n[0] for n in Frontier]:
                    Frontier.append((neighbor, (node, parent)))

x = [[1, 2, 3], [7, 8, 0], [4, 5, 6]]
y = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
m = Puzzle(x, y, 'DFS')
m.solve()
m.printSolution()
m.numExplored