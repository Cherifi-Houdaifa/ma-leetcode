def main(prices: list[int]):
    maxProfit = 0
    price = 10**4 + 1
    for i in prices:
        if i < price:
            price = i
        elif i > price:
            profit = i - price
            if profit > maxProfit:
                maxProfit = profit
    return maxProfit

main([7,6,4,3,1])