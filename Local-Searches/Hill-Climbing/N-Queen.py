import random

class FourQueens:
    def __init__(self):
        self.n = 4

    def generate_random_state(self):
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    def print_board(self, state):
        print(state)
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if state[col] == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()

    def cost(self, state):
        attacking_pairs = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    attacking_pairs += 1
        return attacking_pairs

    def get_neighbors(self, state):
        neighbors = []
        for col in range(self.n):
            for row in range(self.n):
                if state[col] != row:
                    new_state = state[:]
                    new_state[col] = row
                    neighbors.append(new_state)
        return neighbors

    def hill_climbing(self, initial_state):
        current = initial_state
        current_cost = self.cost(current)

        while True:
            neighbors = self.get_neighbors(current)
            next_state = None
            next_cost = current_cost

            for neighbor in neighbors:
                neighbor_cost = self.cost(neighbor)
                if neighbor_cost < next_cost:
                    next_state = neighbor
                    next_cost = neighbor_cost

            if next_state is None or next_cost >= current_cost:
                break
            current = next_state
            current_cost = next_cost

        return current, current_cost

    def random_restart_hill_climbing(self, max_restarts=1000):
        for _ in range(max_restarts):
            initial_state = self.generate_random_state()
            solution, solution_cost = self.hill_climbing(initial_state)
            if solution_cost == 0:
                return solution, solution_cost
        return None

# Initialize and solve the 4-Queens problem
four_queens = FourQueens()
solution, sol_cost = four_queens.random_restart_hill_climbing()


if solution:
    print("Solution Found:")
    four_queens.print_board(solution)
    print('Number Of Attacks', sol_cost)
else:
    print("No solution found after maximum restarts.")
