# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count = 0
    def dfs(self,root,curr_max):
            if not root:
                return
            if root.val >=curr_max:
                self.count+=1
                curr_max=root.val
            self.dfs(root.left,curr_max)
            self.dfs(root.right,curr_max)
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
       



        self.dfs(root,root.val)
        return self.count



        
        