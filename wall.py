import pygame

brickImage = r".\image\brick.png"
rockImage = r".\image\rock.png"
treeImage = r".\image\tree.png"

# 派生普通砖块类
class Brick(pygame.sprite.Sprite):
    def __init__(self):  # 初始化
        super().__init__()  # 调用父类初始化方法

        self.image = pygame.image.load(brickImage).convert_alpha()  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片尺寸
# 派生石头砖块类
class Iron(pygame.sprite.Sprite):
    def __init__(self):  # 初始化
        super().__init__()  # 调用父类初始化方法

        self.image = pygame.image.load(rockImage)  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片尺寸
# 派生树类
class Tree(pygame.sprite.Sprite):
    def __init__(self):  # 初始化
        super().__init__()  # 调用父类初始化方法

        self.image = pygame.image.load(treeImage)  # 加载图片
        self.image.set_colorkey((255, 255, 255))  # 设置透明颜色键
        self.rect = self.image.get_rect()  # 获取图片尺寸

class Map():
    def __init__(self):  # 初始化
        self.brickGroup = pygame.sprite.Group()  # 定义普通砖块精灵组
        self.ironGroup = pygame.sprite.Group()  # 定义石头砖块精灵组
        self.treeGroup = pygame.sprite.Group()  # 定义树精灵组

        # 指定普通砖块位置（数字代表地图中的位置）
        X_1, Y_1 = [0, 1], [4, 5, 20, 21, 22, 23]

        X_2, Y_2 = [8, 9], [0, 1, 2, 3]

        X_3, Y_3 = [16, 17], [0, 1]

        X_4, Y_4 = [14, 15, 18, 19, 20, 21, 22, 23, 24], [6, 7]

        X_5, Y_5 = [8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 23], [8]

        X_6, Y_6 = [8, 9, 10, 11, 12, 13, 18, 19, 23], [9]

        X_7, Y_7 = [12, 13, 23], [10, 11]

        X_8, Y_8 = [2, 3, 6, 7], [15]

        X_9, Y_9 = [0, 1, 2, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17], [16]

        X_10, Y_10 = [0, 1, 2, 5, 6, 7, 8, 11], [17]

        X_11, Y_11 = [10, 11], [18, 19]

        X_12, Y_12 = [14, 15, 16, 17], [19, 20]

        X_13, Y_13 = [2, 3], [22, 23]

        X_14, Y_14 = [2, 3, 4, 5, 18, 19], [24, 25]

        around_home = [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]
        # 指定石头砖块位置（数字代表地图中的位置）
        X1, Y1 = [20, 21, 22, 23, 24, 25], [3]

        X2, Y2 = [12, 13, 14, 15, 16, 17], [12, 13]

        X3, Y3 = [6], [20, 21, 22, 23]

        X4, Y4 = [0, 1], [15, 24, 25]
        # 指定树位置（数字代表地图中的位置）
        X5, Y5 = [2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        X6, Y6 = [0, 1], [8, 9, 10, 11]

        X7, Y7 = [2, 3, 22, 23], [12, 13]

        X8, Y8 = [18, 19, 20, 21, 22, 23], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

        X9, Y9 = [24, 25], [14, 15, 16, 17, 18]

        # 生成普通砖块对象并添加到对应精灵组
        for x in X_1:
            for y in Y_1:
                self.brick = Brick()  # 生成普通砖块对象
                self.brick.rect.x, self.brick.rect.y = 3 + x * 24, 3 + y * 24  # 设定普通砖块位置
                self.brickGroup.add(self.brick)  # 添加到普通砖块精灵组
        for x in X_2:
            for y in Y_2:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_3:
            for y in Y_3:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_4:
            for y in Y_4:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_5:
            for y in Y_5:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_6:
            for y in Y_6:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_7:
            for y in Y_7:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_8:
            for y in Y_8:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_9:
            for y in Y_9:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_10:
            for y in Y_10:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_11:
            for y in Y_11:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_12:
            for y in Y_12:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_13:
            for y in Y_13:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_14:
            for y in Y_14:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x, y in around_home:
            self.brick = Brick()
            self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
            self.brickGroup.add(self.brick)
        # 生成石头砖块对象并添加到对应精灵组
        for x in X1:
            for y in Y1:
                self.iron = Iron()  # 生成石头砖块对象
                self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24  # 设定石头砖块位置
                self.ironGroup.add(self.iron)  # 添加到石头砖块精灵组
        for x in X2:
            for y in Y2:
                self.iron = Iron()
                self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
                self.ironGroup.add(self.iron)
        for x in X3:
            for y in Y3:
                self.iron = Iron()
                self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
                self.ironGroup.add(self.iron)
        for x in X4:
            for y in Y4:
                self.iron = Iron()
                self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
                self.ironGroup.add(self.iron)
        # 生成树对象并添加到对应精灵组
        for x in X5:
            for y in Y5:
                self.tree = Tree()  # 生成树对象
                self.tree.rect.x, self.tree.rect.y = 3 + x * 24, 3 + y * 24  # 设定树位置
                self.treeGroup.add(self.tree)  # 添加到树精灵组
        for x in X6:
            for y in Y6:
                self.tree = Tree()
                self.tree.rect.x, self.tree.rect.y = 3 + x * 24, 3 + y * 24
                self.treeGroup.add(self.tree)
        for x in X7:
            for y in Y7:
                self.tree = Tree()
                self.tree.rect.x, self.tree.rect.y = 3 + x * 24, 3 + y * 24
                self.treeGroup.add(self.tree)
        for x in X8:
            for y in Y8:
                self.tree = Tree()  # 生成普通砖墙对象
                self.tree.rect.x, self.tree.rect.y = 3 + x * 24, 3 + y * 24
                self.treeGroup.add(self.tree)
        for x in X9:
            for y in Y9:
                self.tree = Tree()
                self.tree.rect.x, self.tree.rect.y = 3 + x * 24, 3 + y * 24
                self.treeGroup.add(self.tree)