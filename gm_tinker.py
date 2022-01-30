### Author : Catpockets ###
### This script loops through player main backpack to find all Tinker Tools and loops through make last function

def findTinker():
    tinker = [7864, 7868]
    tinkerList = []
    for item in Player.Backpack.Contains:
        if item.ItemID in tinker:
            tinkerList.append(item.Serial)
    return tinkerList

    
tinker = findTinker()
Misc.SendMessage(len(tinker))
for item in tinker:
    Items.UseItem(item)
    Misc.Pause( 1500 )
    if len(tinker) < 2:
        Misc.SendMessage('Making Tinker Tools')
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 23)
    else:
        Misc.SendMessage('Making Lock Picks')
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 121)
            
            