from biotest import *
# usd_coins = [100, 50, 25, 10, 5, 1, ]
# eur_coins = [100, 50, 20, 10, 5, 2, 1, ]
usd_coins = {100: 20, 50: 20, 25: 20, 10: 20, 5: 20, 1: 20, }
#eur_coins = {100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20, }
eur_coins = {100: 2, 50: 2, 20: 2, 10: 2, 5: 2, 2: 2, 1: 2, }

def get_change(amount, coins=eur_coins):
    change = []
    if amount > 0:
        for coin in sorted(coins, reverse=True):
            print(coin)
            while coin <= amount and coins[coin] > 0:
                amount -= coin
                print('amount:', amount)
                coins[coin] -= 1
                change.append(coin)
            print('coins:', coins)
    if amount != 0: change = []        
    print('change:', change)
    return change

print('text_are_equal 1'); test_are_equal(get_change(0), [])
print('text_are_equal 2'); test_are_equal(get_change(1), [1])
print('text_are_equal 3'); test_are_equal(get_change(2), [2])
print('text_are_equal 4'); test_are_equal(get_change(5), [5])
print('text_are_equal 5'); test_are_equal(get_change(10), [10])
print('text_are_equal 6'); test_are_equal(get_change(20), [20])
print('text_are_equal 7'); test_are_equal(get_change(50), [50])
print('text_are_equal 8'); test_are_equal(get_change(100), [100])
print('text_are_equal 9'); test_are_equal(get_change(3), [2, 1, ])
print('text_are_equal 10'); test_are_equal(get_change(100), [100])
print('text_are_equal 11'); test_are_equal(get_change(15), [10, 5, ])
print('text_are_equal 12'); test_are_equal(get_change(35, usd_coins), [25, 10, ])
print('text_are_equal 13'); test_are_equal(get_change(49, usd_coins), [25, 10, 10, 1, 1, 1, 1, ])
print('text_are_equal 14'); test_are_equal(get_change(49), [])
print('All tests pass!')