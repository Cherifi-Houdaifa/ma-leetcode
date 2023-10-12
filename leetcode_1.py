def main(nums: list, target: int):
    for i in nums:
        numsCopy = nums.copy()
        numsCopy.remove(i)
        try:
            secondNum = numsCopy.index(target - i) + 1
            # secondNum exist
            return [nums.index(i), secondNum]
        except ValueError:
            # secondNum does not exist
            pass

    # O(n^2) implementation
    # count = 0
    # for i in nums[count:]:
    #     numsCopy = nums.copy()
    #     numsCopy.remove(i)
    #     for j in numsCopy:
    #         if (i + j) == target:
    #             num1 = nums.index(i)
    #             nums.remove(i)
    #             num2 = nums.index(j) + 1
    #             return [num1, num2]
    #     count +=1



result = main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19)
print(result)
