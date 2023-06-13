#include <vector>
#include <unordered_map>

class Solution {
public:
    int equalPairs(std::vector<std::vector<int>>& grid) {
        int n = grid.size();
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i] == getColumn(grid, j))
                    count++;
            }
        }
        
        return count;
    }
    
private:
    std::vector<int> getColumn(const std::vector<std::vector<int>>& grid, int col) {
        int n = grid.size();
        std::vector<int> column(n);
        
        for (int i = 0; i < n; i++) {
            column[i] = grid[i][col];
        }
        
        return column;
    }
};
