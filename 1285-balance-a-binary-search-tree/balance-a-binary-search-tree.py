# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inOrderTraverse(curr):
            if curr.left:
                inOrderTraverse(curr.left)
            if curr.val:
                arr.append(curr.val)
            if curr.right:
                inOrderTraverse(curr.right)
        inOrderTraverse(root)
        def arrToBalancedBST(arr, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(arr[mid])
            root.left = arrToBalancedBST(arr, start, mid - 1)
            root.right = arrToBalancedBST(arr, mid + 1, end)
            return root
        return arrToBalancedBST(arr, 0, len(arr) - 1)