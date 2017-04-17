#! /user/bin/python3
# -*- coding:utf-8 -*-
import pygame


class Settings():
	"""存储游戏的所有设置的类"""
	def __init__(self):
		# 初始化游戏的设置
		# 屏幕设置
		self.game_name = 'Alien Invasion 1.0'
		self.screen_width = 800
		self.screen_height = 640
		self.bg_color = (137, 157, 192)

		# 飞船设置
		self.ship_speed_factor = 1.5

		#子弹设置
		self.bullet_speed_factor = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 232, 221, 203
		self.bullets_allowed = 8

