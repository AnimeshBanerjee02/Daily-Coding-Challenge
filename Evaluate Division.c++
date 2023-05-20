#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, unordered_map<string, double>> graph;
        
        // Building  the graph
        for (int i = 0; i < equations.size(); i++) {
            const string& dividend = equations[i][0];
            const string& divisor = equations[i][1];
            const double quotient = values[i];
            
            graph[dividend][divisor] = quotient;
            graph[divisor][dividend] = 1.0 / quotient;
        }
        
        vector<double> results;
        
        // Evaluating the queries
        for (const auto& query : queries) {
            const string& dividend = query[0];
            const string& divisor = query[1];
            
            if (!graph.count(dividend) || !graph.count(divisor)) {
                results.push_back(-1.0);
            } else if (dividend == divisor) {
                results.push_back(1.0);
            } else {
                unordered_map<string, bool> visited;
                double result = dfs(graph, dividend, divisor, 1.0, visited);
                results.push_back(result);
            }
        }
        
        return results;
    }
    
private:
    double dfs(const unordered_map<string, unordered_map<string, double>>& graph, const string& currNode,
               const string& targetNode, double currResult, unordered_map<string, bool>& visited) {
        if (currNode == targetNode) {
            return currResult;
        }
        
        visited[currNode] = true;
        
        for (const auto& neighbor : graph.at(currNode)) {
            const string& nextNode = neighbor.first;
            const double edgeWeight = neighbor.second;
            
            if (!visited[nextNode]) {
                double result = dfs(graph, nextNode, targetNode, currResult * edgeWeight, visited);
                if (result != -1.0) {
                    return result;
                }
            }
        }
        
        return -1.0;
    }
};
