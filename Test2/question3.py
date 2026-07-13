
# 3.Delete the node containing 30 from the linked list and display the updated
# lis
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(25)
head.next.next.next = Node(30)
head.next.next.next.next = Node(40)
head.next.next.next.next.next = Node(50)

temp = head
while temp.next:
    if temp.next.data == 30:
        temp.next = temp.next.next
        break
    temp = temp.next

temp = head
while temp:
    print(temp.data, end=" -> " if temp.next else "")
    temp = temp.next