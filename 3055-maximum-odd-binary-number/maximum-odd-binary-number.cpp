class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        auto count = -1;
        auto l = s.length();
        std::string res = "1";
        for (auto i = 0; i < l; ++i) {
            if (s[i] == '1') {
                ++count;
            }
        }    
        for (auto i = 0; i < l - 1; ++i) {
            if (i < l - 1 - count) {
                res = "0" + res;
            } else {
                res = "1" + res;
            }
        }
        return res;
    }
};