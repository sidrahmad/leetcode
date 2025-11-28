class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], vals: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for v,u in edges: g[v].append(u); g[u].append(v)
        
        def dfs(node,prnt):
            q = vals[node]+sum(dfs(neigh,node) for neigh in g[node] if neigh!=prnt)
            return q+(q.real%k==0)*1j

        return int(dfs(0,-1).imag)