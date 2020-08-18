# this one implements nodes to have both a description and a rank

#tutorial link: https://www.youtube.com/watch?v=GnKHVXv_rlQ

from LinkedList import LinkedList
from Node import Node
import math

class MaxHeap:
    def __init__(self, items = []):
        self.heap = LinkedList()
        for i in range(len(items)):
            self.heap.insert_node(i, Node(items[i]))
            self.__heapifyUp(self.get_size() - 1)

    def push(self, data):
        self.heap.insert_node(-1, Node(data, None))
        self.__heapifyUp(self.get_size() -1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    def pop(self):
        root = False

        if self.get_size() > 2:
            self.__swap(0, self.get_size() - 1)
            root = self.heap.delete(0)
            self.__heapifyDown(0)

        elif self.get_size() == 2:
            root = self.heap.delete(0)

        return root

    # private methods (denoted with "__" at the beginning)

    def __swap(self, i, j):
        j_node = self.heap.find(j)
        i_node = self.heap.find(i)

        self.heap.replace_node(i, j_node)
        self.heap.replace_node(j, i_node)

    def __heapifyUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        current_data = self.heap.find(index).get_data()
        parent_data = self.heap.find(parent).get_data()

        print("current data: {}\nparent data: {}".format(current_data, parent))
        if current_data > parent_data:
            self.__swap(index, parent)
            self.__heapifyUp(parent)

    def __heapifyDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if self.get_size()  > left and self.heap.find(largest) < self.heap.find(left):
            largest = left
        if self.get_size()  > right and self.heap(largest) < self.heap.find(right):
            largest = right

        if largest != index:
            self.__swap(index, largest)
            self.__heapifyDown(largest)

    def to_str(self):
        num_levels = self.get_levels()
        print("size: {}".format(self.get_size()))
        print("num levels: {}".format(num_levels))
        for i in range(1, num_levels + 1):
            level_str = ""
            level_arr = []
            for j in range(int(math.pow(2, i-1)) -1, int(math.pow(2, i))-1):
                level_str += str(self.heap.find(j).get_data()) + " "

            print(level_str)


    def get_levels(self, levels=0, power=0):
        if power >= self.get_size():
            return levels
        return self.get_levels(levels + 1, int(math.pow(2, levels + 1) - 1))
    def get_size(self):
        count = 0
        current_node = self.heap.find(0)
        
        while current_node is not None:
            current_node = current_node.get_next_node()
            count += 1

        return count



heap = MaxHeap([100])
heap.push(36)
heap.push(19)
heap.push(17)
heap.push(25)
heap.push(3)
heap.push(2)
heap.push(7)
heap.push(1)

heap.to_str()
