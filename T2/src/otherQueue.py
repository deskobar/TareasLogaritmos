import math
from src.priorityQueue import PriorityQueueInterface


class aFibonacciHeap(PriorityQueueInterface):

    # internal node class
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.parent = None
            self.child = None
            self.left = None
            self.right = None
            self.degree = 0
            self.mark = False

        def get_degree(self):
            return self.degree
        def increment_degree(self):
            self.degree += 1
        def decrement_degree(self):
            self.degree -= 1
        
    def __init__(self, total_elements):
        self.root_list = None
        self.min_node = None
        self.total_nodes = 0
        self.elements_in_order = [None] * total_elements
        
    def _iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right
    
    def _merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node

    def _merge_with_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node

    def _remove_from_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left

    def _remove_from_child_list(self, parent, node):
        if parent.child == parent.child.right:
            parent.child = None
        elif parent.child == node:
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left

    def _cut(self, x, y):
        self._remove_from_child_list(y, x)
        y.decrement_degree()
        self._merge_with_root_list(x)
        x.parent = None
        x.mark = False

    def _cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if y.mark is False:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def _consolidate(self):
        A = [None] * int(math.log(self.total_nodes) * 2)
        nodes = [w for w in self._iterate(self.root_list)]
        for x in nodes:
            d = x.get_degree() - 1
            while A[d] != None:
                y = A[d]
                if x.value > y.value:
                    temp = x
                    x, y = y, temp
                self._heap_link(y, x)
                A[d] = None
                d += 1
            A[d] = x            
        for node in A:
            if node is not None and node.value < self.min_node.value:
                self.min_node = node

    def _heap_link(self, y, x):
        self._remove_from_root_list(y)
        y.left = y.right = y
        self._merge_with_child_list(x, y)
        x.increment_degree()
        y.parent = x
        y.mark = False

    def empty(self):
        return self.total_nodes == 0

    def extract_min(self):
        z = self.min_node
        if z is not None:
            if z.child is not None:
                children = [x for x in self._iterate(z.child)]
                for i in range(0, len(children)):
                    self._merge_with_root_list(children[i])
                    children[i].parent = None
            self._remove_from_root_list(z)
            if z == z.right:
                self.min_node = None
                self.root_list = None
            else:
                self.min_node = z.right
                self._consolidate()
            self.total_nodes -= 1
        return z.key, z.value

    def insert(self, key, value):
        n = self.Node(key, value)
        n.left = n.right = n
        self._merge_with_root_list(n)
        if self.min_node is None or n.value < self.min_node.value:
            self.min_node = n
        self.total_nodes += 1
        self.elements_in_order[key - 1] = n
        return n

    def decrease_key(self, x, k):
        node = self.elements_in_order[x - 1]
        if k > node.value:
            return None
        node.value = k
        y = node.parent
        if y is not None and node.value < y.value:
            self._cut(node, y)
            self._cascading_cut(y)
        if node.value < self.min_node.value:
            self.min_node = node

    

    

    
