#tutorial link: https://www.youtube.com/watch?v=GnKHVXv_rlQ

import math
from LinkedList import LinkedList
from Node import Node
class MaxHeap:
    def __init__(self):
        self.heap = LinkedList()
        self.size = 0

    def push(self, data):
        self.heap.insert_val(self.size - 1, data)
        self.__heapifyUp(self.size)
        self.__heapifyDown(0)
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
            self.__heapifyDown(0)

        elif self.size == 2:
            self.heap.delete(0)
            root = self.heap.find(0)
        return root

    # private methods (denoted with "__" at the beginning)

    def __swap(self, i, j):
        i_holder = self.heap.find(i).get_data()

        self.heap.find(i).set_data(self.heap.find(j).get_data())
        self.heap.find(j).set_data(i_holder)

    def __heapifyUp(self, index):
        print("index: {} {}".format(index,self.heap))
        parent = (index // 2)
        right = int(index / 2 - 1)
        left = int(index - 1)
        if index <= 1:
            return

        #print("parent: comparing {} with {}".format(self.heap.find(index).get_data()[0], self.heap.find(parent).get_data()[0]))
        if self.heap.find(index).get_data()[0] > self.heap.find(parent).get_data()[0]:
            #print("{} is greater than {}".format(self.heap.find(index).get_data()[0], self.heap.find(parent).get_data()[0]))
            self.__swap(index, parent)
            self.__heapifyUp(parent)


    def __heapifyDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if index % 2 == 0 and self.heap.find(right).get_data()[0] < self.heap.find(left).get_data()[0]:
            print("right: {} is less than {}".format(self.heap.find(right).get_data()[0],
                                                 self.heap.find(largest).get_data()[0]))
            self.__swap(right, left)

        if self.size > left and self.heap.find(largest).get_data()[0] < self.heap.find(left).get_data()[0]:
            largest = left
        if self.size > right and self.heap.find(largest).get_data()[0] < self.heap.find(right).get_data()[0]:
            largest = right

        if largest != index:
            self.__swap(index, largest)
            self.__heapifyDown(largest)

    def to_str(self):
        num_levels = self.get_levels()

        for i in range(1, num_levels + 1):
            level_str = ""
            for j in range(int(math.pow(2, i-1)) - 1, int(math.pow(2, i)) - 1):
                j_data = self.heap.find(j).get_data()[0]
                level_str += str(j_data) + " "
            print(level_str)

        print("\n")


    def get_levels(self, levels=0, power=0):
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







