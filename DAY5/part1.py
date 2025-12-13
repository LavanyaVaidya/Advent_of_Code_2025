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

parts = input.strip().split("\n\n")
valid_ranges = [x.split("-") for x in parts[0].strip().split("\n")]
ingredients = parts[1].strip().split("\n")
# print(ingredients)

ans = 0

for ing in ingredients:
    for range in valid_ranges:
        if (int(ing) >= int(range[0]) and int(ing) <= int(range[1])):
            ans += 1
            break
print(ans)