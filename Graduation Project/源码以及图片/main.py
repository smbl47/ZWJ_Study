import pygame
import sys
import traceback
from pygame.locals import *
from random import *
import time

import myplane
import enemy
import bullet
import supply

# 游戏初始化
pygame.init()
# 游戏音乐初始化
pygame.mixer.init()
# 绘制背景图像
bg_size = width, height = 500, 800
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("空战 --测试")
background = pygame.image.load("images/background.png").convert()
# 定义颜色
Black = (0, 0, 0)
Blue = (0, 0, 255)
Red = (255, 0, 0)
White = (255, 255, 255)
Orange = (255, 204, 153)
Green = (153, 204, 255)
Color1 = (255, 102, 102)
# 载入游戏音乐
pygame.mixer.music.load("sound/Where Is the Love - Josh Vietti.mp3")
pygame.mixer.music.set_volume(0.1)
bullet_sound_1 = pygame.mixer.Sound("sound/bullet_1.wav")
bullet_sound_1.set_volume(0.03)
bullet_sound_2 = pygame.mixer.Sound("sound/bullet_2.aiff")
bullet_sound_2.set_volume(0.02)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.37)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.35)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.7)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.5)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.7)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.1)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.02)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.065)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.25)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.17)
death_sound = pygame.mixer.Sound("sound/death.wav")
death_sound.set_volume(0.5)


# 添加小型敌机组
def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


# 添加中型敌机组
def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)


# 添加大型敌机组
def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


# 添加提升速度
def level_speed(target, level_speed):
    for each in target:
        each.speed += level_speed


