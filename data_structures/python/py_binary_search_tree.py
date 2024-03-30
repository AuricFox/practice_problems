class Node:
    def __init__(self, value, right=None, left=None):
        # Vaule/key of the node 
        self.value = value
        # Right branch
        self.right = right
        # Left branch
        self.left = left

    def __str__(self):
        # Returns the value of the node as a string
        return str(self.value)

class Tree:
    def __init__(self, root:Node=None):
        self.root = root

    def search(self, value:int):
        # Searches for our value inside the tree and returns it if found

        # Check if the tree is empty
        if not self.root: return None
        
        # Start iterating through the tree starting with the root node
        current_node = self.root
        while current_node:
            # Our value is less than the current node's value
            if value < current_node.value:
                if current_node.left:
                    # Traverse the left branch
                    current_node = current_node.left
                else:
                    # No further nodes to traverse
                    return None
            # Our value is greater than the current node's value
            elif value > current_node.value:
                if current_node.right:
                    # Traverse the right branch
                    current_node = current_node.right
                else:
                    # No further nodes to traverse
                    return None
            # Our value equals the current nodes value
            else:
                # This is the node we are looking for
                return current_node
            

    def insert(self, value:int):
        # Inserts our node into the binary search tree
        node = Node(value)

        # Check if the tree is empty
        if not self.root:
            # Set the new node as the root node since it is None
            self.root = node
            return
        
        # Start iterating through the tree starting with the root node
        current_node = self.root
        while current_node:
            # Our node's value is less than the current node's value
            if node.value < current_node.value:
                if current_node.left:
                    # Traverse the left branch
                    current_node = current_node.left
                else:
                    # Set the left branch of the current node to our node
                    current_node.left = node
                    current_node = node
                    break
            # Our node's value is greater than the current node's value
            elif node.value > current_node.value:
                if current_node.right:
                    # Traverse the right branch
                    current_node = current_node.right
                else:
                    # Set the right branch of the current node to our node
                    current_node.right = node
                    current_node = node
                    break
            # The inserted node already exists
            else: break

    def delete(self, value:int):

        parent = None
        current = self.root

        while current and current.value != value:
            parent = current
            if value < current.vlaue:
                current = current.left
            else:
                current = current.right

        # The value was not found and could not be deleted
        if not current: return False

        # Node to be deleted has one or no children
        if not current.left or not current.right:
            if not current.left:
                child = current.right
            else:
                child = current.left

            if not parent:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child

        else:
            successor = current.right
            successor_parent = current

            while successor.left:
                successor_parent = successor
                successor = successor.left

            # Replace the data of the node being deleted
            current.value = successor.value

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right


    def tree_str(self, node:Node):
        # Helper function for printing the tree
        tree = []

        # Return empty list if the node is empty
        if not node: return tree

        tree += self.tree_str(node.left)
        tree += [node.value]
        tree += self.tree_str(node.right)

        return tree

    def __str__(self):
        return str(self.tree_str(self.root))


if __name__ == "__main__":
    myTree = Tree()

    myTree.insert(2)
    myTree.insert(1)
    myTree.insert(3)
    myTree.insert(4)
    myTree.insert(5)
    print(myTree)

    print(myTree.search(4))

    myTree.delete(2)
    print(myTree)