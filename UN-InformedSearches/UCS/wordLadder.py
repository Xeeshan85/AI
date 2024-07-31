from DataStructures import PriorityQueue
from string import ascii_lowercase
import os

# UCS greatly optimizes the problem Using BFS/DFS the average states explored
# were 250 while UCS decreased the count to 20. Nearly 12x more efficient

class Node:
    def __init__(self, state, parent, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost

class Word_Ladder:
    def __init__(self, start_word, goal):
        self.start_word = start_word
        self.goal = goal
        
        base_dir = os.path.dirname(os.path.dirname(__file__))
        dict_path = os.path.join(base_dir, 'BFS-n-DFS', 'dictionary.txt')
        with open(dict_path) as f:
            self.dictionary = f.readlines()
        self.dictionary = [word.strip().lower() for word in self.dictionary]

    def find_neighbours(self, word):
        neighbours = []
        
        for i in range(len(word)):
            for letter in ascii_lowercase:
                if letter != word[i]:
                    new_word = word[:i] + letter + word[i+1:]
                    if new_word in self.dictionary and new_word not in neighbours:
                        neighbours.append(new_word)
        return neighbours
    
    def find_cost(self, word, goal):
        """
        finds the cost with goal_cost = number of characters alike +1 
        how far is the word's character from goal: abs(word[char] - goal[char])
        """
        goal_cost = 0
        char_offset = 0
        N = len(word)
        for i in range(N):
            if word[i] == goal[i]: 
                goal_cost += 1
            else:
                char_offset += abs(ascii_lowercase.find(word[i]) - ascii_lowercase.find(goal[i]))
        return goal_cost + char_offset

    
    def print_solution(self, path, states_explored):
        if path:
            print("Path found:", " -> ".join(path))
            print('States Explored: ', states_explored)
        else:
            print("No path found.")

    def solve(self):
        explored_words = set()
        words_explored = 0

        start = Node(state=self.start_word, parent=None, cost=0)
        frontier = PriorityQueue()
        frontier.add(start)

        while frontier:
            current_node = frontier.remove()
            words_explored += 1

            if current_node.state == self.goal:
                path = []
                while current_node:
                    path.append(current_node.state)
                    current_node = current_node.parent
                path.reverse()
                self.print_solution(path, words_explored)
                return
            
            if current_node.state in explored_words:
                continue

            explored_words.add(current_node.state)

            for neighbour in self.find_neighbours(current_node.state):
                if not frontier.contains_state(neighbour) and neighbour not in explored_words:
                    new_cost = self.find_cost(neighbour, self.goal)
                    new_node = Node(neighbour, current_node, new_cost + current_node.cost)
                    frontier.add(new_node)

        return None


start = 'hit'
goal = 'cog'
game = Word_Ladder(start, goal)
game.solve()