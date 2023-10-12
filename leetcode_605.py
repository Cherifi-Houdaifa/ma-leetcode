def main(flowerbed: list[int], n: int):
    # flowers can not be adjacent (one next to the other)
    # 1 means there is a flower and 0 there isn't

    flowerbedLen = len(flowerbed)
    plantPointer = 0
    while plantPointer < flowerbedLen and n > 0:
        if flowerbed[plantPointer] == 1:
            plantPointer += 1
            continue
        left = True
        right = True
        if plantPointer - 1 >= 0:
            if flowerbed[plantPointer - 1] == 1: left = False
        if plantPointer + 1 < flowerbedLen:
            if flowerbed[plantPointer + 1] == 1: right = False
        
        if right and left:
            n -= 1
            flowerbed[plantPointer] = 1
        plantPointer += 1
    
    return n == 0
print(main([1,0,0,0,1], 2))



# input: [1,0,0,0,1], 1
# output: True

# input: [1,0,0,0,1], 2
# output: False