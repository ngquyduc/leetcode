class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char, char> hash_map;
        set<char> visited;
        for (int i = 0; i < s.length(); ++i) {
            if (!hash_map.contains(s[i])) {
                if (visited.contains(t[i])) {
                    return false;
                }
                hash_map[s[i]] = t[i];
                visited.insert(t[i]);
                continue;
            } else {
                if (!(hash_map[s[i]] == t[i])) {
                    return false;
                }
            }
        }
        return true;
    }
};