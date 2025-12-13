input = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
import collections as c

def euclidian(a: list[int], b: list[int]) -> int:
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

def distance_between_pairs(matrix: list[list[int]], connections: int) -> dict:
    dict = {}
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            dict[tuple([i,j])] = euclidian(matrix[i],matrix[j])
    dict = sorted(dict.items(), key=lambda x : x[1])[:connections]
    dict = [x for x,y in dict]
    return dict

def adjacency_list(distance_dict: dict)->int:
    adj = c.defaultdict(list)
    for a,b in distance_dict:
        adj[a].append(b)
        adj[b].append(a)
    # print(adj)

    visited = set()
    lis = []
    def dfs(node: int) -> int:
        count = 1
        visited.add(node)
        for neigh in adj.get(node, []):
            if neigh not in visited:
                count += dfs(neigh)
        return count

    for node, _ in adj.items():
        if node not in visited:
            lis.append(dfs(node))
    lis.sort(reverse=True)
    lis.extend({1,1,1})
    return lis[0]*lis[1]*lis[2]

matrix = [[int(v) for v in x.split(',')] for x in input.strip().splitlines()]

connections = 1000

distance_dict = distance_between_pairs(matrix,connections)
print(adjacency_list(distance_dict))
