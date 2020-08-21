from LinkedList import LinkedList
from Node import Node
import math

class MaxHeap:
    def __init__(self):
        self.size = 0
        self.heap = LinkedList()

    # public methods

    def push(self, data):
        # Inserts a value in the LinkedList as the new tail, then heapifies up to restore the heap
        self.size += 1
        self.heap.insert_val(self.size, data)
        self.__heapify_up(self.size)

    def peek(self):
        # Returns the root without deleting it
        if self.size <= 0:
            return
        return self.heap.find(0)

    def pop(self):
        # Deletes the root, and returns its value
        if self.size <= 0:
            return

        root = self.heap.get_head_node()
        self.__swap(0, self.size)
        self.heap.delete(self.size)
        self.size -= 1
        self.__heapify_down(0)

        return root
    # Private methods

    def __heapify_up(self, index):
        # Recursively bubbles up from the last (and newest) index, restoring the heap
        parent = index // 2

        # Means you're already at the top of the heap
        if index <= 1:
            return

        # Finds the rank of the parent and the index
        index_priority = self.heap.find(index).get_data()[0]
        parent_priority = self.heap.find(parent).get_data()[0]

        # Checks to see if the index value is higher than its parent. If so, it swaps their information so that the
        # highest priority is on top. It then continues to heapify from that highest location
        if parent_priority < index_priority:
            self.__swap(parent, index)
            self.__heapify_up(index)


    def __heapify_down(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        largest_child = index

        if index >= self.size:
            return

        if right <= self.size - 1:
            if self.heap.find(left).get_data()[0] < self.heap.find(right).get_data()[0]:
                largest_child = right
        else:
            largest_child = left

        # Finds the rank of the largest child and the index
        index_priority = self.heap.find(index).get_data()[0]
        largest_child_priority = self.heap.find(largest_child).get_data()[0]

        print("comparing {} and {}".format(index_priority, largest_child_priority))
        if largest_child_priority > index_priority:
            print("index before: {}, child before: {}".format(self.heap.find(index), self.heap.find(largest_child)))
            self.__swap(largest_child, index)
            print("index after: {}, child after: {}\n".format(self.heap.find(index), self.heap.find(largest_child)))
            self.__heapify_down(largest_child)


    def __swap(self, pos_1, pos_2):
        # Swaps the data of two indexes, so that the node higher up is the one with a higher priority.
        node_1 = self.heap.find(pos_1)
        node_2 = self.heap.find(pos_2)
        node_1_holder = node_1.get_data()

        node_1.set_data(node_2.get_data())
        node_2.set_data(node_1_holder)

    def __repr__(self):
        # The method iterates through all of the levels of the tree in the first loop.
        # The indices on that level are traversed in the nested loop: 2 ^ level - 1 through 2 ^ level.
        # Since the traversal range does not account for whether the last level is actually full or not,
        # There is a conditional that breaks out of the loop as soon as there is no Node at the given index.
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
        # 2 ^ level is the maximum amount of nodes the heap can have with that many levels. The levels start at 0
        # because 2 ^ 0 is the number of nodes at the root The maximum amount of nodes with that many levels should
        # be less than or equal to the size of the heap. If it is, then it is assumed that the level is full,
        # and the next recursive call checks if the next level is full. If it is greater than the size,
        # then the method returns the level + 1 because it started at 0. Otherwise, it continues.

        if int(math.pow(2, levels)) > self.size:
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
heap.push([4, "reading"])
heap.push([12, "studing"])
heap.push([8, "night routine"])
heap.push([15, "speech"])
heap.push([0, "sleep"])
print(heap)

heap.pop()
print(heap)
print(heap.heap)