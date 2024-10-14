# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
ABEDFCHG
CBADEFGH
"""


def helper(preorder, inorder):
    l = len(preorder)
    if l < 1:
        return 0
    root = preorder[0]
    i = inorder.find(root)
    helper(preorder[1 : i + 1], inorder[0:i])
    helper(preorder[i + 1 : l], inorder[i + 1 : l])
    print(root, end="")


inorder = input().strip()
preorder = input().strip()

helper(preorder, inorder)
