while (True):
    nums = sorted(list(map(int, input().split())))
    if nums[0] == 0:
        break
    print("right") if nums[0] * nums[0] + nums[1] * nums[1] == nums[2] * nums[2] else print("wrong")
