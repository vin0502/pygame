#! /user/bin/python3
# -*- coding:utf-8 -*-
# Author: vin
# 将游戏中的大量函数整理为一个模块，简化主体运行文件代码，增强其可读性，逻辑便于理解

import sys
import pygame
from bullet import Bullet
from alien import Alien
from random import randint
from time import sleep


def check_events(ai_settings, screen, ship, bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():				# 退出游戏操作
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):           # 按下按键时，控制飞船移动

	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left = True
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:                   # 按下空格键时，创建一颗子弹，并将其加入到编组bullets中
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_ESCAPE:                  # 按下ESC时，退出游戏
		sys.exit()


def check_keyup_events(event, ship):                      # 松开按键时不再移动
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left = False
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		ship.moving_down = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
	"""更新屏幕上的图像，并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	# screen.fill(ai_settings.bg_color)
	# ai_settings.bg_image(screen)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)

	pygame.display.flip()                             # 让最近绘制的屏幕可见


def fire_bullet(ai_settings, screen, ship, bullets):
	"""检查当前屏幕中子弹数目，若未达到上限则再发射一颗子弹"""
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def update_bullets(ai_settings, screen, ship, aliens, bullets):
	"""更新子弹"""
	bullets.update()                                  # 更新子弹位置

	for bullet in bullets.copy():                    # 删除到达屏幕外的子弹
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
	"""响应子弹与外星人的碰撞---实现子弹消灭外星人"""
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if len(aliens) == 0:                        # 屏幕中外星人全部消失时，新建一个外星人群
		create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
	"""计算每行可容纳多少个外星人"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
	"""计算屏幕可容纳多少行外星人"""
	available_space_y = (ai_settings.screen_height -(3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (1.5 * alien_height))
	return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number, number_of_aliens, number_aliens_x):
	"""创建一个外星人放在当前行"""
	random_aliens = number_of_aliens - number_aliens_x
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number + random_aliens * alien_width
	alien.rect.x = alien.x
	alien.rect.y = (alien.rect.height + 1.2 * alien.rect.height * row_number) - screen.get_rect().bottom * 0.5
	aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
	"""创建外星人群"""
	alien = Alien(ai_settings, screen)
	# number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_of_aliens = get_number_aliens_x(ai_settings, alien.rect.width)
	# number_aliens_x = randint(1,get_number_aliens_x(ai_settings, alien.rect.width))
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	for row_number in range(number_rows):
		number_aliens_x = randint(1, number_of_aliens)
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number, number_of_aliens, number_aliens_x)


def check_fleet_edges(ai_settings, aliens):
	"""外星人到达边缘时采取措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""改变整群外星人的方向"""
	# for alien in aliens.sprites():
	# 	alien.rect.y += self.ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
	"""更新外星人群中所有外星人位置"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
	for alien in aliens.copy():                    # 删除到达屏幕外的飞船
		if alien.rect.bottom >= ai_settings.screen_width:
			aliens.remove(alien)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	"""响应被外星人撞到的飞船"""
	# 将ships_left减1
	stats.ships_left -= 1

	# 清空外星人和子弹列表
	aliens.empty()
	bullets.empty()

	# 创建一群新的外星人，并将飞船放到屏幕底端中央
	create_fleet(ai_settings, screen, ship, aliens)
	ship.center_ship()

	# 暂停
	sleep(0.5)


