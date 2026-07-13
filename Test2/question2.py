
# 2.Insert a new node containing 25 after the node containing 20.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

temp = head
while temp:
    if temp.data == 20:
        new = Node(25)
        new.next = temp.next
        temp.next = new
        break
    temp = temp.next

temp = head
while temp:
    print(temp.data, end=" -> " if temp.next else "")
    temp = temp.next