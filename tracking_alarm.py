########################
### Writen by Ridian ###
########################

# This script will use the tracking skill to see if anyone is approaching. If it picks up something, it will
# then spam the names of characters to party to work as an alarm. According to Tony on discord, this does not count as 
# dualboxxing on UO Discord in PVP as of 2/5/2022.

# Pull tracking gump data
trackinggump = 2976808305
Player.UseSkill("Tracking")
Gumps.WaitForGump(trackinggump, 10000)
Gumps.SendAction(trackinggump, 4)
Misc.Pause(400)
currentgump = Gumps.CurrentGump( )

data = Gumps.LastGumpGetLineList( )

# List out names for the script to ignore. 
list = ['Foxglove', 'Rabies', 'Ridian', 'Ravison', 'DarkSin', 'Sindarwin', 'LightSin', 'Sindar', 'Ravison']

# Add *** to either end of the names found to put special emphisis on characters that are known threats. 
blacklist = []

# Loop through list and push data to party chat. 
for i in data:
    if i not in list:
        Player.ChatParty(i)
    if i in blacklist:
        Player.ChatParty("***" + str(i) + "***")

Misc.Pause( 10200 )
