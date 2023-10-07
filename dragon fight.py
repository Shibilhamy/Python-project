import random

players = ["Nishad", "Waleed", "Faisal", "Shibil", "Navas"]
actions = ["bravely", "cautiously", "fearlessly", "skillfully", "desperately"]
weapons = ["sword", "bow", "staff", "axe", "magic wand"]
dragons = ["fire-breathing dragon", "ice dragon", "poisonous dragon", "thunder dragon", "shadow dragon"]
outcomes = ["victorious", "defeated", "wounded", "terrified", "triumphant"]


player_health=100
dragon_health=100
for i in range(1,20):
    player = random.choice(players)
    action = random.choice(actions)
    weapon = random.choice(weapons)
    dragon = random.choice(dragons)
    outcome = random.choice(outcomes)
    print(player,action,'approached the fearsome',dragon ,'armed with a',weapon,'\nThey clashed in an epic battle, and in the end', player, 'emerged',outcome)
    a=random.randint(5,20)
    b=random.randint(5,20)
    player_health=player_health-a
    dragon_health=dragon_health-b
    print()
    print('player health --',player_health)
    print('dragon health --',dragon_health)
    print()
    if player_health<=0 or dragon_health<=0:
        if player_health<=0:
            print('Dragon wins the fight')
        else:
            print('Player wins the fight')
        exit()
