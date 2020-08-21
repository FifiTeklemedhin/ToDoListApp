import math
from LinkedList import LinkedList
from Node import Node
class MaxHeap:
    def __init__(self):
        self.heap = LinkedList()
        self.size = 0

    def push(self, data):
        self.heap.insert_val(self.size, data)
        self.heapifyUp(self.size)
        self.size += 1

    def peek(self):
        if self.heap.find(0):
            return self.heap.find(0).get_data()[0]
        return False

    def pop(self):
        root = False

        if self.size > 2:
            self.__swap(0, self.size - 1)
            root = self.heap.pop()
            self.heapifyDown(0)

        elif self.size == 2:
            self.heap.delete(0)
            root = self.heap.find(0)
        return root

    # private methods (denoted with "__" at the beginning)

    def __swap(self, i, j):
        i_holder = self.heap.find(i).get_data()

        self.heap.find(i).set_data(self.heap.find(j).get_data())
        self.heap.find(j).set_data(i_holder)

    def heapifyUp(self, index):
        parent = index // 2
        if index % 2 == 1:
            parent -= 1
        #print("parent: {}".format(parent))
        if index <= 1:
            return
        if self.heap.find(index).get_data()[0] > self.heap.find(parent).get_data()[0]:
            self.__swap(index, parent)
            self.heapifyUp(parent)

    def heapifyDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if self.heap.size > left and self.heap.find(largest).get_data()[0] < self.heap.find(left).get_data()[0]:
            largest = left
        if self.heap.size > right and self.heap.find(largest).get_data()[0] < self.heap.find(right).get_data()[0]:
            largest = right

        if largest != index:
            self.__swap(index, largest)
            self.heapifyDown(largest)

    def to_str(self):
        num_levels = self.get_levels()
        for i in range(1, num_levels + 1):
            level_str = ""
            for j in range(int(math.pow(2, i-1)) - 1, int(math.pow(2, i)) - 1):
                level_str += str(self.heap.find(j).get_data()[0]) + " "
            print(level_str)

        print("\n")


    def get_levels(self, levels =0, power = 0):
        if power >= self.size:
            return levels
        return self.get_levels(levels + 1, int(math.pow(2, levels + 1) - 1))



heap = MaxHeap()
heap.push([100, "homework"])
heap.push([36, "groceries"])
heap.push([19, "programming"])
heap.push([17, "workout"])
heap.push([25, "breakfast"])
heap.push([3, "cooking"])
heap.push([2, "paint nails"])
heap.push([7, "email"])
heap.push([1, "clubs"])

heap.heapifyDown(0)
heap.to_str()
print(heap.heap)







