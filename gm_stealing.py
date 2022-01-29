### Script written by Catpockets ###
### Automated Stealing #############

# README Before Use:
# This script requires you to have 2 bags and a stack of stealable items (preferably 10 items that weigh 1 stone each)
# Select 2 bags, and then select the item you with to practice with.
# This will then stack the two bags into eachother, fill the 2nd bag with the chosen item, then drop it on the ground to steal.DistanceTo
# After stealing, it will then put the stolen items back into the second bag until GM. 
# Doing it this way means you do not need a packhorse and the bags will avoid being wiped. 


def container1(): # Select bag One
    sourceContainer1 = Target.PromptTarget('Select 1st bag which to steal from:' )
    container1 = Items.FindBySerial( sourceContainer1 )
    return container1
    
def container2(): # Select bag Two
    sourceContainer2 = Target.PromptTarget('Select 2nd bag which to steal from:' )
    container2 = Items.FindBySerial( sourceContainer2 )
    return container2

def itemtosteal(): # Select item to steal
    sourceItem = Target.PromptTarget('Select item to steal. Best to use stackable objects:' )
    item = Items.FindBySerial( sourceItem )
    return item

def playerpos(): # Determine player location and return 3 point location in python list. 
    playerPos = str(Player.Position)
    stripCharacters = " ()"
    for character in stripCharacters:
        playerPos = playerPos.replace(character,"")
        coordinates = playerPos.split(",")
    return coordinates

# Set pause timer variable
pause = Misc.Pause( 500 )


# Gather item and player data #########################

bag1 = container1()

pause

bag2 = container2()

pause   
    
item1 = itemtosteal()
Misc.SendMessage("Selected Item: " + str(item1.Name))
pause


location = playerpos()
Misc.SendMessage("Player X-Loc: " + str(location[0]))
Misc.SendMessage("Player Y-Loc: " + str(location[1]))
Misc.SendMessage("Player Z-Loc: " + str(location[2]))

# Move Item into bag. 
bagContents = []



Misc.Pause(1000)
Items.Move(item1, bag2, -1)
Misc.Pause(1000)
Items.Move(bag2, bag1, 1)
Misc.Pause(1000)
Misc.SendMessage(bag2.Name)

Misc.SendMessage(bag2.Contains)

for fix in bag2.Contains:
    Misc.SendMessage(fix)
    bagContents.append(fix)
    
for item in bagContents:
    Misc.SendMessage("Bag test: " + str(item))