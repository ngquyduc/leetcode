class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.helper(nums, 0, 0)

    def helper(self, nums: List[int], level: int, currentXOR: int) -> int:
        if level == len(nums):
            return currentXOR
        include = self.helper(nums, level + 1, currentXOR ^ nums[level])
        exclude = self.helper(nums, level + 1, currentXOR)
        return include + exclude