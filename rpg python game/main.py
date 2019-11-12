from classes.game import Person


magic = [{  "name": "fireball", "cost": 50, "dmg" : 70},
         {  "name": "spark", "cost": 40, "dmg" : 65},
         {  "name": "rock throw", "cost": 70, "dmg" : 100}]

skill = [{  "name": "flex", "cost": 50, "dmg" : 70},
         {  "name": "shield bash", "cost": 40, "dmg" : 60}]

player = Person(100, 100, 100, 20, 10, magic, skill)
enemy = Person(200, 50, 50, 10, 20, magic, skill)

running = True
print("WILD ENEMY APPEARS")

while running:
    print("============================")
    print("You have", player.get_hp(), "hp,", player.get_mp(), "mp, and", player.get_stamina(),"stamina.")
    
    player.choose_action()
    print("Choose action:")
    answer = input()

    index = int(answer) - 1
    
    if 0 <= index < 3:
        print("You choose:", player.actions[index])

    if index == 0:
        dmg = player.generate_dmg()
        enemy.take_damage(dmg)
        print("============================")
        print("You did ", dmg, " dmg, Enemy hp:", enemy.get_hp() )
        
    elif index == 1:
        player.choose_magic()
        answer = input()

        index = int(answer) - 1
        print("You choose:", player.magic[index]["name"])
        
        if player.get_mp() < player.get_spell_mp_cost(index):
            print("No mana!")
            continue
        
        else:
            player.reduce_mp(player.get_spell_mp_cost(index)) 
            dmg = player.generate_spell_damage(index)
            enemy.take_damage(dmg)
            print("============================")
            print("You did ", dmg, " dmg, Enemy hp:", enemy.get_hp())
    
    elif index == 2 :
        player.choose_skills()
        answer = input()

        index = int(answer) - 1
        print("You choose:", player.skill[index]["name"])
        
        if player.get_stamina() < player.get_skill_cost(index):
            print("No stamina!")
            continue
        
        else:
            player.reduce_stamina(player.get_skill_cost(index)) 
            dmg = player.generate_skill_damage(index)
            enemy.take_damage(dmg)
            print("============================")
            print("You did", dmg, " dmg, Enemy hp:", enemy.get_hp())
    else:
        print("Choose wisely!")
        continue

    if enemy.get_hp() < 1:
        print("You win with", player.get_hp(), "hp left!")
        running = False
    elif player.get_hp() < 1:
        print("You died.")
        running = False
    else:
        enemy_dmg = enemy.generate_dmg()
        player.take_damage(enemy_dmg)
        print("Enemy hits you for", enemy_dmg, "hp.")


    
