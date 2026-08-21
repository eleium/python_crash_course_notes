# 游戏角色：
# 找一个你喜欢的游戏角色的位图。
# 创建一个类，将该角色绘制到屏幕中央。并将该位图的背景色设置为屏幕的背景色，或反之。
import pygame


class My_Ship:
    def __init__(self, fire_game):
        """初始化飞船，并设置初始位置"""
        self.screen = fire_game.screen
        self.screen_rect = fire_game.screen.get_rect()

        """加载飞船图像并获取其外接矩形"""
        self.image = pygame.image.load("ship_images/ship_large.bmp")
        self.rect = self.image.get_rect()

        """每艘新飞船都放到屏幕底部的中央"""
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """在指定的位置绘制飞船"""
        # bliteme:绘制
        self.screen.blit(self.image, self.rect)
