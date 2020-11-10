j = 0
p = 0
pic = []
import pygame
from pygame.locals import *
from sys import exit
import time
from GalClass import *
from runClass import *
from buttonclass import *
bgimg = "init.jpg"
music = "sweet.wav"
img = "SLButton.png"
load_img = "load.jpg"
save_img = "save.jpg"
sl_bgm = "SL_BGM.mp3"
freeze = False
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

choose = chooseindex()
update = runclass()
button = buttonclass()

pygame.init()
screen = pygame.display.set_mode((640,395),0,32)
clock = pygame.time.Clock()

bg = pygame.image.load(bgimg).convert()
pygame.mixer.music.load(music)

font = pygame.font.Font("hksn.ttf",16)
return_text = split()

surface_init = pygame.Surface((640,395))
surface_init.fill((255,255,255))
surface_init.set_alpha(150)#设置对话的透明度
init_surface = font.render(return_text[0],True,(0,0,255))
surface_init.blit(init_surface,(0,0))
pygame.mixer.music.play(-1)#音频重复播放

screen.blit(bg, (0, 0))
screen.blit(surface_init, (0, 300))

def button_setting():
	global j
	global freeze
	freeze = False
	j = j-1
	return j
while True:
	for event in pygame.event.get():
		pos = pygame.mouse.get_pos()
		if event.type == QUIT:
			exit()
		if event.type == MOUSEBUTTONDOWN:
			#i = count()
			print(freeze)
			print(j)
			click_point = event.dict['pos']
			save_rect = pygame.Rect((600,240),(40,20))
			back_rect = pygame.Rect((50,50),(60,60))
			if back_rect.collidepoint(click_point) and freeze:#进行返回判定
				button_setting()
			else:
				pass
			choose.set(return_index=return_text,num=j)
			return_Button = choose.chooseButton()

			if save_rect.collidepoint(click_point):
				freeze = True
				button.set(point=click_point,screen=screen)
				button.check_sl()

			if not freeze:
				return_Button = choose.chooseButton()

				if return_Button != []:

					first_text, seconde_text, first_num, seconde_num = return_Button
					button.set(first_button_text=first_text, seconde_button_text=seconde_text, button_img=img,
							   screen=screen, font=font, point=click_point, first_button_num=first_num,
							   seconde_button_num=seconde_num,now_button_num=j,return_text=return_text)
					#button.check_button()
					#将返回的button值
					button.set_button()

					j = button.check_button()

				elif return_Button == []:
					#return_bg = update.updateBG()
					#draw(return_BG,bg)
					
					i = count()
					choose.set(return_index=return_text, num=i)
					return_BG = choose.chooseBG()
					return_Text = choose.chooseText()
					return_BGM = choose.chooseBGM()

					surface= pygame.Surface((640,395))
					surface.fill((255,255,255))
					surface.set_alpha(150)
					update.set(bgimg=return_BG,init_bg=bg,bgmusic=return_BGM,index=return_Text,screen=screen,font=font,surface=surface)
					text_surface=update.updateText()
					update.updateBG()
					update.updateBGM()
					screen.blit(surface,(0,300))
				#surface.blit(text_suface,(0,0))
				else :
					pass
			else :
				pass
			time.sleep(0.2)
			clock.tick(8)

	pygame.display.update()