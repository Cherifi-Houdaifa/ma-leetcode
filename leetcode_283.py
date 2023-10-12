def main(nums: list[int]):
    numsLen = len(nums)
    # create new array
    result = [0 for i in nums]


    # loop through nums add zeros to the end and non-zeros to the start
    i = 0
    end = numsLen - 1
    start = 0
    while i < numsLen:
        if nums[i] == 0:
            # add it to the end
            result[end] = 0
            end -= 1
        else:
            # add it to the start
            result[start] = nums[i]
            start += 1
        i+= 1

    # copy the content of the new array to nums
    i = 0
    while i < numsLen:
        nums[i] = result[i]
        i+= 1
    print(nums)
main([0])