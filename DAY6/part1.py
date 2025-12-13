input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
"""

rows = input.strip().splitlines()
numbers, ans = [], 0

for i in range(len(rows)-1):
    numbers.append([int(v) for v in rows[i].split()])

operations = [v for v in rows[len(rows)-1].split()]

for op in range(len(operations)):
    num = 0 if operations[op] == '+' else 1
    for i in range(len(numbers)):
        # print(numbers[i][op])
        if operations[op] == '+':
            num += numbers[i][op]
        else:
            num *= numbers[i][op]
    # print(operations[op])
    ans += num

print(ans)