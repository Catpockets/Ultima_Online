def animaltarget():
    target = Target.PromptTarget('Select animal to tame:' )
    animal = Mobiles.FindBySerial(target)
    
    return animal
    
def release(animalSerial, renameAnimal):
    
    Misc.PetRename (animalSerial, renameAnimal)
    Misc.WaitForContext(animalSerial,2000)
    Misc.ContextReply(animalSerial, 8)
    Gumps.WaitForGump( 2426193729, 10000 )
    Gumps.SendAction( 2426193729, 2 )
    Misc.Pause(400)
    Player.HeadMessage(100, "Releasing Animal")

def tame(followers, animalSerial):
    
    Journal.Clear()
    Misc.Pause ( 500 )
    Player.UseSkill("Animal Taming")
    Target.WaitForTarget( 10000 )
    Target.TargetExecute(animalSerial)

    Misc.Pause ( 500 )
    if Journal.Search("You start to tame the creature.") == True:
        TamingStatus = True
        Misc.SendMessage("Taming Status: " + str(TamingStatus))
        
        while Player.Followers == followers and TamingStatus == True:
            
            Misc.SendMessage("Macro Loop Running")
            Misc.Pause(1000)
            if animalMobile.WarMode == True and peacemakingEbabled == True:
                peacemaking(animalSerial)
                Misc.Pause( 9000 )
                Player.UseSkill("Animal Taming")
            if Journal.Search('You fail to tame the creature.'):
                Player.UseSkill("Animal Taming")
                Misc.Pause(400)
                Target.TargetExecute(Target.GetLast())
                
            if Journal.SearchByType("You are too far away to continue taming.", "Regular" ) == True or Journal.SearchByType("That is too far away.", "Regular" ) == True:
                TamingStatus = False
                Player.HeadMessage(1100, "Macro Loop Ended")

def findinstrument():
    Player.HeadMessage(50, "Looking for instruments.")
    class instruments:
        Lute = 3763
        Drum = 3740
        LapHarp = 3762
        Tamborine = 3741

    playerBackPack = Items.FindBySerial( Player.Backpack.Serial )

    container = playerBackPack.Contains

    instrumentsInBag = []
    for item in container:
        if item.ItemID == instruments.Lute or item.ItemID == instruments.Drum or item.ItemID == instruments.LapHarp or item.ItemID == instruments.Tamborine: 
            instrumentsInBag.append(item.Serial)
    try:    
        Items.UseItem(instrumentsInBag[0])
    except:
        Player.HeadMessage(150, "No Instruments in Main Bag")

def peacemaking(animalSerial):
    Player.UseSkill( "Peacemaking" )
    if Journal.Search("What instrument shall you play?") == True:
        findinstrument()
    else:
        Target.WaitForTarget( 2000, True )
        Target.TargetExecute( animalSerial )     
        
        
######################################################################################
Player.HeadMessage(50, "Select Creature to Tame.") 

wait = Misc.Pause( 500 )
peacemakingEbabled = True # Set false if you do not one to use peacemaking during tames. 
animalMobile = animaltarget()
animalSerial = animalMobile.Serial

if animalMobile.WarMode == True and peacemakingEbabled == True:
    peacemaking(animalSerial)
    Misc.Pause( 9000 )
    


followers = CurrentFollowers = Player.Followers
currentTaming = Player.GetRealSkillValue('AnimalTaming')
currentLore = Player.GetRealSkillValue('AnimalLore')
renameAnimal = (Player.Name)  # Can change to to name the animal after your character

tame(followers, animalSerial)

wait

# Release Animals. To Disable release, comment out the following 2 lines with #
if Player.Followers > followers:
    release(animalSerial, renameAnimal)

# Pring taming gains above head of player
newTaming = Player.GetRealSkillValue('AnimalTaming')
tamingDifference = str(newTaming - currentTaming)
tamingTruncated = str(tamingDifference[0:3])
if newTaming - currentTaming > 0.1:
    Player.HeadMessage(50, 'Taming Gain: ' + (tamingTruncated))
    
# Pring lore gains above head of player   
newLore = Player.GetRealSkillValue('AnimalLore')
loreDifference = str(newLore - currentLore)
loreTruncated = str(loreDifference[0:3])
if newLore - currentLore > 0.1:
    Player.HeadMessage(75, 'Lore Gain: ' + (loreTruncated))

Gumps.WaitForGump(949095101, 10000)
Gumps.SendAction(949095101, 21)