import copy
import random

class Puzzle():
    def __init__(self, initialState, goalState):
        self.start = initialState
        self.goal = goalState
        self.height = len(initialState)
        self.width = len(initialState[0])
        self.solution = None

    def printSolution(self):
        solution = self.solution if self.solution is not None else None
        print()
        print("Solution is: ")
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
    
    def heuristic(self, state):
        # Using Manhattan Distance as the heuristic
        distance = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != 0:
                    goal_pos = self.findPosition(self.goal, state[i][j])
                    distance += abs(goal_pos[0] - i) + abs(goal_pos[1] - j)
        return distance

    def findPosition(self, state, value):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == value:
                    return (i, j)
        return None
    
    def solve(self):
        self.numExplored = 0
        current = self.start
        current_score = self.heuristic(current)
        self.explored = []

        while True:
            self.explored.append(current)
            self.numExplored += 1
            neighbors = self.neighbours(current)
            neighbor_scores = [(self.heuristic(neighbor), neighbor) for neighbor in neighbors]

            best_score, best_neighbor = min(neighbor_scores, key=lambda x: x[0])

            if best_score >= current_score:
                break  # Stop if no better neighbor is found

            current = best_neighbor
            current_score = best_score

            if current == self.goal:
                self.solution = [current]
                return

        self.solution = None
        return

x = [[1, 2, 3], [7, 8, 0], [4, 5, 6]]
y = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
m = Puzzle(x, y)
m.solve()
m.printSolution()
print(f"Number of States explored: {m.numExplored}")
