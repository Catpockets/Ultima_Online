item = Items.FindBySerial(Target.PromptTarget("Select an object"))
Misc.SendMessage("Item Name: " + str(item.Name))
Misc.SendMessage("Item ID: " + str(item.ItemID))
Misc.SendMessage("Item Serial: " + str(item.Serial))