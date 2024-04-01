class Solution {
public:
    int lengthOfLastWord(string s) {
        int res = 0;
        bool flag = true;
        for (int i = s.length() - 1; i >= 0; --i) {
            if (flag && s[i] == ' ') {
                continue;
            }
            if (s[i] != ' ') {
                flag = false;
                ++res;
            } else {
                break;
            }
        }
        return res;
    }
};