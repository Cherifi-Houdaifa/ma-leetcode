from math import sqrt

def main(limit: int):
    # implementing that algorithm
    result = list(range(2, limit + 1))
    
    count = 0
    while count < int(sqrt(limit)):

        if checkPrime(result[count]):
            result = removeMultiplies(result, result[count])
        count += 1
    print(result)
    return result

def checkPrime(num: int):
    # input: 11
    # output: True
    if num in [0, 1]:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def removeMultiplies(lst: list[int], num:int):
    # input: [1,2,3,4,5,6,7,8,9,10], 2
    # output: [1,3,5,7,9]
    lstCopy = lst.copy()
    for i in lst:

        if i != num and i % num == 0:
            lstCopy.remove(i)
    return lstCopy