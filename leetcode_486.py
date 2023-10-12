
def main(nums: list[int]):
    global numsLength
    numsLength = len(nums)


    # input: [1, 5, 2]
    finalScore = playGame(nums)
    if finalScore >= 0:
        return True
    return False



def playGame(nums: list[int]) -> int:
    # this function plays the game
    # the value is p1Score - p2Score (p1 is MAX, p2 is MIN)
    player = PLAYER(nums)

    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        if player == "MAX":
            p1 = max([nums[0], nums[1]])
            p2 = min([nums[0], nums[1]])
            return p1 - p2 # > 0
        elif player == "MIN":
            p2 = max([nums[0], nums[1]])
            p1 = min([nums[0], nums[1]])
            return p1 - p2 # < 0
    
    if player == "MAX":
        value: int = -10000000000000
        value = max([value, playGame(nums[1:]) + nums[0]]) # -97
        value = max([value, playGame(nums[:len(nums) - 1]) + nums[len(nums) - 1]])  # -1
        return value # -1

    elif player == "MIN":
        value: int = 10000000000000
        value = min([value, playGame(nums[1:]) - nums[0]])
        value = min([value, playGame(nums[:len(nums) - 1])  - nums[len(nums) - 1]])
        return value
    
    # the code will not reach this
    return 0

def PLAYER(nums: list[int]):
    move = numsLength - len(nums)
    if move % 2 == 0:
        return "MAX"
    else:
        return "MIN"

print(main([1,5,233,7]))

# we need:
# - a way to know which move it is (Min, Max)
# - a way to know the value which i will make player1Score - player2Score (player1 want this to be Max and player2 want this to be Min)
# - a way to determine the end (probably when the length of nums is 2)