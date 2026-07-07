let comment = ""
let tmp: Position = null
player.onDied(function () {
    escape()
})
function escape () {
    gameplay.setGameRule(SHOW_COORDINATES, true)
    gameplay.setGameMode(
    CREATIVE,
    mobs.target(ALL_PLAYERS)
    )
    player.execute(
    " ability @s worldbuilder true"
    )
}
player.onTravelled(WALK, function () {
    escape()
    superflat()
})
function superflat () {
    player.teleport(world(1000, 20, 1000))
    comment = "X"
    for (let index = 0; index <= 1000; index++) {
        for (let index2 = 0; index2 <= 1000; index2++) {
            player.say("" + index2 + "/1000/" + index + "/1000")
            tmp = world(index + 1000, 20, index2 + 1000)
            builder.teleportTo(tmp)
            builder.place(BEDROCK)
        }
    }
}
