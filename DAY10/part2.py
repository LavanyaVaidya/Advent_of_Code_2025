input = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
import collections as c
import pulp as p

def Integer_Linear_Programming(matrix: list[list[int]], joltage: list[int]):

    Lp_prob = p.LpProblem('Problem', p.LpMinimize)

    ## Each button will be a variable for Lp Model
    variables = [
        p.LpVariable(f"x_{i}", lowBound=0, cat="Integer")
        for i in range(len(matrix))
    ]

    Lp_prob += p.lpSum(variables)

    for i in range(len(joltage)):
        Lp_prob += p.lpSum(matrix[j][i]*variables[j] for j in range(len(matrix))) == joltage[i]

    status = Lp_prob.solve(p.PULP_CBC_CMD(msg=False))
    
    return p.value(Lp_prob.objective)

rows = [rows.split(' ') for rows in input.strip().splitlines()]

joltage = [[int(v) for v in row[-1][1:-1].split(',')] for row in rows]
buttons = [[[int(x) for x in v[1:-1].strip().split(',')] for v in row[1:-1]] for row in rows]

ans = 0

for row, button_list in enumerate(buttons):
    matrix = [[0 for _ in range(len(joltage[row]))] for _ in range(len(button_list))]
    for ind, button in enumerate(button_list):
        for b in button:
            matrix[ind][b] = 1
    ans += Integer_Linear_Programming(matrix,joltage[row])

print(ans)

                
