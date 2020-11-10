from GalClass import *
from runClass import *
bgimg = "init.jpg"
music = "sweet.wav"
j = 0#文本正处于的行数
import pygame
from pygame.locals import *
from sys import exit
import time

def split():
    import re
    a = open('text.txt','r',encoding='utf-8')
    a = a.read()
    pat = r'^\d+?$'
    result = re.compile(pat,re.M)
    findall_result = result.split(a)
    return findall_result

def count():
    global j
    j += 1
    return j

def item_surface(i):#通过count函数返回数据构建一个新的字体surface
    text_surface = font.render(return_text[int(i)],True,(0,0,255))
    return text_surface

pygame.init()
screen = pygame.display.set_mode((640,395),0,32)
clock = pygame.time.Clock()

bg = pygame.image.load(bgimg).convert()
pygame.mixer.music.load(music)

font = pygame.font.Font("hksn.ttf",20)#初始化字体
return_text = split()#获取List方式的文本


#初始化对话框surface
surface = pygame.Surface((640,395))
surface.fill((255,255,255))
surface.set_alpha(150)#设置对话的透明度
text_surface = font.render(return_text[0],True,(0,0,255))
surface.blit(text_surface,(0,0))
pygame.mixer.music.play(-1)#音频重复播放
screen.blit(bg, (0, 0))
screen.blit(surface, (0, 300))
def draw(bgimg2,bg):
    bg2 = pygame.image.load(bgimg2).convert()
    width, height = bg.get_size()
    bg2_up = pygame.transform.scale(bg2, (width, height))
    screen.blit(bg2_up, (0, 0))
def play(music1):
    pygame.mixer.music.load(music1)
    pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            #页面切换功能
            '''bg2 = pygame.image.load(bgimg2).convert()
            width,height = bg.get_size()
            bg2_up = pygame.transform.scale(bg2,(width,height))
            screen.blit(bg2_up, (0, 0))'''
            #draw(bgimg2, bg)
            #文本框切换功能
            surface = pygame.Surface((640, 395))
            surface.fill((255, 255, 255))
            surface.set_alpha(150)
            i = count()
            text_surface= item_surface(i)

            #BGM切换功能
            '''pygame.mixer.music.load(music1)
            pygame.mixer.music.play(-1)'''
            #play(music1)
            surface.blit(text_surface, (0, 0))
            screen.blit(surface, (0, 300))
            time.sleep(0.2)
        clock.tick(5)
    pygame.display.update()
