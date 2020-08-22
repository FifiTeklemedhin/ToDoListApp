from Node import Node
class LinkedList:
    def __init__(self, head_node = Node(None)):
        self.head_node = head_node
        self.size = 1

    #accessor and mutators for self.head_node
    def set_head_node(self, node):
        self.head_node = node

    def get_head_node(self):
        return self.head_node


    #finds the index of a certain piece of data in the linked list
    '''
    def find(self, data : Node):
        current_node = self.get_head_node()
        count = 0

        while current_node.get_data() != data:
            current_node = current_node.get_data()
            count += 1

        return count
    '''
    # finds the node at a given index
    def find(self, ind : int):
        current_node = self.get_head_node()
        count = 1
        if ind == 0:
            return self.get_head_node()
        while count != ind:
            if count < self.size:
                print("out of bounds")
                return
            #print("current node : {}".format(current_node))
            if current_node.get_next_node() is None:
                return current_node
            current_node = current_node.get_next_node()
            count += 1

        return current_node

    #inserts a Node object at a specific index in the linked list
    def insert_node(self, pos, inserting: Node):
        node_before = self.get_head_node()

        if node_before is None or node_before.get_data() is None:
            self.set_head_node(inserting)
            return

        if pos == 0:
            inserting.set_next_node(self.get_head_node())
            self.set_head_node(inserting)
            return

        for i in range(pos-1):
            if node_before.get_next_node() is None:
                node_before.set_next_node(inserting)
                return

            node_before = node_before.get_next_node()

        inserting.set_next_node(node_before.get_next_node())
        node_before.set_next_node(inserting)
        self.size += 1
    #inserts a Node object at a specific index by using a value and using it to create a Node
    def insert_val(self, pos, val: float):
        self.insert_node(pos,Node(val, None))

    #removes a Node object at a specific index from the linked list
    def delete(self, pos):
         if pos == 0:
            self.set_head_node(self.get_head_node.get_next_node())
            return
         current_node = self.get_head_node()
         for i in range(pos - 1):
             if current_node.get_next_node().get_next_node() is None:
                break
             current_node = current_node.get_next_node()
         #print("node before {}".format(current_node))
         current_node.set_next_node(None)

    #toString() method that prints out the linked list from head to tail
    def __repr__(self):
        summary = "Linked List: \n"
        current_node = self.get_head_node()

        while current_node.get_next_node() is not None:
            summary += "{} -> ".format(current_node.get_data())
            current_node = current_node.get_next_node()

        summary += "{}".format(current_node.get_data())
        return summary

#recursive program that creates new Nodes, and sets them as pointers for a given head, increasing in value by 1 each time
'''
def init(n: int, count: int):
    if count != n:
        pointer = Node(count, init(n, count + 1))
        return pointer
    else:
        pointer = Node(count, None)
        return pointer


#tester
h = Node(1, init(8, 2))
lst = LinkedList(h)

lst.insert_val(10, 10.5)
print(lst)
'''