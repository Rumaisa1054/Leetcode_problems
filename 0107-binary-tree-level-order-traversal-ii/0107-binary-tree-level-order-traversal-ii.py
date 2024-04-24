# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root == None):
            return []
        
        Queue = []
        Queue.append(root)

        Elements = []

        while(len(Queue) != 0):
            X = len(Queue)
            liste = []
            for i in range(X):
                M = Queue.pop(0)
                if(M.left):
                    Queue.append(M.left)
                if(M.right):
                    Queue.append(M.right)
                
                liste.append(M.val)
            Elements.append(liste)
        
        Elements.reverse()
        return Elements