def findContainer():
    Player.HeadMessage(150,"Select Container")
    container = Items.FindBySerial(Target.PromptTarget("Select Container",150))
    if container.IsContainer == True:
        Player.HeadMessage(20, str(container.Name))
        return container
    else:
        Player.HeadMessage(20, str("Container not Selected"))
        
def findWeapon(container):
    Player.HeadMessage(50, "Looking for weapons.")
    class weapon: # Add weapons to this list using item id
        warfork = 5125
        katana = 5119
        dagger = 3992
        kryss = 5121
        longsword = 3937
        broadsword = 3934
    weaponlist = []   
    
    for item in container.Contains:
        
        if item.ItemID == weapon.warfork or item.ItemID == weapon.katana or item.ItemID == weapon.dagger or item.ItemID == weapon.kryss or item.ItemID == weapon.longsword or item.ItemID == weapon.broadsword:
            Misc.SendMessage(item.Name, 11 )
            weaponlist.append(item)
    return weaponlist
    
def findBottles():
    bottleID = 3854    
    Player.HeadMessage(50, "Looking for bottles")
    bottles = []
    
    backpack = Player.Backpack.Contains
    for item in backpack:
        if item.ItemID == bottleID:
            bottles.append(item)
            Misc.SendMessage(item)
            
    return bottles

def findPoisons():
    poisonID = 3850        
    Player.HeadMessage(50,"Looking for poison")
    poisons = []
    
    backpack = Player.Backpack.Contains
    for item in backpack:
        if item.ItemID == poisonID:
            poisons.append(item)
            Misc.SendMessage(item)
    return poisons

def findKegs():

    kegID = 6464   
    Player.HeadMessage(50,"Looking for kegs")
    kegs = []
    backpack = Player.Backpack.Contains
    for item in backpack:
        if item.ItemID == kegID:
            kegs.append(item)
            Misc.SendMessage(item)
    return kegs   
    
container = findContainer()
Misc.Pause( 400 )
weapons = findWeapon(container)
Misc.Pause( 400 )
poisons = findPoisons()
Misc.SendMessage("---")
kegs = findKegs()


for weapon in weapons:
    poisons = findPoisons()

    for poison in poisons:
        poisonCount = 0 + poison.Amount
        while poisonCount == 1:
            Misc.SendMessage("Loop Running")
            Misc.Pause( 1000 )
            Misc.SendMessage("Poisons Left: " + str(poisonCount))
            if poisonCount == 1:
                for keg in kegs:
                    Player.HeadMessage(150, "Using Keg")
                    Items.UseItem(keg)
            if poisonCount > 0:
                
                Player.UseSkill("Poisoning")
                Target.WaitForTarget(2000,False)
                Target.TargetExecute(poison)
                Misc.Pause(200)
                Target.WaitForTarget(2000,False)
                weaponpoisoned = Items.FindBySerial(weapon.Serial)
                Target.TargetExecute(weaponpoisoned.Serial)
                Misc.SendMessage("Poisoning: " + str(weaponpoisoned))
                Player.HeadMessage(55,"Poisoning: " + str(weapon))
                Misc.Pause( 10200 )