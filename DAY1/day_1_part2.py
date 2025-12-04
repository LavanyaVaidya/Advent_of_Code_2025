raw = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

def day_1(raw: str) -> int:
    nums = raw.strip().splitlines()
    pos = 50
    ans = 0
    for line in nums:
        direction = line[0]
        steps = int(line[1:])
        full_cycles = steps // 100  
        steps = steps % 100
        prev_pos = pos
        if direction == 'L':
            pos = pos - steps
            if pos <= 0 and prev_pos != 0:
                ans += 1
        else:
            pos = pos + steps
            if pos > 99:
                ans += 1
        pos = pos%100
        ans += full_cycles
        print(line, " ", prev_pos, " ", pos, " ", ans)
    return ans

print(day_1(raw))