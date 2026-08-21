class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置：1366x768 分辨率下，留出一点边缘空间
        self.screen_width = 1366
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # ---- 飞船设置（大幅提速！） ----
        # 让你的飞船能“瞬移”一样快速跑到边缘。
        self.ship_speed = 8.0  
        self.ship_limit = 3

        # ---- 子弹设置 ----
        # 子弹必须快到“所见即所击”
        self.bullet_speed = 7.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 老机器限制子弹数量，防止卡顿
        self.bullets_allowed = 5

        # ---- 外星人设置（解决“你追我赶”的耗时问题） ----
        # 外星人横向移动必须变快，给玩家制造“快去拦截”的紧迫感，而不是“等它们爬过来”。
        self.alien_speed = 2.5  

        # ⭐ 核心修改：大幅降低下落的幅度。
        # 原书是大屏用的，小屏幕只要外星人微微下压一点，就会给玩家造成心理压力。
        # 设为 0.8 或 1.0，意味着它们会在屏幕上“徘徊”很久，你完全有时间跑个来回。
        self.fleet_drop_speed = 0.8  

        self.fleet_direction = 1

        # ---- 游戏节奏加速设置 ----
        self.speedup_scale = 1.1
        #外星人分数值的提高
        self.score_scale=1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的属性"""
        # 让游戏初始速度稍微温和一点，但依然保持敏捷
        self.ship_speed = 6.0
        self.bullet_speed = 6.0
        self.alien_speed = 2.0  
        self.fleet_direction = 1

        #计分设置：
        self.alien_points=50


    def increase_speed(self):
        #increase: 增加，提高
        """提高速度设置的值和外星人分数"""
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale

        self.alien_points=int(self.alien_points*self.score_scale)
        print(self.alien_points)

