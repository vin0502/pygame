#! /user/bin/python3
# -*- coding:utf-8 -*-
# Author: vin

import sys
import os
import pygame
from settings import Settings

#创建游戏主体--窗口

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.game_name)

	#开始游戏的主循环
	while True:

		#监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:     #点击X以退出游戏
				sys.exit()

		#每次循环时都重绘屏幕
		screen.fill(ai_settings.bg_corlor)
		#让最近绘制的屏幕可见
		pygame.display.flip()


run_game()