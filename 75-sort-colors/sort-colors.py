class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, v0, v1 = 0, 0, 0, 1
        while r < len(nums):
            if nums[r] == v0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        r = l
        while r < len(nums):
            if nums[r] == v1:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1