import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    # invasion:侵入
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏，并创建游戏资源"""
        pygame.init()
        # pygame.init() 是你在使用 Pygame 所有功能之前，必须执行的“总开关”或“初始化仪式
        self.clock = pygame.time.Clock()
        # Clock是pygame模块中的一个类。这是创建pygame.time模块中的类Clock的一个实例化对象。
        # 这个类可以定义游戏的速度（帧率）

        self.settings = Settings()
        # 从模块settings中导入的Settings类，实例化一个对象settings,就可以调用类Settings中的属性。拿到类Settings的所有属性。
        #这个self,就是以后的主类的实例化对象： ai_game.
        #有了ai_game.settings,其他类就可以调用主类的设置属性。

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # 这个函数的标准格式是：pygame.display.set_mode(尺寸元组, 标志位)
        # (0, 0)：这是一个元组。当你给它传入 (0, 0)，Pygame 会把它解读为“宽度=0，高度=0”。而不是坐标值。
        # pygame.FULLSCREEN：这是第二个参数，一个特殊的标志位。
        # 【关键核心】当这两个参数组合在一起时，Pygame 有一个特殊规则：
        # 如果你指定了 FULLSCREEN（全屏模式），并且尺寸传的是 (0, 0)，Pygame 就会自动把你的显示器物理分辨率（比如 1920x1080）赋值给窗口。
        # 所以这行代码的作用是：“创建一个全屏窗口，大小自动匹配我当前显示器的最大分辨率。”

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # 用self.screen.get_rect().width/height抓取真正的屏幕尺寸，赋值给setting
        # 游戏界面大小

        pygame.display.set_caption("Alien Invasion")
        # 这是类的命令执行语句，非属性非方法。__inin__()一运行就立马执行。不被别的对象调用，不返回任何值。
        # 游戏标题：Alien Invasion

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        # 创建子弹的精灵编组，现在是空的
        self.aliens = pygame.sprite.Group()
        # 创建外星人的精灵编组，现在是空的

        # 创建统计信息实例
        self.stats = GameStats(self)

        # 创建储存游戏统计信息的实例，并创建记分牌
        self.sb = Scoreboard(self)

        self._creat_fleet()
        # 新增一个：创建舰队的方法
        #在 __init__ 里直接调用 self._creat_fleet()，不是为了“生成一个属性”，而是为了“确保游戏对象在出生时，就立刻处于正确的初始状态”。
        # __init__的英文全称是 Initialization（初始化）。它的意义不是“用来存放代码”，而是“当这个对象刚被创建出来的那一瞬间，必须立刻执行的动作”。
        # 写在 __init__ 里，是为了“自动生效”。

        # 游戏启动后处于非活动状态
        self.game_active = False

        # 创建一个按钮实例,msg='Play'
        self.play_button = Button(self, "Play")

    def _creat_fleet(self):
        """创建一个外星舰队"""
        # 创建一个外星人，再不断的添加，直到没有空间添加外星人为止：
        # 外星人的间距为外星人的宽度
        # 先创建一个外星人：
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        #size 是pygame.rect自带的属性，内置了width,height数据元组。类似的属性还有： width,height,top,bottom，x,y,left,center等
        current_x, current_y = alien_width, alien_height
        #current_x,rect_x永远指向alien的左上角的坐标值。alien_width,alien_height,是具体的数字：60个像素，80个像素的数字值，而不代表宽，高。
        while current_y < (self.settings.screen_height - 15 * alien_height):
            #self.settings.screen_height-15*alien_height: 从底往上15倍自身高度的地方
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._creat_alien(current_x, current_y)
                current_x += 2 * alien_width

            # 添加一行外星人后，重置x值，并递增y值
            current_x = alien_width
            current_y += 2 * alien_height

    def _creat_alien(self, x_position, y_position):
        """创建一个外星人，并将其放在当前行中"""

        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

        # self.aliens.add(alien)
        # 把这个外星人添加到储存外星舰队的编组中。add是pygame的方法,类似python append(列表)

    def _check_aliens_bottom(self):
        """检测是否有外星人到达了屏幕的下边缘"""
        for alien in self.aliens.sprites():
            #这是一个方法。当你调用 self.aliens.sprites() 时，Pygame 会打开这个仓库，把里面当前存放的所有外星人精灵，整理成一个列表（List）返回给你
            if alien.rect.bottom >= self.settings.screen_height:
                # 像飞船被撞到一样进行处理：
                self._ship_hit()
                break

    def _ship_hit(self):
        """响应飞船和外星人的碰撞"""
        if self.stats.ship_left > 0:
            # 将ships_left减去1并更新记分牌
            self.stats.ship_left -= 1
            self.sb.prep_ships()

            # 清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()

            # 创建一个新的外星人舰队，并将我方飞船放到屏幕底部中央
            self._creat_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(1)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _check_fleet_edges(self):
        """在有外星人到达边缘时采取的响应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整个外星舰队向下移动，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            self.settings.fleet_direction *= -1

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #有意为之的一个死循环，让游戏一直运行，直到输入q或键盘点击窗口上的 x
            self._check_events()
            # 重构函数，新增_check_events()方法。
            # 侦听键盘和鼠标事件
            if self.game_active:
                self.ship.update()
                # 根据键鼠事件，更改飞船的状态（即飞船位置）

                self._update_bullets()
                # 更新子弹的状态

                self._update_aliens()
                # 更新外星人舰队的移动，新建一个_update_alien()方法

            self._update_screen()
            # 重构，新增_update_screen()方法

            self.clock.tick(60)
            #  在这个函数运行循环后，类Clock的实例化对象self.clock调用一个tick()方法。参数是60，一秒60次刷新。

    def _check_events(self):
        """响应接触和鼠标事件，把事件的动作归类到一个辅助方法里。"""
        for event in pygame.event.get():
            # event: 事件 event.get()所有的鼠标啊，键盘啊的待处理动作，收集为一个事件列表
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                #执行按下键的方法
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                #执行抬起键的方法

            # 检测到鼠标点击动作：
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #，获取鼠标点击的具体坐标数值（是一个元组，x,y）
                self._check_play_button(mouse_pos)
                #根据这个元组，去判断是否与play这个button重合

    def _check_play_button(self, mouse_pos):
        """玩家点击play按钮时，开始游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # collidepoint它的全称是 Collide Point（碰撞点）,两个对象的rect属性重合，即碰撞
        if button_clicked and not self.game_active:
            # 还原游戏设置
            self.settings.initialize_dynamic_settings()
            self.sb.prep_score()
            # 把重置后的0变成图
            self.sb.prep_level()
            # 把重置后的等级为1变成图
            self.sb.prep_ships()
            #显示剩余飞船

            if self.play_button.rect.collidepoint(mouse_pos):
                # 重置游戏的统计信息
                self.stats.reset_stats()
                self.game_active = True

                # 清空外星人和子弹的列表
                self.bullets.empty()
                self.aliens.empty()

                # 创建一个新的外星人舰队，并将我方飞船放在屏幕的底部的中央
                self._creat_fleet()
                self.ship.center_ship()

                # 游戏进行时，隐藏光标
                pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船。event.key：事件的key属性：按下键。pygame.K_RIGHT:向右的箭头键
            # event.key 和 pygame.K_RIGHT，都是编号，是数字，所以可以对比判断。
            self.ship.moving_right = True
            # 调用了ship的moving_right属性，按下键就一直向右移动
        #     self.ship.rect.x += 1
        # 没有调用ship里面的moving_right属性，只能一次移动一个单位。
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        # 新增一个开火事件。用的也是_fire_bullet(),辅助方法，类内使用。重构主类。

    def _fire_bullet(self):
        """创建一个子弹，并将其加入编组bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            # 从类Bullet实例化一个子弹实例
            self.bullets.add(new_bullet)
        # add()是pygame的编组增加元素用法，与列表的append类似
        # self.bullets 不是列表（List），它是一个 pygame.sprite.Group（精灵组）对象。new_bullet 是被存放进了这个“精灵组”里。

    # list.append() 和 group.add() 的核心区别
    # 特性	             Python 列表 (my_list.append())                            Pygame 精灵组 (my_group.add())
    # 存放的内容	     可以放任何东西（数字、字符串、子弹、飞船等）。	           只能存放继承了 pygame.sprite.Sprite 的精灵对象（比如子弹、外星人）。
    # 底层结构	         像一串链条，按顺序排列。	                               底层使用哈希表/集合，不强制保序，但查找和删除速度极快。
    # 添加方式	         my_list.append(元素)	                                   my_group.add(元素)
    # 批量添加	         只能一个一个加，或用 extend()。    	                   可以直接一次性加一堆，比如 group.add(bullet1, bullet2, bullet3)。
    # 如何画出来	     需要自己写 for 循环，挨个调用 blit() 画出来。	           自带大招：直接写 my_group.draw(screen)，它会自动把组里所有精灵画在屏幕上！

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """更新子弹的位置，并删除已经消失的子弹"""
        # 更新子弹的位置：
        self.bullets.update()
        # 循环内更新子弹状态，要在更新屏幕之前。
        # 在对编组调用update()时，编组会对其中的每一个精灵调用update().

        # 删除已经出了屏幕的子弹：
        for bullet in self.bullets.copy():
            # 遍历编组中的精灵的副本
            # 因为如果你在遍历一个列表或编组的同时，试图去“删除”里面的元素，程序会直接崩溃报错。为了解决这个问题，我们需要遍历它的“副本（copy）”。
            # 现在遍历副本（副本不变），但是操作原本（从原本中删除），顺序不会变。

            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                # 从编组中删除出界的子弹。
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # 检测是否有子弹击中了外星人
        # 如果是，就删除相应的外星人和子弹
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # pygame.sprite.groupcollide() 翻译成中文就是：“检测两组精灵之间的碰撞。”
        # 四个参数分别是啥？（看仔细了！）
        # 它一共接收 4 个参数，顺序非常严格：
        # pygame.sprite.groupcollide(组1, 组2, 删除组1的子弹吗?, 删除组2的子弹吗?)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # 删除现有子弹，并创建一个新的外星舰队
            self.bullets.empty()
            self._creat_fleet()
            self.settings.increase_speed()

            # 提高等级
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """检测是否有外星人在屏幕边缘，并更新外星舰队的所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # print("Ship hit!!!")
            self._ship_hit()

        # 检测是否有外星人达到了屏幕的下边缘：
        self._check_aliens_bottom()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        # 括号内是类Setting的实例化对象settings,调用该类的属性，当参数传给run_game()函数的self.screen.fill()方法。
        # 每次循环都重新绘制屏幕背景

        # fill()方法接受参数，用self.bg_color充满屏幕。
        # 让最近绘制的屏幕可见

        for bullet in self.bullets.sprites():
            # bullets.sprites()返回一个列表，里面元素是bullets编组中的所有精灵。
            bullet.draw_bullet()
            # 绘制子弹的代码，放到blitme()绘制飞船前面。以防止子弹在飞船之上。

        self.ship.blitme()
        # 把飞船绘制到屏幕

        self.aliens.draw(self.screen)
        # 此处用的是draw而非blit.
        # pygame.draw.rect()和Group.draw()是完全不同的两个函数
        # pygame.draw.rect()：这是一个底层绘图函数。用来在屏幕上画一个“纯色长方形”（你画子弹用的就是它）。
        # Group.draw()：这是一个精灵批量管理方法。专门用来把精灵组里所有的精灵图片（bmp/png）一次性贴上屏幕。

        # 显示得分
        self.sb.show_score()

        # 如果游戏处于非活动状态，就绘制play按钮：
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
        # flip():把内存中的画面显示到屏幕上。翻新。

        # 1. screen.fill(颜色) —— 铺底纸（清理画布）
        # 作用： 把整个屏幕窗口（screen）全部涂成一种纯色。
        # 核心用途： 因为我们的游戏画面是每秒钟刷新 60 次的。上一帧的飞船还在左边，这一帧要跑到右边。
        # 如果你不先用 fill() 把屏幕全涂成背景色（相当于擦掉旧画），那么飞船留下的旧痕迹就会一直留在屏幕上，变成“拉丝”或拖影。
        # 执行顺序： 第一。必须先擦干净，才能画新的。

        # 2. ship.blitme() (底层调用了 screen.blit()) —— 画图（贴图）
        # 作用： 把一张图片（比如飞船的 self.image），按照指定的位置坐标（self.rect），“拷贝/粘贴”到屏幕内存中。
        # 理解： 你可以类比为在 Word 文档里“粘贴”一张图片。这张图片覆盖了下面的一小部分背景。
        # 执行顺序： 第二。必须在 fill() 之后，flip() 之前。
        # 注：blitme() 是你自己定义的函数（里面调用了 self.screen.blit()），而 blit() 是 Pygame 官方提供的底层方法。

        # 3. pygame.display.flip() —— 展出（翻页显示）
        # 作用： 将刚才在内存（后台）中画好并粘贴好飞船的那一整帧画面，一次性推送到计算机的显示器上，让你肉眼看到。
        # 为什么叫 flip()（翻转）？ Pygame 底层使用了一种叫 “双缓冲”（Double Buffering） 的技术。
        # 你其实是在后台的一个“看不见的隐形屏幕”上画图（用 fill 和 blit），当画完后，调用 flip() 会将这个隐形屏幕和当前观众看到的屏幕瞬间“翻转”互换。
        # 执行顺序： 最后。必须放在所有绘图步骤之后。




if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    # 它的两个核心作用：
    # 做程序的启动接口（就像汽车的启动按钮）。
    # 防止被导入时自动运行（让导入进来的代码只当“工具箱”用）。

    # 📌 它的作用是啥？
    # 作用	                              说明
    # 作为程序入口	                      当你直接运行这个 .py 文件时，__name__ 会被设置为 "__main__"，代码块被执行
    # 防止被导入时执行	                  当这个文件被 import 到其他文件时，__name__ 是文件名（如 "alien_invasion"），代码块不会执行
    # 下面这个代码块，只有你直接运行 settings.py 时才会执行！而别的程序如果导入settings，不会触发这些代码。
    # 做测试最方便安全。

    # if __name__ == '__main__':
    #     test_setting = Settings()
    #     print("测试屏幕宽度:", test_setting.screen_width)
    #     print("测试背景颜色:", test_setting.bg_color)

    ai = AlienInvasion()
    ai.run_game()
