input = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

matrix = [[(int)(v) for v in x.split(',')] for x in input.strip().split()]

ans = 0

for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
        ans = max(ans,(abs(matrix[i][0]-matrix[j][0])+1)*(abs(matrix[i][1]-matrix[j][1])+1))

print(ans)