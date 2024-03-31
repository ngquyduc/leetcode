class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int left = -1, right = -1;
        vector<int> res;
        if (nums.size() == 1) {
            res.push_back(pow(nums[0], 2));
            return res;
        }
        for (size_t i = 1; i < nums.size(); ++i) {
            if (abs(nums[i]) > abs(nums[i - 1])) {
                res.push_back(pow(nums[i - 1], 2));
                left = i - 2;
                right = i;
                break;
            }
        }
        if (left == -1 && right == -1) {
            for (int i = nums.size() - 1; i >= 0; --i) {
                res.push_back(pow(nums[i], 2));
            }
            return res;
        }
        while (left >= 0 && right < nums.size()) {
            if (abs(nums[left]) <= abs(nums[right])) {
                res.push_back(pow(nums[left], 2));
                --left;
            } else {
                res.push_back(pow(nums[right], 2));
                ++right;
            }
        }
        while (left >= 0) {
            res.push_back(pow(nums[left], 2));
            --left;
        }
        while (right < nums.size()) {
            res.push_back(pow(nums[right], 2));
            ++right;
        }
        return res;
    }
};