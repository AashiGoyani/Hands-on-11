class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.insert_recursively(self.root, value)

    def insert_recursively(self, node, value):
        if value < node.value:
            if node.left:
                self.insert_recursively(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self.insert_recursively(node.right, value)
            else:
                node.right = TreeNode(value)

    def search(self, value):
        return self.search_recursively(self.root, value)

    def search_recursively(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self.search_recursively(node.left, value)
        else:
            return self.search_recursively(node.right, value)

    def delete(self, value):
        self.root = self.delete_recursively(self.root, value)

    def delete_recursively(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self.delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self.delete_recursively(node.right, value)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_node = self.find_min(node.right)
            node.value = min_node.value
            node.right = self.delete_recursively(node.right, min_node.value)
        return node

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        result = []
        self.inorder_traversal_recursively(self.root, result)
        return result

    def inorder_traversal_recursively(self, node, result):
        if node:
            self.inorder_traversal_recursively(node.left, result)
            result.append(node.value)
            self.inorder_traversal_recursively(node.right, result)

# Test BST
bst = BST()
bst.insert(6)
bst.insert(4)
bst.insert(8)
bst.insert(2)
bst.insert(5)
bst.insert(1)
bst.insert(3)

print("Binary Search Tree after insertion:")
print(bst.inorder_traversal()) 

bst.delete(2)
bst.delete(4)
bst.delete(8)

print("Binary Search Tree after deletion of value 3:")
print(bst.inorder_traversal())  
print("Searching for value 6:", bst.search(6))  # True
print("Searching for value 2:", bst.search(2))  # False
