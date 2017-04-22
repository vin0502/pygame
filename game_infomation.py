#! /user/bin/python3
# -*- coding:utf-8 -*-

import pygame.ftfont


class infomation():
	"""显示各类信息的类"""

	def __init__(self, ai_settings, screen, stats):
		"""初始化显示游戏信息"""
		self.screen = screen
		self.screen_rect = screen.get_rect
		self.ai_settings = ai_settings
		self.stats = stats

		# 显示信息默认使用字体设置
		self.text_corlor = (30, 30, 30)
		self.font = pygame.ftfont.SysFont(None, 48)

		# 准备初始信息图像
		self.prep_info()

