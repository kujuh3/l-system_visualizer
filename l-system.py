import turtle
import random
# https://en.wikipedia.org/wiki/L-system
# This program works as a self-similar fractal curve visual translator using L-system
# Input variables and rules to output a visual representation
def MainMenu():
    def clientinput(variables: str, repeatable: bool):
        inputobject = {}
        for index, char in enumerate(variables):
            rule = input(f"""
            Input rule for variable {char}. Type the part after -> sign.
            Example: {char} -> {char}+{variables[len(variables)-1]}+{char}+{char}:
            """).lower()
            inputobject[char] = rule
        return inputobject
        # while True:
        #     value = input(prompt)
        #     inputobject[value] = value
        #     newline = input("Input a second one? Y/N: ")
        #     if newline.lower() == "n":
        #         return inputobject
        #     if not repeatable:
        #         value = input(prompt)
        #         inputobject[value] = value
        #         return inputobject

    print("""
    _______________________________________________________________
    This program will draw visualisations of simple L-system curves.
    Some things such as displacement/memorisation are not supported.
    _______________________________________________________________
    """)
    variables = input("Input variables: ").lower()
    start = input(
        f"Input starting variable or sequence (e.x {variables[0]} or {variables[0]}-{variables[random.randint(0, len(variables)-1)]}+{variables[random.randint(0, len(variables)-1)]}): ").lower()
    rules = clientinput(variables, False)
    iterations = int(input("How many iterations?: "))
    speed = 11  # int(input("How fast should we draw? (0-11): "))
    angle = int(input("Input angle: "))
    size = int(input("Input the desired size: "))

    chardefinitions = {}
    for obj in rules:
        for char in rules[obj]:
            if char not in chardefinitions:
                definition = input(f"""
        What does this character ({char}) mean?
        Input the definition according to this list:
            -Means draw forward: type "forward"
            -Means turn left: type "left"
            -Means turn right: type "right"
            -Means ignore: type "none"
        """).lower()
                chardefinitions[char] = definition
    if input("Press any key to draw. Type N to start over: ").lower() == "n":
        MainMenu()
    else:
        curveMain(chardefinitions, rules, angle,
                  start, iterations, speed, size)


def curveMain(definitions, rules, angle, start, levels, speed, size):
    definitions, rules, angle, start, size = definitions, rules, angle, start, size
    turtle.clear()
    turtle.speed(speed)
    screenwidth = 10000
    screenheight = 10000
    screen = turtle.Screen()
    screen.screensize(canvwidth=screenwidth,
                      canvheight=screenheight, bg="black")

    turtle.setup(width=1000, height=800, startx=640/2, starty=480/2)
    canvas = screen.getcanvas()
    turtle.color('orange', 'pink')

    def mapconstructor(rules, angle):
        for item in rules:
            if rules[item] == "forward":
                rules[item] = lambda a, char: RunCurve(a, False, char)
            if rules[item] == "left":
                rules[item] = lambda a, char: turtle.left(angle)
            if rules[item] == "right":
                rules[item] = lambda a, char: turtle.right(angle)
            if rules[item] == "none":
                rules[item] = lambda a, char: None

        return rules

    curverules = mapconstructor(definitions, angle)

    # Recursive function for drawing the sequence
    # Level for iterations, startSequence for long axioms and char for rule of given character
    def RunCurve(level, startSequence: bool = False, char: str = ""):
        if level == 0:
            turtle.forward(size)
            return

        for character in start if startSequence else rules[char]:
            curverules[character](level-1, character)

    def sequenceCheck():
        if len(start) > 1:
            RunCurve(levels, True)
        else:
            RunCurve(levels, False, start)

    sequenceCheck()

    match input("""
    Draw again -> R
    New curve -> A
    Quit -> Q
    """).lower():
        case "r":
            curveMain(definitions, rules, angle,
                      start, levels, speed, size)
        case "a":
            MainMenu()
        case "q":
            quit()


if __name__ == "__main__":
    MainMenu()
