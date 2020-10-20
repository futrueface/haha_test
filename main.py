import random


def fight(x_hp, x_power, y_hp, y_power):
    my_final_hp = x_hp - y_power
    enemy_final_hp = y_hp - x_power

    if my_final_hp > enemy_final_hp:
        return "we win"
    elif my_final_hp < enemy_final_hp:
        return 'we false'
    else:
        return '平局'


if __name__ == "__main__":
    enemy_hp = [random.randint(800, 1000) for _ in range(4)]

    # enemy_hp = [x for x in range(100, 1100)]
    roundq = 1
    while True:
        # a = random.choice(enemy_hp)
        # b = random.choice(enemy_hp)
        # c = random.choice(enemy_hp)
        # d = random.choice(enemy_hp)
        result = fight(enemy_hp[0], enemy_hp[1], enemy_hp[2], enemy_hp[3])
        p_round = '第' + str(roundq) + '回合:'
        if result == 'we win':
            print(p_round, result, '双方数据：', enemy_hp[0], enemy_hp[1], enemy_hp[2], enemy_hp[3])
            break
        else:
            print(p_round, result, '双方数据：', enemy_hp[0], enemy_hp[1], enemy_hp[2], enemy_hp[3])
        roundq += 1
        if roundq == 11:
            break
