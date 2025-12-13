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
import collections as co

def create_boundary(grid: list[list[str]], min_row: dict, max_row: dict, min_col: dict, max_col: dict):
    for key, _ in min_row.items():
        for i in range(min_row[key]+1,max_row[key]):
            if grid[i][key] == '.':
                grid[i][key] = '#'
    for key, _ in min_col.items():
        for i in range(min_col[key]+1,max_col[key]):
            if grid[key][i] == '.':
                grid[key][i] = '#'

def floodfill(grid: list[list[int]]):
    row, col = len(grid), len(grid[0])
    q = co.deque()
    visited = [[False for _ in range(col)] for _ in range(row)]
    for i in range(row):
        if grid[i][0] == '.' and visited[i][0] == False:
            grid[i][0] = 'o'
            visited[i][0] = True
            q.append((i,0))
        if grid[i][col-1] == '.' and visited[i][col-1] == False:
            grid[i][col-1] = 'o'
            visited[i][col-1] = True
            q.append((i,col-1))
    for i in range(col):
        if grid[0][i] == '.' and visited[0][i] == False:
            grid[0][i] = 'o'
            visited[0][i] = True
            q.append([0,i])
        if grid[row-1][i] == '.' and visited[row-1][i] == False:
            grid[row-1][i] = 'o'
            visited[row-1][i] = True
            q.append((row-1,i))

    while q:
        r,c = q.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < row and 0 <= nc < col:
                if grid[nr][nc] == '.' and visited[nr][nc] == False:
                    grid[nr][nc] = 'o'
                    visited[nr][nc] = True
                    q.append((nr,nc))

matrix = [[(int)(v) for v in x.split(',')] for x in input.strip().split()]

############# Getting row and column for the grid simulation ###############
m, n, ans = max([row[0] for row in matrix]), max([row[1] for row in matrix]), 0

############ Forming Grid ##############
grid = [['.' for _ in range(m+1)] for _ in range(n+1)]
min_row, max_row, min_col, max_col = co.defaultdict(lambda : n), co.defaultdict(lambda : 0), co.defaultdict(lambda : m), co.defaultdict(lambda : 0)
for a,b in matrix:
    min_row[a] = min(min_row[a],b)
    max_row[a] = max(max_row[a],b)
    min_col[b] = min(min_col[b],a)
    max_col[b] = max(max_col[b],a)
    grid[b][a] = '#'

###### Connecting points on same row or same column ######
# print(min_row," ",min_col," ",max_row," ",max_col)
create_boundary(grid,min_row,max_row,min_col,max_col)

#### Floodfilling outside the boundaries #####
floodfill(grid)

for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
        if grid[matrix[j][1]][matrix[i][0]] != 'o' and grid[matrix[i][1]][matrix[j][0]] != 'o':
            ans = max(ans,(abs(matrix[i][0]-matrix[j][0])+1)*(abs(matrix[i][1]-matrix[j][1])+1))

#### To visualize on cmd ######
reconstruct = "\n".join("".join(row) for row in grid)
print(ans)