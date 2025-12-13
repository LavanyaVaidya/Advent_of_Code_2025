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

def distance_between_pairs(matrix: list[list[int]]) -> dict:
    dict = {}
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            dict[tuple([i,j])] = euclidian(matrix[i],matrix[j])
    dict = sorted(dict.items(), key=lambda x : x[1])
    dict = [x for x,_ in dict]
    return dict

def adjacency_list(distance_dict: dict, matrix: list[list[int]])->int:
    # print(matrix)
    # print(distance_dict)
    parent = list(range(len(matrix)))
    counter = len(matrix)

    def find(a: int):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]
    
    def union(a: int, b: int) -> bool:
        pa, pb = find(a), find(b)
        if pb == pa:
            return False

        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb
        return True
    
    for a,b in distance_dict:
        if union(a,b):
            counter -= 1
        if counter == 1:
            # print(matrix[a]," ",matrix[b])
            return matrix[a][0] * matrix[b][0]
    return 0
    

matrix = [[int(v) for v in x.split(',')] for x in input.strip().splitlines()]

distance_dict = distance_between_pairs(matrix)
print(adjacency_list(distance_dict,matrix))
