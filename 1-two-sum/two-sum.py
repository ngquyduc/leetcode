class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for i in range(len(nums)):
            if nums[i] in hash_table.keys():
                return [hash_table[nums[i]], i]
            hash_table[target - nums[i]] = i

