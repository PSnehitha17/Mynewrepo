class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class CircularLinkedList:
    
    def __init__(self):
        self.head = None  

    def append(self, data):
    
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        
        new_node = Node(data)
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node  
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node  

        self.head = new_node  

    def delete(self, key):
        
        if not self.head:
            return

        temp = self.head
        prev = None

        
        if temp.data == key:
            if temp.next == self.head:
                self.head = None
                return
            else:
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
                return

        
        while temp.next != self.head:
            prev = temp
            temp = temp.next
            if temp.data == key:
                prev.next = temp.next
                return

    def display(self):
        
        if not self.head:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")

cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.prepend(5)
print("Circular Linked List:")
cll.display()

cll.delete(20)
print("After deleting 20:")
cll.display()
