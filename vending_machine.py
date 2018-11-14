from biotest import *

# coins available: 100, 50, 20, 10, 5, 2, 1

def get_change(amount):
    list_avail_coins = [100, 50, 20, 10, 5, 2, 1, ]
    
    if amount ==0: 
        return []
    
    if amount in list_avail_coins:  
        return [amount]

    change = []
    for coin in list_avail_coins:
        if coin <= amount:
            change.append(coin)
            
    return change




test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2, 1,])
test_are_equal(get_change(7), [5, 2, ])


print('All tests pass!')