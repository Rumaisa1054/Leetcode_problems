"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        Elements = []
        Queue = []
        Queue.append(root)
        while Queue:
            X = len(Queue)
            layer = []
            for i in range(X):
                M = Queue.pop(0)
                if M.left:
                    Queue.append(M.left)
                if M.right:
                    Queue.append(M.right)
                layer.append(M)
            Elements.append(layer)
        
        for i in range(len(Elements)):
            for j in range(len(Elements[i])-1):
                print(Elements[i][j].val)
                Elements[i][j].next = Elements[i][j+1]
            print()
        return root