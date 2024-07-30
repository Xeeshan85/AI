from collections import deque
from string import ascii_lowercase

class Word_Ladder:
    def __init__(self, start, goal, algorithm):
        self.start = start
        self.goal = goal
        self.BFS = False
        self.DFS = False
        if algorithm.upper() == 'BFS':
            self.BFS = True
        elif algorithm.upper() == 'DFS':
            self.DFS = True
        else:
            raise Exception('Invalid Algorithm Parameter. Use \'BFS\' or \'DFS\'.')
        
        with open("dictionary.txt") as f:
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
    
    def print_solution(self, path, states_explored):
        if path:
            print("Path found:", " -> ".join(path))
            print('States Explored: ', states_explored)
        else:
            print("No path found.")

    def solve(self):
        frontier = deque()
        frontier.append(self.start)

        explored_words = set()
        parent_map = {self.start: None}
        words_explored = 0

        while frontier:
            if self.BFS:
                word = frontier.popleft()
            elif self.DFS:
                word = frontier.pop()

            if word == self.goal:
                path = []
                while word:
                    path.append(word)
                    word = parent_map[word]
                path.reverse()
                self.print_solution(path, words_explored)
                return
            
            explored_words.add(word)
            words_explored += 1

            for neighbour in self.find_neighbours(word):
                if neighbour not in explored_words and neighbour not in frontier:
                    parent_map[neighbour] = word # Set the parent
                    frontier.append(neighbour)

        return None


start = 'hit'
goal = 'cog'
algorithm = 'bfs' # BFS/DFS
game = Word_Ladder(start, goal, algorithm)
game.solve()