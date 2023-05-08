import random, pickle, sys, pygame
import pickle
from setting import *
from level import Level
# from time import sleep #이건 메세지 창 나올때 시간간격두기위해 필요한거 time.sleep() ()안에 숫자넣으면됨
# # import os #이건 os.system('cls')라는  함수쓰는건데 이게 화면 넘어갈떄 글자 밀어내는게아니라 새로운화면 나오는것처럼 연출가능하데


# # one_line: str = '-*-' * 10
# rank: int = 1
# current_upgraded: int = 0
# fps: int = 15
# upgrade_prob: int = 0
# exp: int = 0
# need_exp: int = current_upgraded * 1.3 + 500
# exx: float = exp/need_exp
# running: bool = True

# rank_table: dict = {1: '평범한', 2: '기묘한', 3: '이상한', 4: '고상한', 5: '비범한'}
# stat: dict = {"str": 4, "dex": 4, "int": 4, "luk": 4, "atk": 4, "def": 4, "crt_chance": 1.0, "crt_multiply": 1.1}
# moster: dict = {1: "슬라임", 2: "다람쥐"}#이거 몬스터 정보 써놓은거면 내가 나중에 바꾼다?
# loaction: dict = {1: '오프닝', 2: '메인메뉴', 3: '강화소',4: '학교'}
# whi = (255, 255, 255)
# blk = (0, 0, 0)
# pink = (231,113,202)
# blu = (7,153,231)
# ylw = (240, 216, 35)

# init() # pygame 초기화
# display.set_caption("진우 키우기") # pygame title set
# dis = display.set_mode((1280, 720), 0, 32) #  window set
# clock = time.Clock() # time setting
# digi_font = 'resourse\\fonts\\EliceDigitalCodingverH_Regular.ttf'
# ui_font = 'resourse\\fonts\\SUITE-Light.ttf'
# son_font = 'resourse\\fonts\\nanumsongulssi.ttf'
# son2_font = 'resourse\\fonts\\daluigeado.ttf'
# but_img = image.load('resourse\\images\\img_button.png')
# sq_img = image.load('resourse\\images\\sq_but.png')
# bg_img = image.load('resourse\\images\\bg.png')
# school_img = image.load('resourse\\images\\school.png')



# class Slime:
#     def __init__(self, hp, dei, rank, crt_chance):
#         self.hp = hp
#         self.rank = rank
#         self.dei = dei
#         self.crt_chance = crt_chance


# class Button():
    
#     def __init__(self,x,y,image,scale):
        
#         width = image.get_width()
        
#         height = image.get_height()
        
#         self.image = transform.scale(image, (int(width*scale),int(height*scale)))
        
#         self.rect = self.image.get_rect()
        
#         self.rect.center=(x,y)
        
#         self.clicked = False
     
#     def draw(self):

#         action = False

#         pos=mouse.get_pos()

#         if self.rect.collidepoint(pos):
            
#             if mouse.get_pressed()[0] == 1 and self.clicked == False:
                
#                 self.clicked = True
                
#                 action = True
                
#             if mouse.get_pressed()[0] == 0:
            
#                 self.clicked = False
            
#         dis.blit(self.image,(self.rect.x,self.rect.y))
        
#         return action



# start_but = Button(640, 400, but_img, 8)
# fight_but = Button(170, 610, but_img, 8)
# upgrade_but = Button(360, 610, but_img, 8)
# upgrade1_but = Button(640, 610, but_img, 8)
# exit_but = Button(80, 80, sq_img, 10)
# back_but = Button(80, 80, sq_img, 10)

# local = loaction[1]




# def text(fon,size,text,x,y,color):
    
#     fontset = font.Font(fon,size)
    
#     fontsetrender=fontset.render(str(text),True,color)
    
#     textrect = fontsetrender.get_rect()
    
#     textrect.center = (x,y)
    
#     # fontset.bold = True
    
#     dis.blit(fontsetrender,textrect)

