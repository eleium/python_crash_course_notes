"""
火箭小游戏
- 屏幕中央显示一艘火箭
- 玩家通过上下左右方向键移动火箭
- 火箭不能移到屏幕之外
- 火箭图像路径：D:/alien_invasion/课堂作业/images/rocket.bmp
"""

import sys
import pygame


class Rocket:
    """管理火箭的位置与绘制"""

    def __init__(self, screen):
        """初始化火箭并设置其初始位置"""
        self.screen = screen

        # 加载火箭图像并获取其外接矩形
        try:
            self.image = pygame.image.load(
                r"D:/alien_invasion/课堂作业/images/rocket.bmp"
            )
        except FileNotFoundError:
            # 找不到图像时给一个友好提示，避免直接闪退
            print("未找到火箭图像：D:/alien_invasion/课堂作业/images/rocket.bmp")
            print("将使用占位矩形代替，请将 rocket.bmp 放到该路径下。")
            self.image = pygame.Surface((60, 80))
            self.image.fill((200, 200, 200))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新火箭放在屏幕中央
        self.rect.center = self.screen_rect.center

        # 移动标志（按住方向键时连续移动）
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # 移动速度（像素/帧）
        self.rocket_speed = 1.5

    def update(self):
        """根据移动标志调整火箭位置，并阻止其移出屏幕"""
        # 更新 X 轴位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.rocket_speed

        # 更新 Y 轴位置
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.rocket_speed

    def blitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image, self.rect)


def run_game():
    """初始化游戏、创建屏幕对象并启动主循环"""
    pygame.init()

    screen_width = 1200
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("火箭小游戏 - 方向键移动，Q 退出")

    # 设置背景色（深蓝灰）
    bg_color = (30, 30, 60)

    rocket = Rocket(screen)

    # 主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = True
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = True
                elif event.key == pygame.K_UP:
                    rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = True
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = False
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                elif event.key == pygame.K_UP:
                    rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = False

        # 让火箭根据移动标志移动（带越界保护）
        rocket.update()

        # 每次循环都重绘屏幕
        screen.fill(bg_color)
        rocket.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
