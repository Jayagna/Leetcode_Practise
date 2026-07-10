# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        high = max(p.val,q.val)
        low = min(p.val,q.val)

        if low < root.val and root.val < high:
            return root
        if low == root.val or high == root.val:
            return root
        
        if high < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if low > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        