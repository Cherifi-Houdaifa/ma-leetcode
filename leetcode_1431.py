def main(candies: list[int], extraCandies: int):
    # input: [2,3,5,1,3], 3
    # output: [true,true,true,false,true]
    
    # get the maximum amount of candies
    maxCandies = 0
    for i in candies:
        if i > maxCandies:
            maxCandies = i
    
    result = []

    # loop through each kid candies add extraCandies and compare to maxCandies
    for i in candies:
        if i + extraCandies >= maxCandies:
            result.append(True)
        else:
            result.append(False)

    return result
main([12, 1, 12], 10)