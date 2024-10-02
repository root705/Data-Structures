class Node: # this is the NODE data structure in Python
    def __init__(self, data) -> None:
        self.data = data
        self.next:object = None

"""
This is the explanation for how to use node before implementing linked list

>>> a = Node(3)
>>> b = Node(7)
>>> c = Node(10)

# the above nodes (a,b,c) does not know the address of there next node

>>> a.next = b
>>> b.next = c

# print(a.next.data) #a.next = b and a.next.data = b.data
# print(b.data) 
# print(b.next.data) 
"""

# Implementation of LINKED LIST
class LinkedList:
    def __init__(self, node:object=None) -> None:
        self.head = node
    
    def add(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def display(self):
        current_node = self.head
        while current_node!=None:
            print(current_node.data)
            current_node = current_node.next

    def size(self):
        length = 0
        if self.head:
            current_node = self.head
            while current_node!=None:
                length += 1
                current_node = current_node.next
            return length
        return 0
    
    def remove(self):
        if self.head == None:
            return
        self.head = self.head.next

    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            else:
                current_node = current_node.next
        return False

l = LinkedList() # create a instances/object for the class 'LinkedList'

while True:
    print("1. ADD")
    print("2. SIZE")
    print("3. REMOVE")
    print("4. SEARCH")
    print("5. DISPLAY")
    print("6. EXIT")
    option = int(input("Enter your choice: "))

    if option == 1:
        element = int(input("Enter a Value: "))
        l.add(element)

    if option == 2:
        print(l.size())

    if option == 3:
        l.remove()
        print("Last node has been removed!")

    if option == 4:
        element = int(input("Enter the value to search: "))
        if l.search(element):
            print(f"{element} is found!")
        else:
            print(f"{element} is not found!")

    if option == 5:
        l.display()

    if option == 6:
        break