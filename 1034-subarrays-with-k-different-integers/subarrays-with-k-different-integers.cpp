class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return subarraysWithAtmostKDistinct(nums, k) - subarraysWithAtmostKDistinct(nums, k - 1);
    }
    int subarraysWithAtmostKDistinct(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        int l = 0, r = 0, res = 0;
        while (r < nums.size()) {
            count[nums[r]]++;
            while (count.size() > k) {
                count[nums[l]]--;
                if (count[nums[l]] == 0) {
                    count.erase(nums[l]);
                }
                l++;
            }
            res += r - l + 1;
            r++;
        }    
        return res;
    }
};