# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, maxval):
            if not node:
                return 0
            if node.val >= maxval:
                gn = 1
                maxval = node.val
            else:
                gn = 0
                    
            left_good = dfs(node.left,maxval)
            right_good = dfs(node.right,maxval)

            return gn + left_good + right_good
        return dfs(root,root.val)
        