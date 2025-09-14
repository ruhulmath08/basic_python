def total(gallons, sickles, knuts):
    return (gallons * 17 + sickles) * 29 + knuts


def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)


coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), " knuts")  # 50775  knuts

"""
TypeError: total() missing 2 required positional arguments: 'sickles' and 'knuts'
print(total(coins), " knuts")
"""

# * -> unpacking: unpacking the list into positional arguments
print(total(*coins), " knuts")  # 50775  knuts

print(total(gallons=100, sickles=50, knuts=25), " knuts")  # 50775  knuts

coins_set = {"gallons": 100, "sickles": 50, "knuts": 25}
print(total(coins_set["gallons"], coins_set["sickles"], coins_set["knuts"]), " knuts")
print(total(**coins_set), " knuts")  # total(**coins_set) same as total(gallons=100, sickles=50, knuts=25)

f(100, 50, 25)  # Positional: (100, 50, 25)
f(100, 50, 25, 5)  # Positional: (100, 50, 25, 5)

# Named: {'gallons': 100, 'sickles': 50, 'knuts': 25}
f(gallons=100, sickles=50, knuts=25)
