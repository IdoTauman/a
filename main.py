filePath = input("Path: ")

code = open(filePath, "r")

instructionList = {
    1: "add",
    2: "substract",
    3: "output",
    4: "start loop",
    5: "end loop",
    6: "move right",
    7: "move left",
}


class ArrayValueOutOfRange(Exception):
    # Raised when a value is higher than 255 or lower than 0
    pass


class ArrayPointerOutOfRange(Exception):
    # Raised when array pointer is not in the 10000 availible indexes
    pass


def ConvertInstructionsToCode(instructions):
    mainArr = [0 for x in range(10000)]
    ptrIndex = 0

    loopIndexes = []

    i = 0
    while i < len(instructions):
        instruction = instructions[i]

        if instruction == "a":
            try:
                mainArr[ptrIndex] += 1
                if mainArr[ptrIndex] > 255:
                    raise ArrayValueOutOfRange
            except ArrayValueOutOfRange:
                print(
                    f"Exception occured: Array value out of range at index {ptrIndex} with value {mainArr[ptrIndex]}"
                )

        elif instruction == 2 * "a":
            try:
                mainArr[ptrIndex] -= 1
                if mainArr[ptrIndex] < 0:
                    raise ArrayValueOutOfRange
            except ArrayValueOutOfRange:
                print(
                    f"Exception occured: Array value out of range at index {ptrIndex} with value {mainArr[ptrIndex]}"
                )

        elif instruction == 3 * "a":
            print(chr(mainArr[ptrIndex]))

        elif instruction == 4 * "a":
            loopIndexes.append(i)

        elif instruction == 5 * "a":
            if not mainArr[ptrIndex] == 0:
                i = loopIndexes[-1]
            else:
                loopIndexes.pop(-1)

        elif instruction == 6 * "a":
            try:
                ptrIndex += 1
                if ptrIndex > 9999:
                    raise ArrayPointerOutOfRange
            except:
                print(
                    f"Exception occured: Array pointer is not in the range of 0 - 9999, pointer index: {ptrIndex}"
                )

        elif instruction == 7 * "a":
            try:
                ptrIndex -= 1
                if ptrIndex < 0:
                    raise ArrayPointerOutOfRange
            except:
                print(
                    f"Exception occured: Array pointer is not in the range of 0 - 9999, pointer index: {ptrIndex}"
                )

        i += 1


def Compile(code=code):
    global instructionList

    lineArr = [x for x in code]
    instructions = []

    for line in enumerate(lineArr):
        for n in range(1, 8):
            if line[1] == n * "a" + "\n":
                instructions.append(n * "a")

    ConvertInstructionsToCode(instructions=instructions)


Compile(code)
