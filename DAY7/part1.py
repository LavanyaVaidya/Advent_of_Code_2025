input = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

def processing_input(input: str):
    rows = input.strip().splitlines()
    matrix = [list(v) for v in rows]
    return matrix

def helper(n: int, m: int, matrix: list[list[str]], already_processed: list[list[bool]]) -> int:
    i, num1, num2 = n, 0, 0
    while i < len(matrix):
        if matrix[i][m] == '^' and already_processed[i][m] == False:
            already_processed[i][m] = True
            num1 += 1
            if m-1 >= 0:
                num1 += helper(i,m-1,matrix,already_processed)
            if m+1 < len(matrix[0]):
                num2 = helper(i,m+1,matrix,already_processed)
        if matrix[i][m] == '^':
            break
        if matrix[i][m] == '.':
            matrix[i][m] = '|' #Simulating the splitting of the beams
        i += 1
    return 0 if i == len(matrix) else num1 + num2
        

matrix = processing_input(input)

n, m = len(matrix), len(matrix[0])

already_processed = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'S':
            print(helper(i,j,matrix,already_processed))
            break

###### variable reconstruct can be used to view how to beam travelled from top to bottom ######
# print(matrix)
# reconstruct = "\n".join("".join(row) for row in matrix)
# print(reconstruct)