class Node:
    def __init__(self, key, color="RED"):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.root = self.NIL

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "RED"
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)

        self.root.color = "BLACK"

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def search(self, key):
        result = self._search(self.root, key)
        if result == self.NIL:
            return None
        return result.key

    def _search(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node != self.NIL:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def remove(self, key):
            node = self._search(self.root, key)
            if node == self.NIL:
                return
            self.remove_node(node)

    def remove_node(self, node):
        if node.left != self.NIL and node.right != self.NIL:
            successor = self.find_successor(node.right)
            node.key = successor.key
            self.remove_node(successor)
        else:
            child = node.right if node.right != self.NIL else node.left
            self.transplant(node, child)
            if node.color == "BLACK":
                self.fix_remove(child)

    def find_successor(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def fix_remove(self, node):
        while node != self.root and node.color == "BLACK":
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    node.parent.color = "RED"
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == "BLACK" and sibling.right.color == "BLACK":
                    sibling.color = "RED"
                    node = node.parent
                else:
                    if sibling.right.color == "BLACK":
                        sibling.left.color = "BLACK"
                        sibling.color = "RED"
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = "BLACK"
                    sibling.right.color = "BLACK"
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    node.parent.color = "RED"
                    self.right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == "BLACK" and sibling.left.color == "BLACK":
                    sibling.color = "RED"
                    node = node.parent
                else:
                    if sibling.left.color == "BLACK":
                        sibling.right.color = "BLACK"
                        sibling.color = "RED"
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = "BLACK"
                    sibling.left.color = "BLACK"
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = "BLACK"

rbt = RedBlackTree()
rbt.insert(8)
rbt.insert(4)
rbt.insert(13)
rbt.insert(10)
rbt.insert(22)
rbt.insert(9)
rbt.insert(11)

print(rbt.inorder_traversal())  

rbt.remove(22)
print("Red-Black Tree inorder traversal after deletion of key 22:")
print(rbt.inorder_traversal())  
print("Search for key 10:", rbt.search(10))  # 10
print("Search for key 5:", rbt.search(5))    # None
print("Search for key 22:", rbt.search(22))    # None
