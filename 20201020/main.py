import random


def fight(x_hp, x_power, y_hp, y_power):
    my_final_hp = x_hp
    enemy_final_hp = y_hp
    roundq = 1
    while True:
        p_round = '第' + str(roundq) + '回合:'
        print(p_round)
        # 我方剩余血量
        my_final_hp = my_final_hp - y_power
        if my_final_hp > 0:
            print(f'敌人进攻：敌人干掉我{y_power}的血量，我还在坚持！双方情况：我方血量{my_final_hp},敌方血量{enemy_final_hp}')
        else:
            print(f'敌人进攻：敌人太厉害，我被干掉了，但是敌人也被我重创，敌人的血量还剩：{enemy_final_hp}')
            return 'we false'
        # 敌方剩余血量
        enemy_final_hp = enemy_final_hp - x_power
        if enemy_final_hp > 0:
            print(f'我方进攻：我给敌人造成了{x_power}点的伤害，我们还在僵持！双方情况：我方血量{my_final_hp},敌方血量{enemy_final_hp}')
        else:
            print(f'我方进攻：敌人虽然勇猛，但是我方勇猛杀敌，敌方被杀的丢盔弃甲,大败而归！我方血量{my_final_hp}')
            return "we win"
        roundq += 1


if __name__ == "__main__":

    # enemy_hp = [x for x in range(100, 1100)]
    while True:
        both_hp_info = [random.randint(800, 1000) for _ in range(2)]
        both_power_info = [random.randint(80, 100) for _ in range(2)]
        # a = random.choice(both_hp_info)
        # b = random.choice(both_hp_info)
        # c = random.choice(both_hp_info)
        # d = random.choice(both_hp_info)
        result = fight(both_hp_info[0], both_power_info[0], both_hp_info[1], both_power_info[1])

        if result == 'we win':
            print(result, '双方数据：', both_hp_info[0], both_power_info[0], both_hp_info[1], both_power_info[1])
            break
        else:
            print(result, '双方数据：', both_hp_info[0], both_power_info[0], both_hp_info[1], both_power_info[1])
            break
