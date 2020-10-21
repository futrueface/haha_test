import random


def fight(x_hp, x_power, y_hp, y_power):
    my_final_hp = x_hp
    enemy_final_hp = y_hp
    while True:
        my_final_hp = my_final_hp - y_power
        enemy_final_hp = enemy_final_hp - x_power
        if my_final_hp > 0 and enemy_final_hp > 0:
            print(f'敌人干掉我{my_final_hp}的血量，我还在坚持！我方血量{x_hp-my_final_hp}')
        elif my_final_hp <= 0:
            print(f'敌人太厉害，我被干掉了，但是敌人也被我重创，敌人的血量还剩：{enemy_final_hp}')
            return 'we false'
        elif enemy_final_hp <= 0:
            print(f'敌人虽然勇猛，但是在我方坚强抵抗下，被杀的丢盔弃甲！我方血量{my_final_hp}')
            return "we win"


if __name__ == "__main__":

    # enemy_hp = [x for x in range(100, 1100)]
    roundq = 1
    while True:
        enemy_hp = [random.randint(800, 1000) for _ in range(4)]
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
