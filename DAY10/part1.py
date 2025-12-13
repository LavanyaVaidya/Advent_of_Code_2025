input = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
import collections as c

def knapshak(index: int, row_ind: int,  button_val: list[str], row: list[int], mp: dict, ans: int):
    if index == len(row):
        for idx, val in enumerate(button_val[row_ind]):
            # print(idx," ",val," ")
            if val == '.' and mp.get(idx, 0)%2 != 0:
                return float('inf')
            if val == '#' and mp.get(idx, 0)%2 != 1:
                return float('inf')
        return ans
    a = knapshak(index+1,row_ind,button_val,row,mp,ans)
    for lights in row[index]:
        mp[lights] += 1
    b = knapshak(index+1,row_ind,button_val,row,mp,ans+1)
    for lights in row[index]:
        mp[lights] -= 1
    return min(a,b)

rows = [rows.split(' ') for rows in input.strip().splitlines()]

button_val = [list(row[0][1:-1]) for row in rows]
joltage = [[int(v) for v in row[-1][1:-1].split(',')] for row in rows]
button_switch = [[[int(x) for x in v[1:-1].strip().split(',')] for v in row[1:-1]] for row in rows]
# print(button_switch)
# print(button_val)
final_ans = 0

for row_ind,row in enumerate(button_switch):
    mp = c.defaultdict(int)
    ans = knapshak(0,row_ind,button_val,row,mp,0)
    final_ans += ans if ans != 10**9 + 7 else 0
    # print("*****",ans,"******")

print(final_ans)
                
