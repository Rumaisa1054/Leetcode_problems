# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root):
    if root.left == None and root.right == None:
        return 1
    if root.right == None and root.left != None:
        left = inorder(root.left)
        return left+1
    elif root.left == None and root.right != None:
        right = inorder(root.right)
        return right+1
    else:
        left = inorder(root.left)
        right = inorder(root.right)
        return min(left,right)+1
    
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return inorder(root)
    # in this Question it is a must that we explore the branches only... Supose a tree has only one branch then we return length of that branch + 1 ---- if we start to take 