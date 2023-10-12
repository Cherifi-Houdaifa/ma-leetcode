def main(digits: str):
    mappings = {
        2: ["abc", 3],
        3: ["def", 3],
        4: ["ghi", 3],
        5: ["jkl", 3],
        6: ["mno", 3],
        7: ["pqrs", 4],
        8: ["tuv", 3],
        9: ["wxyz", 4]
    }

    combinations = 1
    for i in digits:
        combinations *= mappings[int(i)][1]
    result = ["" for i in range(combinations)]
    
    digitsLen = len(digits)
    i = 0
    while i < digitsLen:
        i+=1
main("23")