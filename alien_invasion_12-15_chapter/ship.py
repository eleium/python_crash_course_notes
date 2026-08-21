import pygame
from pygame.sprite import Sprite



class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船，并设置初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """加载飞船图像并获取其外接矩形"""
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        """每艘新飞船都放到屏幕底部的中央"""
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中，存储一个浮点数：注意，这个x属性（横移属性）是自定义的，不是pygame定义的。
        self.x = float(self.rect.x)

        # 移动标志（飞船一开始不移动）
        self.moving_right = False
        # 当 self.moving_right = True 时，意味着飞船的大脑收到了指令：“保持向右走！”
        # 自己定义的一个bool值。按键按下，一直是true,抬起按键，变成false,不动了。
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置："""

        # 更新飞船的属性x值，而不是其外接矩形的属性x的值：
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            # rect.x 横向移动

        # 根据self.x更新rect对象：
        self.rect.x = self.x
        # 你的 self.x 是一个存在内存里的“数据”，但 Pygame 在画图时根本不认识 self.x！ 它只认识 self.rect 这个矩形框。
        # 即：pygame 画图只认rect.
        # 所以，你在 update() 的最后必须写上一句：self.rect.x=self.x

        # 把你自己算好的小数位置（self.x），四舍五入/取整回传给 Pygame 的坐标（self.rect.x）
        # rect强制取整。但是每次取整，将会丢失小数点的累计。
        # 用self.x=float()来记住所有整数和小数点，用rect只取最后一次的整数，最大限度的保持了数值最接近。
        # 这是平滑移动的最佳方法

    def blitme(self):
        """在指定的位置绘制飞船"""
        # bliteme:绘制
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将飞船放在屏幕底部的中央"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
