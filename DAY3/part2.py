input = """
987654321111111
811111111111119
234234234234278
818181911112111
"""
import collections as c

ans = 0
bank = input.strip().splitlines()
for batteries in bank:
    n, stk, i = len(batteries), [], 0
    while ((n-i) != 12-len(stk)):
        # print(i, " ", n-i, " ", 12-len(stk))
        if len(stk) and stk[-1] < batteries[i]:
            stk.pop()
        elif (12-len(stk)) != 0:
            stk.append(batteries[i])
            i += 1
        else:
            i += 1
        # print(stk)
    # print(i)
    if len(stk) != 12:
        stk.extend(batteries[-(12-len(stk)):])
    # print(stk)
    ans += (int)("".join(stk))

print(ans)
