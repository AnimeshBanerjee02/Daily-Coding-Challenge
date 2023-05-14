class Solution {
public:
    void backtrack(vector<string>& ans, string& s, int i) {
        if (i == s.size()) {
            ans.push_back(s);
            return;
        }
        if (isalpha(s[i])) {
            s[i] = tolower(s[i]);
            backtrack(ans, s, i+1);
            s[i] = toupper(s[i]);
        }
        backtrack(ans, s, i+1);
    }
    vector<string> letterCasePermutation(string s) {
        vector<string> ans;
        backtrack(ans, s, 0);
        return ans;
    }
};
