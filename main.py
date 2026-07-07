comment = ""
tmp: Position = None

def on_on_died():
    escape()
player.on_died(on_on_died)

def escape():
    gameplay.set_game_rule(SHOW_COORDINATES, True)
    gameplay.set_game_mode(CREATIVE, mobs.target(ALL_PLAYERS))
    player.execute(" ability @s worldbuilder true")

def on_travelled_walk():
    escape()
    superflat()
player.on_travelled(WALK, on_travelled_walk)

def superflat():
    global comment, tmp
    player.teleport(world(1000, 20, 1000))
    comment = "X"
    for index in range(1001):
        for index2 in range(1001):
            player.say("" + str(index2) + "/1000/" + str(index) + "1000")
            tmp = world(index + 1000, 20, index2 + 1000)
            if not (blocks.test_for_block(BEDROCK, tmp)):
                blocks.place(BEDROCK, tmp)