class BTreeNode:
    def __init__(self, leaf=True):
        # Constructor to initialize a B-tree node
        self.leaf = leaf        # Indicates whether the node is a leaf node
        self.keys = []          # List to store keys
        self.children = []      # List to store child nodes

class BTree:
    def __init__(self, t):
        # Constructor to initialize the B-tree with minimum degree t
        self.root = BTreeNode() # Create a new root node
        self.t = t              # Minimum degree of the B-tree

    def search(self, key):
        # Public method to search for a key in the B-tree
        return self._search(self.root, key)

    def _search(self, node, key):
        # Private recursive method to search for a key starting from a given node
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True     # Key found
        if node.leaf:
            return False    # Key not found in a leaf node
        return self._search(node.children[i], key)    # Recursively search in the appropriate child

    def insert(self, key):
        # Public method to insert a key into the B-tree
        if len(self.root.keys) == (2 * self.t) - 1:
            # If the root is full, split it and create a new root
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        # Private method to insert a key into a non-full node
        i = len(node.keys) - 1
        if node.leaf:
            # If the node is a leaf, insert the key into the appropriate position
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # If the node is not a leaf, find the child to insert the key and recursively insert
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                # If the child is full, split it before inserting the key
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, index):
        # Private method to split a full child of a parent node
        t = self.t
        child = parent.children[index]
        new_child = BTreeNode(leaf=child.leaf)
        parent.keys.insert(index, child.keys[t - 1])
        parent.children.insert(index + 1, new_child)
        new_child.keys = child.keys[t:(2 * t) - 1]
        child.keys = child.keys[0:t - 1]
        if not child.leaf:
            new_child.children = child.children[t:(2 * t)]
            child.children = child.children[0:t - 1]

    def delete(self, key):
        # Public method to delete a key from the B-tree
        self._delete(self.root, key)

    def _delete(self, node, key):
        # Private method to delete a key from the B-tree starting from a given node
        if not node:
            return None

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            # Case 1: Key is found in the current node
            if node.leaf:
                # Case 1a: Key is in a leaf node
                del node.keys[i]
            else:
                # Case 1b: Key is in an internal node
                predecessor = self._predecessor(node, i)
                node.keys[i] = predecessor
                self._delete(node.children[i], predecessor)
        else:
            # Case 2: Key is not found in the current node
            if node.leaf:
                # Key does not exist in the tree
                return None

            if len(node.children[i].keys) < self.t:
                # Case 2a: Child has fewer than t keys, adjust it before deletion
                if i > 0 and len(node.children[i - 1].keys) >= self.t:
                    # Case 2a1: Borrow from the left sibling if possible
                    self._borrow_from_left_sibling(node, i)
                elif i < len(node.children) - 1 and len(node.children[i + 1].keys) >= self.t:
                    # Case 2a2: Borrow from the right sibling if possible
                    self._borrow_from_right_sibling(node, i)
                else:
                    # Case 2a3: Merge child with its sibling
                    if i < len(node.children) - 1:
                        self._merge_children(node, i)
                    else:
                        self._merge_children(node, i - 1)
            self._delete(node.children[i], key)

    def _predecessor(self, node, index):
        # Private method to find the predecessor key of
        # Go to the leftmost child of the right child of the node
        node = node.children[index + 1]
        while not node.leaf:
            node = node.children[0]
        # Return the rightmost key of the leaf node
        return node.keys[-1]

    def _borrow_from_left_sibling(self, parent, index):
        # Private method to borrow a key from the left sibling of the child node
        child = parent.children[index]
        left_sibling = parent.children[index - 1]

        # Move the rightmost key from the left sibling to the parent node
        child.keys.insert(0, parent.keys[index - 1])
        parent.keys[index - 1] = left_sibling.keys.pop()

        if not left_sibling.leaf:
            # Move the rightmost child from the left sibling to the child node
            child.children.insert(0, left_sibling.children.pop())

    def _borrow_from_right_sibling(self, parent, index):
        # Private method to borrow a key from the right sibling of the child node
        child = parent.children[index]
        right_sibling = parent.children[index + 1]

        # Move the leftmost key from the right sibling to the parent node
        child.keys.append(parent.keys[index])
        parent.keys[index] = right_sibling.keys.pop(0)

        if not right_sibling.leaf:
            # Move the leftmost child from the right sibling to the child node
            child.children.append(right_sibling.children.pop(0))

    def _merge_children(self, parent, index):
        # Private method to merge a child with its sibling
        child = parent.children[index]
        sibling = parent.children[index + 1]

        # Move the key from the parent to the child
        child.keys.append(parent.keys.pop(index))

        # Move keys and children from the sibling to the child
        child.keys.extend(sibling.keys)
        child.children.extend(sibling.children)

        # Remove the sibling from the parent's children list
        parent.children.pop(index + 1)

    def inorder_traversal(self):
        # Public method to perform inorder traversal of the B-tree
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        # Private method to perform inorder traversal recursively
        if node is not None:
            i = 0
            while i < len(node.keys):
                if i < len(node.children):
                    self._inorder_traversal(node.children[i])
                print(node.keys[i], end=' ')
                i += 1
            if i < len(node.children):
                self._inorder_traversal(node.children[i])


if __name__ == '__main__':

    b_tree = BTree(3)  # Create a B-tree with minimum degree 3

    # Insert keys into the B-tree
    b_tree.insert(10)
    b_tree.insert(20)
    b_tree.insert(5)
    b_tree.insert(6)
    b_tree.insert(12)
    b_tree.insert(30)
    b_tree.insert(7)
    b_tree.insert(17)
    b_tree.insert(3)

    # Perform inorder traversal to print the keys in sorted order
    print("Inorder traversal of the B-tree:")
    b_tree.inorder_traversal()

    # Delete a key from the B-tree
    key_to_delete = 10
    b_tree.delete(key_to_delete)
    print(f"\nAfter deleting key {key_to_delete}:")
    b_tree.inorder_traversal()