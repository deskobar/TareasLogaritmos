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
        
