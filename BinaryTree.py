class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def delete(self, data):
        self.root = self._delete(data, self.root)

    def _delete(self, data, node):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(data, node.left)
        elif data > node.data:
            node.right = self._delete(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.data = min_node.data
                node.right = self._delete(min_node.data, node.right)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self.print_tree(node.left, level + 1)

tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

print("Original tree:")
tree.print_tree(tree.root)

tree.delete(20)

print("\nTree after deleting 20:")
tree.print_tree(tree.root)

tree.delete(30)

print("\nTree after deleting 30:")
tree.print_tree(tree.root)

tree.delete(50)

print("\nTree after deleting 50:")
tree.print_tree(tree.root)

