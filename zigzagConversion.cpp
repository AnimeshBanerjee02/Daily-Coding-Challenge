class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s; // If numRows is 1, return the input string as it is
        }
        string result;
        int cycleLen = 2 * numRows - 2;
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; i + j < s.size(); j += cycleLen) {
                result += s[i + j];
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < s.size()) {
                    result += s[j + cycleLen - i];
                }
            }
        }
        return result;
    }
};
