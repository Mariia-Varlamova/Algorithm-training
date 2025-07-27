# Каково минимальное количество монет номиналами в coins, 
# необходимое для сдачи в 77 центов?
coins = [25, 10, 5, 1]
amount = 77

def min_coins(amount, coins):
    count = 0
    for coin in coins:
        if amount == 0:
            break
        num_coins = amount // coin
        count += num_coins
        amount -= num_coins * coin
    return count

print(min_coins(amount, coins))