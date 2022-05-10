itemQualityToKeep = [
    'Vanquishing', 'Invulnerability',
    'Power/Supremely Accurate', 'Power/Exceedingly Accurate',

    ### Slayer Types ###
    # Slayer Group: Humanoid
    'Repond', 'Goblin', 'Orc', 'Ogre', 'Troll',
    # Slayer Group: Undead
    'Undead', 'Silver',
    # Slayer Group: Fey
    'Fey',
    # Slayer Group: Elemental
    'Elemental', 'Air', 'Vacuum', 'Blood', 'Earth', 'Fire', 'Flame', 'Poison', 'Snow', 'Summer', 'Water',
    # Slayer Group: Abyss
    'Demon', 'Exorcism', 'Daemon', 'Gargoyle', 'Balron',
    # Slayer Group: Arachnid
    'Arachnid', 'Scorpion', 'Spider', 'Terathan',
    # Slayer Group: Reptilian
    'Reptile', 'Reptilian', 'Dragon', 'Lizardman', 'Ophidian', 'Snake'
]

Player.HeadMessage(300,'Select source container to ID contents:')
bag1 = Items.FindBySerial(Target.PromptTarget('Select source container to ID contents:',300))
Items.UseItem(bag1)

Player.HeadMessage(300,'Select Bag for items to remove:')
bag2 = Items.FindBySerial(Target.PromptTarget('Select Bag for items to remove:',300))
Items.UseItem(bag2)

Player.HeadMessage(300,'Select bag for items to keep:')
bag3 = Items.FindBySerial(Target.PromptTarget('Select bag for items to keep: ',300))
Items.UseItem(bag3)
contents1 = bag1.Contains
idlist = []

for item in contents1:
    proplist = Items.GetPropStringList(item)
    for prop in proplist:
        if prop == 'Unidentified':
            idlist.append(item)

Player.HeadMessage(420, 'Total Items: ' + str(len(contents1)))
Player.HeadMessage(420, 'Total Items to ID: ' + str(len(idlist)))

for itemid in idlist:   
    Misc.Pause(1000)    
    Player.HeadMessage(10, 'Using item id: ' + str(itemid.Name))
    Player.UseSkill("Item ID")
    Target.WaitForTarget(2000, False)
    Target.TargetExecute(itemid)

Player.HeadMessage(420,'All items Identified')
Player.HeadMessage(420,'Starting Sort Operation')

keepitemlist = []
for keepitem in contents1:
    for properties in Items.GetPropStringList(keepitem):
        if properties in itemQualityToKeep:
            keepitemlist.append(keepitem)

for moveitemkeep in keepitemlist:
    Misc.Pause(400)
    Items.Move(moveitemkeep, bag3.Serial, -1)
            
Player.HeadMessage(300,'Keep Sort Operation Complete: Starting Discard Operation')
Misc.Pause(1000)
contents2 = bag1.Contains
for discarditem in contents2:
    #Misc.Pause(400)
    Misc.SendMessage(discarditem)
    Items.Move(discarditem, bag2.Serial, -1)    
    
Player.HeadMessage(300,'Discard Sort Operation Complete')
