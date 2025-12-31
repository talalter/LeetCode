# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = float('inf')

        def dfs(node):
            # 1) base case
            if not node:
                return True, INF, -INF

            # 2) recursion
            left_ok, left_min, left_max = dfs(node.left)
            right_ok, right_min, right_max = dfs(node.right)

            # 3) validate current node
            if not (left_ok and right_ok and left_max < node.val < right_min):
                return False, 0, 0

            # 4) propagate min/max up
            subtree_min = min(left_min, node.val)
            subtree_max = max(right_max, node.val)
            return True, subtree_min, subtree_max

        ok, _, _ = dfs(root)
        return ok