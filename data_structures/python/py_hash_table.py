class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None

class HashTable:
    def __init__(self, size=10):
        # Size of the hash table
        self.size = size
        # Populating hash table with None type
        self.table = [None for i in range(size)]

    # Perform a division hash
    def hash(self, key):
        # Key needs to be converted from a string to an integer
        if (type(key) is str):
            return int(key) % self.size
        # Just need to hash the integer
        elif (type(key) is int):
            return key % self.size
        # Invalid key type for hashing
        else:
            return None
    
    def add(self, key, data):
        # Get the index from the hashed key
        id = self.hash(key)
        # Key is invalid
        if (id == None):
            print("Invalid Key Type!")
            return
        
        node = Node(key, data)
        # Nothing has been added at this index location
        if(self.table[id] == None):
            self.table[id] = node

        # The index location is populated [collision]
        else:
            head = self.table[id]
            # Iterate thru the linked list
            while head.next != None:
                # Move head to the next node
                head = head.next
            # Add new data here
            head.next = node
    
    # Get first instance of key
    def get(self, key):
        id = self.hash(key)
        if (id == None):
            print("Invalid Key Type!")
            return
        
        # No data to retrieve since location is empty
        if (self.table[id] == None):
            print("No Data Found, List is Empty!")
            return
        else:
            head = self.table[id]
            # Loop until the end is reached
            while head != None:
                # First key has been found, return data
                if (head.key == key):
                    return head.data
                
                # Move head to the next node
                head = head.next
            print("No Data Found!")

    # Get everything with the corresponding key
    def getAll(self, key):
        id = self.hash(key)
        if (id == None):
            print("Invalid Key Type!")
            return
        
        # No data to retrieve since location is empty
        if (self.table[id] == None):
            print("No Data Found, List is Empty!")
            return
        else:
            head = self.table[id]
            data = []
            # Loop until the end is reached
            while head != None:
                # First key has been found, return data
                if (head.key == key):
                    data.append(head.data)
                
                # Move head to the next node
                head = head.next
            return data

if __name__ == "__main__":
    myTable = HashTable()
    myTable.add(1, 2)
    myTable.add(2, 3)
    myTable.add(2, 4)
    myTable.add(2, 5)
    myTable.add(11, 5)
    print("Data: ", myTable.get(11))
    print("All Data: ", myTable.getAll(2))