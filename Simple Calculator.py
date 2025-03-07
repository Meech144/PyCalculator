inp1 = input("Please select a number between 1 and 10 or 'quit' to exit: ")
if inp1 == 'quit':
    print("Goodbye")
    exit()
while not inp1.isdigit():
    print("Incorrect input please try again")
    inp1 = input("Please select a number between 1 and 10 or 'quit' to exit")
else:
    pass
inp2 = input("Please select a second number between 1 and 10 or 'quit' to exit: ")
if inp2 == 'quit':
    print("Goodbye")
    exit()
while not inp2.isdigit():
    input("Please select a number between 1 and 10 or 'quit' to exit: ")
    inp2 = input("Please select a second number between 1 and 10: ")
else:
    pass
sel = int(input("1. for +, 2. for -, 3. for *, 4 for /: "))
num1 = int(inp1)
num2 = int(inp2)
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
if sel == 1:
    print(f"{num1} + {num2} = {add}")
if sel == 2:
    print(f"{num1} - {num2} = {sub}")
if sel ==3:
    print(f"{num1} * {num2} = {mul}")
if sel == 4:
    print(f"{num1} / {num2} = {div}")