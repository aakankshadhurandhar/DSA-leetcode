# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recurse(self,root,targetsum,ans,temp):
        if not root:
            return 
        temp.append(root.val)
        if not root.left and not root.right and targetsum==root.val:
            ans.append(list(temp))
        print(temp)
        self.recurse(root.left,targetsum-root.val,ans,temp)
        self.recurse(root.right,targetsum-root.val,ans,temp)
        temp.pop()

        

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans=[]
        temp=[]
        self.recurse(root,targetSum,ans,temp)
        return ans

        
        