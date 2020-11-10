import pygame
from pygame.locals import *
from GalClass import *
from runClass import *
bgimg = "init.jpg"
choose = chooseindex()
update = runclass()
class slclass(object):
	def __init__(self):
		self.first_button_text = None
		self.seconde_button_text = None
		self.button_img = None
		self.screen = None
		self.font = None
		self.point = None
		self.firs_button_num = None
		self.seconde_button_num = None
	def set_button(self):
		font = self.font
		bg = pygame.image.load(self.button_img).convert_alpha()
		bg1 = pygame.image.load(self.button_img).convert_alpha()
		width,height = (200,50)
		bg_up = pygame.transform.scale(bg,(width,height))
		bg1_up = pygame.transform.scale(bg1,(width,height))
		#click_point = self.point
		rect_text = self.first_button_text
		rect_text1 = self.seconde_button_text
		text_surface = font.render(rect_text,True,(0,0,255))
		text_surface1 = font.render(rect_text1,True,(0,0,255))
		bg_up.blit(text_surface,(20,16))
		bg1_up.blit(text_surface1,(20,16))

		self.screen.blit(bg_up,[150,90])
		self.screen.blit(bg1_up,[150,170])
	def check_button(self):
		bg3 = pygame.image.load(bgimg).convert()
		rect = pygame.Rect((150,90),(200,50))
		rect1 = pygame.Rect((150,170),(200,50))
		if rect.collidepoint(self.point)==True:
			choose.set(return_index=self.return_text, num=int(self.first_button_num))
			return_BG = choose.chooseBG()
			return_Text = choose.chooseText()
			return_BGM = choose.chooseBGM()

			surface= pygame.Surface((640,395))
			surface.fill((255,255,255))
			surface.set_alpha(150)
			update.set(bgimg=return_BG,init_bg=bg3,bgmusic=return_BGM,index=return_Text,screen=self.screen,font=self.font,surface=surface)
			update.updateText()
			update.updateBGM()
			update.updateBG()
			self.screen.blit(surface,(0,300))
			now_num = int(self.now_button_num)+1
			return int(now_num)
		elif rect1.collidepoint(self.point)==True:
			choose.set(return_index=self.return_text, num=int(self.seconde_button_num))
			return_BG = choose.chooseBG()
			return_Text = choose.chooseText()
			return_BGM = choose.chooseBGM()

			surface= pygame.Surface((640,395))
			surface.fill((255,255,255))
			surface.set_alpha(150)
			update.set(bgimg=return_BG,init_bg=bg3,bgmusic=return_BGM,index=return_Text,screen=self.screen,font=self.font,surface=surface)
			update.updateText()
			update.updateBGM()
			update.updateBG()
			self.screen.blit(surface,(0,300))

			now_num = int(self.now_button_num)+1
			return int(now_num)
		else:
			now_num = self.now_button_num
			return_num = now_num
			return int(return_num)
	def sl_button(self):
		pygame.init()
		font = pygame.font.Font("hksn.ttf",16)
		save_surface = pygame.Surface((40,20))
		save_surface.fill((255,255,255))
		save_surface.set_alpha(150)
		surface_save = font.render("SAVE",True,(0,0,255))
		save_surface.blit(surface_save,(0,0))

		load_surface = pygame.Surface((40,20))
		load_surface.fill((255,255,255))
		load_surface.set_alpha(150)
		surface_load = font.render("LOAD",True,(0,0,255))
		load_surface.blit(surface_load,(0,0))
		self.screen.blit(save_surface,(600,240))
		self.screen.blit(load_surface,(600,270))

	def set(self,first_button_text=None,seconde_button_text=None,button_img=None,screen=None,font=None,point=None,first_button_num=None,seconde_button_num=None,now_button_num=None,return_text=None):
		self.first_button_text = first_button_text
		self.seconde_button_text = seconde_button_text
		self.button_img = button_img
		self.screen = screen
		self.font = font
		self.point = point
		self.first_button_num = first_button_num
		self.seconde_button_num = seconde_button_num
		self.now_button_num = now_button_num
		self.return_text = return_text