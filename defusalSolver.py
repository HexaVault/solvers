a = ""
print("This script will keep running till you input \"end\", at which point it will end")
print("Below is a list of module names, and in brackets, shorter versions")
print("Wires")
print("Button")
print("Hexadecimal (Hexa)")
print("Tiles")
print("Keypad")
print("Binary")
print("Mathematics (Math)")
print("Color Code (CC)")
print("Multi Buttons (Multi)")
print("Timing")
print("Morse Code (Morse)")
print("capitalisation is irrelevant, however make sure you spell correctly")
while a != "end":
    a = input("Module type: ")
    a = str.lower(a)
    if a == "wires":
        i = input("Wire amount: ")
        if i == 5:
            g = input("Light color: ")
            g = str.lower(g)
            if g == "red":
                print("Cut the first wire")
            elif g == "green":
                print("Cut the second wire")
            elif g == "blue":
                print("Cut the third wire")
            elif g == "yellow":
                print("Cut the fourth wire")
            else:
                print("Cut the fifth wire")
        else:
            g = input("Wire Colors: ")
            g = str.lower(g)
            if i == "3":
                if g.count("red") == 0:
                    print("Cut the first wire")
                elif g.count("white") != 0:
                    print("Cut the second wire")
                else:
                    print("Cut the third wire")
            else:
                if g.count("green") == 0:
                    print("Cut the first wire")
                elif g.count("blue") == 0:
                    print("Cut the second wire")
                elif g.count("white") == 0:
                    print("Cut the third wire")
                else:
                    print("Cut the fourth wire")
    elif a == "button":
        z = input("First letter of colour text & button colour (as letter, no spaces): ")
        z = str.lower(z)
        if z == "db":
            print("Press the button once, then press the up arrow")
        elif z[1] == "r":
            print("Press the button twice, then press the up arrow")
        elif z[0] == "a":
            print("Press the button thrice, then press the down arrow")
        else:
            print("Press the button 4 times, then press the down arrow")
    elif a == "hexadecimal" or a == "hexa":
        b = input("Type in the display, exactly as shown (incl spaces): ")
        b1 = int(b[0]+b[1], 16) - 97
        b2 = int(b[3]+b[4], 16) - 97
        b3 = int(b[6]+b[7], 16) - 97
        b4 = int(b[9]+b[10], 16) - 97
        bo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        print(bo[b1] + bo[b2] + bo[b3] + bo[b4])
    elif a == "tiles":
        t1 = input("color of left tile: ")
        t2 = input("color of right tile: ")
        t1 = str.lower(t1)
        t2 = str.lower(t2)
        ti = ["ignore", "red", "yellow", "ignore 2", "ignore 3", "white", "pink", "ignore 4", "ignore 5", "green"]
        print(ti.index(t1) + ti.index(t2))
    elif a == "keypad":
        kIn = input("input the numbers, english reading order, with a space inbetween each number, and adding a leading 0 to single digit numbers: ")
        k1 = kIn[0] + kIn[1]
        k2 = kIn[3] + kIn[4]
        k3 = kIn[6] + kIn[7]
        k4 = kIn[9] + kIn[10]
        kOut1 = 0
        kOut2 = int(k1) + int(k2) + int(k3) + int(k4)
        kOut2 = kOut2 / 2
        if int(k1) == 10 or int(k1) == 20:
            kOut1 = 10
        elif int(k1) < 10:
            kOut1 = 15
        elif int(k1) < 20:
            kOut1 = 20
        else:
            kOut1 = 30
        if int(k2) == 10 or int(k2) == 20:
            kOut1 -= 10
        elif int(k2) < 10:
            kOut1 += 10
        elif int(k2) < 20:
            kOut1 *= 2
        else:
            kOut1 *= 3
        if int(k3) == 10 or int(k3) == 20:
            kOut1 = kOut1
        elif int(k3) < 10:
            kOut1 *= 2
        elif int(k3) < 20:
            kOut1 *= 3
        else:
            kOut1 -= 5
        if int(k4) == 10 or int(k4) == 20:
            kOut1 *= 3
        elif int(k4) < 10:
            kOut1 *= 2
        elif int(k4) < 20:
            kOut1 += 20
        else:
            kOut1 += 50
        kOut3 = kOut1 - kOut2
        if kOut3 < 0:
            print("Press the buttons in the order: Top left, Top right, Bottom left, Bottom right")
        elif kOut3 < 20:
            print("Press the buttons in the order: Top left, Top right, Bottom right, Bottom left")
        elif kOut3 < 50:
            print("Press the buttons in the order: Bottom right, Bottom left, Top right, Top left")
        elif kOut3 < 90:
            print("Press the buttons in the order: Bottom left, Top left, Bottom right, Top right")
        else:
            print("Press the buttons in the order: Top right, Bottom left, Top left, Bottom right")
    elif a == "binary":
        i = input("Input binary: ")
        x = 10
        if i.count("1") == 7:
            x = 9
        if i.count("1") > 5:
            x = 8
        if i.count("0") > 3:
            x = 7
        if (i[0] == "1") & (i[1] == "1") & (i[2] == "1") & (i[3] == "1"):
            x = 6
        if (i[0] == "1") & (i[1] == "1") & (i[2] == "1"):
            x = 5
        if (i[0] == "0") & (i[6] == "0"):
            x = 4
        if (i[0] == "1") & (i[1] == "1"):
            x = 3
        if (i[1] == "1") & (i[6] == "0"):
            x = 2
        if i.count("0") == 7:
            x = 1
        print(x)
    elif a == "math" or a == "mathematics":
        mIn = input("input what math shows (incl space): ")
        mi = ["h", "a", "d", "b", "e", "f", "g", "c", "i", "j"]
        print(int(str(mi.index(mIn[0])) + str(mi.index(mIn[1]))) * int(str(mi.index(mIn[3])) + str(mi.index(mIn[4]))))
    elif a == "color code" or a == "cc":
        ccIn1 = input("light colors (red = r, green = g), no spaces: ")
        ccIn2 = input("Letters given (no spaces: ")
        ccI1 = ["r", "g", "b", "y", "w"]
        i3 = 0
        ccOut1 = 0
        while i3 < 5:
            ccOut1 += ccI1.index(ccIn1[i3])
            if not ccI1.index(ccIn1[i3]) == 0:
                ccOut1 -= 1
            i3 += 1
        i3 = 0
        ccOut2 = 5
        ccI2 = ["r", "b", "g", "y", "w"]
        while i3 < 5:
            ccOut2 += ccI2.index(ccIn2[i3])
            if not ccI2.index(ccIn2[i3]) < 3:
                ccOut2 -= 1
            i3 += 1
        if not (ccOut2 > ccOut1):
            print("Press the green button, without pressing the red button")
        else:
            print("Press the red button", ccOut2 - ccOut1, "times, then press the red button")
    elif a == "multi buttons" or a == "multi":
        mbIn = input("type in the 6 numbers shown on the display: ")
        if int(mbIn[0]) < 6:
            mb1 = "red"
            mb4 = "orange"
        else:
            mb1 = "orange"
            mb4 = "red"
        if int(mbIn[1]) < 6:
            mb2 = "yellow"
            mb5 = "green"
        else:
            mb2 = "green"
            mb5 = "yellow"
        if int(mbIn[2]) < 6:
            mb3 = "blue"
            mb6 = "purple"
        else:
            mb3 = "purple"
            mb6 = "blue"
        if int(mbIn[3]) < 7:
            print("Press the buttons in the order:", mb1, mb2, mb3, mb5, mb6, mb4)
        elif int(mbIn[4]) < 7:
            print("Press the buttons in the order:", mb1, mb2, mb3, mb6, mb5, mb4)
        elif int(mbIn[5]) > 5:
            print("Press the buttons in the order:", mb1, mb2, mb3, mb4, mb5, mb6)
        else:
            print("Press the buttons in the order:", mb1, mb2, mb3, mb4, mb6, mb5)
    elif a == "timing":
        timIn = input("input what timing shows (incl space): ")
        timi = ["0", "1", "2", "b", "a", "5", "6", "c", "8", "d"]
        tim1 = timi.index(timIn[0]) + timi.index(timIn[1])
        tim2 = int(timIn[3]) + int(timIn[4])
        tim3 = tim1 * tim2
        if tim3 < 60:
            timeOut = "white"
        elif tim3 < 100:
            timeOut = "red"
        elif tim3 < 200:
            timeOut = "yellow"
        elif tim3 < 300:
            timeOut = "green"
        else:
            timeOut = "blue"
        print("Press the button when the light is", timeOut)
    elif a == "morse code" or a == "morse":
        mcIn = input("Morse string, with . as short, and - as long. Leave a space between each letter, which is signified by a medium (not long) gap: ")
        mcOut1 = mcIn.split(" ")
        mcI1 = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mcI2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        i7 = 0
        mcOut2 = ""
        while i7 < 5:
            mcOut2 = mcOut2 + mcI2[mcI1.index(mcOut1[i7])]
            i7 += 1
        mcIn2 = input("Type in the serial: ")
        if mcIn2.count("a") > 0:
            print("The word is", mcOut2, "and you should press the yellow button")
        elif mcIn2.count("6") > 0:
            print("The word is", mcOut2, "and you should press the blue button")
        elif mcIn2.count("d") > 0:
            print("The word is", mcOut2, "and you should press the blue button")
        elif mcIn2.count("8") > 0:
            print("The word is", mcOut2, "and you should press the blue button")
        elif mcIn2.count("i") > 0:
            print("The word is", mcOut2, "and you should press the yellow button")
        elif mcIn2.count("1") > 0:
            print("The word is", mcOut2, "and you should press the yellow button")
        else:
            print("The word is", mcOut2, "and you should press the blue button")
    elif a != "end":
        print("Not a valid module")

