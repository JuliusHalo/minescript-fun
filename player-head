import system.lib.minescript as minescript
import time

def spawn_modern_dummy():
    texture = "eyJ0ZXh0dXJlIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDNiNDFhY2E1N2YyZGEzOGM4ZWRlNmM2ZDE0ZDRiM2U0MzU0ZTU3ODRjYTU0N2Q5ZTNmZDQyMzU3YjZhIn19"
    
    minescript.echo("§e[1/2] Summoning Armor Stand...")
    # a tag 'debug_fly' so we can target it
    summon_cmd = (
        'summon armor_stand ~ ~ ~ {'
        'Tags:["debug_fly"],'
        'Invisible:1b,ShowArms:1b,NoGravity:1b,'
        'CustomName:"Hi im test",'
        'CustomNameVisible:1b}'
    )
    minescript.execute(summon_cmd)

    # small pause to let the server register the entity
    time.sleep(0.1)

    minescript.echo("§e[2/2] Equipping Custom Head (1.21 Format)...")
    equip_cmd = (
        f'item replace entity @e[type=armor_stand,tag=debug_fly,limit=1,sort=nearest] armor.head with '
        f'minecraft:player_head[minecraft:profile={{properties:[{{name:"textures",value:"{texture}"}}]}}]'
    )
    minescript.execute(equip_cmd)
    minescript.echo("§aDone! You should see a head now.")

if __name__ == "__main__":
    spawn_modern_dummy()
