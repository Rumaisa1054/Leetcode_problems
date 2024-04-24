# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if(root == None):
            return []
        # Declaring the queue
        Queue = []
        # Answer array of array
        Elements = []
        # Starting with root
        Queue.append(root)

        # While the Queue doesnot get empty -> we would continue the process
        while(len(Queue) != 0):
            # Array for Levels
            liste = []
            # total Nodes right now
            Total_nodes_now_in_queue = len(Queue)
            # for all nodes right now in Queue
            i = 0
            x = 0
            while(x < Total_nodes_now_in_queue):
                x += 1
                # Pop the one right now
                Node = Queue.pop(i)
                # Push its left and right 
                if(Node.left):
                    Queue.append(Node.left)
                
                if(Node.right):
                    Queue.append(Node.right)
                liste.append(Node.val)
            Elements.append(sum(liste)/len(liste))
        return Elements