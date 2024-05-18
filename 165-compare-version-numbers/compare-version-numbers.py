class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        l1, l2 = len(nums1), len(nums2)
        for i in range(max(l1, l2)):
            i1 = int(nums1[i]) if i < l1 else 0
            i2 = int(nums2[i]) if i < l2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        return 0
