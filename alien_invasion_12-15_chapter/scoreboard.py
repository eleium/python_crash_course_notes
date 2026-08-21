import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """显示得分信息的类"""

    def __init__(self, ai_game):
        """初始化记录得分的属性"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分信息时使用的字体设置：
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备包含最高分和当前得分的图像
        # 准备初始得分的图像：
        self.prep_score()
        # prep:准备。  prep_score:准备得分
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_level(self):
        """将等级渲染为图像"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )

        # 将等级放到分数的下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        """将最高分渲染为图像"""
        high_score = round(self.stats.high_score, -1)
        # round() 是一个内置函数（BIF），它的核心作用是：对浮点数（小数）进行“四舍五入”取整，或者保留指定位数的小数。
        # 参数 -1 是什么意思？
        # round() 的第二个参数叫 ndigits（保留的位数）：
        # 正数 n：保留小数点后 n 位。比如 round(123.456, 2) → 123.46。
        # 0：四舍五入到个位数（整数）。比如 round(123.456, 0) → 123.0。
        # 负数 -n：向前（向左）对整数部分进行舍入，即四舍五入到 10的n次方 位。
        # -1 意味着：对十位（10的1次方）进行四舍五入。

        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        # 将最高分放到屏幕的顶部的中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.center = self.screen_rect.center
        self.high_score_rect.top = self.screen_rect.top

    def prep_score(self):
        """将得分渲染为图像"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )
        # render:渲染   “用这个字体（self.font），把 score_str 这个字符串，开启抗锯齿（True），
        # 用这个前景色（text_color），以这个背景色（bg_color）作底，画成一张图片，存给 self.score_image。”

        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上绘制得分，等级和余下的飞船"""
        self.screen.blit(self.score_image, self.score_rect)
        # 此处用blit,将已有图片绘制到内存。而非draw，创作出一个画面，多以线条，圆形矩形等.
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        # 当你调用 group.draw(surface) 时：  为啥用draw?
        # Pygame 会自动遍历这个组里的所有精灵（即那 3 艘小船图标）。
        # 自动调用每个精灵的 blitme() 方法（或者直接 blit 它们的 image 和 rect）。
        # 把画出来的结果，画到你传入的那个画布上。

    def check_high_score(self):
        """检测是否是诞生了新的最高分"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            # self.stats.high_score = max(self.stats.score, self.stats.high_score)这么写更简洁，或用条件表达式：
            # self.stats.high_score = self.stats.score if self.stats.score > self.stats.high_score else self.stats.high_score

            self.prep_high_score()

    def prep_ships(self):
        """显示还有多少飞船余留"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
