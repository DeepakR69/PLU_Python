# 4.Count and display the total number of nodes in the linked list
count = 0
temp = head

while temp:
    count += 1
    temp = temp.next

print("Total Nodes:", count)