import pygame

class Home(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # 调用父类初始化方法
        self.time = 0
        self.image = pygame.image.load(r".\image\home.png").convert_alpha()  # 加载home图
        self.image.set_colorkey((255, 255, 255))  # 设置透明颜色键
        self.rect = self.image.get_rect()  # 获取位置信息
        self.rect.left, self.rect.top = 3 + 12 * 24, 3 + 24 * 24  # 修改位置信息

class Home_Destroyed(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # 调用父类初始化方法

        self.image = pygame.image.load(r".\image\home_destroyed.png").convert_alpha()  # 加载home被摧毁图
        self.image.set_colorkey((255, 255, 255))  # 设置透明颜色键
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 3 + 12 * 24, 3 + 24 * 24
