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
    q = c.deque([])
    for b in batteries:
        battery = (int)(b)
        if len(q) < 2:
            q.append(battery)
        elif q[0] < q[1]:
            q.popleft()
            q.append(battery)
        else:
            if q[1] < battery:
                q.pop()
                q.append(battery)
    print(q[0]*10 + q[1])
    ans += q[0]*10 + q[1]

print(ans)
