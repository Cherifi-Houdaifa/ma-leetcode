def main(nums: list[int]):
    result = [1 for i in nums]

    numsLen = len(nums)

    i = 0
    product = 1
    while i < numsLen:
        temp = nums[i]
        result[i] *= product
        product = product * temp

        i += 1

    i = numsLen - 1
    product = 1
    while i >= 0:
        temp = nums[i]
        result[i] *= product
        product = product * temp
        i -= 1

    return result

main([-1,1,0,-3,3])


# the implementation:
# loop two times one from left to right and one in the opposite way
# and then gradually calculate the product and use it
