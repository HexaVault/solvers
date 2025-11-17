a = ""
print("This script will keep running till you input \"end\", at which point it will end")
print("Below is a list of module names, and in brackets, shorthands")
for value in ["Wires", "Button", "Hexadecimal (Hexa)", "Tiles", "Keypad", "Binary", "Mathematics (Math)", "Color Code (CC)",
              "Multi Buttons (Multi)", "Timing", "Morse Code (Morse)"]:
    print(value)
print("capitalisation is irrelevant, however make sure you spell correctly")

pos = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"]

def wires():
    wireCount = input("Wire count: "),
    if wireCount == "5":
        return "Cut the " + pos[["r", "g", "b", "y", "w"].index(input("Color of light (rgybw): ").lower())] + "wire"
    wireColors = input("Wire colors (rgybw, no spaces inbetween, i.e. rrbw): ")
    if wireCount == "4":
      if wireColors.count("g") == 0: return "Cut the first wire"
      if wireColors.count("b") == 0: return "Cut the second wire"
      if wireColors.count("w") == 0: return "Cut the third wire"
      return "Cut the fourth wire"
    if wireColors.count("r") == 0: return "Cut the first wire"
    if wireColors.count("w") != 0: return "Cut the second wire"
    return "Cut the third wire"

def button():
    col = input("Button color (rbgyw): ")
    txt = input("Button text: ")
    count = 4
    if txt == "abort":
        count = 3
    if col == "r":
        count = 2
    if (txt == "detonate" or txt == "deto") and col == "b":
        count = 1
    return "Press the button " + str(count) + "times, then press the " + ["up", "down"][(count-1)//2] + "arrow"

def hexadecimal():
    display = input("Type in the display, exactly as shown (incl spaces): ").split(" ")
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    return "String is:" +  letters[int(display[1], 16) - 97] + letters[int(display[0], 16) - 97] + letters[int(display[2], 16) - 97] + letters[int(display[3], 16) - 97]

def tiles():
    tile1 = input("color of left tile: ").lower()
    tile2 = input("color of right tile: ").lower()
    tileValues = ["ignore", "red", "yellow", "ignore 2", "ignore 3", "white", "pink", "ignore 4", "ignore 5", "green"]
    return tileValues.index(tile1) + tileValues.index(tile2)

def keypad():
    keypadValues = [0, 0, 0, 0]
    i = 0
    while i < 4:
        keypadValues[i] = int(input("Value on the " + str(i+1) + "th keypad: "))
        i += 1
    keypadRules = [
      [15, 20, 30, 10],
      [lambda x: x-10, lambda x: x * 2, lambda x: x * 3, lambda x: x - 10],
      [lambda x: x * 2, lambda x: x * 3, lambda x: x - 5, lambda x: x],
      [lambda x: x * 2, lambda x: x + 20, lambda x: x + 50, lambda x: x * 3]
    ]
    
    def intToOption(value):
        if value < 10: return 0
        if value > 10 and value < 20: return 1
        if value > 20 and value < 80: return 2
        return 3

    xVal = keypadRules[0][intToOption(keypadValues[0])]
    yVal = keypadValues[0]
    i = 1
    while i < 4:
        xVal = keypadRules[i][intToOption(keypadValues[i])](xVal)
        yVal += keypadValues[i]
        i += 1
    finalValue = xVal - (yVal/2)
    if finalValue < 0: return "Order: Top left, Top right, Bottom left, Bottom right"
    if finalValue < 20: return "Order: Top left, Top right, Bottom right, Bottom left"
    if finalValue < 50: return "Order: Bottom right, Bottom left, Top right, Top left"
    if finalValue < 90: return "Order: Bottom left, Top left, Bottom right, Top right"
    return "Order: Top right, Bottom left, Top left, Bottom right"

def binary():
    binaryVal = input("Binary (as 1010101): ")
    setBits = binaryVal.count("1")
    unsetBits = binaryVal.count("0")
    binaryVal = int(binaryVal, 2)
    if unsetBits == 0:
        return "Press the red button once, then the green button"
    if binaryVal % 64 == binaryVal and binaryVal > 1 % 2 == 1:
        return "Press the red button twice, then the green button",
    if binaryVal % 4 == 3:
        return "Press the red button thrice, then the green button"
    if binaryVal % 64 == binaryVal and binaryVal % 2 == 0:
        return "Press the red button quartice (4), then the green button"
    if unsetBits > 3:
        return "Press the red button septice (7), then the green button"
    if setBits > 5:
        return "Press the red button eight times, then the green button"
    return "Press the red button ten times, then the green button"

def math():
    display = input("Displayed value, including space: ")
    convOrder = ["h", "a", "d", "b", "e", "f", "g", "c", "i", "j"]
    print(int(str(convOrder.index(display[0])) + str(convOrder.index(display[1]))) * int(str(convOrder.index(display[3])) + str(convOrder.index(display[4]))))
  
def colorCode():
    lights = input("Light colors, as letters (rgbyw): ")
    letters = input("Letters: ")
    lightCount = 0; letterCount = 0
    # RGBYW
    letterValues = [1, 3, 2, 3, 4]; lightValues = [0, 0, 1, 2, 3]; order = ["r", "g", "b", "y", "w"]
    i = 0
    while i < 5:
        lightCount += lightValues[order.index(lights[i])]
        letterCount += letterValues[order.index(letters[i])]
        i += 1
    finalCount = letterCount - lightCount
    if finalCount <= 0:
        return "Press the green button",
    return "Press the red button " + str(finalCount) + " times, then press the green button"

def multiButtons():
    buttons = ["", "", "", "", "", ""]
    display = input("type in the 6 numbers shown on the display: ")
    if int(display[0]) < 6:
        buttons[0] = "red"
        buttons[3] = "orange"
    else:
        buttons[0] = "orange"
        buttons[3] = "red"
    if int(display[1]) < 6:
        buttons[1] = "yellow"
        buttons[4] = "green"
    else:
        buttons[1] = "green"
        buttons[4] = "yellow"
    if int(display[2]) < 6:
        buttons[2] = "blue"
        buttons[5] = "purple"
    else:
        buttons[2] = "purple"
        buttons[5] = "blue"
    finalOrder = [buttons[0], buttons[1], buttons[2]]
    if int(display[3]) < 7:
        finalOrder.append(buttons[4]); finalOrder.append(buttons[5]); finalOrder.append(buttons[3])
    elif int(display[4]) < 7:
        finalOrder.append(buttons[5]); finalOrder.append(buttons[4]); finalOrder.append(buttons[3])
    elif int(display[5]) > 5:
        finalOrder.append(buttons[3]); finalOrder.append(buttons[4]); finalOrder.append(buttons[5])
    else:
        finalOrder.append(buttons[3]); finalOrder.append(buttons[5]); finalOrder.append(buttons[4])
    returnString = "Press the buttons in the order: "
    for value in finalOrder:
        returnString += str(value) + " "
    return returnString

def timing():
    display = input("Timing display (no space): ")
    letterIndex = ["0", "1", "2", "b", "a", "5", "6", "c", "8", "d"]
    letters = letterIndex.index(display[0]) + letterIndex.index(display[1])
    numbers = int(display[1]) + int(display[2])
    finalValue = numbers * letters
    orderArray = ["white", 60, "red", 100, "yellow", 200, "green", 300, "blue", 400]
    i = 0
    while i < 6:
        if orderArray[2 * i - 1] > finalValue:
            return "Press the button when the light is " + orderArray[2 * i - 2]
        i += 1 

morseAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
regularAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def morse():
    morseStr = input("Morse String: (long: - | short: . | end of letter: \" \"): ")
    regularStr = ""
    try:
      for value in morseStr.split(" "):
          regularStr += regularAlphabet[morseAlphabet.index(value)]
    except:
        return "Morse string was invalid"
    serial = input("Serial number: ")
    serialCheck = "a6d8i1"; buttonChoices = "ybbbyyb"
    def letterToText(letter): return "yellow" if letter == "y" else "blue"
    i = 0
    while i < 6:
        if serial.count(serialCheck[i]) > 0: return "Input is " + regularStr + " and button to press is " + letterToText(buttonChoices[i])
        i += 1
    return "Input is " + regularStr + " and button to press is blue"

def div():
    i = 0
    while i < 3:
        divStr = input("Number on screen: ")
        newDivs = "FADBCEBCFEBCEAAD"
        try:
            divStr = int(divStr)
        except:
            print("Not a number")
            return
        bits = 0
        if (divStr % 2 == 0): bits += 1
        if (divStr % 3 == 0): bits += 2
        if (divStr % 5 == 0): bits += 8
        if (divStr % 7 == 0): bits += 4
        print("Press", newDivs[bits])
        i += 1
        
while a != "end":
    a = input("Module type: ").lower()
    if a == "wires": print(wires())
    if a == "button": print(button())
    if a == "hexadecimal" or a == "hexa": print(hexadecimal())
    if a == "tiles": print(tiles())
    if a == "keypad": print(keypad())
    if a == "binary": print(binary())
    if a == "math" or a == "mathematics": print(math())
    if a == "color code" or a == "cc": print(colorCode())
    if a == "multi buttons" or a == "multi": print(multiButtons())
    if a == "timing": print(timing())
    if a == "morse code" or a == "morse": print(morse())
    if a in ["divs", "div", "divisability", "divisibility"]: div()
