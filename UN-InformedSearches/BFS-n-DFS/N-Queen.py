from collections import deque
import random


class n_queen():
    def __init__(self, size, algorithm):
        if size < 4:
            raise Exception("Size must be greater than 4.")
        self.BFS = False
        self.DFS = False
        if algorithm == 'BFS':
            self.BFS = True
        elif algorithm == 'DFS':
            self.DFS = True
        else:
            raise Exception('Invalid Algorithm Parameter. Use \'BFS\' or \'DFS\'.')
        
        self.size = size
        self.board = [random.randint(0, self.size-1) for _ in range(self.size)]
        print(self.board)
        print("Initial Board: ")
        self.Print_board(self.board)
        
    def Print_board(self, board):
        for col in range(self.size):
            line = ''
            for row in range(self.size):
                if board[row] == col:
                    line += "Q "
                else:
                    line+= '. '
            print(line)
        print()

    def find_neighbours(self, state):
        neighbours = []
        for col in range(self.size):
            for row in range(self.size):
                if state[col] != row:
                    new_state = state[:]
                    new_state[col] = row
                    neighbours.append(new_state)
        return neighbours

    def find_cost(self, state):
        attacking_pairs = 0
        for i in range(self.size):
            for j in range(i+1, self.size):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    attacking_pairs += 1
        return attacking_pairs

    def solve(self):
        self.states_explored = 0

        frontier = deque()
        initial_state = self.board
        frontier.append(initial_state)

        explored_states = set()
        while True:
            if not frontier:
                raise Exception ("Empty Frontier.")
            
            if self.BFS:
                state = frontier.popleft()
            elif self.DFS:
                state = frontier.pop()
            
            if self.find_cost(state) == 0:
                print('Solution Found')
                print("States Explored: ", self.states_explored)
                return state
            
            explored_states.add(tuple(state))
            self.states_explored += 1
            
            for neighbour in self.find_neighbours(state):
                if tuple(neighbour) not in explored_states and neighbour not in frontier:
                    frontier.append(neighbour)



# Complexity exponentialy increases for large number of Queens
# Parameter1 >= 4, Patameter2: BFS/DFS
s = n_queen(4, 'BFS')
# s = n_queen(4, 'DFS')
print()
s.Print_board(s.solve())
