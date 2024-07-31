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