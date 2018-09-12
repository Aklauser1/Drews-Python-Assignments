# create function for break in between stanzas 
def pause () :
    print ("")
# create function for short cheer that can be called to later
def shortCheer () :
    print("Go, team, go!")
    print("Defeat your foe.")
# create function for long cheer that can call short cheer and be called to later    
def longCheer () :
    shortCheer ()
    print("Simply the best,")
    print("Better than the rest.")
    shortCheer()
# create function that calls the three previous functions in a specific order to accomplish task 
def sing_fight_song () :
    shortCheer()
    pause()
    longCheer()
    pause()
    longCheer()
    pause()
    shortCheer()
#Calls final funciton to show fight song when program is ran 
sing_fight_song()
    