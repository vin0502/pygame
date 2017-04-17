import pygame


class Ship():

	def __init__(self, ai_settings, screen):
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 将飞船的位置属性改为float以便支持小数值的改变
		self.centerx = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)


		# 移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""根据移动标志调整飞船的位置，此处更新的是飞船center值，而不是rect"""
		if self.moving_right and self.rect.right < self.screen_rect.right:              # 限制飞船无法到达屏幕以外区域
			self.centerx += self.ai_settings.ship_speed_factor                           # 根据预设速度调整飞船位置
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.bottom > self.screen_rect.bottom * 2/3:
			self.bottom -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.ai_settings.ship_speed_factor

		# 根据centerx值更新rect值，此处rect只存储整数值
		self.rect.centerx = self.centerx
		self.rect.bottom = self.bottom

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)

