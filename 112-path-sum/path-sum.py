# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            targetSum-=root.val
            if targetSum==0:
                return True
            return False
        leftSum=self.hasPathSum(root.left,targetSum-root.val)
        rightSum=self.hasPathSum(root.right,targetSum-root.val)

        if leftSum or rightSum:
            return True
        return False

        