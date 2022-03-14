import pygame
import random
#小型机
class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 生成小型机
        self.image=pygame.image.load("images/enemy1.png").convert_alpha()
        self.rect = self.image.get_rect()
        # 添加一个列表存放敌方小型飞机毁灭图
        self.destroy_images=[]
        self.destroy_images.extend([
            pygame.image.load("images/enemy1_down1.png").convert_alpha(),
            pygame.image.load("images/enemy1_down2.png").convert_alpha(),
            pygame.image.load("images/enemy1_down3.png").convert_alpha(),
            pygame.image.load("images/enemy1_down4.png").convert_alpha()
        ])
        self.mask = pygame.mask.from_surface(self.image)
        #敌方飞机的速度
        self.speed = 2
        # 定义为小型机存活
        self.active=True
        # 敌方飞机的初始位置
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left,self.rect.top=random.randint(0,self.width-self.rect.width),random.randint(-5*self.height,0)
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    def reset(self):
        self.active = True
        self.rect.left,self.rect.top=random.randint(0,self.width-self.rect.width),random.randint(-5*self.height,0)
#中型机
class MidEnemy(pygame.sprite.Sprite):
    #定义全局变量(血条)
    energy=8
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 生成中型机
        self.image=pygame.image.load("images/enemy2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.image_hit = pygame.image.load("images/enemy2_hit.png").convert_alpha()
        # 添加一个列表存放敌方中型飞机毁灭图
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/enemy2_down1.png").convert_alpha(),
            pygame.image.load("images/enemy2_down2.png").convert_alpha(),
            pygame.image.load("images/enemy2_down3.png").convert_alpha(),
            pygame.image.load("images/enemy2_down4.png").convert_alpha()
        ])
        self.mask = pygame.mask.from_surface(self.image)
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        #定义为中型机存活
        self.active=True
        self.rect.left,self.rect.top=random.randint(0,self.width-self.rect.width),random.randint(-10*self.height,-self.height)
        self.energy= MidEnemy.energy
        self.hit=False
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    def reset(self):
        self.active=True
        self.energy = MidEnemy.energy
        self.rect.left,self.rect.top=random.randint(0,self.width-self.rect.width),random.randint(-10*self.height,-self.height)
#大型机
class BigEnemy(pygame.sprite.Sprite):
    energy=20
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        #生成大型机
        self.image1=pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.image2=pygame.image.load("images/enemy3_n2.png").convert_alpha()
        self.image_hit=pygame.image.load("images/enemy3_hit.png").convert_alpha()
        self.rect = self.image1.get_rect()
        # 添加一个列表存放敌方大型飞机毁灭图
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/enemy3_down1.png").convert_alpha(),
            pygame.image.load("images/enemy3_down2.png").convert_alpha(),
            pygame.image.load("images/enemy3_down3.png").convert_alpha(),
            pygame.image.load("images/enemy3_down4.png").convert_alpha(),
            pygame.image.load("images/enemy3_down5.png").convert_alpha(),
            pygame.image.load("images/enemy3_down6.png").convert_alpha()
        ])
        self.mask = pygame.mask.from_surface(self.image1)
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        #定义为大型机存活
        self.active=True
        self.hit = False
        self.energy=BigEnemy.energy
        self.rect.left,self.rect.top=random.randint(0,self.width-self.rect.width),random.randint(-15*self.height, -5*-self.height)
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    #敌方飞机重生
    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left,self.rect.top=random.randint(0,self.width-self.rect.width),random.randint(-15*self.height, -5*-self.height)