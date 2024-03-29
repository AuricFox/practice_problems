class Node:
    def __init__(self, data, next=None):
        # Node contents
        self.data = data
        # next node
        self.next = next

class Stack:
    def __init__(self):
        # Initializing list
        self.head = None

    # Adding new node to the stack
    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        # List is empty
        if(self.head == None):
            print("List is Empty!")
            return

        # Getting data from the first node
        data = self.head.data
        # Moving pointer to next node
        self.head = self.head.next
        return data

    # Prints the entire Stack
    def printList(self):

        if self.head == None:
            print("List is Empty!")

        else:
            llist = ''
            head = self.head
            while head != None:
                llist += str(head.data)

                if (head.next != None):
                    llist += ' -> '
                head = head.next
            print(llist)


if __name__ == "__main__":
    myList = Stack()
    
    # Adding data 0-9 to stack
    for i in range(10):
        myList.push(i)
    myList.printList()

    # Removing data from the stack
    myList.pop()
    myList.pop()
    myList.printList()