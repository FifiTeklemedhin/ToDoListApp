class Node:
    def __init__(self, data = None, next_node = None):
      self.data = data
      self.next_node = next_node

    #getters
    def get_data(self):
        return self.data
    def get_next_node(self):
        return self.next_node

    #setters
    def set_data(self, data):
        self.data = data
    def set_next_node(self, next_node):
        self.next_node = next_node

    def __repr__(self):
        return "Node, val {}".format(self.get_data())