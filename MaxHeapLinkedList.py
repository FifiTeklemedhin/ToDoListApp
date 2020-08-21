from LinkedList import LinkedList
from Node import Node
import math

class MaxHeap:
    def __init__(self):
        self.size = 0
        self.heap = LinkedList()

    # public methods

    def push(self, data):
        #inserts a value in the LinkedList as the new tail, then heapifies up to restore the heap
        self.size += 1
        self.heap.insert_val(self.size, data)
        self.__heapify_up(self.size)

    def peek(self):
        if self.size <= 0:
            return
        return self.heap.find(0)

    def pop(self):
        if self.size <= 0:
            return

        root = self.heap.get_head_node()
        self.heap.delete(0)

        self.__heapify_down()

        return root
    # private methods

    def __heapify_up(self, index):
        parent = index // 2
        if index <= 1:
            print("index is root")
            return

        index_priority = self.heap.find(index).get_data()[0]
        parent_priority = self.heap.find(parent).get_data()[0]

        print("parent: {}\n index: {}".format(parent_priority, index_priority))
        if parent_priority < index_priority:
            print("swapping {} and {}".format(index_priority, parent_priority))
            self.__swap(parent, index)
            self.__heapify_up(index)


    def __heapify_down(self, index):
        pass
    def __swap(self, pos_1, pos_2):
        # swaps the data of two indexes, so that the node higher up is the one with a higher priority
        node_1 = self.heap.find(pos_1)
        node_2 = self.heap.find(pos_2)
        node_1_holder = node_1.get_data()

        node_1.set_data(node_2.get_data())
        node_2.set_data(node_1_holder)

    def __repr__(self):
        levels = self.num_levels()
        level_str = ""
        for i in range(1, levels):
            level_str += "\n"
            for j in range(int(math.pow(2, i - 1)), int(math.pow(2, i))):
                if self.heap.find(j) is None:
                    break
                level_str += str(self.heap.find(j).get_data()[0]) + " "
        level_str += "\n"
        return level_str

    def num_levels(self, levels = 0):
        if int(math.pow(2, levels)) >= self.size:
            return levels + 1

        levels += 1
        return self.num_levels(levels)




    #pop
    #peek
    #__repr__

    #heapify down
    #swap


heap = MaxHeap()
heap.push([30, "homework"])
heap.push([100, "video games"])
heap.push([35, "eating"])
heap.push([19, "programming"])
heap.push([17, "workout"])
heap.push([25, "breakfast"])
heap.push([3, "cooking"])
heap.push([2, "paint nails"])
heap.push([7, "email"])
heap.push([1, "clubs"])
print(heap.heap)
print(heap)