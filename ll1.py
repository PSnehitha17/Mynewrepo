class LinkedListNode:
    def __init__(self,n):
        self.data=n
        self.next=None
def printLinkedList(head):
    current=head
    while(current!=None):
        print(current.data,end=" ")
        current=current.next

obj1=LinkedListNode(70)
obj2=LinkedListNode(60)
obj3=LinkedListNode(50)
obj4=LinkedListNode(40)
obj5=LinkedListNode(30)
obj6=LinkedListNode(20)
obj7=LinkedListNode(10)
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
printLinkedList(obj1)
def search_value(head_node, value):
  cur_node = head_node
  while cur_node != None:
    if cur_node.value == value:
      print("Found a matching node for value:", value)
      return cur_node
    cur_node = cur_node.next
  print("Couldn't find a matching node for value:", value)
  return None
head_node = printLinkedList()
node = search_value(head_node, 2)
node = search_value(head_node, 19)



