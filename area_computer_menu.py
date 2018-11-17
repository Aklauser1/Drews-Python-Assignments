
def Menu():
    print("Welcome to the area computation tool!")
    print(" ")
    print("****** MENU ******")
    print("tri    Computer area of a triangle")
    print("trap   Computer area of a trapezoid")
    print("sqr    Compute area of a square")
    print("quit   Quit the tool")


def userInput():
    choice = input("Please enter your choice: ")
    while choice != "tri" and choice !="trap" and choice != "sqr" and choice != "quit":
        print("{0} is an invalid choice".format(choice))
        choice = input("Please enter your choice: ")
    return choice 
def main():
    Menu()
    choice = userInput()
    print("You chose: {0}".format(choice))
    
main()

    