#tutorial link: https://www.youtube.com/watch?v=GnKHVXv_rlQ

import math

class MaxHeap:
    def __init__(self, items = [[]]):
        self.heap = []
        for i in items:
            self.heap.append(i)
            self.__heapifyUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__heapifyUp(len(self.heap) -1)

    def peek(self):
        if self.heap[0]:
            return self.heap[0][0]
        return False

    def pop(self):
        root = False

        if len(self.heap) > 2:
            self.__swap(0, len(self.heap) - 1)
            root = self.heap.pop()
            self.__heapifyDown(0)

        elif len(self.heap) == 2:
            self.heap.remove(self.heap[0])
            root = self.heap[0]
        return root

    # private methods (denoted with "__" at the beginning)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __heapifyUp(self, index):
        parent = index // 2
        right = int(index / 2 -1)
        left = int(index / 2)
        if index <= 1:
            return

        if index % 2 == 0 and self.heap[right][0] < self.heap[index][0]:
            self.__swap(index, right)
            self.__heapifyUp(right)


        elif index % 2 == 1 and self.heap[left][0] > self.heap[index][0]:
            self.__swap(index, left)
            self.__heapifyUp(left)

        if self.heap[index][0] > self.heap[parent][0]:
            self.__swap(index, parent)
            self.__heapifyUp(parent)

    def __heapifyDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if len(self.heap) > left and self.heap[largest][0] < self.heap[left][0]:
            largest = left
        if len(self.heap) > right and self.heap[largest][0] < self.heap[right][0]:
            largest = right

        if largest != index:
            self.__swap(index, largest)
            self.__heapifyDown(largest)

    def to_str(self):
        num_levels = self.get_levels()

        for i in range(1, num_levels + 1):
            level_str = ""
            for j in self.heap[int(math.pow(2, i-1)) - 1: int(math.pow(2, i)) - 1]:
                level_str += str(j[1]) + " "
            print(level_str)

        print("\n")


    def get_levels(self, levels=0, power=0):
        if power >= len(self.heap):
            return levels
        return self.get_levels(levels + 1, int(math.pow(2, levels + 1) - 1))



heap = MaxHeap([[100, "homework"]])
heap.push([36, "groceries"])
heap.push([19, "programming"])
heap.push([17, "workout"])
heap.push([25, "breakfast"])
heap.push([3, "cooking"])
heap.push([2, "paint nails"])
heap.push([7, "email"])
heap.push([1, "clubs"])


heap.to_str()
heap.pop()
heap.pop()
heap.pop()
heap.pop()
heap.pop()
heap.pop()
heap.pop()
heap.pop()
heap.pop()
heap.pop()
heap.pop()
heap.pop()


heap.to_str()
print("root: " + str(heap.peek()))
