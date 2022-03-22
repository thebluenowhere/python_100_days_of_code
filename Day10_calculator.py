""" CALCULATOR """

from art import logo

def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def divide(n1, n2):
  return n1 / n2
def multiply(n1, n2):
  return n1 * n2

operations = {
  "+": add,
  "-": subtract,
  "/": divide,
  "*": multiply
}

def calculator():
  print(logo)
  stop = False
  num1 = float(input("What's the first number?: "))
  while not stop:
    for key in operations:
      print(key)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}.")
    choice = (input(f"Type 'Y' to continue calculating with {answer}, or type 'N' to exit.: "))
    num1 = answer
    if choice == 'N'.lower().strip():
      stop = True
      calculator()

calculator()
