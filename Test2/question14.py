#  14.Perform an Inorder Traversal on a binary tree.
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

inorder(root)