# def set_gamma(img, gamma):
#     buf = img.get_buffer()
#     gmap = bytes( min(255, int(255*pow(i/255, gamma))) for i in range(256) )
#     buf.write(buf.raw.translate(gmap), 0)
#     return

# def fadein(t):
    
#     fadein=Surface((1280,720))
    
#     for i in range(t*10):
        
#         fadein.set_alpha(i/2.5)
        
#         dis.blit(fadein,(0,0))
        
#         display.flip()
        
#         time.delay(t)

# def opening():
#     dis.fill(pink)
#     text(son_font, 100, '진우의 학교 생활', 640, 200, blk)
#     if start_but.draw():
#         return 1
#     text(ui_font, 80, '시작',640, 400, blk)
#     return None

# def mainmenu():
#     global running, local
#     dis.blit(bg_img,(0,0))
#     if fight_but.draw():
#         local = loaction[4]
#         print(3)
#         return '학'
#     if upgrade_but.draw():
#         local = loaction[3]
#         print(4)
#         return '강'
#     if exit_but.draw():
#         running = False
#         quit()
#         sys.exit()
#     # text(digi_font, 50, f'+ {current_upgraded:>3} {rank_table[rank]} 진우',643,96.5,blk)
#     text(son2_font, 50, f'+ {current_upgraded:>3} {rank_table[rank]} 진우',645,90,whi)
#     text(son2_font, 50, f"힘 {stat['str']:>4} / 민첩 {stat['dex']:>4} / 지능 {stat['int']:>4} / 운 {stat['luk']:>4} / 공격력 {stat['atk']:>4}", 640,195, whi)
#     text(son2_font, 50, f"크리티컬 확률 {stat['crt_chance']:>4} / 방어력 {stat['def']:>4}", 640,245, whi)
#     text(son2_font, 50, f"경험치 {exx:>5.2f}%", 640,295, ylw)
#     text(son_font, 50, '등교', 170, 610, blu)
#     text(son_font, 50, '공부', 360, 610, ylw)
#     text(son_font, 50, '종료', 80, 80, pink)
#     return None

# def upgrade():
#     global current_upgraded, upgrade_prob, rank
#     dis.blit(bg_img,(0,0))
#     if upgrade_prob >= 69:
#             upgrade_prob = 70
#     if back_but.draw():
#         return '3'
#     if upgrade1_but.draw():
#         ra = ran.randint(1,100)
#         d = pow(stat["luk"], 1/3) * (ra / 100) + ra
#         if d >= upgrade_prob:
#             upgrade_prob += 7
#             current_upgraded += 1
#         if d < upgrade_prob:
#             upgrade_prob -= 7
#             current_upgraded -= 1
#         print(d,100- upgrade_prob, current_upgraded)
#     text(son2_font, 50, f'+ {current_upgraded:>3} {rank_table[rank]} 진우',645,90,whi)
#     text(son_font, 50, '공부 성공 확률 : {0:>3}%'.format(100 - upgrade_prob),640,245,pink)
#     text(son2_font, 80, '공부', 640, 600, blu)
#     text(son_font, 40, '뒤로', 80, 80, pink)
#     return None
    
# def school():
#     dis.blit(school_img,(0,0))
#     if back_but.draw():
#         return '3'
#     text(son2_font,50,'뒤로',80,80,whi)
#     return None


# while running:
#     for e in event.get():
#         if e.type == QUIT:
#             quit()
#             sys.exit()
#         if e.type == KEYDOWN:
#             if e.key == K_ESCAPE:
#                 quit()
#                 sys.exit()
#     if local == loaction[1]:
#         if opening() == 1:
#             fadein(5)
#             local = loaction[2]
#     if local == loaction[2]:
#         if mainmenu() == '학':
#             print(4444)
#             local = loaction[4]
#         if mainmenu() == '강':
#             print(3333)
#             local = loaction[3]
#     if local == loaction[3]:
#         if upgrade() == '3':
#             local = loaction[2]
#     if local == loaction[4]:
#         if school() == '3':
#             local = loaction[2]
#     display.flip()
#     clock.tick(fps)

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.level = Level()
        
    def run(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run() 
