### RANDOM COIN FLIP
import random

# Randomise seed
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Random integer between 0 and 1
rand_int = random.randint(0, 1)
# Print result
if rand_int == 1:
    print("Heads")
else:
    print("Tails")
