#import sys
import pygame

from setting import Setting
from ship import Ship
from pygame.sprite import Group
import game_function as gf

def run_game():
    #初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings,screen)

    bullets = Group()

    aliens = Group()

    gf.create_fleet(ai_settings,screen,aliens)

    #设置背景色
    bg_color = (230,230,230)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
  


run_game()