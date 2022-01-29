### Author : Catpockets ###
### This script loops through player backpack to find all instruments and loops through make last function

def findMorter():
    morter = 3739    
    morterList = []
    for item in Player.Backpack.Contains:
        if item.ItemID == morter:
            morterList.append(item.Serial)
    return morterList

    
morter = findMorter()
for item in morter:
    Items.UseItem(item)
    
Misc.Pause( 500 )

Gumps.WaitForGump(949095101, 10000)
Gumps.SendAction(949095101, 21)