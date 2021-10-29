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
        self.parent = None
        self.child = None
        self.left = None
        self.right = None
        self.degree = 0
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
    
    def set_value(self, k):
        if self.key > k:
            self.key = k
    
    def isolate(self):
        if self.parent != None:
            if self.parent.child == self:
                if self.right != None:
                    self.parent.child = self.right
                else:
                    self.parent.child = self.left
            self.parent.degree -= 1
            self.parent = None
        
        former_left = self.left
        former_right = self.right

        if former_left != None:
            former_left.right = former_right

        if former_right != None:
            former_right.left = former_left
        
        self.left = None
        self.right = None

        self.unmark()
       
    def array_of_right_elements(self):
        arr = []
        current_node = self
        next_node = self.right
        while next_node != None:
            arr.append(next_node)
            current_node = next_node
            next_node = current_node.right
            current_node.isolate()
        return arr
    
    def array_of_left_elements(self):
        arr = []
        next_node = self.left
        while next_node != None:
            arr.append(next_node)
            current_node = next_node
            next_node = current_node.left
            current_node.isolate()
        return arr
        
