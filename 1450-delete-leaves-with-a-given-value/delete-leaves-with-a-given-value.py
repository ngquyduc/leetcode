# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        stack = []
        curr = root
        last_right = None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            if curr.right and curr.right is not last_right:
                curr = curr.right
                continue
            stack.pop()
            if not curr.right and not curr.left and curr.val == target:
                if not stack:
                    return None
                parent = stack[-1] if stack else None
                if parent and parent.left is curr:
                    parent.left = None
                elif parent and parent.right is curr:
                    parent.right = None
            last_right = curr
            curr = None
        return root
            
