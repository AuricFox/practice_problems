class Node:
    def __init__(self, key, color='Red'):
        # Node class representing a node in the Red-Black Tree
        self.key = key          # Key value stored in the node
        self.left = None        # Pointer to the left child
        self.right = None       # Pointer to the right child
        self.parent = None      # Pointer to the parent node
        self.color = color      # Color of the node ('Red' or 'Black')

class RedBlackTree:
    def __init__(self):
        # Initialize the Red-Black Tree with an empty root
        self.root = None

    def search(self, key):
        # Public method to search for a key in the Red-Black Tree
        return self._search(self.root, key)

    def _search(self, node, key):
        # Private recursive method to search for a key starting from a given node
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def insert(self, key):
        # Public method to insert a key into the Red-Black Tree
        new_node = Node(key)
        self._insert_helper(new_node)

    def _insert_helper(self, new_node):
        # Private helper method to insert a new node into the Red-Black Tree
        if self.root is None:
            # If the tree is empty, set the new node as the root and color it black
            self.root = new_node
            self.root.color = 'Black'
            return

        parent = None
        current = self.root

        # Traverse the tree to find the appropriate position for insertion
        while current is not None:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        # Insert the new node as left or right child of the parent
        if new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix any violations of Red-Black Tree properties after insertion
        self._fix_insertion(new_node)

    def _fix_insertion(self, node):
        # Private method to fix any violations of Red-Black Tree properties after insertion
        while node != self.root and node.parent.color == 'Red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == 'Red':
                    # Case 1: Red uncle
                    node.parent.color = 'Black'
                    uncle.color = 'Black'
                    node.parent.parent.color = 'Red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: Right child of a left child
                        node = node.parent
                        self._left_rotate(node)
                    # Case 3: Left child of a left child
                    node.parent.color = 'Black'
                    node.parent.parent.color = 'Red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == 'Red':
                    # Case 1: Red uncle
                    node.parent.color = 'Black'
                    uncle.color = 'Black'
                    node.parent.parent.color = 'Red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2: Left child of a right child
                        node = node.parent
                        self._right_rotate(node)
                    # Case 3: Right child of a right child
                    node.parent.color = 'Black'
                    node.parent.parent.color = 'Red'
                    self._left_rotate(node.parent.parent)

        self.root.color = 'Black'

    def delete(self, key):
        # Public method to delete a node with a given key from the Red-Black Tree
        node = self.search(key)
        if node is None:
            return
        self._delete_node(node)

    def _delete_node(self, node):
        # Private method to delete a node from the Red-Black Tree
        if node.left is None or node.right is None:
            # Case 1: Node has zero or one child
            child = node.right or node.left
            if node.parent is None:
                self.root = child
            elif node.parent.left == node:
                node.parent.left = child
            else:
                node.parent.right = child
            if child:
                child.parent = node.parent
            if node.color == 'Black':
                self._fix_deletion(child, node.parent)
        else:
            # Case 2: Node has two children
            successor = self._min_value_node(node.right)
            node.key = successor.key
            self._delete_node(successor)

    def _fix_deletion(self, node, parent):
        # Private method to fix any violations of Red-Black Tree properties after deletion
        while node != self.root and (node is None or node.color == 'Black'):
            if node == parent.left:
                sibling = parent.right
                if sibling.color == 'Red':
                    # Case 1: Red sibling
                    sibling.color = 'Black'
                    parent.color = 'Red'
                    self._left_rotate(parent)
                    sibling = parent.right
                if (sibling.left is None or sibling.left.color == 'Black') and \
                        (sibling.right is None or sibling.right.color == 'Black'):
                    # Case 2: Black sibling with black children
                    sibling.color = 'Red'
                    node = parent
                    parent = node.parent
                else:
                    if sibling.right is None or sibling.right.color == 'Black':
                        # Case 3: Black sibling with red left child
                        sibling.left.color = 'Black'
                        sibling.color = 'Red'
                        self._right_rotate(sibling)
                        sibling = parent.right
                    # Case 4: Black sibling with red right child
                    sibling.color = parent.color
                    parent.color = 'Black'
                    sibling.right.color = 'Black'
                    self._left_rotate(parent)
                    node = self.root
            else:
                sibling = parent.left
                if sibling.color == 'Red':
                    # Case 1: Red sibling
                    sibling.color = 'Black'
                    parent.color = 'Red'
                    self
                # Case 1: Red sibling
                sibling.color = 'Black'
                parent.color = 'Red'
                self._right_rotate(parent)
                sibling = parent.left
            if (sibling.right is None or sibling.right.color == 'Black') and \
                    (sibling.left is None or sibling.left.color == 'Black'):
                # Case 2: Black sibling with black children
                sibling.color = 'Red'
                node = parent
                parent = node.parent
            else:
                if sibling.left is None or sibling.left.color == 'Black':
                    # Case 3: Black sibling with red right child
                    sibling.right.color = 'Black'
                    sibling.color = 'Red'
                    self._left_rotate(sibling)
                    sibling = parent.left
                # Case 4: Black sibling with red left child
                sibling.color = parent.color
                parent.color = 'Black'
                sibling.left.color = 'Black'
                self._right_rotate(parent)
                node = self.root
        if node:
            node.color = 'Black'

    def _min_value_node(self, node):
        # Private method to find the node with the minimum key value in a subtree
        current = node
        while current.left:
            current = current.left
        return current

    def _left_rotate(self, x):
        # Private method to perform a left rotation at a given node
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        # Private method to perform a right rotation at a given node
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def inorder_traversal(self):
        # Public method to perform inorder traversal of the Red-Black Tree
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        # Private method to perform inorder traversal recursively
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)

if __name__ == '__main__':

    rb_tree = RedBlackTree()
    rb_tree.insert(10)
    rb_tree.insert(20)
    rb_tree.insert(30)
    rb_tree.insert(40)
    rb_tree.insert(50)
    rb_tree.insert(60)
    
    print("Inorder traversal before deletion:")
    rb_tree.inorder_traversal()
    
    rb_tree.delete(20)
    print("\nInorder traversal after deletion:")
    rb_tree.inorder_traversal()
