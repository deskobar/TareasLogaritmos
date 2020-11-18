class Node:

    def __init__(self, value, *children):
        self.key = value
        self.children = children
    
class DupleNode(Node):

    def __init__(self, x, k, *children):
        self.key = (x, k)
        self.children = children

class BMinHeapNode:

    def __init__(self, x, k, spawn_pos):
        self.element = x
        self.key = k
        self.pos = spawn_pos

    def set_key(self, k):
        self.key = k

    def set_pos(self, new_pos):
        self.pos = new_pos
    
    def get_pos(self):
        return self.pos


class BinomNode:

    def __init__(self, x, k):
        self.element = x
        self.key = k
        self.child = None
        self.left = None
        self.right = None
        # self.children = []
        self.degree = 0
        self.parent = None
        self.marked = False
    
    def mark(self):
        if self.parent != None:
            self.marked = True
    
    def unmark(self):
        self.marked = False
    
    def is_marked(self):
        return self.marked

    def add_child(self, new_child):
        if self.child == None:
            self.child = new_child
        else:
            self.child.append_node(new_child)
        # self.children.append(new_child)
        self.degree += 1
        new_child.set_parent(self)
    
    def append_node(self, new_node):
        if self.right != None:
            self.right.left = new_node
            new_node.right = self.right
        self.right = new_node
        new_node.left = self
    
    def set_parent(self, new_parent):
        self.parent = new_parent
    
    def get_parent(self):
        return self.parent
    
    '''
    def swap_with_parent(self):
        former_parent = self.parent
        aux_degree = self.degree
        self.parent.swap_with_child(aux_degree)
        #self.children[aux_degree] = former_parent
        if self.parent != None:
            self.parent.children[self.degree] = self

    
    def swap_with_child(self, child_deg):
        #print("child degree:", child_deg, "len(self.children) =", len(self.children))
        swap_child = self.children[child_deg]
        aux_parent = self.parent
        aux_children = self.children
        aux_degree = self.degree
        aux_children[child_deg] = self # OJO
        self.set_tree_pos(swap_child, swap_child.children, swap_child.degree)
        swap_child.set_tree_pos(aux_parent, aux_children, aux_degree)
    
    def set_tree_pos(self, new_parent, new_children, new_degree):
        self.parent = new_parent
        self.children = new_children
        for child in self.children:
            child.set_parent(self)
        self.degree = new_degree
    
    def _float_up(self):
        while self.parent != None and self.parent.key > self.key:
            self.swap_with_parent()
    
    def set_value_and_relocate(self, k):
        if self.key > k:
            self.key = k
            self._float_up()
    '''
    def set_value(self, k):
        if self.key > k:
            self.key = k
    
    #def remove_child(self, child_deg):
    #    self.children.pop(child_deg)
    #   self.degree -= 1
    
    def isolate(self):
        if self.parent != None:
            if self.parent.child == self:
                if self.right != None:
                    self.parent.child = self.right
                else:
                    self.parent.child = self.left
            self.parent.degree -= 1
            self.parent = None
        
        if self.left != None:
            self.left.right = self.right
        self.left = None

        if self.right != None:
            self.right.left = self.left
        self.right = None

        self.unmark()
    
    def add_left_to_array(self, arr):
        if self.left != None:
            arr.append(self.left)
            self.left.add_left_to_array(arr)
        
    def add_right_to_array(self, arr):
        if self.right != None:
            arr.append(self.right)
            self.right.add_right_to_array(arr)
        