# 调用函数
def main():
    # 游戏背景音乐循环播放
    global e1_destroy_index, e2_destroy_index, e3_destroy_index, me_destroy_index, bullets
    pygame.mixer_music.play(-1)
    # 创建时钟对象
    clock = pygame.time.Clock()
    # 添加分数,字体
    score = 0
    font1 = pygame.font.Font("font/汉仪南宫体简.ttf", 36)
    font2 = pygame.font.Font("font/汉仪南宫体简.ttf", 25)
    # 生成我方飞机
    me = myplane.MyPlane(bg_size)  # 我方飞机
    enemies = pygame.sprite.Group()
    # 敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)
    # 敌方中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 5)
    # 敌方大型飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 2)
    # 添加中弹图片
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0
    # 生命数
    life_image = pygame.image.load("images/life.png").convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 3
    # 是否暂停游戏
    paused = False
    pause_nor_image = pygame.image.load('images/pause_nor.png').convert_alpha()
    pause_pressed_image = pygame.image.load('images/pause_pressed.png').convert_alpha()
    resume_nor_image = pygame.image.load('images/resume_nor.png').convert_alpha()
    resume_pressed_image = pygame.image.load('images/resume_pressed.png').convert_alpha()
    paused_rect = pause_nor_image.get_rect()  # 获得图片的长宽
    paused_rect.top, paused_rect.left = 10, width - paused_rect.width - 15
    paused_image = pause_nor_image  # 默认显示图
    # 设置难度级别
    level = 1
    # 定义炸弹
    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
    bomb_nmb = 2
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/汉仪南宫体简.ttf", 48)
    # 触发补给包
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    SUPPLY_TIME = USEREVENT  # 设置自定义事件
    pygame.time.set_timer(SUPPLY_TIME, 15 * 1000)  # 设置补给发放的时间(间隔15秒发放一次)
    # 子弹补给包定时器
    BULLET_TIMER = USEREVENT + 1
    # 无敌时间定时器
    INV_TIMER = USEREVENT + 2
    # 是否使用超级子弹
    is_bullet_timer = False
    # 生成子弹
    bullet1 = []
    bullet1_index = 0
    B1_num = 4
    for i in range(B1_num):
        bullet1.append(bullet.Bullet1(me.rect.midtop))  # 生成子弹在我方飞机上方
    # 生成超级子弹
    bullet2 = []
    bullet2_index = 0
    B2_num = 10
    for i in range(B2_num // 2):
        bullet2.append(bullet.Bullet2((me.rect.centerx - 18, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx + 15, me.rect.centery)))
    # 游戏结束界面
    gameover_font = pygame.font.Font('font/汉仪南宫体简.ttf', 48)
    again_image = pygame.image.load('images/again.png').convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load('images/gameover.png').convert_alpha()
    gameover_rect = gameover_image.get_rect()
    Game_Over = pygame.font.Font('font/汉仪南宫体简.ttf', 60)
    # 用于存档
    Record_un = False
    # 切换图片
    switch_image = True
    # 延迟
    delay = 100
    # 游戏主循环
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:  # 鼠标按下
                if event.button == 1 and paused_rect.collidepoint(event.pos):  # 检测悬停鼠标是否在矩形之内
                    paused = not paused  # 取反
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME, 0)  # 检测暂停时，补给包暂停发送，背景音乐、音效停止
                        pygame.mixer_music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 15 * 1000)  # 检测非暂停时，补给包开始发送，背景音乐、音效开始播放
                        pygame.mixer_music.unpause()
                        pygame.mixer.unpause()

            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):  # 修改暂停的图标样式
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = pause_nor_image
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_nmb:
                        bomb_nmb -= 1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False
                elif paused:
                    pygame.time.set_timer(SUPPLY_TIME, 0)
                    if event.key == K_SPACE:
                        if bomb_nmb:
                            bomb_nmb -= 1

            elif event.type == SUPPLY_TIME:
                supply_sound.play()
                # 随机获取任意补给
                if choice([True, False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            elif event.type == BULLET_TIMER:
                is_bullet_timer = False
                pygame.time.set_timer(BULLET_TIMER, 0)
            elif event.type == INV_TIMER:
                me.unmatched = False
                pygame.time.set_timer(INV_TIMER, 0)
        # 根据用户得分增加难度
        if level == 1 and score >= 15000:
            level = 2
            upgrade_sound.play()
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 1)
            level_speed(small_enemies, 0.5)

        if level == 2 and score >= 30000:
            level = 3
            upgrade_sound.play()
            pygame.mixer_music.pause()
            pygame.mixer_music.load("sound/World of Our Own - Westlife.mp3")
            pygame.mixer_music.play(-1)
            pygame.mixer_music.set_volume(0.1)
            add_small_enemies(small_enemies, enemies, 8)
            add_mid_enemies(mid_enemies, enemies, 4)
            add_big_enemies(big_enemies, enemies, 1)
            level_speed(small_enemies, 0.5)
            level_speed(mid_enemies, 0.5)

        if level == 3 and score >= 60000:
            level = 4
            upgrade_sound.play()
            add_small_enemies(small_enemies, enemies, 8)
            add_mid_enemies(mid_enemies, enemies, 5)
            add_big_enemies(big_enemies, enemies, 2)
            level_speed(small_enemies, 0.5)

        if level == 4 and score >= 100000:
            level = 5
            upgrade_sound.play()
            pygame.mixer_music.pause()
            pygame.mixer_music.load("sound/Young - The Chainsmokers.mp3")
            pygame.mixer_music.play(-1)
            pygame.mixer_music.set_volume(0.1)
            add_small_enemies(small_enemies, enemies, 10)
            add_mid_enemies(mid_enemies, enemies, 6)
            add_big_enemies(big_enemies, enemies, 3)
            level_speed(small_enemies, 0.5)

        if level == 5 and score >= 115000:
            level = 6
            upgrade_sound.play()
            add_small_enemies(small_enemies, enemies, 10)
            add_mid_enemies(mid_enemies, enemies, 6)
            add_big_enemies(big_enemies, enemies, 3)
            level_speed(small_enemies, 0.2)

        if level == 6 and score >= 130000:
            level = 7
            upgrade_sound.play()
            add_small_enemies(small_enemies, enemies, 12)
            add_mid_enemies(mid_enemies, enemies, 7)
            add_big_enemies(big_enemies, enemies, 3)
            level_speed(small_enemies, 0.2)

        if level == 7 and score >= 160000:
            level = 8
            upgrade_sound.play()
            add_small_enemies(small_enemies, enemies, 13)
            add_mid_enemies(mid_enemies, enemies, 8)
            add_big_enemies(big_enemies, enemies, 3)
            level_speed(small_enemies, 0.2)

        if level == 8 and score >= 200000:
            level = 9
            upgrade_sound.play()
            pygame.mixer_music.pause()
            pygame.mixer_music.load("sound/Fearless - Tule.mp3")
            pygame.mixer_music.play(-1)
            pygame.mixer_music.set_volume(0.1)
            add_small_enemies(small_enemies, enemies, 13)
            add_mid_enemies(mid_enemies, enemies, 7)
            add_big_enemies(big_enemies, enemies, 4)
            level_speed(small_enemies, 1)

        if level == 9 and score >= 250000:
            level = 10
            upgrade_sound.play()
            pygame.mixer_music.pause()
            pygame.mixer_music.load("sound/Cornfield Chase - Hans Zimmer.mp3")
            pygame.mixer_music.play(-1)
            pygame.mixer_music.set_volume(0.1)
            add_small_enemies(small_enemies, enemies, 20)
            add_mid_enemies(mid_enemies, enemies, 10)
            add_big_enemies(big_enemies, enemies, 5)
            level_speed(small_enemies, 0.2)

        screen.blit(background, (0, 0))

        if life_num and not paused:
            # 键盘控制
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()
            # 检测是否获得补给
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):
                    get_bomb_sound.play()
                    score += 200
                    if bomb_nmb < 5:
                        bomb_nmb += 1
                    else:
                        bomb_nmb = 5
                    bomb_supply.active = False

            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, me):
                    score += 200
                    get_bullet_sound.play()
                    is_bullet_timer = True
                    pygame.time.set_timer(BULLET_TIMER, 20 * 1000)
                    bullet_supply.active = False
            # 发射子弹
            if not (delay % 10):
                bullet_sound_1.play()
                if is_bullet_timer:
                    bullet_sound_1.stop()
                    bullet_sound_2.play()
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx - 18, me.rect.centery))
                    bullets[bullet2_index + 1].reset((me.rect.centerx + 15, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % B2_num
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % B1_num

            # 检测子弹是否击中敌机
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            # 检测中大型敌机是否被击中，击中energy-1
                            if e in mid_enemies or e in big_enemies:
                                e.hit = True
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False

            # 绘制大型敌机(遍历每一个敌机)
            for each in big_enemies:
                if each.active:
                    each.move()
                    # 绘制被击中的画面
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)

                    # 绘制血条
                    pygame.draw.line(screen, Black,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5),
                                     2)
                    # 生命大于50%显示蓝色，否则为红色
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.5:
                        energy_color = Blue
                    else:
                        energy_color = Red
                    pygame.draw.line(screen, energy_color,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5),
                                     2)
                    # 音效
                    if each.rect.bottom == -50:
                        enemy3_fly_sound.play(-1)
                # (敌机毁灭)
                else:
                    if not (delay % 3):
                        # 初始值e3为0
                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        # 到第六张图时，e3为5，一轮毁灭后执行下一步(重生)
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()  # 播放毁灭音效
                            enemy3_fly_sound.stop()  # 停止飞行音效
                            score += 1000
                            each.reset()
            # 中型机
            for each in mid_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)
                    pygame.draw.line(screen, Black,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5), 2)
                    # 生命大于50%显示蓝色，否则为红色
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.5:
                        energy_color = Blue
                    else:
                        energy_color = Red
                    pygame.draw.line(screen, energy_color,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5),
                                     2)
                else:
                    if not (delay % 3):
                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()  # 播放毁灭音效
                            score += 500
                            each.reset()
            # 小型机
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if not (delay % 3):
                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()  # 播放毁灭音效
                            score += 100
                            each.reset()
            # 检测我方飞机是否被撞
            enemies_down = pygame.sprite.spritecollide(me, enemies, False,
                                                       pygame.sprite.collide_mask)  # 调用spritecollide中的mask若发生碰撞返回一组数组
            if enemies_down and not me.unmatched:  # 当无敌为真事件时，取反，不会发生碰撞
                me.active = False
                for e in enemies_down:
                    e.active = False

            # 绘制我方飞机
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                if not (delay % 3):
                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        me_down_sound.play()  # 播放毁灭音效
                        life_num -= 1
                        me.reset()
                        pygame.time.set_timer(INV_TIMER, 3 * 1000)

            # 绘制得分
            max_score=score
            text1 = font1.render('分数:%s' % str(score), True, White)  # 将字符串转换成space对象进行操作
            screen.blit(text1, (10, 10))
            if level >= 10:
                text2 = font2.render('等级:%s(Max)' % str(level), True, Green)
                screen.blit(text2, (13, 45))
            else:
                text2 = font2.render('等级:%s' % str(level), True, Green)
                screen.blit(text2, (13, 45))
            if life_num == 0:
                # 停止音乐和音效,播放死亡声音
                death_sound.play()
                time.sleep(2)
                pygame.mixer.init()
                pygame.mixer_music.load("sound/alittlesomething - ldst.mp3")
                time.sleep(1)
                me_down_sound.stop()
                enemy3_fly_sound.stop()
                pygame.mixer_music.play(-1)
                pygame.mixer_music.set_volume(0.1)
        # 绘制结束画面
        elif life_num == 0:
            # 停止发送补给
            pygame.time.set_timer(SUPPLY_TIME, 0)
            record_score_text = font1.render("最高分:%d" % max_score, True, White)
            screen.blit(record_score_text, (15, 20))
            if not Record_un:
                Record_un = True
                with open('record_1.txt', 'r') as f:
                    max_score = int(f.read())
                if score > max_score:
                    max_score = score
                    with open('record_1.txt', 'w') as f:
                        f.write(str(score))
            # 绘制结束界面
            record_score_text = font1.render("最高分:%d" % max_score, True, White)
            screen.blit(record_score_text, (15, 20))

            Game_Over_text = Game_Over.render("游戏结束！", True, Color1)
            screen.blit(Game_Over_text, (130, 185))

            gameover_text1 = gameover_font.render("本局分数", True, White)
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                (width - gameover_text1_rect.width) // 2, height // 3
            screen.blit(gameover_text1, gameover_text1_rect)

            gameover_text2 = gameover_font.render(str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                (width - gameover_text2_rect.width) // 2, \
                gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                (width - again_rect.width) // 2, \
                gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                (width - again_rect.width) // 2, \
                again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)

            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                # 获取鼠标坐标
                pos = pygame.mouse.get_pos()
                # 如果用户点击“重新开始”
                if again_rect.left < pos[0] < again_rect.right and \
                        again_rect.top < pos[1] < again_rect.bottom:
                    # 调用main函数，重新开始游戏
                    pygame.mixer.init()
                    pygame.mixer_music.load("sound/Where Is the Love - Josh Vietti.mp3")
                    main()
                # 如果用户点击“结束游戏”
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                        gameover_rect.top < pos[1] < gameover_rect.bottom:
                    # 退出游戏
                    pygame.quit()
                    sys.exit()

        # 绘制生命数量
        if life_num:
            for i in range(life_num):
                screen.blit(life_image, (width - (i + 1) * life_rect.width, height + 20 - bomb_rect.height))
        # 绘制特殊炸弹
        if bomb_nmb < 5:
            bomb_text = bomb_font.render("× %d" % bomb_nmb, True, Orange)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image, (10, height - 5 - bomb_rect.height))
            screen.blit(bomb_text, (bomb_rect.width - 5, height - 15 - text_rect.height))
        elif bomb_nmb == 5:
            bomb_text = bomb_font.render("× %d(Max)" % bomb_nmb, True, Orange)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image, (10, height - 5 - bomb_rect.height))
            screen.blit(bomb_text, (bomb_rect.width - 5, height - 15 - text_rect.height))

        # 绘制暂停按钮
        screen.blit(paused_image, paused_rect)

        # 切换图片
        if not (delay % 5):
            switch_image = not switch_image

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except SystemError:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
