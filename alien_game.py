#! /user/bin/python3
# -*- coding:utf-8 -*-
# Author: vin

import sys
import os
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

# 创建游戏主体--窗口


def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.game_name)

	bg = pygame.image.load('images/bg_image.jpg')

	# 创建一艘飞船
	ship = Ship(ai_settings, screen)
	# 创建一个用于存储子弹的编组
	bullets = Group()
	aliens = Group()
	# 创建外星人
	gf.create_fleet(ai_settings, screen, aliens)

	# 开始游戏的主循环
	while True:
		# 绘制背景
		screen.blit(bg, (0, 0))

		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
