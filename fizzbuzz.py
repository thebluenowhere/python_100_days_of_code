### never heard of this childrens game
# Print numbers from 1 to 100, if num /3, /5, /15 change num


for num in range(1, 101):

    if num % 15 == 0:
        num = "fizzbuzz"
    elif num % 3 == 0:
        num = "fizz"
    elif num % 5 == 0:
        num = "buzz"
    elif num % 7 == 0:
        num = "baz"
    print(num)

# Friends solution

for i in range(101):
    v = ''
    if i % 3 == 0:
        v += 'fizz'
    if i % 5 == 0:
        v += 'buzz'
    if len(v) == 0:
        v = i
    print(v)
