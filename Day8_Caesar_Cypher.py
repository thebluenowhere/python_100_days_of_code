alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  new_index = []
  cipher_text = ""
  for letter in text:
    new_index.append(alphabet.index(letter) + shift)
  print(new_index)
  for index in new_index:
    if index >= 26:
      cipher_text += alphabet[index - 26]
    else: 
      cipher_text += alphabet[index]
  print(cipher_text)
  
  
encrypt(text, shift)
