import random as ran
import pickle as pik
from time import sleep #이건 메세지 창 나올때 시간간격두기위해 필요한거 time.sleep() ()안에 숫자넣으면됨
# import os #이건 os.system('cls')라는  함수쓰는건데 이게 화면 넘어갈떄 글자 밀어내는게아니라 새로운화면 나오는것처럼 연출가능하데
import sys
from pygame import *

one_line: str = '-*-' * 10
rank: int = 1
current_upgraded: int = 0
fps: int = 30
running: bool = True

rank_table: dict = {1: '평범한', 2: '기묘한', 3: '이상한', 4: '고상한', 5: '비범한'}
stat: dict = {"str": 4, "dex": 4, "int": 4, "luk": 4, "atk": 5, "def": 1, "crt_chance": 0.0, "crt_multiply": 1.1}
moster: dict = {1: "슬라임", 2: "다람쥐"}#이거 몬스터 정보 써놓은거면 내가 나중에 바꾼다?

init() # pygame 초기화

display.set_caption("진우 키우기") # pygame title set
dis = display.set_mode((1000, 1000), 0, 32) #  window set
clock = time.Clock() # time setting
system_font = font.SysFont('굴림', 50)


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


    # A = input("선택:")
    # if A=="1":
    #     pass
    # elif A=="2":
    #     print("강화를 시작합니다.")
    #     print("강화방식을 선택해주십시오")
    #     time.sleep(0.8)
    #     print("1.안정적이지만 수치가 낮은 강화 2.위험하지만 수치가 높은 강화 3.평범한 강화")
    #     B = input("선택:")
    #     if B =="1":
    #         print("1.안정적이지만 수치가 낮은 강화를 선택하셨습니다.")
    #         print("강화를 시작합니다.")
    #         time.sleep(3)
    #         g = ran.randint(0,100)
    #         print(g)

    #         if g % 1.5 == 0:
    #             print("강화에 성공했습니다.\n게임을 시작합니다.")

    #         else:
    #             print("강화에 실패했습니다.\n게임을 시작합니다.")
    #     if B =="2":
    #         print("2.위험하지만 수치가 높은 강화를 선택하셨습니다.")
    #         print("강화를 시작합니다.")
    #         time.sleep(3)
    #         g = ran.randint(0,100)
    #         print(g)

    #         if g % 3 == 0:
    #             print("강화에 성공했습니다.\n게임을 시작합니다.")

    #         else:
    #             print("강화에 실패했습니다.\n게임을 시작합니다.")

    #     if B =="3":
    #         print("3.평범한 강화를 선택하셨습니다.")
    #         print("강화를 시작합니다.")
    #         time.sleep(3)
    #         g = ran.randint(0,100)
    #         print(g)

    #         if g % 2 == 0:
    #             print("강화에 성공했습니다.\n게임을 시작합니다.")

    #         else:
    #             print("강화에 실패했습니다.\n게임을 시작합니다.")



    # A = input("선택:")
    # if A=="1":
    #     print("당신은 전진합니다.")
    #     print(luk)
    #     if luk<=30:
    #         print("당신은 적과 조우합니다.")

    #     pass
    # elif A =="2":
    #     print("당신은 불길함을 느끼고 후퇴하기로 결정합니다.")
    #     pass #이거 pass말고 뒤로돌아가는거 추가하셈
    # elif A =="3":
    #     print("당신은 돌아가기로 결정합니다.")
    #     pass #이것도 뒤로돌아가는걸로 바꿔

class Button():
    
    def __init__(self,x,y,image,scale):
        
        width = image.get_width()
        
        height = image.get_height()
        
        self.image = transform.scale(image, (int(width*scale),int(height*scale)))
        
        self.rect =self.image.get_rect()
        
        self.rect.center=(x,y)
        
        self.clicked = False
     
    def draw(self):

        action = False

        pos=mouse.get_pos()

        if self.rect.collidepoint(pos):
            
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                
                
                self.clicked = True
                
                action = True
                
            if mouse.get_pressed()[0] == 0:
            
                self.clicked = False
            
        dis.blit(self.image,(self.rect.x,self.rect.y))
        
        return action

while running:
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    dis.fill((255, 255, 255))
    dis.blit(system_font.render("JINU IS DUMB", 1, (0, 0, 0)), (500, 500))
    
    display.flip()
    clock.tick(fps)





