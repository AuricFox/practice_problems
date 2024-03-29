# Linked List

class Node:
    def __init__(self, data, parent=None, child=None):
        # Node contents
        self.data = data
        # Previous node
        self.parent = parent
        # Next node
        self.child = child

class Queue:
    def __init__(self):
        # Initializing list
        self.head = None

    # See if the Queue is empty
    def isEmpty(self):
        return self.head == None

    # Look at the data of the first element but don't remove
    def peek(self):
        if (self.isEmpty()):
            print("Queue is Empty!")
            return None
        
        return self.head.data

    # Add to the queue
    def enqueue(self, data):
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

    # Remove from the queue
    def dequeue(self, idx=0):
        # List is empty
        if(self.head == None):
            print("List is Empty!")
            return

        # List is populated
        head = self.head
        # Current head needs to be removed
        if (idx == 0 or idx == -1 and head.child == None):
            # Get data
            data = head.data
            # Move head to next element
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
                    return
                
                # Update values
                index += 1
                head = head.child

    # Print the entire active queue
    def printList(self):

        if self.head == None:
            print("List is Empty!")

        else:
            head = self.head
            myQueue = ''
            while head != None:
                myQueue += str(head.data)

                if (head.child != None):
                    myQueue += ' -> '

                head = head.child
            print(myQueue)


if __name__ == "__main__":
    myList = Queue()

    # Adding data to the queue
    for i in range(10):
        myList.enqueue(i)
    myList.printList()

    # Removing data from the queue
    myList.dequeue()
    myList.dequeue()
    myList.printList()