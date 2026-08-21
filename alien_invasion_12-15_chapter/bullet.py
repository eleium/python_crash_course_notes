import sys
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船发射的子弹的类"""

    def __init__(self, ai_game):
        """在飞船的当前位置创建一个子弹对象"""
        super().__init__()
        #继承父类Sprite,如何知道这个父类的属性和方法？为啥要继承这个父类？啥作用？
        #精灵：把一群同样的实例组队，让子弹具备“精灵”的能力，方便批量管理
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #为啥不能自己调用导入settings，非得用ai_game的settings?：
        #为了保持所有模块的配置“统一”。
        self.color = self.settings.bullet_color

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置：
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        # Rect()接收四个参数：left,top,width,height,都是float
        self.rect.midtop = ai_game.ship.rect.midtop
        # midtop是指y=0的屏幕中间，还是y=700的屏幕中间?
        #都不是，是飞船的顶部的中间。因为是ai_game.ship的 rect.midtop.如果没有ship.，就要换成screen等。

        # 存储用浮点数表示的子弹位置：
        self.y = float(self.rect.y)

    def update(self):

        """向上移动子弹"""

            # 更新子弹的准确位置
        self.y -= self.settings.bullet_speed
            #位置（位移）如何用速度表达：时间单位是每帧？=1/60秒？
            #每秒60帧，每帧3speed像素，每秒就是180像素的移动距离
            # 更新表示子弹矩形的位置：
        self.rect.y = self.y
            #使得pygame可以接受的方式计算。

    def draw_bullet(self):   
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
            #pygame.draw,与flip()的不同？
            #draw（self,rect,color）：凭空画出，简单的矩形、圆形、线条等到内存中。fill()是一个特例，用纯色充满屏幕
            #blit(self,image,rect) :把引用导入的bmp,png的图片已经存在的，绘制到内存中
            #flip():从内存中把图像读出，再显示到屏幕上。
