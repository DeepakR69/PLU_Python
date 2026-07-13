# 13.Create the following binary tree:
# ```
# 50
# / \
# 30 70
# ```

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(50)
root.left = Node(30)
root.right = Node(70)

print("Root:", root.data)
print("Left Child:", root.left.data)
print("Right Child:", root.right.data)
