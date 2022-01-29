def findinstrument():
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
        Player.HeadMessage(150, 'No Instruments in Main Bag')

currentPeaceMaking = Player.GetRealSkillValue('Peacemaking')

while not Player.IsGhost and Player.GetRealSkillValue( 'Peacemaking' ) < Player.GetSkillCap( 'Peacemaking' ):

    Journal.Clear()
    Misc.Pause(200)
    Player.UseSkill( 'Peacemaking' )
    Misc.Pause(200)
    
    if Journal.Search('What instrument shall you play?') == True:
        findinstrument()
    else:
        Target.ClearLastandQueue()
        Misc.Pause(200)
        Target.WaitForTarget( 2000, True )
        Target.TargetExecute( Player.Serial )
        
        newPeaceMaking = Player.GetRealSkillValue('Peacemaking')
        PeaceMakingDifference = str(newPeaceMaking - currentPeaceMaking)
        PeaceMakingTruncated = str(PeaceMakingDifference[0:3])
        if newPeaceMaking - currentPeaceMaking > 0.1:
            Player.HeadMessage(50, 'PeaceMaking Gain: ' + (PeaceMakingTruncated))


    if ( Journal.SearchByType( 'You play hypnotic music, calming your target.', 'Regular' ) or
            Journal.SearchByType( 'You play your hypnotic music, stopping the battle.', 'Regular' ) or
            Journal.SearchByType( 'You attempt to calm everyone, but fail.', 'Regular' ) or
            Journal.SearchByType( 'You play hypnotic music, but there is nothing in range for you to calm.', 'Regular' ) or
            Journal.SearchByType( 'You attempt to calm your target, but fail.', 'Regular' ) ):
            Misc.Pause( 10200 )