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
		self.ship_limit = 3

		# 子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 232, 221, 203
		self.bullets_allowed = 25

		# 外星人设置
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 1
		# fleet_direction为1时向右移动，为-1时向左移动
		self.fleet_direction = 1


