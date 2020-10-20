
def fight(a, b):
    my_hp = 1000
    my_power = 200
    my_final_hp = my_hp - b
    enemy_final_hp = a - my_power

    if my_final_hp > enemy_final_hp:
        print("we win")
    elif my_final_hp < enemy_final_hp:
        print('we false')
    else:
        print('平局')


fight()
