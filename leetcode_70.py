def main(n: int):
    def fac(n: int):
        if n == 0:
            return 1
        if n == 1:
            return 1
        return n * fac(n - 1)

    count = 1
    replaced = 0

    while True:
        replaced += 1
        if replaced > n / 2:
            break
        l = n - replaced
        count += fac(l) / (fac(replaced) * fac(l-replaced))
    
    return count
    
print(main(5))    

