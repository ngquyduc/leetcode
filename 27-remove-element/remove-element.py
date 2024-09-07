class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r, k = 0, 0, 0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                k += 1
                l += 1
            r += 1
        return k