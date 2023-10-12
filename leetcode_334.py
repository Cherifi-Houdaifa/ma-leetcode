def main(nums: list[int]):
    i= 0
    numsLen = len(nums)
    while i <  numsLen:
        left = nums[:i]
        right = nums[i+1:]
        leftIsSmaller = False
        rightIsBigger = False
        for num in left:
            if num < nums[i]:
                leftIsSmaller = True
                break
        for num in right:
            if num > nums[i]:
                rightIsBigger = True
                break
        if leftIsSmaller and rightIsBigger:
            return True
        i+=1
    return False

print(main([2,1,5,0,4,6]))