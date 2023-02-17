import turtle
# https://en.wikipedia.org/wiki/L-system
# This program works as a self-similar fractal curve visual translator using L-system
# Input variables and rules to output a visual representation


def MainMenu():
    def clientinput(prompt: str, repeatable: bool):
        inputobject = {}
        while True:
            value = input(prompt)
            inputobject[value] = value
            newline = input("Input a second one? Y/N: ")
            if newline.lower() == "n":
                return inputobject
            if not repeatable:
                value = input(prompt)
                inputobject[value] = value
                return inputobject
    """This program will draw visualisations of simple L-system curves."""
    # start = input(
    #     "Input starting variable or starting sequence (e.x A or A-F-G): ")
    # iterations = int(input("How many iterations?: "))
    # speed = int(input("How fast should we draw? (0-11): "))
    # rules = clientinput(
    #     "Input rule. Example (A->*****) Where * are the rules for variable present: ", False)
    # angle = int(input("Input angle: "))
    # size = int(input("Input the desired size: "))
    start = "f-g-g"
    iterations = 2
    speed = 7
    rules = {
        "f-g+f+g-f": "f-g+f+g-f",
        "gg": "gg"
    }
    angle = 120
    size = 10

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
        """)
                chardefinitions[char] = definition
    if input("Press any key to draw. Type N to start over: ") == "N":
        MainMenu()
    else:
        curveMain(chardefinitions, rules, angle, start, iterations, speed, size)


def curveMain(definitions, rules, angle, start, levels, speed, size):
    definitions, rules, angle, start, size = definitions, rules, angle, start, size
    turtle.speed(speed)
    screenwidth = 10000
    screenheight = 10000
    screen = turtle.Screen()
    screen.screensize(canvwidth=screenwidth,
                      canvheight=screenheight, bg="black")

    turtle.setup(width=1000, height=800, startx=640/2, starty=480/2)

    turtle.color('orange', 'pink')
    def mapconstructor(rules, angle, start):
        for item in rules:
            if rules[item] == "forward":
                if item == start[0]:
                    rules[item] = lambda a: RunCurve(a, True)
                else:
                    rules[item] = lambda a: RunCurve(a, False)
            if rules[item] == "left":
                rules[item] = lambda a: turtle.left(angle)
            if rules[item] == "right":
                rules[item] = lambda a: turtle.right(angle)
        return rules

    curverules = mapconstructor(definitions, angle, start)

    # Recursive function for drawing the sequence
    # Level for iterations, is_a for leading character, startSequence for if the curve requires a start longer than one character
    def RunCurve(level, is_a: bool = True, startSequence: bool = False):
        if level == 0:
            turtle.forward(size)
            return

        if startSequence:
            for index, char in enumerate(start):
                curverules[char](level-1)
        
        for char in list(rules.items())[0][1] if is_a else list(rules.items())[1][1]:
            curverules[char](level-1)

    if len(start) > 1:
        RunCurve(levels, True, True)
    else:
        RunCurve(levels)
    
    turtle.done()


if __name__ == "__main__":
    MainMenu()
