import math

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

    def __init__(self) -> None:
        self.tree = []
        self.min = None
        self.min_pos = None
        self.n = 0
    
    def extract_min(self):
        extracted_min = self.min
        self.tree[self.min_pos] = self.tree[self.n - 1]
        self.min = self.tree[self.min_pos][1]
        self.tree.pop()
        self.n -= 1
        self._relocate_min()
        h = self._get_height()
        floor = 2**(h - 1)
        elements_on_h_level = self.n - floor
        for i in range(floor - math.ceil(elements_on_h_level // 2) + elements_on_h_level, self.n):
            examined = self.tree[i]
            if examined < self.min:
                self.min = examined
                self.min_pos = i
        return extracted_min

    def insert(self, x, k):
        self.tree.append((x, k))
        self.n += 1
        if self.n == 1:
            self.min = k
            # self.min_pos = 0
        else:
            self._float_up(self.n, k)
    
    def empty(self):
        return bool(self.n)
    
    def decrease_key(self, x, k):
        for i in range(self.n):
            if self.tree[i][0] == x:
                self.tree[i] = x, min(self.tree[i][1], k) # RECORDAR OPTIMIZAR ESTO
                #self.tree[i][1] = 
                self._float_up(i, k)
                break
    
    def _float_up(self, node_pos, k):
        child_pos = node_pos
        parent_pos = self._get_parent_node_pos(node_pos)
        
        while child_pos > 0 and self._get_parent_node(child_pos)[1] > k:
            self._swap(child_pos, parent_pos)
            child_pos = parent_pos
            parent_pos = self._get_parent_node_pos(child_pos)
        if self.min > k:
            self.min = k
            # self.min_pos = aux_1 - 1
    
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
        left_node_pos = self._get_left_node_pos()
        right_node_pos = self._get

    def _get_left_node_pos(self, pos):
        return 2 * (pos + 1) - 1
    
    def _get_right_node_pos(self, pos):
        return 2 * (pos + 1)

    def _get_left_node(self, pos):
        return self.tree[2 * (pos + 1) - 1]
    
    def _get_right_node(self, pos):
        return self.tree[2 * (pos + 1)]
    
    def _get_parent_node_pos(self, pos):
        return ((pos + 1) // 2) - 1

    def _get_parent_node(self, pos):
        return self.tree[self._get_parent_node_pos]
    
    def _swap(self, pos_1, pos_2):
        aux = self.tree[pos_1]
        self.tree[pos_1] = self.tree[pos_2]
        self.tree[pos_2] = aux



class FibonacciHeap(PriorityQueueInterface):

    class Node:
        """
        a -> b -> c
            / \
           d   e
        """
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.parent = None
            self.child = None
            self.left = None
            self.right = None
            self.degree = 0
            self.mark = False
            
            
    def __init__(self, n) -> None:
        self.root_list = [None for i in range(n)]
        self.min_node_index  = -1
        self.used_nodes = 0

    def extract_min(self):
        current_min_index = self.min_node_index

        # lista -> bosque binomial
        if current_min_index != -1:
            current_min = self.root_list[current_min_index]
            
        
        pass
    
    def insert(self, x, k):
        node = Node(x, k)
        self.root_list[x] = node
        current_min = self.root_list[self.min_node_index] 
        if current_min is None or node.key < self.current_min.key:
            self.min_node_index = x
        self.used_nodes += 1
        return node

    def empty(self):
        return used_nodes == 0
    
    def decrease_key(self, x, k):
        self.root_list[x].value = k
        pass