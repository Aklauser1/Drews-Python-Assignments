import graphics as g
win = g.GraphWin ("My House", 500, 300)
# made a square function to use with the windows, door, and wall
def square(x1, y1, x2, y2, fill):
    square = g.Rectangle(g.Point(x1, y1), g.Point(x2, y2))
    square.setFill(fill)
    square.draw(win)
# made a bird function to place a bird wherever I want
def bird(x1, y1):
    rightWing = g.Line(g.Point(x1 - 15 , y1 - 15), g.Point(x1, y1))
    leftWing = g.Line(g.Point(x1, y1), g.Point( x1 + 15 , y1 - 15))
    rightWing.setFill("blue")
    leftWing.setFill("blue")
    rightWing.draw(win)
    leftWing.draw(win)
# called my specialized functions
wall = square(100, 100, 300, 299, "grey")
door = square(175, 230, 225, 299, "brown")
windowRight = square(225, 135, 275, 204, "white")
windowLeft = square(125, 135, 175, 204, "white")
bird1 = bird(50, 75)
bird2 = bird(75, 50)
bird3 = bird(85, 85)
# I did not make a function for roof, because it would not be productive to do so
middleRoofLine = g.Point(200, 50)
roofLeft = g.Line(g.Point(100, 100), middleRoofLine)
roofRight = g.Line(middleRoofLine, g.Point(300, 100))
roofLeft.draw(win)
roofRight.draw(win)
# I did not make a function for sun, because it would not be productive to do so
sun = g.Circle(g.Point(400, 50), 40)
sun.setFill("yellow")
sun.draw(win)

textBox = g.Text(g.Point(400, 275), "My House")
textBox.draw(win)

win.getMouse()
fireText = "My House is on Fire!"
textBox.setText(fireText)
door = square(175, 230, 225, 299, "red")
windowRight = square(225, 135, 275, 204, "red")
windowLeft = square(125, 135, 175, 204, "red")
