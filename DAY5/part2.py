input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
############# We will approach it by merging the overlapping intervals #################

parts = input.strip().split("\n\n")
valid_ranges = [[int(v) for v in x.split("-")] for x in parts[0].strip().split("\n")]

valid_ranges.sort(key=lambda x: (x[0],x[1]))

n, i, left, right, ans = len(valid_ranges), 1, valid_ranges[0][0], valid_ranges[0][1], 0
while i < n:
    if valid_ranges[i][0] <= right:
        right = max(right,valid_ranges[i][1])
    else:
        ans += (right-left+1)
        right, left = valid_ranges[i][1], valid_ranges[i][0]
    i += 1

ans += (right-left+1)
print(ans)

