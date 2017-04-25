#! /user/bin/python3
# -*- coding:utf-8 -*-

import pygame.ftfont


class Scoreboard():
    """显示各类信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示游戏信息"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示信息默认使用字体设置
        self.text_color = (255, 255, 255)
        self.font = pygame.ftfont.SysFont(None, 48)

        # 准备初始信息图像
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """将分数转换为一幅渲染的图像"""
        score_str = "{:,}".format(self.stats.score)
        # score_str = self.stats.score
        # score_str = str(score_str)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # 将得分显示在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)

    def prep_high_score(self):

        high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # 将最高分显示在屏幕顶部中央
