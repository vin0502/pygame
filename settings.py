#! /user/bin/python3
# -*- coding:utf-8 -*-

class Settings():
	"""存储游戏的所有设置的类"""
	def __init__(self):
		#初始化游戏的设置
		#屏幕设置
		self.game_name = 'Alien Invasion 1.0'
		self.screen_width = 800
		self.screen_height = 640
		self.bg_corlor = (137, 157, 192)