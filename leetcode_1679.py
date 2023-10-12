def main(nums: list[int], k: int):

    numsLen = len(nums)
    maxOperations = 0

    numsMap: dict = dict()

    i = 0
    while i < numsLen:
        currentNum = nums[i]

        try:
            # this exists as a target
            numsMap[currentNum] -= 1
            maxOperations += 1
            if numsMap[currentNum] <= 0:
                numsMap.pop(currentNum)
        except KeyError:
            # does not exist as a target
            try:
                numsMap[k - currentNum] += 1
            except KeyError:
                numsMap[k - currentNum] = 1

        i+= 1
    return maxOperations


main([1, 2, 3, 3], 5)