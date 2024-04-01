class Node:
    def __init__(self, key, color='Red'):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def insert(self, key):
        new_node = Node(key)
        self._insert_helper(new_node)

    def _insert_helper(self, new_node):
        if self.root is None:
            self.root = new_node
            self.root.color = 'Black'
            return

        parent = None
        current = self.root

        while current is not None:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self._fix_insertion(new_node)

    def _fix_insertion(self, node):
        while node != self.root and node.parent.color == 'Red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == 'Red':
                    node.parent.color = 'Black'
                    uncle.color = 'Black'
                    node.parent.parent.color = 'Red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'Black'
                    node.parent.parent.color = 'Red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == 'Red':
                    node.parent.color = 'Black'
                    uncle.color = 'Black'
                    node.parent.parent.color = 'Red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'Black'
                    node.parent.parent.color = 'Red'
                    self._left_rotate(node.parent.parent)

        self.root.color = 'Black'

    def delete(self, key):
        node = self.search(key)
        if node is None:
            return
        self._delete_node(node)

    def _delete_node(self, node):
        if node.left is None or node.right is None:
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
            successor = self._min_value_node(node.right)
            node.key = successor.key
            self._delete_node(successor)

    def _fix_deletion(self, node, parent):
        while node != self.root and (node is None or node.color == 'Black'):
            if node == parent.left:
                sibling = parent.right
                if sibling.color == 'Red':
                    sibling.color = 'Black'
                    parent.color = 'Red'
                    self._left_rotate(parent)
                    sibling = parent.right
                if (sibling.left is None or sibling.left.color == 'Black') and \
                        (sibling.right is None or sibling.right.color == 'Black'):
                    sibling.color = 'Red'
                    node = parent
                    parent = node.parent
                else:
                    if sibling.right is None or sibling.right.color == 'Black':
                        sibling.left.color = 'Black'
                        sibling.color = 'Red'
                        self._right_rotate(sibling)
                        sibling = parent.right
                    sibling.color = parent.color
                    parent.color = 'Black'
                    sibling.right.color = 'Black'
                    self._left_rotate(parent)
                    node = self.root
            else:
                sibling = parent.left
                if sibling.color == 'Red':
                    sibling.color = 'Black'
                    parent.color = 'Red'
                    self._right_rotate(parent)
                    sibling = parent.left
                if (sibling.left is None or sibling.left.color == 'Black') and \
                        (sibling.right is None or sibling.right.color == 'Black'):
                    sibling.color = 'Red'
                    node = parent
                    parent = node.parent
                else:
                    if sibling.left is None or sibling.left.color == 'Black':
                        sibling.right.color = 'Black'
                        sibling.color = 'Red'
                        self._left_rotate(sibling)
                        sibling = parent.left
                    sibling.color = parent.color
                    parent.color = 'Black'
                    sibling.left.color = 'Black'
                    self._right_rotate(parent)
                    node = self.root
        if node:
            node.color = 'Black'

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _left_rotate(self, x):
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
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
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
