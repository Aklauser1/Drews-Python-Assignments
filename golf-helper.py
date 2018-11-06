print("Welcome to the Golf Club Helper!")
print("Tell me your situation, and I'll recommend a club")

onGreen = input("Did you hit it on the green (y/n)?")
distance = int(input("How far is the ball from the hole?"))

if onGreen == "y":
    print("I recommend using your Putter")
elif onGreen == "n":
    if distance >= 200:
        print("I recommend using your Driver")
    elif distance >= 140 and distance < 200:
        print("I recommend using your 5-Iron")
    elif distance >= 100 and distance < 140:
        print("I recommend using your 9-Iron")
    elif distance < 100:
        inSand = input("Is the ball in a sandtrap? (y/n)")
        if inSand == "y" :
            print("I recommend using your Sand Wedge")
        elif inSand == "n":
            print("I recommend using your Pitching Wedge")
                        