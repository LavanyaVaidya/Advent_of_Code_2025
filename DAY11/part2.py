input = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
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

a = dfs(adj,'svr','fft',visited) 
visited, mp = set(), c.defaultdict(lambda : -1)
b = dfs(adj,'fft','dac',visited) 
visited, mp = set(), c.defaultdict(lambda : -1)
d = dfs(adj,'dac','out',visited)
visited, mp = set(), c.defaultdict(lambda : -1)

print(a*b*d)