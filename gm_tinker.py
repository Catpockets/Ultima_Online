Def setitems()
    bag = Items.FindBySerial(Target.PromptTarget('Select Bag of Tools',150))
    Misc.SendMessage(bag.Name)
    tool = Items.FindBySerial(Target.PromptTarget('Select Tool',150))
    container = bag.Contains
    containerCount = Items.ContainerCount(bag.Serial,tool.ItemID)

# Def makelockpicks()
#     Misc.SendMessage('Tools Left: '+str(containerCount))
#     containerCount = containerCount
#     Items.UseItem(seriallist[i])
#     Misc.SendMessage(item)
#     Misc.Pause( 200 )
#     Gumps.WaitForGump(949095101, 10000)
#     Gumps.SendAction(949095101, 21)
#     Misc.Pause ( 1100 )   
    
setitems()
