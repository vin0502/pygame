#! /user/bin/python3
# -*- coding:utf-8 -*-
import pygame


class Settings():
	"""存储游戏的所有设置的类"""
	def __init__(self):
		# 初始化游戏的静态设置
		# 屏幕设置
		self.game_name = 'Alien Invasion 1.0'
		self.screen_width = 800
		self.screen_height = 640
		self.bg_color = (137, 157, 192)

		# 飞船设置
		self.ship_limit = 3

		# 子弹设置
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 232, 221, 203
		self.bullets_allowed = 25

		# 外星人设置
		self.fleet_drop_speed = 1
		# fleet_direction为1时向右移动，为-1时向左移动
		self.fleet_direction = 1

		#以什么样的速度加快游戏
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""初始化随游戏速度变化的设置"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		# fleet_direction为1时向右移动，为-1时向左移动
		self.fleet_direction = 1

	def increase_speed(self):
		"""提高游戏速度"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
