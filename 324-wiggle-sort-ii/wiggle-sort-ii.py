class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sort the array
        sorted_nums = sorted(nums)
        # 1 pointer on the left and 1 pointer on the right
        left = len(nums) // 2 - 1 if len(nums) % 2 == 0 else len(nums) // 2
        right = len(nums) - 1
        # add back the elements
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = sorted_nums[left]
                left -= 1
            else:
                nums[i] = sorted_nums[right]
                right -= 1