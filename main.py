import random as ran
import pickle as pik

one_line: str = '-*-' * 10
rank: int = 1
current_upgraded: int = 0
running: bool = True

rank_table: dict = {1: '평범한', 2: '기묘한', 3: '이상한', 4: '고상한', 5: '비범한'}
stat: dict = {"str": 4, "dex": 4, "int": 4, "luk": 4, "atk": 5, "def": 1, "crt_chance": 0.0, "crt_multiply": 1.1}
moster: dict = {1: "슬라임", 2: "다람쥐"}
moster_info = {""}


class Slime:
    def __init__(self, hp, dei, rank, crt_chance):
        self.hp = hp
        self.rank = rank
        self.dei = dei
        self.crt_chance = crt_chance

    def health(self):
        hp = 10
        return hp

    def defence(self):
        dei = 3
        return dei

    def rank(self):
        rank = 1
        return rank

    def crt_chance(self):
        crt_chance = 10.0
        return crt_chance


def main_display():
    print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
{0}
|       진우 강화하기          |
{0}
|      +{2} {1} 진우         |
{0}
|1. 모험    2. 강화     3. 종료|
{0}""".format(one_line, rank_table[rank], current_upgraded))


def battle_filed():
    print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
{0}
|         이계의 전장         |
{0}
|1. 전진   2. 후퇴  3. 돌아가기|
""".format(one_line))


def main():
    main_display()
    while running:
        u = int(input('>> '))
        if u == 3:
            exit()
        elif u == 1:
            battle_filed()
            u = int(input('>> '))
            if u == 3:
                main()
            elif u == 1:
                monster_encounter = ran.randint(1, 2)
                if monster_encounter == 1:
                    s = Slime(10,3,1,10.0)
                    print(s.rank(), s.hp())


main()
