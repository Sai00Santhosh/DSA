class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right
    
    def get_grandparent(self):
        if self.parent is not None:
            return self.parent.parent
        else:
            return None

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        p = self.parent
        n = self.left
        
        self.left, n.right = n.right, self
        n.parent = p
        self.parent = n
        
        if self.left is not None:
          self.left.parent = self
          
        if p is not None:
          if p.left == self:
            p.left = n
          else:
            p.right = n
            
        return n
        
    def rotate_left(self):
        p = self.parent
        n = self.right
        
        self.right, n.left = n.left, self
        n.parent = p
        self.parent = n
        
        if self.right is not None:
          self.right.parent = self
          
        if p is not None:
          if p.left == self:
            p.left = n
          else:
            p.right = n
            
        return n


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, n):
        
        while n.parent is not None and n.get_grandparent is not None:
            if not (n.is_red() and n.parent.is_red()):
                break;
            
            if n.get_uncle() is not None and n.get_uncle().is_red():
                n.get_grandparent().make_red()
                n.parent.make_black()
                n.get_uncle().make_black()
                n = n.get_grandparent()
            else:
                if n.parent == n.get_grandparent().left and n == n.parent.right:
                    n, _ = n.parent, n.parent.rotate_left()
                elif n.parent == n.get_grandparent().right and n == n.parent.left:
                    n, _ = n.parent, n.parent.rotate_right()
                else:
                    n.parent.make_black()
                    n.get_grandparent().make_red()
                    
                    if n.parent == n.get_grandparent().left:
                        n = n.get_grandparent().rotate_right()
                    else:
                        n = n.get_grandparent().rotate_left()
                    if n.parent is None:
                        self.root = n
                        
        if self.root.is_red():
            self.root.make_black()

                    
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"