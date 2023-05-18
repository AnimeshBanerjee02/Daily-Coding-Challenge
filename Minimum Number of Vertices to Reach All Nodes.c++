class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<bool> isReachable(n, false);
        
        
        for (const auto& edge : edges) {
            int to = edge[1];
            isReachable[to] = true;
        }
        
        vector<int> result;
        
        
        for (int i = 0; i < n; i++) {
            if (!isReachable[i]) {
                result.push_back(i);
            }
        }
        
        return result;
    }
};
