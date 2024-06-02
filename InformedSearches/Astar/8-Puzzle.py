from queue import PriorityQueue
import copy

class Puzzle():
    def __init__(self, initialState, goalState):
        self.start = initialState
        self.goal = goalState
        self.height = len(initialState)
        self.width = len(initialState[0])
        self.solution = None

    def printSolution(self):
        solution = self.solution if self.solution is not None else None
        print("Solution is: ")
        self.print(self.start)
        print()
        if solution:
            for sol in solution:
                self.print(sol)
                print()
    
    def print(self, node):
        for row in node:
            print(row)

    def neighbours(self, node):
        row, col = self.findEmptySlide(node)
        # Directions  (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        result = []
        for (r, c) in directions:
            new_row = row + r
            new_col = col + c
            if 0 <= new_row < self.height and 0 <= new_col < self.width:
                neighbour = copy.deepcopy(node)
                neighbour[row][col], neighbour[new_row][new_col] = neighbour[new_row][new_col], neighbour[row][col]
                result.append(neighbour)
        return result
    
    def findEmptySlide(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    return (i, j)
        return None

    def heuristic(self, state):
        if state == self.goal:
            return 0
        count = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != 0 and state[i][j] != self.goal[i][j]:
                    count += 1
        return count

    def solve(self):
        self.numExplored = 0  # To keep track of number of moves taken

        Frontier = PriorityQueue()
        Frontier.put((self.heuristic(self.start), 0, self.start, None))  # (f, g, node, parent)

        self.explored = set()
        while not Frontier.empty():
            f, g, node, parent = Frontier.get()
            
            if node == self.goal:  # Backtrack to find solution
                cell = []
                while parent is not None:
                    cell.append(node)
                    node, parent = parent
                cell.reverse()
                self.solution = cell
                return
            
            self.explored.add(tuple(map(tuple, node)))  # Keep track of explored nodes to avoid exploring them again
            self.numExplored += 1

            for neighbor in self.neighbours(node):
                new_g = g + 1  # Increment cost by 1 for each move
                if tuple(map(tuple, neighbor)) not in self.explored:
                    f = new_g + self.heuristic(neighbor)
                    Frontier.put((f, new_g, neighbor, (node, parent)))

# Test the A* algorithm with the 8-puzzle problem
# x = [[1, 5, 3], [7, 8, 0], [4, 2, 6]]
# y = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# x = [[1, 2, 3], [7, 8, 0], [4, 5, 6]]
# y = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

x = [[4,1,3], [0,2,6], [7,5,8]]
y = [[1,2,3], [4,5,6], [7,8,0]]
m = Puzzle(x, y)
m.solve()
print("Solved Puzzle (A*): ")
m.printSolution()
print(f"Number of States explored: {m.numExplored}")
