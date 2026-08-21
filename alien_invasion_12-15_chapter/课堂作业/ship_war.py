# 蓝色的天空 创建一个背景色为蓝色的pygame窗口

import pygame
import sys
from my_ship import My_Ship


class Ship_War:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 600))
        self.bg_color = (0, 0, 255)
        pygame.display.set_caption("Ship War")
        self.clock = pygame.time.Clock()
        self.fire_ship = My_Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.fire_ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    ship_war = Ship_War()
    ship_war.run_game()
