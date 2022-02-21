# Things I have learned!
- To output variable as two decimal points:
```{v:.2f}``` use f string.

 - To make numbers more readable:
 ```332_001.00``` use underscore.

 - To evaluate if a number is divisible by another number:
 ```i % n == 0``` if divisible without remainder then it is a multiple of n.

 - To replace indice of list using For loop:
 ```
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

word_length = len(chosen_word)
display = []
for _ in chosen_word:
    display.append('_')

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
print(display)
 ```
 
