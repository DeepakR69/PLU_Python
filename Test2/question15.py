
# 15.Count the total number of nodes present in a binary tree.
def countNodes(root):
    if root is None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

print(countNodes(root))