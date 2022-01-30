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

Misc.SendMessage(tinker)
for item in tinker:
    Items.UseItem(item)
    
Misc.Pause( 500 )

