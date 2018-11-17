import graphics as g
win = g.GraphWin ("My House", 500, 300)

wall = g.Rectangle(g.Point(100, 100), g.Point(300, 299))
wall.setFill("grey")
wall.draw(win)

door = g.Rectangle(g.Point(175, 230), g.Point(225, 299))
door.setFill("brown")
door.draw(win)

window = door.clone()
window.move(50, -95)
window.setFill("white")
window.draw(win)

windowLeft = window.clone()
windowLeft.move(-100, 0)
windowLeft.draw(win)

middleRoofLine = g.Point(200, 50)
roofLeft = g.Line(g.Point(100, 100), middleRoofLine)
roofRight = g.Line(middleRoofLine, g.Point(300, 100))
roofLeft.draw(win)
roofRight.draw(win)

sun = g.Circle(g.Point(400, 50), 40)
sun.setFill("yellow")
sun.draw(win)

textBox = g.Text(g.Point(400, 275), "My House")
textBox.draw(win)

win.getMouse()
fireText = "My House is on Fire!"
textBox.setText(fireText)
window.setFill("red")
door.setFill("red")
windowLeft.setFill("red")
