input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def helper(matrix: list[str]) -> int:
    n, m, ans = len(matrix), len(matrix[0]), 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != '@':
                continue
            k, l, v, q, cnt = max(0,i-1), max(0,j-1), min(n,i+2), min(m,j+2), 0
            # print(i, " ", j)
            # print(k, " ", l, " ", v, " ", q)
            for x in range(k,v):
                for y in range(l,q):
                    # print(x, " ", y)
                    if matrix[x][y] == '@':
                        cnt += 1
            if cnt <= 4:
                # print(i, " ", j)
                ans += 1
    return ans

matrix = input.strip().splitlines()
print(matrix)
print(helper(matrix))