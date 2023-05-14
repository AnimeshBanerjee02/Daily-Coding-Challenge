class Solution {
public:
    void backtrack(vector<vector<int>>& ans, vector<int>& nums, int start) {
        if (start == nums.size()) {
            ans.push_back(nums);
            return;
        }
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);
            backtrack(ans, nums, start+1);
            swap(nums[start], nums[i]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        backtrack(ans, nums, 0);
        return ans;
    }
};
