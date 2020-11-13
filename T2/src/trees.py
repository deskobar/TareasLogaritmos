class Node:

    def __init__(self, value, *children):
        self.value = value
        self.children = children
    
class DupleNode(Node):

    def __init__(self, x, k, *children):
        self.value = (x, k)
        self.children = children

class BinomNode:

    def __init__(self, x, k):
        self.element = x
        self.value = k
        self.children = []
        self.degree = 0
        self.parent = None
    
    def add_child(self, child):
        self.children.append(child)
        self.degree += 1
    
    def set_parent(self, new_parent):
        self.parent = new_parent
    
    def get_parent(self):
        return self.parent
    
    def swap_with_parent(self):
        former_parent = self.parent
        self.parent.swap_with_child(self.degree)
        self.children[self.degree] = former_parent
        self.degree += 1
    
    def swap_with_child(self, child_deg):
        swap_child = self.children[child_deg]
        aux_parent = self.parent
        aux_children = self.children
        self.set_tree_pos(swap_child, swap_child.children)
        self.degree -= 1
        swap_child.set_tree_pos(aux_parent, aux_children)
    
    def set_tree_pos(self, new_parent, new_children):
        self.parent = new_parent
        self.children = new_children
    
    def _float_up(self):
        while self.parent != None and self.parent.value > self.value:
            self.swap_with_parent()
    
    def set_value_and_relocate(self, k):
        self.value = k
        self._float_up()
