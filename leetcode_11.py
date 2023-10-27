def main(height: list[int]):
    left = 0
    right = len(height) - 1
    maxArea = -1

    while left < len(height) and right > 0:
        # print(right, left)
        # print("--------------", min(height[left],height[right]) * abs(right - left))

        if min(height[left],height[right]) * abs(right - left) > maxArea:
            maxArea = min(height[left],height[right]) * abs(right - left)
        
        if height[left] > height[right]:
            right -=1
        elif height[left] < height[right]:
            left +=1
        else:
            left +=1
        
    return maxArea



print(main([1,1]))