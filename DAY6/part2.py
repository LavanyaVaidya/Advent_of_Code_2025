input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
"""

rows = input.strip().splitlines()

# for i in range(len(rows)-1):
#     numbers.append([v for v in rows[i].split(" ")])

operations = [v for v in rows[len(rows)-1].split()]

ans, total, cnt = 0, 1 if operations[0] == '*' else 0, 0

for i in range(len(rows[0])):
    num, flag = 0, False
    for j in range(len(rows)-1):
        if rows[j][i] != ' ':
            flag = True
            num = num*10 + int(rows[j][i])
    if flag == False:
        cnt += 1
        ans += total
        total = 0 if (cnt)<len(operations) and operations[cnt] == '+' else 1
    else:
        if operations[cnt] == '+':
            total += num
            # print("PLUS ", total)
        else:
            total *= num
            # print("MUL ",total)
        # print(num)

if total != 0:
    ans += total

print(ans)