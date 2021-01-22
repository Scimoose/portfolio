from classes.game import Person
from rich.console import Console
from rich.table import Table


console = Console()
# magic skills user can use in game
magic = [{"name": "fireball", "cost": 50, "dmg": 70},
         {"name": "spark", "cost": 40, "dmg": 65},
         {"name": "rock throw", "cost": 70, "dmg": 100}]
# skills user can use in game
skill = [{"name": "flex", "cost": 50, "dmg": 70},
         {"name": "shield bash", "cost": 40, "dmg": 60}]

player = Person(100, 100, 100, 20, 10, magic, skill)
enemy = Person(200, 50, 50, 10, 20, magic, skill)

console.print("\n [bold]WILD ENEMY APPEARS[/bold] \n")

while True:
    # table initialization
    table = Table(title="Stats", show_header=True, header_style="bold yellow")
    table.add_column("Character", style="dim", width=12)
    table.add_column("HP", style="dim", width=12)
    table.add_column("MP", justify="right")
    table.add_column("Stamina", justify="right")
    table.add_row("Player", str(player.get_hp()), str(player.get_mp()), str(player.get_stamina()))
    table.add_row("Enemy", str(enemy.get_hp()), str(enemy.get_mp()), str(enemy.get_stamina()))
    console.print(table)
    # additional information
    console.print("You have", player.get_hp(), "[bold red]hp [/bold red],", player.get_mp(),
          "[bold cyan] mp[/bold cyan], and", player.get_stamina(), "[bold green] stamina[/bold green]. \n")
    # which action is chosen?
    player.choose_action()
    console.print("\n Choose action:")
    answer = input()

    index = int(answer) - 1

    if 0 <= index < 3:
        console.print("You choose:", player.actions[index])
    # base attack logic
    if index == 0:
        dmg = player.generate_dmg()
        enemy.take_damage(dmg)
        console.print("\n============================\n")
        console.print("You did ", dmg, "[italic brown] dmg[/italic brown], Enemy hp:", enemy.get_hp())
    
    # magic logic
    elif index == 1:
        player.choose_magic()
        answer = input()

        index = int(answer) - 1
        console.print("You choose:", player.magic[index]["name"])

        if player.get_mp() < player.get_spell_mp_cost(index):
            console.print("No mana!")
            continue

        else:
            player.reduce_mp(player.get_spell_mp_cost(index))
            dmg = player.generate_spell_damage(index)
            enemy.take_damage(dmg)
            console.print("============================")
            console.print("You did ", dmg, "[italic brown] dmg[/italic brown], Enemy hp:", enemy.get_hp())
    
    # stamina logic
    elif index == 2:
        player.choose_skills()
        answer = input()

        index = int(answer) - 1
        console.print("You choose:", player.skill[index]["name"])

        if player.get_stamina() < player.get_skill_cost(index):
            console.print("No stamina!")
            continue

        else:
            player.reduce_stamina(player.get_skill_cost(index))
            dmg = player.generate_skill_damage(index)
            enemy.take_damage(dmg)
            console.print("============================")
            console.print("You did", dmg, "[italic brown] dmg[/italic brown], Enemy hp:", enemy.get_hp())
    
    # if user inputs something else than 1-3
    else:
        console.print("Choose wisely!")
        continue
    # rest - enemy taking damage, exit conditions
    if enemy.get_hp() < 1:
        console.print("You win with", player.get_hp(), "hp left!")
        input("Enter any key to exit \n")
        break
    elif player.get_hp() < 1:
        console.print("You died.")
        input("Enter any key to exit \n")
        break
    else:
        enemy_dmg = enemy.generate_dmg()
        player.take_damage(enemy_dmg)
        console.print("Enemy hits you for", enemy_dmg, "hp. \n")
