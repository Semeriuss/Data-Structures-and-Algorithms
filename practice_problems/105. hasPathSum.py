# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        if root.val == targetSum and not root.left and not root.right: return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

root = TreeNode(1, TreeNode(2), TreeNode(3))
targetSum = 4
print(Solution().hasPathSum(root, targetSum)) 
            
            