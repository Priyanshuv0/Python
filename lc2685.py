class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n
        count = 0

        for start in range(n):
            if visited[start]:
                continue

            nodes = []
            stack = [start]
            visited[start] = True

            while stack:
                node = stack.pop()
                nodes.append(node)
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            num_nodes = len(nodes)
            num_edges = sum(len(adj[node]) for node in nodes) // 2

            if num_edges == num_nodes * (num_nodes - 1) // 2:
                count += 1

        return count
