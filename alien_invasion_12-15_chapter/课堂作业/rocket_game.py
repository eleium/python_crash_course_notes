# 练习12.4 火箭
# 编写一个游戏，它在屏幕中央显示一艘火箭，玩家可以上下左右移动火箭。
# 火箭不能移到屏幕之外。
import sys
import pygame
from rocket import Rocket


class RocketGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 700))
        self.clock = pygame.time.Clock()
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Rocket Game")
        # 这是类的命令执行语句，非属性非方法。__inin__()一运行就立马执行。不被别的对象调用，不返回任何数据。
        self.rocket = Rocket(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = True
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = False
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = False

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

    def run_game(self):
        while True:
            self.check_events()
            self.rocket.update()
            self.update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    r_game = RocketGame()
    r_game.run_game()
