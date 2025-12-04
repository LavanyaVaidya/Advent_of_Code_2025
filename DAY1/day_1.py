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
    # print(nums)
    init, ans = 50, 0
    for i in range(len(nums)):
        if nums[i][0] == 'L':
            init = init - (int)(nums[i][1:])
            if init < 0:
                init = (init%100)
        else:
            init = init + (int)(nums[i][1:])
            if init > 99:
                init = (init%100)
        # print(init)
        if init == 0:
            ans = ans + 1
    return ans

print(day_1(raw))