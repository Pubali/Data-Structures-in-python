# Python program to demonstrate circular linked list traversal
# author @Pubali Bhaduri
# Structure for a Node
class Node:

    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:

    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        new_node = Node(data)
        temp = self.head

        new_node.next = self.head

        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node

        else:
            new_node.next = new_node # For the first node

        self.head = new_node
    def addend(self,data):
        new_node = Node(data)
        temp = self.head
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        else:
            self.push(data)

    def addafter(self,data,item):
        new_node = Node(data)
        temp = self.head
        if(self.head is None):
            self.push(data)

        while(temp and temp.data!=item):
            if (temp.next ==self.head):
                print "Item not present"
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node



    # Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print "%d" %(temp.data),
                temp = temp.next
                if (temp == self.head):
                    break
    def deletenode(self,key):
        curr = self.head
        prev = None
        # check whether the linked List is empty
        if(self.head is None):
            print "Linked list is empty"
            return
        # Check if node is only node
        if curr.next == self.head:
            self.head = None
        while(curr and curr.data!=key):
            if (curr.next == self.head):
                print "Node not found"
                return
            prev = curr
            curr = curr.next

        # If more than one node, check if it is first node
        if(curr == self.head):
            temp = self.head
            while(temp.next!=self.head):
                temp = temp.next
            self.head = curr.next
            temp.next = self.head
        # check if node is last node
        elif(curr.next == self.head):
            prev.next = self.head
        else:
            prev.next = curr.next
            curr.next = None
# Driver program to test above function

# Initialize list as empty
cllist = CircularLinkedList()

# Created linked list will be 11->2->56
cllist.push(56)
cllist.push(2)
cllist.push(11)
cllist.push(12)
cllist.addafter(4,56)
cllist.addend(5)

print "Contents of circular Linked List"
cllist.printList()
cllist.deletenode(5)
print "\nContents of circular Linked List after deletion"
cllist.printList()


