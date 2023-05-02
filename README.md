# JINU's School Life!

---

## 진우의 학교생활 개발장

---

# 기본 정보

## 화면 사이즈

- 1280 x 720 HD

## ui 폰트

- [스위트](https://sunn.us/suite/)
- [엘리스 디지털 코딩](https://elice.io/elice/brand#elice_digital_coding)
---

### 버튼 생성법

- `a = Button([x], [y], [이미지 주소], 10)`
- `a.draw()`
- `a.draw()`는 리턴값으로 `boolean` 값을 뱉음 따라서 `if`문에 넣어 활용 가능하다.
- 버튼 자체에는 텍스트가 없다. 따라서 이미지 자체에 텍스트를 넣던가 따로 텍스트를 넣어줘야 한다.
- 텍스트를 넣을때는 항상 `draw()` 뒤에 텍스트가 오도록 작성한다.
```python
but_img = image.load('resourse\\images\\img_button.png')
start_but = Button(640, 500, but_img, 10) # 버튼객체 생성됨
if start_but.draw(): # 화면에 표시, 만약 버튼이 눌리면 작동
...
text(ui_font, 80, '시작', 100, 100, (0, 0, 0)) # 밑에 있는 객체가 나중에 생성되므로 버튼의 이미지를 뒤덮게 됨
```


### 텍스트 생성법

- `text(폰트, 사이즈, '글자', x, y, (r, g, b))`
- `(r, g, b)` 에는 미리 설정한 `튜플값` 대입 가능
```python
# 1번
red = (100, 0, 0)
text(digi_font, 100, '안녕', 100, 100, red)

# 2번
prefix = '멍청한'
rank_table = {1:'유약한', 2:'튼튼한'}
rank = 1
text(ui_font, 100, f'{prefix} {rank_table[rank]}', 100, 100, (0, 0, 0))
```

---

아래는 참고용으로 만든 게임

<details>

<summary> 열기 / 닫기 </summary>

## 벌레 잡기

```python
import pygame as pga

import random, pickle

#기본 정의/변수 선언
pga.init() 

pga.mixer.init()                                              

pga.display.set_caption('Bug Attack')                       

Window_Height = 900

Window_Width = 1600

state='main'

lo_state = ''

coin = 0

score = 0

high_score = 0

progress = 0

isRunning = True

pga.mouse.set_visible(True)

clock=pga.time.Clock()

boomspawn_time = 8

mosqispawn_time = 1

pinspawn_time = 20

surface = pga.display.set_mode((Window_Width,Window_Height))
#이미지/소리 정의
main_font = 'Project_Game\Fonts\PFStardust.ttf'

gungseoche = 'Project_Game\Fonts\ChosunCentennial_ttf.ttf'

BG=pga.image.load("Project_Game\\images\\BG.png")

maru = pga.image.load("Project_Game\\images\\marubadak.png")

shop = pga.image.load('Project_Game\images\shop.png')

m_pointer=pga.image.load("Project_Game\\images\\Pointer.png")

m_pointer2=pga.image.load('Project_Game\images\Pointer2.png')

m_pointer3=pga.image.load('Project_Game\images\Pointer3.png')
        
S_button=pga.image.load("Project_Game\images\start.png")

chi_button=pga.image.load("Project_Game\images\chi.png")

nor_button=pga.image.load("Project_Game\\images\\nor.png")

ssanai_button=pga.image.load("Project_Game\\images\\ssanai.png")

back_button=pga.image.load("Project_Game\\images\\back.png")

shopbu=pga.image.load('Project_Game\images\shopbu.png')

savebu=pga.image.load('Project_Game\images\save.png')

loadbu=pga.image.load('Project_Game\images\load.png')

buybu=pga.image.load('Project_Game\\images\\buy.png')

qmark=pga.image.load('Project_Game\images\qmark.png')

clicksound=pga.mixer.Sound('Project_Game\Musics\cilck.mp3')

bgm = pga.mixer.Sound('Project_Game\Musics\evolution.mp3')

boombug_image = pga.image.load('Project_Game\\images\\bombbug1.png')
    
boombug_image = pga.transform.scale(boombug_image,(90,90))

mosqi_image = pga.image.load('Project_Game\images\Mosquito1.png')

mosqi_image = pga.transform.scale(mosqi_image,(125,125))

pin_image = pga.image.load('Project_Game\images\pincer1.png')

pin_image = pga.transform.scale(pin_image,(100,100))
#이미지/소리 정의 끝
boombugs = []

mosqis = []

pins = [] 

bgm.set_volume(70.0)

bgm.play(-1)

pga.mouse.set_cursor((0,0),m_pointer)

skinset = 1

endtime = 3 #게임오버 대기시간

tim = 3 #준비시간

timer = 60 #게임 시간

white = (255,255,255)

pga.time.set_timer(pga.USEREVENT,1000) # 1초
#문자 띄우기
def text(font,size,text,x,y,color):
    
    fontset = pga.font.Font(font,size)
    
    fontsetrender=fontset.render(str(text),True,color)
    
    textrect = fontsetrender.get_rect()
    
    textrect.center = (x,y)
    
    surface.blit(fontsetrender,textrect)
#버튼 정의
class Button():
    
    def __init__(self,x,y,image,scale):
        
        width = image.get_width()
        
        height = image.get_height()
        
        self.image = pga.transform.scale(image, (int(width*scale),int(height*scale)))
        
        self.rect =self.image.get_rect()
        
        self.rect.center=(x,y)
        
        self.clicked = False
     
    def draw(self):

        action = False

        pos=pga.mouse.get_pos()

        if self.rect.collidepoint(pos):
            
            if pga.mouse.get_pressed()[0] == 1 and self.clicked == False:
                
                clicksound.play()
                
                self.clicked = True
                
                action = True
                
            if pga.mouse.get_pressed()[0] == 0:
            
                self.clicked = False
            
        surface.blit(self.image,(self.rect.x,self.rect.y))
        
        return action
#화면전환
def fadein():
    
    global Window_Height,Window_Width
    
    fadein=pga.Surface((Window_Width,Window_Height))
    
    for i in range(100):
        
        fadein.set_alpha(i/4)
        
        surface.blit(fadein,(0,0))
        
        pga.display.update()
        
        pga.time.delay(10)
#버튼 그리기    
chickenbutton=Button(Window_Width/2,1*Window_Height/5,chi_button,1)

ordrbutton=Button(Window_Width/2,2*Window_Height/5,nor_button,1)

ssanaibutton=Button(Window_Width/2,3*Window_Height/5,ssanai_button,1)

qmbutton=Button(Window_Width/12,4*Window_Height/5,qmark,1)

generalbutton=Button(Window_Width/2,3*Window_Height/4,S_button,1)

skinbutton=Button(Window_Width/9,8*Window_Height/9,shopbu,1)

backbutton=Button(Window_Width/15,Window_Height/9,back_button,1)

gamesbutton=Button(8*Window_Width/9,8*Window_Height/9,S_button,1)

savebutton=Button(3*Window_Width/8,8*Window_Height/9,savebu,1)

loadbutton=Button(5*Window_Width/8,8*Window_Height/9,loadbu,1)

buybutton1=Button(1.7*Window_Width/8,2.785*Window_Height/5,buybu,1)

buybutton2=Button(3.1*Window_Width/8,2.785*Window_Height/5,buybu,1)

buybutton3=Button(4.5*Window_Width/8,2.785*Window_Height/5,buybu,1)
#게임오버시 변수 초기화
def reset():
    global boombugs,mosqis,pins,score,pinspawn_time,mosqispawn_time,boomspawn_time,timer,tim
    
    boombugs = []

    mosqis = []

    pins = []

    tim = 3

    timer = 60
    
    boomspawn_time = 8

    mosqispawn_time = 1

    pinspawn_time = 20

    score = 0

while  isRunning:
    
    clock.tick(30)
    
    for e in pga.event.get(): #이벤트 정의부분
            
        if e.type==pga.KEYDOWN:
                
            if e.key==pga.K_ESCAPE: 
                    
                isRunning = False
                    
        if e.type==pga.QUIT:
                
            isRunning = False
        
        if e.type==pga.KEYDOWN and e.key!=pga.K_ESCAPE and state == 'main':   
             
                state='modeset'
                
                surface.blit(BG,(0,0))
        
        if e.type == pga.USEREVENT:
            
            if lo_state=='fight':
                
                tim -= 1
                
            if tim <= 0:
                
                timer -= 1
                
                boomspawn_time -= 1
                
                mosqispawn_time -= 1
                
                pinspawn_time -= 1
                
                if boomspawn_time == -1:
                    
                    boomspawn_time = 2
                
                if timer == 0:
                    
                    lo_state='die'
                    
            if lo_state=='die':
                
                endtime -= 1
                
                if endtime == 0:
                    
                    lo_state='house'
                    
                    endtime = 3
                    
                    tim=3
                    
                    timer=60
    
        if e.type == pga.MOUSEBUTTONDOWN and lo_state == 'fight':
            
            for (boombug, dx, dy) in boombugs:
                
                if boombug.collidepoint(e.pos):
                        
                    boombugs.remove((boombug,dx,dy))
                    
                    clicksound.play()
                        
                    score -= 4
                                       
            for (mosqi, dxm, dym) in mosqis:
                
                if mosqi.collidepoint(e.pos):
                        
                    mosqis.remove((mosqi,dxm,dym))
                    
                    clicksound.play()
                        
                    score += 3 
                    
                    coin += 2
                    
            for (pin , dxp, dyp) in pins:
                
                if pin.collidepoint(e.pos):
                    
                    pins.remove((pin,dxp,dyp))
                    
                    clicksound.play()
                    
                    score += 5
                    
                    coin += 4
                                       
    if state=='main':
        
        surface.blit(BG,(0,0))
        
        text(main_font,200,'벌레 때려잡기',Window_Width/2,Window_Height/5,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

        
        text(main_font,50,'아무 키나 입력해 시작',Window_Width/2,4*Window_Height/5,white)
        
    if state == 'modeset':
        
        if generalbutton.draw() and state != 'state':
            
            surface.blit(BG,(0,0))
            
            state='gene'
            
    if state == 'gene' :
        
        if chickenbutton.draw():
            
            fadein()
            
            state='dichic'
            
            lo_state = 'house'
            
        if ordrbutton.draw():
            
            fadein()
            
            state='diordr'
            
            lo_state='house'
            
        if ssanaibutton.draw():
            
            state='dissa'
            
            lo_state='house'
            
            fadein()
            
        #if qmbutton.draw():
            
        #    state='diqm'
            
        #    fadein()  
            
    if lo_state =='skin':
        
            surface.blit(shop,(0,0))
            
            text(gungseoche,70,'!바꿀때마다 코인 소비됨!',Window_Width/2,Window_Height/6,(200,5,5))
            
            if buybutton1.draw():
                
                skinset = 1
                
                pga.mouse.set_cursor((0,0),m_pointer)
                
            text(main_font,30,'0코인',1.7*Window_Width/8,2*Window_Height/5,(0,0,0))
            
            if buybutton2.draw():
                
                if coin >= 10000 and skinset != 2:
                    
                    skinset = 2
                    
                    pga.mouse.set_cursor((0,0),m_pointer3)
                    
                    coin -= 10000
                    
            if buybutton3.draw():
                
                if coin >= 5000 and skinset != 3:
                    
                    skinset = 3
                    
                    pga.mouse.set_cursor((0,0),m_pointer2)
                    
                    coin -= 5000
                    
            text(main_font,30,'5000코인',4.5*Window_Width/8,2*Window_Height/5,(0,0,0))
                    
            text(main_font,30,'10000코인',3.1*Window_Width/8,2*Window_Height/5,(0,0,0))
            
            text(main_font,30,'현재코인: '+str(coin),11*Window_Width/12,Window_Height/9,white)
            
            if backbutton.draw():
                
                fadein()
                
                lo_state='house'
                
    if lo_state =='house' :
        
        endtime = 3
        
        surface.blit(maru,(0,0))
        
        text(main_font,50,'최고점수 : '+ str(high_score),8*Window_Width/12,Window_Height/9,white)
        
        text(main_font,50,'현재코인: '+str(coin),2*Window_Width/12,Window_Height/9,white)
        
        if gamesbutton.draw():
            
            lo_state='fight'
            
        if skinbutton.draw():
            
            fadein()
            
            lo_state='skin'
            
        if savebutton.draw() and progress == 1:
            
            data = {
            
            'high_score' : high_score,
            
            'coin' : coin,
            
            'progress' : progress
            
            }
        
            with open('data.gyesanhighschool','wb') as f:
            
                pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        
        text(gungseoche,30,'누르면 데이터는 덮어 씌어짐',3*Window_Width/8,8.7*Window_Height/9,(0,0,0))
         
        if loadbutton.draw():
            
            with open('data.gyesanhighschool','rb') as f:
                
                data = pickle.load(f)
                
            high_score = int(data['high_score'])
                        
            coin = int(data['coin'])
                
    if lo_state == 'fight':
        
        surface.fill((0,0,0))
        
        text(main_font,30,'현재코인: '+str(coin),6*Window_Width/12,Window_Height/9,white)
        
        if tim > 0:
            
            text(main_font,50,'준비...'+str(tim),Window_Width/2,Window_Height/2,white)
        
        if tim <= 0:
            
            surface.blit(maru,(0,0))
            
            text(main_font,50,str(timer),11*Window_Width/12,Window_Height/9,white)
        
            text(main_font,50,'점수 : '+ str(score),Window_Width/12,Window_Height/9,white)
            
            if score >= high_score:
                
                high_score = score
                
            text(main_font,50,'최고점수 : '+ str(high_score),5*Window_Width/12,Window_Height/9,white)
            
            for (boombug, dx, dy) in boombugs:
                
                boombug.left += dx
                
                boombug.top += dy
                
            for (mosqi, dxm, dym) in mosqis:
                
                mosqi.left += dxm
                
                mosqi.top += dym
                
            for (pin , dxp, dyp) in pins:
                
                pin.left += dxp
                
                pin.top += dyp
                
            for (boombug, dx, dy) in boombugs:
                
                surface.blit(boombug_image, boombug)
                
            for (mosqi, dxm, dym) in mosqis:
                    
                surface.blit(mosqi_image, mosqi)
            
            for (pin, dxp, dyp) in pins:
                    
                surface.blit(pin_image, pin)
                
            if boomspawn_time == 0:
                
                boombug = pga.Rect(boombug_image.get_rect())
                        
                boombug.left = random.randrange(0,Window_Width)
                
                boombug.top = random.randrange(0,Window_Height)
                
                if state=='dichic':
                        
                    dx=random.randrange(-5,5,2)    
                                        
                    dy=random.randrange(-5,5,2)
            
                if state=='diordr':
                    
                    dx=random.randrange(-10,10,2)
        
                    dy=random.randrange(-10,10,2)
            
                if state=='dissa':
                
                    dx=random.randrange(-15,15,2)
                        
                    dy=random.randrange(-15,15,2)
                        
                boombugs.append((boombug,dx,dy))
            
            if mosqispawn_time <= 0:
                
                mosqi = pga.Rect(mosqi_image.get_rect())
                    
                mosqi.left = random.randrange(0,Window_Width)
                    
                mosqi.top = random.randrange(0,Window_Height)
                    
                if state=='dichic':
                        
                    dxm=random.randrange(-7, 7,5)  
                                   
                    dym=random.randrange(-7, 7,5)
            
                if state=='diordr':
                
                    dxm=random.randrange(-15, 15,4)
    
                    dym=random.randrange(-15, 15,4)
            
                if state=='dissa':
                
                    dxm=random.randrange(-30,30,4)
                        
                    dym=random.randrange(-30,30,4)
                        
                mosqis.append((mosqi,dxm,dym))

            if pinspawn_time <= 0:
                
                pin = pga.Rect(pin_image.get_rect())
                        
                pin.left = random.randrange(0,Window_Width)
                
                pin.top = random.randrange(0,Window_Height)
                
                if state=='dichic':
                        
                    dxp=random.randrange(-20,20,11)    
                                        
                    dyp=random.randrange(-20,20,11)
            
                if state=='diordr':
                    
                    dxp=random.randrange(-30,30,13)
        
                    dyp=random.randrange(-30,30,13)
            
                if state=='dissa':
                
                    dxp=random.randrange(-45,45,17)
                        
                    dyp=random.randrange(-45,45,17)
                        
                pins.append((pin,dxp,dyp))
                  
    if lo_state == 'die':
        
        surface.fill((0,0,0))
        
        progress = 1
        
        reset()
        
        text(main_font,100,'TIME OUT!',Window_Width/2,1*Window_Height/3,white)
        
        text(main_font,50,'메인화면으로 '+str(endtime)+'...',Window_Width/2,Window_Height/2,white)
        
        text(main_font,50,'최고점수 : '+ str(high_score),Window_Width/2,6*Window_Height/9,white)
        
    if state =='diqm' :
        
        surface.fill((0,0,0))
        
        text(gungseoche,50,'뭐 만들지 생각 안함 ㅎ',Window_Width/2,Window_Height/2,white)
        
        if backbutton.draw():
            
            state = 'modeset'
    
    pga.display.update()
    
pga.quit()
```

</details>
