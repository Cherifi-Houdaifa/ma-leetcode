def main(nums: list[int]):
    # NOTE if you can reach a given index you can reach all prior indexes
    # NOTE the only way you can't reach the last index is having a zero that can not be jumped over
    numsLen = len(nums)
    goal = numsLen - 1
    position = 0

    while position < goal:
        maxJump = nums[position]
        
        if nums[position] == 0:
            # check if you can jump over this zero and jump if you can
            if position == 0:
                return False
            
            zeroPosition = position
            tempPosition = zeroPosition - 1
            while tempPosition >= 0:
                if tempPosition + nums[tempPosition] > zeroPosition:
                    # here we can jump over the zero
                    position = tempPosition
                    break
                else:
                    tempPosition -= 1
            else:
                return False

        else:
            position += maxJump  # add the maximum jump

    return True

print(main([3,2,1,0,4]))