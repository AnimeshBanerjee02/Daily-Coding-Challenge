from typing import List
import collections

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(bombs)

        def buildGraph():
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    xi, yi, ri = bombs[i]
                    xj, yj, _ = bombs[j]
                    if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                        graph[i].append(j)

        def dfs(cur, visited):
            visited.add(cur)
            for neib in graph[cur]:
                if neib not in visited:
                    dfs(neib, visited)
            return len(visited)

        answer = 0
        buildGraph()
        for i in range(n):
            visited = set()
            answer = max(answer, dfs(i, visited))

        return answer
