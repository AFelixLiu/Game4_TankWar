import pygame
import sys
import traceback
import home
import wall
import food
import myTank
import enemyTank

def main():
    pygame.init()  # 初始化pygame所有模块
#ceshi
    resolution = (630, 630)  # 指明图形窗口分辨率
    screen = pygame.display.set_mode(resolution)  # 创建图形窗口
    pygame.display.set_caption("坦克大战")  # 设置窗口标题
    background_image = pygame.image.load(r".\image\background.png")  # 加载背景图
    # 加载音效

    '''
    start_sound = pygame.mixer.Sound(r".\music\start.wav") # 加载游戏场景音效
    start_sound.play() # 播放游戏场景音效
    '''

    fire_sound = pygame.mixer.Sound(r".\music\Gunfire.wav")  # 加载开火音效
    bang_sound = pygame.mixer.Sound(r".\music\bang.wav")  # 加载中弹被毁音效

    homeGroup = pygame.sprite.Group()  # 定义home精灵组
    allTankGroup = pygame.sprite.Group()  # 定义总坦克精灵组
    mytankGroup = pygame.sprite.Group()  # 定义玩家精灵组
    allEnemyGroup = pygame.sprite.Group()  # 定义总敌方精灵组
    redEnemyGroup = pygame.sprite.Group()  # 定义敌方红色精灵组
    sEnemyGroup = pygame.sprite.Group()  # 定义敌方高级别精灵组
    otherEnemyGroup = pygame.sprite.Group()  # 定义敌方其它精灵组
    enemyBulletGroup = pygame.sprite.Group()  # 定义敌方子弹精灵组
    # 创建地图对象
    bgMap = wall.Map()
    # 创建home对象
    HOME = home.Home()
    homeGroup.add(HOME)
    # 创建home_destroyed对象
    HOME_DESTROYED = home.Home_Destroyed()
    homeGroup.add(HOME_DESTROYED)
    # 创建道具对象（但不显示）
    prop = food.Food()
    # 创建玩家坦克对象
    myTank_T1 = myTank.MyTank(1)
    allTankGroup.add(myTank_T1)
    mytankGroup.add(myTank_T1)
    myTank_T2 = myTank.MyTank(2)
    allTankGroup.add(myTank_T2)
    mytankGroup.add(myTank_T2)
    # 创建敌方坦克对象
    for i in range(1, 4):
        enemy = enemyTank.EnemyTank()
        allTankGroup.add(enemy)
        allEnemyGroup.add(enemy)
        if enemy.isred == True:
            redEnemyGroup.add(enemy)
            continue
        if enemy.kind == 3:
            sEnemyGroup.add(enemy)
            continue
        otherEnemyGroup.add(enemy)

    # 加载敌军坦克出现动画
    appearance_image = pygame.image.load(r".\image\appear.png").convert_alpha()
    appearance = []
    appearance.append(appearance_image.subsurface((0, 0), (48, 48)))
    appearance.append(appearance_image.subsurface((48, 0), (48, 48)))
    appearance.append(appearance_image.subsurface((96, 0), (48, 48)))

    homeBomb_image = pygame.image.load(r".\image\boom_dynamic.png").convert_alpha()
    homeBomb = []
    homeBomb.append(homeBomb_image.subsurface((0,0),(48,48)))
    homeBomb.append(homeBomb_image.subsurface((48,0),(48,48)))
    homeBomb.append(homeBomb_image.subsurface((96,0),(48, 48)))
    homeBomb.append(homeBomb_image.subsurface((144,0),(48, 48)))
    homeBomb.append(homeBomb_image.subsurface((192,0),(48, 48)))

    # 设置敌方坦克延迟200
    DELAYEVENT = pygame.constants.USEREVENT  # 自定义计时事件
    pygame.time.set_timer(DELAYEVENT, 200)  # 每隔指定时间发送一次自定义事件
    # 设置敌方子弹冷却延迟1000
    ENEMYBULLETNOTCOOLINGEVENT = pygame.constants.USEREVENT + 1
    pygame.time.set_timer(ENEMYBULLETNOTCOOLINGEVENT, 1000)
    # 设置玩家子弹冷却延迟200
    MYBULLETNOTCOOLINGEVENT = pygame.constants.USEREVENT + 2
    pygame.time.set_timer(MYBULLETNOTCOOLINGEVENT, 200)
    # 设置敌方坦克静止延迟8000
    NOTMOVEEVENT = pygame.constants.USEREVENT + 3
    pygame.time.set_timer(NOTMOVEEVENT, 8000)

    delay = 100
    moving = 0  # 代表玩家一是否正在移动
    movdir = 0  # 代表玩家一方向
    moving2 = 0  # 代表玩家二是否正在移动
    movdir2 = 0  # 代表玩家二方向
    enemyNumber = 3  # 敌方数量
    enemyCouldMove = True  # 表示敌方可以移动
    switch_R1_R2_image = True
    homeSurvive = True  # home生命
    running_T1 = True
    running_T2 = True
    clock = pygame.time.Clock()
    # gameover文字显示
    pygame.font.init()
    fontOver=pygame.font.Font(r".\font\Modern No. 20.ttf",60)
    textGameOver = fontOver.render("GAME OVER",True,(255,255,255),(58,58,58))
    # 游戏循环
    gameStatus = True
    while gameStatus:
        for event in pygame.event.get():
            # 退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 玩家子弹冷却事件
            if event.type == MYBULLETNOTCOOLINGEVENT:
                myTank_T1.bulletNotCooling = True
            # 敌方子弹冷却事件
            if event.type == ENEMYBULLETNOTCOOLINGEVENT:
                for each in allEnemyGroup:
                    each.bulletNotCooling = True
            # 敌方坦克静止事件
            if event.type == NOTMOVEEVENT:
                enemyCouldMove = True
            # 敌方坦克延迟事件
            if event.type == DELAYEVENT:
                if enemyNumber < 4:
                    enemy = enemyTank.EnemyTank()
                    if pygame.sprite.spritecollide(enemy, allTankGroup, False, None):
                        break
                    allEnemyGroup.add(enemy)
                    allTankGroup.add(enemy)
                    enemyNumber += 1
                    if enemy.isred == True:
                        redEnemyGroup.add(enemy)
                    elif enemy.kind == 3:
                        sEnemyGroup.add(enemy)
                    else:
                        otherEnemyGroup.add(enemy)
            # 隐藏操作
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:  # 组合按键"ctrl + c"：退出
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_e:  # 按键"e"：玩家升级
                    myTank_T1.levelUp()
                if event.key == pygame.K_q:  # 按键"q"：玩家降级
                    myTank_T1.levelDown()
                if event.key == pygame.K_3:  # 按键"3"：玩家直接升满级
                    for i in range(3):
                        myTank_T1.levelUp()
                if event.key == pygame.K_2:  # 按键"2"：修改玩家速度
                    if myTank_T1.speed == 3:
                        myTank_T1.speed = 6
                    else:
                        myTank_T1.speed = 3
                if event.key == pygame.K_1:  # 按键"1"：为保护目标重设普通砖墙
                    for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
                        bgMap.brick = wall.Brick()
                        bgMap.brick.rect.left, bgMap.brick.rect.top = 3 + x * 24, 3 + y * 24
                        bgMap.brickGroup.add(bgMap.brick)
                if event.key == pygame.K_4:  # 按键"4"：为保护目标重设石头砖墙
                    for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
                        bgMap.iron = wall.Iron()
                        bgMap.iron.rect.left, bgMap.iron.rect.top = 3 + x * 24, 3 + y * 24
                        bgMap.ironGroup.add(bgMap.iron)
        # 检查玩家操作
        key_pressed = pygame.key.get_pressed()
        # 玩家一的移动操作
        if moving:
            moving -= 1
            if movdir == 0:  # 代表玩家一此时方向向上
                allTankGroup.remove(myTank_T1)  # 移除是因为需要进行下面的碰撞检测
                if myTank_T1.moveUp(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving += 1
                allTankGroup.add(myTank_T1)  # 重新添加
                running_T1 = True
            if movdir == 1:  # 代表玩家一此时方向向下
                allTankGroup.remove(myTank_T1)
                if myTank_T1.moveDown(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving += 1
                allTankGroup.add(myTank_T1)
                running_T1 = True
            if movdir == 2:  # 代表玩家一此时方向向左
                allTankGroup.remove(myTank_T1)
                if myTank_T1.moveLeft(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving += 1
                allTankGroup.add(myTank_T1)
                running_T1 = True
            if movdir == 3:  # 代表玩家一此时方向向右
                allTankGroup.remove(myTank_T1)
                if myTank_T1.moveRight(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving += 1
                allTankGroup.add(myTank_T1)
                running_T1 = True

        if not moving:
            if key_pressed[pygame.K_w]:
                moving = 7
                movdir = 0
                running_T1 = True
                allTankGroup.remove(myTank_T1)
                if myTank_T1.moveUp(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving = 0  # 碰撞即暂停
                allTankGroup.add(myTank_T1)
            elif key_pressed[pygame.K_s]:
                moving = 7
                movdir = 1
                running_T1 = True
                allTankGroup.remove(myTank_T1)
                if myTank_T1.moveDown(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving = 0
                allTankGroup.add(myTank_T1)
            elif key_pressed[pygame.K_a]:
                moving = 7
                movdir = 2
                running_T1 = True
                allTankGroup.remove(myTank_T1)
                if myTank_T1.moveLeft(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving = 0
                allTankGroup.add(myTank_T1)
            elif key_pressed[pygame.K_d]:
                moving = 7
                movdir = 3
                running_T1 = True
                allTankGroup.remove(myTank_T1)
                if myTank_T1.moveRight(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving = 0
                allTankGroup.add(myTank_T1)
        if key_pressed[pygame.K_j]:  # 发射子弹操作
            if not myTank_T1.bullet.life and myTank_T1.bulletNotCooling:
                fire_sound.play()  # 播放子弹发射声音
                myTank_T1.shoot()
                myTank_T1.bulletNotCooling = False  # 子弹冷却

        # 玩家二的移动操作
        if moving2:
            moving2 -= 1
            if movdir2 == 0:
                allTankGroup.remove(myTank_T2)
                if myTank_T2.moveUp(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving += 1
                allTankGroup.add(myTank_T2)
                running_T2 = True
            if movdir2 == 1:
                allTankGroup.remove(myTank_T2)
                if myTank_T2.moveDown(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving += 1
                allTankGroup.add(myTank_T2)
                running_T2 = True
            if movdir2 == 2:
                allTankGroup.remove(myTank_T2)
                if myTank_T2.moveLeft(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving += 1
                allTankGroup.add(myTank_T2)
                running_T2 = True
            if movdir2 == 3:
                allTankGroup.remove(myTank_T2)
                if myTank_T2.moveRight(allTankGroup, bgMap.brickGroup, bgMap.ironGroup):
                    moving += 1
                allTankGroup.add(myTank_T2)
                running_T2 = True

        if not moving2:
            if key_pressed[pygame.K_UP]:
                allTankGroup.remove(myTank_T2)
                myTank_T2.moveUp(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
                allTankGroup.add(myTank_T2)
                moving2 = 3
                movdir2 = 0
                running_T2 = True
            elif key_pressed[pygame.K_DOWN]:
                allTankGroup.remove(myTank_T2)
                myTank_T2.moveDown(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
                allTankGroup.add(myTank_T2)
                moving2 = 3
                movdir2 = 1
                running_T2 = True
            elif key_pressed[pygame.K_LEFT]:
                allTankGroup.remove(myTank_T2)
                myTank_T2.moveLeft(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
                allTankGroup.add(myTank_T2)
                moving2 = 3
                movdir2 = 2
                running_T2 = True
            elif key_pressed[pygame.K_RIGHT]:
                allTankGroup.remove(myTank_T2)
                myTank_T2.moveRight(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
                allTankGroup.add(myTank_T2)
                moving2 = 3
                movdir2 = 3
                running_T2 = True
        if key_pressed[pygame.K_SPACE]:
            if not myTank_T2.bullet.life and myTank_T2.bulletNotCooling:
                fire_sound.play()  # 播放子弹发射声音
                myTank_T2.shoot()
                myTank_T2.bulletNotCooling = False  # 子弹冷却

        # 绘制背景
        screen.blit(background_image, (0, 0))
        # 绘制普通砖墙
        for each in bgMap.brickGroup:
            screen.blit(each.image, each.rect)
        # 绘制石头砖墙
        for each in bgMap.ironGroup:
            screen.blit(each.image, each.rect)
        # 绘制玩家一
        if not (delay % 5):
            switch_R1_R2_image = not switch_R1_R2_image
        if switch_R1_R2_image and running_T1:
            screen.blit(myTank_T1.tank_R0, (myTank_T1.rect.left, myTank_T1.rect.top))
            running_T1 = False
        else:
            screen.blit(myTank_T1.tank_R1, (myTank_T1.rect.left, myTank_T1.rect.top))
        # 绘制玩家二
        if switch_R1_R2_image and running_T2:
            screen.blit(myTank_T2.tank_R0, (myTank_T2.rect.left, myTank_T2.rect.top))
            running_T2 = False
        else:
            screen.blit(myTank_T2.tank_R1, (myTank_T2.rect.left, myTank_T2.rect.top))
        # 绘制敌方坦克
        for each in allEnemyGroup:
            # 判断是否播放出场特效
            if each.flash:
                # 判断画左动作还是右动作
                if switch_R1_R2_image:
                    screen.blit(each.tank_R0, (each.rect.left, each.rect.top))
                    if enemyCouldMove:
                        allTankGroup.remove(each)
                        each.move(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
                        allTankGroup.add(each)
                else:
                    screen.blit(each.tank_R1, (each.rect.left, each.rect.top))
                    if enemyCouldMove:
                        allTankGroup.remove(each)
                        each.move(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
                        allTankGroup.add(each)
            else:
                # 播放出场特效
                if each.times > 0:
                    each.times -= 1
                    if each.times <= 10:
                        screen.blit(appearance[2], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 20:
                        screen.blit(appearance[1], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 30:
                        screen.blit(appearance[0], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 40:
                        screen.blit(appearance[2], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 50:
                        screen.blit(appearance[1], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 60:
                        screen.blit(appearance[0], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 70:
                        screen.blit(appearance[2], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 80:
                        screen.blit(appearance[1], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 90:
                        screen.blit(appearance[0], (3 + each.x * 12 * 24, 3))
                if each.times == 0:
                    each.flash = True
        # 绘制敌方子弹
        for each in allEnemyGroup:
            if not each.bullet.life and each.bulletNotCooling and enemyCouldMove:
                enemyBulletGroup.remove(each.bullet)  # 移除上次可能没有被发射的子弹
                each.shoot()  # 赋予子弹生命并为其调整位置
                enemyBulletGroup.add(each.bullet)  # 添加到敌方子弹精灵组
                each.bulletNotCooling = False  # 子弹冷却
            if each.flash:  # 出场特效播放完毕
                if each.bullet.life:  # 子弹有生命
                    if enemyCouldMove:  # 敌方可以移动
                        each.bullet.move()  # 子弹移动并进行边界碰撞检测
                    screen.blit(each.bullet.bullet, each.bullet.rect)  # 绘制子弹
                    # 检测敌方子弹碰撞情况
                    if pygame.sprite.collide_rect(each.bullet, myTank_T1):  # 碰撞玩家一
                        bang_sound.play()  # 播放中弹音效
                        if(myTank_T1.level==0):
                            each.bullet.life = False  # 子弹失去生命
                            moving = 0  # 重置玩家移动控制参数
                            for i in range(myTank_T1.level + 1):
                                myTank_T1.levelDown()  # 玩家等级降为最低
                            myTank_T1.rect.left, myTank_T1.rect.top = 3 + 8 * 24, 3 + 24 * 24  # 重置玩家位置
                        else:
                            myTank_T1.level-=1;
                    if pygame.sprite.collide_rect(each.bullet, myTank_T2):  # 碰撞玩家二
                        bang_sound.play()
                        myTank_T2.rect.left, myTank_T2.rect.top = 3 + 16 * 24, 3 + 24 * 24
                        each.bullet.life = False
                        moving2 = 0
                    if pygame.sprite.spritecollide(each.bullet, bgMap.brickGroup, True, None):  # 碰撞普通砖墙（发生则删除）
                        each.bullet.life = False  # 子弹失去生命

                    if each.bullet.strong:  # 子弹可以击碎石头砖墙
                        if pygame.sprite.spritecollide(each.bullet, bgMap.ironGroup, True, None):  # 碰撞石头砖墙
                            each.bullet.life = False  # 子弹失去生命
                    else:  # 子弹不能击碎（子弹无法穿透石头砖墙）
                        if pygame.sprite.spritecollide(each.bullet, bgMap.ironGroup, False, None):
                            each.bullet.life = False
                    if pygame.sprite.collide_rect(each.bullet, HOME):  # 碰撞home
                        homeSurvive = False
                        
        # 绘制玩家一子弹
        if myTank_T1.bullet.life:  # 执行shoot()函数后子弹被赋予生命
            myTank_T1.bullet.move()  # 子弹移动并进行边界碰撞检测
            screen.blit(myTank_T1.bullet.bullet, myTank_T1.bullet.rect)  # 绘制子弹
            # 碰撞检测
            for each in enemyBulletGroup:
                if each.life:
                    if pygame.sprite.collide_rect(myTank_T1.bullet, each):
                        myTank_T1.bullet.life = False
                        each.life = False
                        pygame.sprite.spritecollide(myTank_T1.bullet, enemyBulletGroup, True, None)
            # 子弹碰撞敌方坦克
            if pygame.sprite.spritecollide(myTank_T1.bullet, redEnemyGroup, True, None):
                prop.change()
                bang_sound.play()
                enemyNumber -= 1
                myTank_T1.bullet.life = False
            elif pygame.sprite.spritecollide(myTank_T1.bullet, sEnemyGroup, False, None):
                for each in sEnemyGroup:
                    if pygame.sprite.collide_rect(myTank_T1.bullet, each):
                        if each.life == 1:
                            pygame.sprite.spritecollide(myTank_T1.bullet, sEnemyGroup, True, None)
                            bang_sound.play()
                            enemyNumber -= 1
                        elif each.life == 2:
                            each.life -= 1
                            each.tank = each.enemy_3_0
                        elif each.life == 3:
                            each.life -= 1
                            each.tank = each.enemy_3_2
                myTank_T1.bullet.life = False
            elif pygame.sprite.spritecollide(myTank_T1.bullet, otherEnemyGroup, True, None):
                bang_sound.play()
                enemyNumber -= 1
                myTank_T1.bullet.life = False
                # if pygame.sprite.spritecollide(myTank_T1.bullet, allEnemyGroup, True, None):
            #    bang_sound.play()
            #    enemyNumber -= 1
            #    myTank_T1.bullet.life = False
            # 子弹 碰撞 brickGroup
            if pygame.sprite.spritecollide(myTank_T1.bullet, bgMap.brickGroup, True, None):
                myTank_T1.bullet.life = False
                myTank_T1.bullet.rect.left, myTank_T1.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24
            # 子弹 碰撞 brickGroup
            if myTank_T1.bullet.strong:
                if pygame.sprite.spritecollide(myTank_T1.bullet, bgMap.ironGroup, True, None):
                    myTank_T1.bullet.life = False
                    myTank_T1.bullet.rect.left, myTank_T1.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24
            # 子弹碰撞home
            if pygame.sprite.collide_rect(myTank_T1.bullet, HOME):  # 碰撞home
                        homeSurvive = False
            else:
                if pygame.sprite.spritecollide(myTank_T1.bullet, bgMap.ironGroup, False, None):
                    myTank_T1.bullet.life = False
                    myTank_T1.bullet.rect.left, myTank_T1.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24

        # 绘制玩家二子弹
        if myTank_T2.bullet.life:
            myTank_T2.bullet.move()
            screen.blit(myTank_T2.bullet.bullet, myTank_T2.bullet.rect)
            # 子弹 碰撞 敌方坦克
            if pygame.sprite.spritecollide(myTank_T2.bullet, allEnemyGroup, True, None):
                bang_sound.play()
                enemyNumber -= 1
                myTank_T2.bullet.life = False
            # 子弹 碰撞 brickGroup
            if pygame.sprite.spritecollide(myTank_T2.bullet, bgMap.brickGroup, True, None):
                myTank_T2.bullet.life = False
                myTank_T2.bullet.rect.left, myTank_T2.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24
            # 子弹 碰撞 brickGroup
            if myTank_T2.bullet.strong:
                if pygame.sprite.spritecollide(myTank_T2.bullet, bgMap.ironGroup, True, None):
                    myTank_T2.bullet.life = False
                    myTank_T2.bullet.rect.left, myTank_T2.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24
            else:
                if pygame.sprite.spritecollide(myTank_T2.bullet, bgMap.ironGroup, False, None):
                    myTank_T2.bullet.life = False
                    myTank_T2.bullet.rect.left, myTank_T2.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24

        # 最后画食物/道具
        if prop.life:
            screen.blit(prop.image, prop.rect)
            # 我方坦克碰撞 食物/道具
            if pygame.sprite.collide_rect(myTank_T1, prop):
                if prop.kind == 1:  # 敌人全毁
                    for each in allEnemyGroup:
                        if pygame.sprite.spritecollide(each, allEnemyGroup, True, None):
                            bang_sound.play()
                            enemyNumber -= 1
                    prop.life = False
                if prop.kind == 2:  # 敌人静止
                    enemyCouldMove = False
                    prop.life = False
                if prop.kind == 3:  # 子弹增强
                    myTank_T1.bullet.strong = True
                    prop.life = False
                if prop.kind == 4:  # 家得到保护
                    for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
                        bgMap.iron = wall.Iron()
                        bgMap.iron.rect.left, bgMap.iron.rect.top = 3 + x * 24, 3 + y * 24
                        bgMap.ironGroup.add(bgMap.iron)
                    prop.life = False
                if prop.kind == 5:  # 坦克无敌
                    prop.life = False
                    pass
                if prop.kind == 6:  # 坦克升级
                    myTank_T1.levelUp()
                    prop.life = False
                if prop.kind == 7:  # 坦克生命+1
                    myTank_T1.life += 1
                    prop.life = False
        # 绘制树
        for each in bgMap.treeGroup:
            screen.blit(each.image, each.rect)
        # 绘制home
        if homeSurvive:
            screen.blit(HOME.image, HOME.rect)
        else: 
            if HOME.time==0:
                HOME.time=pygame.time.get_ticks()
            else:
                tempTime = pygame.time.get_ticks()
                sub = tempTime-HOME.time
                t =100 # 控制动画速度
                if sub <= t:
                    screen.blit(homeBomb[0], HOME.rect)
                elif sub <= t*2:
                    screen.blit(homeBomb[1], HOME.rect)
                elif sub <= t*3:
                    screen.blit(homeBomb[2], HOME.rect)
                elif sub<= t*4:
                    screen.blit(homeBomb[3], HOME.rect)
                elif sub<= t*12:
                    screen.blit(homeBomb[4], HOME.rect)
                else:
                    screen.blit(textGameOver,(120,300))
                    # gameStatus = False
            # screen.blit(HOME_DESTROYED.image, HOME_DESTROYED.rect)
        # 延迟
        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()