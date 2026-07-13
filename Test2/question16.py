#  16.Find and display all the leaf nodes of a binary tree.
def leafNodes(root):
    if root:
        if root.left is None and root.right is None:
            print(root.data)
        leafNodes(root.left)
        leafNodes(root.right)

leafNodes(root)