class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sort the array
        sorted_nums = sorted(nums)
        print(sorted_nums)
        # 1 pointer on the left and 1 pointer on the right
        left = 0
        right = len(nums) // 2 if len(nums) % 2 == 0 else len(nums) // 2 + 1
        # add back the elements
        for i in range(len(nums) // 2):
            nums[2 * i] = sorted_nums[left]
            nums[2 * i + 1] = sorted_nums[right]
            left += 1
            right += 1
        if len(nums) % 2 != 0:
            nums[len(nums) - 1] = sorted_nums[left]