input = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
import collections as c

def dfs(adj: dict, current: str, target: str, visited: set) -> int:
    if current == target:
        return 1
    count = 0
    visited.add(current)
    for neigh in adj.get(current, []):
        if neigh not in visited:
            count += dfs(adj,neigh,target,visited)
        else:
            count += mp[neigh]
    mp[current] = count
    return count

matrix = [x.split(':') for x in input.strip().splitlines()]

start_node = [row[0] for row in matrix]
other_nodes = [row[1].strip().split(" ") for row in matrix]

adj, mp = c.defaultdict(list), c.defaultdict(lambda : -1)
visited = set()
for i in range(len(start_node)):
    adj[start_node[i]] = other_nodes[i]
ans = dfs(adj,'you','out',visited)

print(ans)