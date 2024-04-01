class TreeNode:
    def __init__(self, key):
        # Constructor to initialize a tree node
        self.key = key           # Key value stored in the node
        self.left = None         # Reference to the left child node
        self.right = None        # Reference to the right child node
        self.height = 1          # Height of the node, initially set to 1

class AVLTree:
    def __init__(self):
        # Constructor to initialize the AVL tree
        self.root = None         # Reference to the root node of the AVL tree

    def search(self, key):
        # Public method to search for a key in the AVL tree
        return self._search(self.root, key)

    def _search(self, root, key):
        # Private method to recursively search for a key in the AVL tree
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._search(root.left, key)   # Search in the left subtree
        else:
            return self._search(root.right, key)  # Search in the right subtree

    def insert(self, key):
        # Public method to insert a key into the AVL tree
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        # Private method to recursively insert a key into the AVL tree
        if root is None:
            return TreeNode(key)   # Create a new node if the current node is None
        elif key < root.key:
            root.left = self._insert(root.left, key)   # Recursively insert into the left subtree
        else:
            root.right = self._insert(root.right, key) # Recursively insert into the right subtree

        # Update the height of the current node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Check balance factor and perform rotations if necessary
        balance = self._get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self._rotate_right(root)        # Left-Left case, perform right rotation
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)        # Left-Right case, perform left-right rotation

        if balance < -1:
            if key > root.right.key:
                return self._rotate_left(root)         # Right-Right case, perform left rotation
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)         # Right-Left case, perform right-left rotation

        return root

    def delete(self, key):
        # Public method to delete a key from the AVL tree
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        # Private method to recursively delete a key from the AVL tree
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)    # Recursively delete from the left subtree
        elif key > root.key:
            root.right = self._delete(root.right, key)  # Recursively delete from the right subtree
        else:
            if root.left is None:
                return root.right                      # Case: Node with only right child
            elif root.right is None:
                return root.left                       # Case: Node with only left child
            else:
                successor = self._get_min_value_node(root.right)
                root.key = successor.key
                root.right = self._delete(root.right, successor.key)

        if root is None:
            return root

        # Update the height of the current node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Check balance factor and perform rotations if necessary
        balance = self._get_balance(root)

        if balance > 1:
            if self._get_balance(root.left) >= 0:
                return self._rotate_right(root)        # Left-Left case, perform right rotation
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)        # Left-Right case, perform left-right rotation

        if balance < -1:
            if self._get_balance(root.right) <= 0:
                return self._rotate_left(root)         # Right-Right case, perform left rotation
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)         # Right-Left case, perform right-left rotation

        return root

    def _get_height(self, root):
        # Private method to calculate the height of a node
        if root is None:
            return 0
        return root.height

    def _get_balance(self, root):
        # Private method to calculate the balance factor of a node
        if root is None:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def _rotate_left(self, z):
        # Private method to perform left rotation at a node
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        # Private method to perform right rotation at a node
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_min_value_node(self, root):
        # Private method to find the node with the minimum key value in the AVL tree
        current = root
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        # Public method to perform inorder traversal of the AVL tree
        self._inorder_traversal(self.root)
        
    def _inorder_traversal(self, root):
        # Private method to perform inorder traversal recursively
        if root is not None:
            self._inorder_traversal(root.left)
            print(root.key, end=' ')
            self._inorder_traversal(root.right)

if __name__ == '__main__':
    # Create an AVL tree
    avl_tree = AVLTree()

    # Insert some keys
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.insert(25)

    # Perform inorder traversal to check if keys are inserted in sorted order
    print("Inorder Traversal after insertion:")
    avl_tree.inorder_traversal()  # Output: 10 20 25 30 40 50

    # Search for a key
    print("\n\nSearch for key 30:")
    result = avl_tree.search(30)
    if result:
        print("Key 30 found in the AVL tree.")
    else:
        print("Key 30 not found in the AVL tree.")

    # Delete a key
    avl_tree.delete(20)

    # Perform inorder traversal after deletion
    print("\nInorder Traversal after deletion:")
    avl_tree.inorder_traversal()  # Output: 10 25 30 40 50
