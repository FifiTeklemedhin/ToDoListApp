#tutorial link: https://www.youtube.com/watch?v=GnKHVXv_rlQ
from collections import deque
import math

class MaxHeap:
    def __init__(self, items = []):
        self.heap = []
        for i in items:
            self.heap.append(i)
            self.__heapifyUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__heapifyUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    def pop(self):
        root = False

        if len(self.heap) > 2:
            self.__swap(0, len(self.heap) - 1)
            root = self.heap.pop()
            self.__heapifyDown(0)

        elif len(self.heap) == 2:
            root = self.heap.pop()

        return root

    # private methods (denoted with "__" at the beginning)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __heapifyUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__heapifyUp(parent)

    def __heapifyDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != index:
            self.__swap(index, largest)
            self.__heapifyDown(largest)

    def to_str(self):
        num_levels = self.get_levels()
        print("num levels: {}".format(num_levels))
        for i in range(1, num_levels + 1):
            level_str = ""
            for j in self.heap[int(math.pow(2, i-1)) -1: int(math.pow(2, i))-1]:
                level_str += str(j) + " "
            print(level_str)


    def get_levels(self, levels=0, power=0):
        if power >= len(self.heap):
            return levels
        return self.get_levels(levels + 1, int(math.pow(2, levels + 1) - 1))






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






