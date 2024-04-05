class Solution {
public:
    string makeGood(string s) {
        stack<char> st;
        for (int i = 0; i < s.length(); ++i) {
            if (st.empty() || abs(st.top() - s[i]) != 32) {
                st.push(s[i]);
            } else {
                st.pop();
            }
        }
        string res;
        while (!st.empty()) {
            char c = st.top();
            st.pop();
            res.push_back(c);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};