import random
amount = random.randrange(1, 5)
if amount > 1:
    print(amount, " coin flips:")
n = 0
while n < amount:
    coin = random.randint(0, 1)
    if coin:
        print("Heads!")
    else:
        print("Tails!")
    n = n+1
