# 练习12.5 按键
# 编写一个创建空屏幕的pygame文件。在事件循环中，每当检测到pygame.KEYDOWN事件时，都打印属性event.key
# 运行这个程序，并按下不同的键，看看控制台窗口输出。以便了解pygame会如何响应。

import pygame
import sys


class SpaceScreen:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 600))
        # self.screen.rect = pygame.get_rect()
        self.clock = pygame.time.Clock()
        self.speed=1.5
        self.bg_color=(230,230,230)



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
 
                    # self.moving_left += self.speed
                    print(f"event.key的属性是{event.key}")

    def update_screen(self):
        self.screen.fill(self.bg_color)
        # self.blitme()
        pygame.display.flip()

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    ss = SpaceScreen()
    ss.run_game()
