#! /user/bin/python3
# -*- coding:utf-8 -*-

import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg, title):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸及其他属性
        self.width, self.height = 200, 70
        self.button_color = (3, 38, 58)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮标签只需创建一次
        self.prep_msg(msg)
        self.title_msg(title)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        # self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.centery = self.rect.centery - 10

    def title_msg(self, title):
        self.font = pygame.font.SysFont(None, 25)
        self.title_image = self.font.render(title, True, self.text_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.rect.centerx
        self.title_image_rect.centery = self.rect.centery + self.msg_image_rect.height * 1/2

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        # self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.title_image, self.title_image_rect)
