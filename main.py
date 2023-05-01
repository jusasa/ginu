import random as ran
import pickle as pik
import time #이건 메세지 창 나올때 시간간격두기위해 필요한거 time.sleep() ()안에 숫자넣으면됨
import os #이건 os.system('cls')라는  함수쓰는건데 이게 화면 넘어갈떄 글자 밀어내는게아니라 새로운화면 나오는것처럼 연출가능하데

one_line: str = '-*-' * 10
rank: int = 1
current_upgraded: int = 0
running: bool = True

rank_table: dict = {1: '평범한', 2: '기묘한', 3: '이상한', 4: '고상한', 5: '비범한'}
stat: dict = {"str": 4, "dex": 4, "int": 4, "luk": 4, "atk": 5, "def": 1, "crt_chance": 0.0, "crt_multiply": 1.1}
moster: dict = {1: "슬라임", 2: "다람쥐"}#이거 몬스터 정보 써놓은거면 내가 나중에 바꾼다?
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
    A = input("선택:")
    if A=="1":
        pass
    elif A=="2":
        print("강화를 시작합니다.")
        print("강화방식을 선택해주십시오")
        time.sleep(0.8)
        print("1.안정적이지만 수치가 낮은 강화 2.위험하지만 수치가 높은 강화 3.평범한 강화")
        B = input("선택:")
        if B =="1":
            print("1.안정적이지만 수치가 낮은 강화를 선택하셨습니다.")
            print("강화를 시작합니다.")
            time.sleep(3)
            g = ran.randint(0,100)
            print(g)

            if g % 1.5 == 0:
                print("강화에 성공했습니다.\n게임을 시작합니다.")

            else:
                print("강화에 실패했습니다.\n게임을 시작합니다.")
        if B =="2":
            print("2.위험하지만 수치가 높은 강화를 선택하셨습니다.")
            print("강화를 시작합니다.")
            time.sleep(3)
            g = ran.randint(0,100)
            print(g)

            if g % 3 == 0:
                print("강화에 성공했습니다.\n게임을 시작합니다.")

            else:
                print("강화에 실패했습니다.\n게임을 시작합니다.")

        if B =="3":
            print("3.평범한 강화를 선택하셨습니다.")
            print("강화를 시작합니다.")
            time.sleep(3)
            g = ran.randint(0,100)
            print(g)

            if g % 2 == 0:
                print("강화에 성공했습니다.\n게임을 시작합니다.")

            else:
                print("강화에 실패했습니다.\n게임을 시작합니다.")






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


main()#010 6245 4059 배창득교수님(배터리특강)
