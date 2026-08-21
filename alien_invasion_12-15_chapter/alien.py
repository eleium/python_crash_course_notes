import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        """初始化外星人，并设置初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 导入外星人图片，设置rect属性：
        self.image = pygame.image.load("images/alienn.bmp")
        # pygame.image.load是pygame的加载图像的模式。
        self.rect = self.image.get_rect()
        # image.get_rect(): 取得图片的rect属性

        # 每一个外星人最初都在屏幕的左上角附近：
        # 在 Pygame 中，self.rect.x 和 self.rect.y 永远指的是这个矩形的左上角在屏幕上的位置。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精准水平位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """向左或右移动外星人"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
