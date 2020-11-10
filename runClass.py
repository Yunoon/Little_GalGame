import pygame
from pygame.locals import *
CHAR = u'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-=[]:;{}+_,.?!()@<>""''/\\'''
LINENUMBER = 35
init_X = 20
init_Y = 15
vsize = 20
pic = []

def sl_button(a):
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
	a.blit(save_surface,(600,240))
	a.blit(load_surface,(600,270))

class runclass(object):
	def __init__(self):
		self.bgimg = None
		self.init_bg = None
		self.bgmusic = None
		self.index = None

	def updateSLBG(self):
		bg2 = pygame.image.load(self.bgimg).convert()
		width, height = self.init_bg.get_size()
		bg2_up = pygame.transform.scale(bg2, (width, height))
		self.screen.blit(bg2_up, (0, 0))

	def updateBG(self):
		global pic
		if self.bgimg == "":
			last_pic = "".join(pic[len(pic) - 1])
			bg2 = pygame.image.load(last_pic).convert()
			width, height = self.init_bg.get_size()
			bg2_up = pygame.transform.scale(bg2, (width, height))
			self.screen.blit(bg2_up, (0, 0))
			a = self.screen
			sl_button(a)

		else:
			pic.append(self.bgimg)
			print(pic)
			bg2 = pygame.image.load(self.bgimg).convert()
			width, height = self.init_bg.get_size()
			bg2_up = pygame.transform.scale(bg2, (width, height))
			self.screen.blit(bg2_up, (0, 0))
			a = self.screen
			sl_button(a)

	def updateBGM(self):
		if self.bgmusic == "":
			pass
		else:
			pygame.mixer.music.load(self.bgmusic)
			pygame.mixer.music.play(-1)

	def updateText(self):
		def textToList2(text):
			width = 0
			textList = []
			textStr = ''
			for i in text:
				if i in CHAR or i.isdigit() or i.isspace():
					width += 1
				else:
					width += 2
				textStr += i
				if width >= LINENUMBER * 2 - 1:
					textList.append(textStr)
					textStr = ''
					width = 0
			textList.append(textStr)
			return textList
		if self.index == "":
			pass
		else:
			text = self.index
			return_index = textToList2(text)
			font = self.font
			for i in range(len(return_index)):
				now_index = return_index[i]
				Vsize = vsize
				pos_X = init_X
				pos_Y = init_Y + i*Vsize
				text_surface = font.render(now_index,True,(0,0,255))
				self.surface.blit(text_surface,(pos_X,pos_Y))

	def set(self,bgimg=None,init_bg=None,bgmusic=None,index=None,screen=None,font=None,surface=None):
		self.bgimg = bgimg
		self.init_bg = init_bg
		self.bgmusic = bgmusic
		self.index = index
		self.font = font
		self.surface = surface
		self.screen = screen
		