class Node:
    def __init__(self, data, parent=None, child=None):
        # Node contents
        self.data = data
        # Previous node
        self.parent = parent
        # Next node
        self.child = child

class LinkedList:
    def __init__(self):
        # Initializing list
        self.head = None

    def add(self, data):

        # List is empty
        if(self.head == None):
            # Set element as head
            self.head = Node(data, None, None)
            return

        # List is populated
        head = self.head
        # Loop thru list until the end of the list is reached
        while head != None:
            if (head.child == None):
                # Add the new data here
                head.child = Node(data, head, None)
                return

            # Move to next element
            head = head.child

    def insert(self, data, idx):
        # Set as head since the list is empty
        if (self.head == None):
            self.head = Node(data, None, None)
            return
        
        head = self.head
        # Add to the front of the list
        if (idx == 0):
            self.head = Node(data, None, head)
        else:
            # Looking at child index
            index = 1
            while head.child != None:
                if (idx == index):
                    # Insert new data between head and it's child
                    head.child = Node(data, head, head.child)
                    return
                
                # Update values
                index += 1
                head = head.child

    def remove(self, data):
        # List is empty
        if(self.head == None):
            print("List is Empty!")
            return

        # List is populated
        head = self.head
        # Current head needs to be removed
        if (head.data == data):
            # Move head to next element
            self.head = head.child
            return

        # Loop thru list until the end of the list is reached
        while head != None:
            # Remove child and replace with grandchild
            if (head.child.data == data and head.child.child != None):
                head.child = head.child.child
                return
            # There is no grandchild
            elif (head.child.data == data and head.child.child == None):
                head.child = None

            # Move to next element
            head = head.child

    def pop(self, idx=-1):
        # List is empty
        if(self.head == None):
            print("List is Empty!")
            return

        # List is populated
        head = self.head
        # Current head needs to be removed
        if (idx == 0 or idx == -1 and head.child == None):
            # Move head to next element
            data = head.data
            self.head = head.child
            return data
        else:
            # Looking at child index
            index = 1
            while head.child != None:
                # Remove node between head and it's grandchild
                if (idx == index):
                    data = head.child.data
                    head.child = head.child.child
                    return data
                # Remove node at the end of the list
                elif (idx == -1 and head.child.child == None):
                    data = head.child.data
                    head.child = None
                    return data
                
                # Update values
                index += 1
                head = head.child

    # Print the entire list
    def printList(self):

        if self.head == None:
            print("List is Empty!")

        else:
            llist = ''
            head = self.head
            while head != None:
                llist += str(head.data)

                if (head.child != None):
                    llist += ' -> '
                head = head.child
            print(llist)


if __name__ == "__main__":
    myList = LinkedList()

    for i in range(10): 
        myList.add(i)
    myList.printList()

    myList.insert(20, 2)
    myList.insert(11, 0)
    myList.printList()

    myList.remove(20)
    myList.remove(11)
    myList.printList()
    