# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def call_make(liste):
    if len(liste) == 0:
        return None
    maxi = -1
    index = -1
    for i in range(len(liste)):
        if liste[i] > maxi:
            maxi = max(liste[i],maxi)
            index = i
    root = TreeNode(maxi)
    
    root.left = call_make(liste[:index])
    root.right = call_make(liste[index+1:])
    return root

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return call_make(nums)