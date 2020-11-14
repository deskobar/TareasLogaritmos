import math
from src.trees import BMinHeapNode, BinomNode
from src.utils import log2_ceil

'''
PriorityQueueInterface
pseudo-interfaz para implementar colas de prioridad
'''
class PriorityQueueInterface:
    
    def extract_min(self):
        """Extrae el minimo de la cola"""
        pass
    
    def insert(self, x, k):
        """Inserta el (x, k) en la cola"""
        pass
    
    def empty(self):
        """Retorna si la cola está vacía o no"""
        pass
    
    def decrease_key(self, x, k):
        """Cambia la clave de elemento (x, k) -> (x, k')"""
        pass


class BinaryHeap(PriorityQueueInterface):
    
    def __init__(self, total_elements) -> None:
        self.tree = []
        self.n = 0
        self.elements_in_order = [None] * total_elements
    
    def extract_min(self):
        self._swap(0, self.n - 1)
        extracted_min = self.tree.pop()
        self.elements_in_order[extracted_min[0] - 1] = None
        self.n -= 1
        if self.n > 0:
            self._min_heapify()
        return extracted_min

    def insert(self, x, k):
        new_duple = BMinHeapNode(x, k, self.n)
        self.tree.append(new_duple)
        self.elements_in_order[x - 1] = new_duple
        self.n += 1
        self.float_node_up(self.n - 1)
    
    def empty(self):
        return not bool(self.n)
    
    def decrease_key(self, x, k):
        for i in range(self.n):
            if self.tree[i][0] == x:
                self.elements_in_order[x - 1] = min(self.tree[i][1], k) # RECORDAR OPTIMIZAR ESTO 
                self._float_up(i, k)
                break
    
    def _float_up(self, node_pos, k):
        child_pos = node_pos
        parent_pos = self._get_parent_node_pos(node_pos)
        
        while child_pos > 0 and self.tree[parent_pos][1] > k:
            self._swap(child_pos, parent_pos)
            child_pos = parent_pos
            parent_pos = self._get_parent_node_pos(child_pos)
    
    def _get_height(self):
        if self.n == 0:
            return 0
        k = 1
        logn = 0
        halfn = self.n // 2
        while k <= halfn:
            logn += 1
            k += k
        return logn
    
    def _min_heapify(self):
        node_pos = 0
        left_node_pos = self._get_left_node_pos(node_pos)
        right_node_pos = self._get_right_node_pos(node_pos)
        min_child_pos = 0
        while left_node_pos < self.n:
            min_child_pos = self._get_min_pos_from(left_node_pos, right_node_pos)
            if self.tree[node_pos][1] > self.tree[min_child_pos][1]:
                self._swap(node_pos, min_child_pos)
                node_pos = min_child_pos
                left_node_pos = self._get_left_node_pos(node_pos)
                right_node_pos = self._get_right_node_pos(node_pos)
            else: break
    
    def _get_min_pos_from(self, pos_1, pos_2):
        if pos_1 < self.n and (pos_2 >= self.n or self.tree[pos_1][1] <= self.tree[pos_2][1]):
            return pos_1
        if pos_2 < self.n:
            return pos_2
        return None

    def _get_left_node_pos(self, pos):
        return 2 * (pos + 1) - 1
    
    def _get_right_node_pos(self, pos):
        return 2 * (pos + 1)
    
    def _get_right_node(self, pos):
        if pos < self.n:
            return self.tree[2 * (pos + 1)]
        return None

    def _get_parent_node_pos(self, pos):
        return ((pos + 1) // 2) - 1
    
    def _swap(self, pos_1, pos_2):
        aux = self.tree[pos_1]
        self.tree[pos_1] = self.tree[pos_2]
        self.tree[pos_2] = aux



class FibonacciHeap(PriorityQueueInterface):

    def __init__(self, total_elements) -> None:
        self.queue = []
        self.queue_length = 0
        self.min_element = None
        self.min_value = None
        self.min_pos = -1
        self.elements_in_order = [None] * total_elements
    

    def insert(self, x, k):
        new_node = BinomNode(x, k)
        self.queue.append(new_node)
        self.elements_in_order[x - 1] = new_node
        self.queue_length += 1
        if self.min_value == None or self.min_value > k:
            self.min_value = k
            self.min_element = x
            self.min_pos = self.queue_length - 1
    

    def empty(self):
        return not bool(self.queue_length)
    

    def decrease_key(self, x, k):
        self.elements_in_order[x - 1].set_value_and_relocate(k)
    

    def extract_min(self):
        if self.min_pos == -1:
            return None
        
        # extraction
        ret_node = self.queue[self.min_pos]
        self.queue.pop(self.min_pos)
        for child in ret_node:
            self.queue.append(child)

        # conversion to binomial forest
        aux_queue = [None] * log2_ceil(self.queue_length)
        for tree in self.queue:
            transition_tree = tree
            while aux_queue[transition_tree.degree] != None:
                transition_tree = self.fuse(transition_tree, aux_queue[transition_tree.degree])
                aux_queue[transition_tree.degree] = None
            aux_queue[transition_tree.degree] = transition_tree
        self.queue = aux_queue


    def _fuse(self, tree_1, tree_2):
        if tree_1.degree > tree_2.degree:
            greater_tree = tree_2
            tree_2.add_child(tree_1)
        else:
            greater_tree = tree_1
            tree_1.add_child(tree_2)
        return greater_tree