bag = ["sword", "healing potion", "teleportation scroll"]
for item in bag:
    print item

pick = raw_input("Which item do you pick?")
for ans in pick:
    print "You took the", pick
    break
else:
    print "Nothing? Are you sure?"
