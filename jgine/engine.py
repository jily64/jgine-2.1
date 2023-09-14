import time
import pygame
import random
import sys
import asyncio
from jgine import config
from jgine import scr
from jgine import obj
from jgine import additionsls as ad
from os import environ
from sys import platform as _sys_platform
from screeninfo import get_monitors

def platform():
    if 'ANDROID_ARGUMENT' in environ:
        return 'android'
    elif _sys_platform in ('linux', 'linux2', 'linux3'):
        return 'linux'
    elif _sys_platform in ('win32', 'cygwin'):
        return 'win'

# Создаем игру и окно
async def run():

    WIDTH = 480
    HEIGHT = 360
    FPS = 60
    pygame.init()
    pygame.mixer.init()
    config.screen = pygame.display.set_mode((480, 330))
    pygame.display.set_caption("jgine2")
    scr.run()
    a = get_monitors()
    a = a[0]
    time.sleep(1)
    print(a.width, a.height)
    if platform() == 'android':
        path = "/data/data/org.test.apkb"
    elif platform() == 'linux':
        path = './'
    elif platform() == 'win':
        path = ''
    config.screen.fill((40, 40, 40))
    clock = pygame.time.Clock()
    running = True
    config.screen = pygame.display.set_mode((a.width, a.height), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
    add = scr.scr()
    while running:
        await ad.ev(config.objs)
        add.run()
        obj.draw(config.objs)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        print(clock.get_fps())



# Запуск игры
