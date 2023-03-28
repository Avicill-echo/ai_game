# 学校名称:天津职业技术师范大学
# 姓   名:慕长平
# 开发时间:2023/3/28 11:01
import sys
import pygame
from settings import Settings
from ship import Ship

'''创建pygame窗口以及响应用户输入'''
class AlienIncasion:
    '''管理游戏资源【参数设置】'''
    def __init__(self):
        pygame.init()

        self.settings=Settings()                                           #【封装好设置参数】继承Setting类的所有属性
        #
        # #设置窗口大小 # self.screen=pygame.display.set_mode((1200,800))
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width,self.settings.screen_height))      #【固定API设置】窗口的大小

        # 全屏运行
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')                       #【固定API设置】窗口的名称

        self.ship=Ship(self)                                               #【调用Ship类中的属性】





    def run_game(self):
        '''开始主循环'''
        while True:
            self._check_events()                                           #分装函数——检查事件
            self.ship.update()                                             # 分装函数——按键操作指令
            self._update_screen()                                          #分装函数——更新屏幕


    def _check_events(self):
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # 离开
            elif event.type == pygame.KEYDOWN:   #如果输入类型为键入[按下按键]
                self._check_keydown_event(event)


            elif event.type == pygame.KEYUP:     #如果输入类型为键出[松开按键]
                self._check_keyup_event(event)




    def _update_screen(self):
        # 更新屏幕上的图像，并切换到新屏幕上
        '''设置每次循环重绘制屏幕'''
        # self.screen.fill(self.bg_color)
        self.screen.fill(self.settings.bg_color)

        # 绘制飞船
        self.ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _check_keyup_event(self,event):

        if event.key == pygame.K_RIGHT:  # 如果输入为右方向键
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            # 向有移动飞船
            # self.ship.rect.x += 1      #
    def _check_keydown_event(self,event):

        if event.key == pygame.K_RIGHT:  # 如果输入为右方向键
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()


if __name__=='__main__':
    ai=AlienIncasion()
    ai.run_game()


