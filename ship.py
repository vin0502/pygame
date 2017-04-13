import pygame

class Ship():

	def __init__(self,screen):
		"""初始化飞船并设置其初始位置"""
		self.screen = screen

		#加载飞船图像并或前期其外接矩形
		self.image = pygame.image.load('images/ship.png')
