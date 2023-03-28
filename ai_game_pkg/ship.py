# 学校名称:天津职业技术师范大学
# 姓   名:慕长平
# 开发时间:2023/3/28 15:19
'''管理飞船的类'''
import pygame


class Ship:
    def __init__(self,ai_game):
        '''初始化飞船及位置'''
        self.screen=ai_game.screen
        # 飞船移动速度
        self.settings =ai_game. settings

        self.screen_rect=ai_game.screen.get_rect()

        #加载飞船并获取其外接矩形
        self.image=pygame.image.load('data/images/ship.png')
        self.rect=self.image.get_rect()

        #对于每艘新飞船，都将其放在屏幕底部中央
        self.rect.midbottom=self.screen_rect.midbottom


        #移动标志
        self.moving_right=False
        self.moving_left = False


        #飞船的x属性中存放小数值
        self.x=float(self.rect.x)





    def update(self):
        '''依据移动飞船标志调整飞船的位置'''
        # 限制飞船边界
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            # 更新slef中rect对象

        self.rect.x = self.x



        #右移
        if self.moving_right:
            self.x+=self.settings.ship_speed
        #左移动
        if self.moving_left:
            self.x-=self.settings.ship_speed






    def blitme(self):
        '''指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)



