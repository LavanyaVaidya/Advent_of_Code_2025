input = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

chunks = input.strip().split('\n\n')
gift_sizes, ans = [], 0
for i in range(len(chunks)-1):
    gift_size = 0
    for ch in chunks[i]:
        if ch == '#':
            gift_size += 1
    gift_sizes.append(gift_size)

regions_and_gifts = [x.strip().split(":") for x in chunks[-1].strip().splitlines()]

regions = [[int(v) for v in row[0].strip().split("x")] for row in regions_and_gifts]
gifts = [[int(v) for v in row[1].strip().split(" ")] for row in regions_and_gifts]

for i in range(len(regions)):
    if regions[i][1]*regions[i][0] >= 9*sum(gifts[i]):
        ans += 1
    elif regions[i][1]*regions[i][0] >= sum(gift_sizes[x]*gifts[i][x] for x in range(len(gifts[i]))):
        ans += 1


print(ans)