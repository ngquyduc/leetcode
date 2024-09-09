class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, pr = [], 1
        post, po = [], 1
        res = []
        l = len(nums)
        for i in range(len(nums)):
            pre.append(pr)
            post.append(po)
            pr *= nums[i]
            po *= nums[l - 1 - i]
        for i in range(len(nums)):
            res.append(pre[i] * post[l - 1 - i])
        return res