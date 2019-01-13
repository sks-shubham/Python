import re

print("Calc")
print("type quit to exit\n")
print("enter c to clear")

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == "quit":
        run = False
    else:
        if str(equation) == "c":
            previous = 0
            equation = '0'

        equation = re.sub('a-zA-Z,./;,:', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+equation)

        print("You Typed", previous)


while run:
    perform_math()

