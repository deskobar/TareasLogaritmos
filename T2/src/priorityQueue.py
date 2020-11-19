import math
from src.trees import BMinHeapNode, BinomNode
from src.utils import log2_ceil, log2_floor

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
        """Retorna si la cola esta vacia o no"""
        pass
    
    def decrease_key(self, x, k):
        """Cambia la clave de elemento (x, k) -> (x, k')"""
        pass


class BinaryHeap(PriorityQueueInterface):
    
    def __init__(self, total_elements):
        self.tree = []
        self.n = 0
        self.elements_in_order = [None] * total_elements
    
    def extract_min(self):
        self._swap(0, self.n - 1)
        extracted_min = self.tree.pop()
        self.elements_in_order[extracted_min.element - 1] = None
        self.n -= 1
        if self.n > 0:
            self._min_heapify()
        return extracted_min.element, extracted_min.key

    def insert(self, x, k):
        new_duple = BMinHeapNode(x, k, self.n)
        self.tree.append(new_duple)
        self.elements_in_order[x - 1] = new_duple
        self.n += 1
        self._float_node_up(self.n - 1)
    
    def empty(self):
        return not bool(self.n)
    
    def decrease_key(self, x, k):
        node_to_move = self.elements_in_order[x - 1]
        if node_to_move.key > k:
            node_to_move.set_key(k)
        self._float_node_up(node_to_move.get_pos())
    
    def _float_node_up(self, node_pos):
        child_pos = node_pos
        parent_pos = self._get_parent_node_pos(node_pos)
        
        # compare with parent and swap
        while child_pos > 0 and self.tree[parent_pos].key > self.tree[child_pos].key:
            self._swap(child_pos, parent_pos)
            self.tree[child_pos].set_pos(child_pos) # redefine position label to former parent node 
            child_pos = parent_pos
            parent_pos = self._get_parent_node_pos(child_pos)
        
        self.tree[child_pos].set_pos(child_pos)     # redefine position label to moved node


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
            if self.tree[node_pos].key > self.tree[min_child_pos].key:
                self._swap(node_pos, min_child_pos)
                self.tree[node_pos].set_pos(node_pos)
                node_pos = min_child_pos
                left_node_pos = self._get_left_node_pos(node_pos)
                right_node_pos = self._get_right_node_pos(node_pos)
            else: break
        
        self.tree[node_pos].set_pos(node_pos)

    
    def _get_min_pos_from(self, pos_1, pos_2):
        if pos_1 < self.n and (pos_2 >= self.n or self.tree[pos_1].key <= self.tree[pos_2].key):
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

    def __init__(self, total_elements):
        self.queue = []
        self.queue_length = 0
        self.min = None
        self.current_elements = 0
        self.elements_in_order = [None] * total_elements
    

    def insert(self, x, k):
        new_node = BinomNode(x, k)
        self._add_to_queue(new_node)
        self.elements_in_order[x - 1] = new_node
        self.current_elements += 1
        if self.min.key > k:
            self.min = new_node
    

    def empty(self):
        # print('is heap empty?')
        return self.min == None
    

    def decrease_key(self, x, k):
        changed_node = self.elements_in_order[x - 1]
        changed_node.set_value(k)
        if changed_node.parent != None:
            self._cut(changed_node)
        if k < self.min.key:
            self.min = changed_node

    def _cut(self, node):
        parent_node = node.get_parent()
        if parent_node != None:
            node.isolate()
            self._add_to_queue(node)
            if parent_node.is_marked():
                self._cut(parent_node)
            else:
                parent_node.mark()

    def extract_min(self):
        if self.min == None:
            return None
        
        # extraction
        former_min = self.min
        self._extract_list(former_min.child)
        rts_arr = self._roots_array()
        former_min.isolate()
        self.elements_in_order[former_min.element - 1] = None
        self.current_elements -= 1

        # conversion to binomial forest
        aux_queue = [None] * (log2_ceil(self.current_elements + 1) + 1)
        for tree in rts_arr:
            tree.isolate()
            transition_tree = tree
            while aux_queue[transition_tree.degree] != None:
                transition_tree = self._fuse(transition_tree, aux_queue[transition_tree.degree])
                aux_queue[transition_tree.degree - 1] = None
               # print('transition tree has degree {} and aux_queue has size {}'.format(transition_tree.degree, len(aux_queue)))
               # print('total number of elements is {}'.format(self.current_elements))
            aux_queue[transition_tree.degree] = transition_tree
        
        # redefine heap
        self.min = None
        for node in aux_queue: 
            if node != None:
                self._add_to_queue(node)
                
        return former_min.element, former_min.key


    def _fuse(self, tree_1, tree_2):
        if tree_1.key > tree_2.key:
            greater_tree = tree_2
            lesser_tree = tree_1
        else:
            greater_tree = tree_1
            lesser_tree = tree_2
        greater_tree.add_child(lesser_tree)
        return greater_tree
    
    def _add_to_queue(self, node):
        if self.min != None:
            self.min.append_node(node)
            if self.min.key > node.key:
                self.min = node
        else:
            self.min = node

    def _extract_list(self, node):
        if node != None:
            right_node = node.right
            node.isolate()
            self._add_to_queue(node)
            self._extract_list(right_node)
    
    def _roots_array(self):
        if self.min != None:
            return self.min.array_of_left_elements() + self.min.array_of_right_elements()
        return []
