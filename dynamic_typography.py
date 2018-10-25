messageInput = input("Enter your dynamic message: ")

import graphics as g
win = g.GraphWin ("dynamic", 1000, 200)

win.setBackground("light green")

xValue = 10
# used the ordinal value for the y value of the character 
for letters in messageInput:
    text = g.Text(g.Point(xValue,ord(letters)), letters)
    text.setSize(36)
    #the ordinal value also plays a role in the color intensity of the letter
    textColor = "#%02x%02x%02x" % (ord(letters)*int(.5), ord(letters),ord(letters)*2)
    text.setFill(textColor)
    text.setStyle("bold")
    xValue = xValue + 29
    text.draw(win)