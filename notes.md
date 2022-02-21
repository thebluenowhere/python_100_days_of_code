# Things I have learned!
- To output variable as two decimal points:
```{v:.2f}``` use f string.

 - To make numbers more readable:
 ```332_001.00``` use underscore.

 - To evaluate if a number is divisible by another number:
 ```i % n == 0``` if divisible without remainder then it is a multiple of n.

 - To replace indice of list using For loop:
 ```
 word_list = ["aardvark", "baboon", "camel"]

 chosen_word = random.choice(word_list)
 display = []
 word_length = len(chosen_word)
 
 for _ in range(word_length):
 >>>>display += "_"

 guess = input("Guess a letter:").lower()
 
 for position in range(word_length):
 >>>>letter = chosen_word[position]
 >>>>if letter == guess:
 >>>>>>>>display[position] = letter
 ```
 
