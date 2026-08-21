import pygame


class Rocket:
    def __init__(self, r_game):

        self.screen = r_game.screen
        self.screen_rect = r_game.screen.get_rect()  # 必须先拿到矩形
        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center  # 放在中央

        # 移动设置
        self.x = float(self.rect.x)
        # 设置成float,精细化操作火箭的移动，达到平滑的目的
        # 用rect会强制每次移动量是整数，舍弃小数部分，舍弃的叠加量越来越多，误差越来越大。
        # 最佳方法：前期用float计算，最后一次用rect取整计算，最大限度避免误差累积。
        self.y = float(self.rect.y)
        self.speed = 1.5  # 速度变量

        # 移动标志(初始时是静止状态)
        self.moving_up = False
        # 属性moving_up是一种状态，或者说是一种行为。不是具体的数值。一种开关。
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        # 火箭的移动的更新
        # 通过坐标轴计算火箭位置： 坐标原点在self.rect的左上方，向右x增加，向下y增加
        # 原点（0,0）： 位于屏幕（self.rect 或 screen_rect）的 左上角。
        # X 轴： 向右增加（正数）。
        # Y 轴： 向下增加（正数）。

        if self.moving_up and self.rect.top > 0:
            # 向上移动：
            # movng-up 不是数值，是布尔值，是开关：如果>0，结果为真，开始移动，移动值：slef.y-=self.speed
            # self.rect.top是数值，是火箭的矩形的顶部坐标值。如果>0，就一直在游戏矩形之内。
            self.y -= self.speed
            # 往上走，y值一直减小，一直到屏幕顶端为0.

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # 向下移动，火箭的矩形底部坐标值<屏幕底部坐标值，确保不会跑出游戏矩形。
            self.y += self.speed
            # y轴向下，值增加

        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
            # x轴向左，值减小，不能小于0，确保不跑出游戏矩形。
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
            # x轴向右，值增大，但是不能大于屏幕的右x坐标值。

        self.rect.x = self.x
        self.rect.y = self.y
        # 把浮点数更新回整数的rect，因为pygame只认rect值，不认self.x

    def blitme(self):
        # 在内存中画出屏幕和火箭
        self.screen.blit(self.image, self.rect)
        # 其实它是包含了坐标的！ 这里的 self.rect 就是坐标！
        # 在 Pygame 中，self.rect 不仅仅是一个矩形框，它本身就是一个“包含位置信息（x, y）和大小（width, height）的容器”。
        # 当你把这行代码传给 blit 时，Pygame 会立刻读取 self.rect 当前这一刻的 x 和 y 数值，然后根据这个数值，把 self.image 拷贝到内存画布上的那个具体位置。

        # 🔑 blit 的绝对定位原则
        # 在 Pygame 中，blit 执行的是“绝对坐标覆盖（Absolute Positioning）”，而不是“相对坐标叠加（Relative Offsetting）”。
        # 你的理解是对的： 每次调用 blit，Pygame 都会直接读取 self.rect 里的 x 和 y，把图片“钉”在那个坐标上。
        # 绝对定位的好处（为什么这么设计？）： 因为每次刷新都是绝对定位，所以在游戏循环里，你完全不需要去“擦除”上一帧的飞船。你只需要：
        # 先 fill 把整张画布涂成背景色（抹掉上一帧的一切）。
        # 再用新的 self.rect.x 和 self.rect.y blit 出飞船。
        # flip 展示。


# 一下是检测这个Rocket类的运行情况，也就是if __name__=="__main__":除了程序接口功能 的另外一个用法：独立测试一个类，而不用加载主类。
if __name__ == "__main__":
    # 1. 必须先初始化 Pygame 和窗口
    pygame.init()
    # 创建一个专门的测试屏幕
    test_screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("火箭独立测试")

    # 2. 造一个“假的主游戏对象”
    class FakeGame:
        def __init__(self):
            self.screen = test_screen

    # 3. 把假对象传给火箭（必须要有括号里的参数！）
    fake_r_game = FakeGame()
    rocket = Rocket(fake_r_game)

    # 4. 启动专门的测试循环
    clock = pygame.time.Clock()
    while True:
        # 处理退出事件（按右上角X关闭）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # 测试绘制画面
        test_screen.fill((230, 230, 230))  # 涂上灰色背景
        rocket.blitme()  # 画出火箭
        pygame.display.flip()  # 更新屏幕
        clock.tick(60)
