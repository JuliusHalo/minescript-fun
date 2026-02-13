import system.lib.minescript
import system.lib.minescript as m
import time
import math

def place_block_below_player():
    while True:
        x, y, z = m.player_position()
        x, y, z = math.floor(x), math.floor(y), math.floor(z)

        block_below = m.get_block(x, y-1, z)
        m.execute(f"setblock {x} {y-1} {z} minecraft:crying_obsidian")
        if any(target in str(block_below) for target in ["minecraft:crying_obsidian"]):
            m.execute(f"setblock {x} {y-1} {z} minecraft:barrier")
        TARGET_BLOCKS = ["minecraft:dirt", "minecraft:sand", "minecraft:gravel", "minecraft:stone", "minecraft:barrier"]
        if any(target in str(block_below) for target in TARGET_BLOCKS):
            m.execute(f"setblock {x} {y-1} {z} minecraft:shroomlight")
        time.sleep(0.1)
    while False:
        pass

if __name__ == "__main__":
#    m.echo("Starting the block placer script...")
    place_block_below_player()

# use # to comment out code that you don't want to run, or to add comments to your code.
# also when running the code do \place_block_below_player without .py on minecraft
# you can change the file name "place_block_below_player.py" to your liking, like "p.py" so its easier to execute "\p"
