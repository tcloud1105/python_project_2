import re


print("My Magical Calculator");
print("Type 'quit' to exit \n")
previous = 0
running = True

def  performMath():
    global running
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter a equation: ")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Good bye")
        running = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+equation)
        print("You typed ", previous)

while running:
    performMath()