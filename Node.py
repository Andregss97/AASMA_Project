class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.state == other.state

    def __lt__(self, other):
        return self.f < other.f