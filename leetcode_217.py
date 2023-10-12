def main(nums: list[int]) -> bool:
    # input: [1, 2, 3, 1]

    # normal approach
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
                return True
            j+=1
        i+= 1
    return False

print(main([1,1,1,3,3,4,3,2,4,2]))