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
        current_min = self.min
        self.tree[self.min_pos] = self.tree[self.n - 1]
        self.tree.pop()
        self.n -= 1
        h = self._get_height()
        floor = 2**(h - 1)
        basement = floor // 2
        elements_on_h_level = self.n - floor
        for i in range(floor - math.ceil(elements_on_h_level // 2) + elements_on_h_level, self.n):



    def insert(self, x, k):
        self.tree.append((x, k))
        self.n += 1
        if self.n == 1:
            self.min = k
            self.min_pos = 0
        else:
            self._relocate_node(self.n, k)
    
    def empty(self):
        return bool(self.n)
    
    def decrease_key(self, x, k):
        for i in range(self.n):
            if self.tree[i][0] == x:
                self.tree[i][1] = k
                self._relocate_node(i + 1, k)
                break
    
    def _relocate_node(self, node_ref, k):
        aux_1 = node_ref
        aux_2 = node_ref // 2
        while aux_2 > 0 and self.tree[aux_2 - 1][1] < k:
            self.tree.swap(aux_1 - 1, aux_2 - 1)
            aux_1 //= 2
            aux_2 //= 2
        if self.min > k:
            self.min = k
            self.min_pos = aux_1 - 1
    
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


class FibonacciHeap(PriorityQueueInterface):

    def __init__(self) -> None:
        self.min = None
        self.tree = []
        pass

    def extract_min(self):
        pass
    
    def insert(self, x, k):
        pass
    
    def empty(self):
        pass
    
    def decrease_key(self, x, k):
        pass