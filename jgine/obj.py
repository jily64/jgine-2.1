import pygame
from jgine import config, additionsls
import copy
from pygame.sprite import Sprite
import pygame.image
def draw(objl):
    config.screen.fill((0, 0, 0))
    for obj in objl:
        if obj.is_visible == True:
            if obj.type == 'rect':
                pygame.draw.rect(config.screen, obj.color, pygame.Rect(obj.pos1, obj.pos2), 0)
            elif obj.type == 'sprite':
                config.screen.blit(obj.sprite,(obj.pos1[0],obj.pos1[1]))
    #config.objs = []
    pygame.display.flip()


class Rect:
    def __init__(self, pos1=(100, 100), pos2=(200, 200), color=(255, 255, 255), hitbox=False):
        self.pos1 = pos1
        self.pos2 = pos2
        self.color = color
        self.events = []
        self.hitbox = hitbox
        self.type = 'rect'
        self.is_visible = True
        config.objs.append(self)
    def set_pos(self, pos1 = None, pos2 = None):
        if pos1 == None:
            self.pos2 = pos2
        elif pos2 == None:
            self.pos1 = pos1
        elif pos2 != None and pos1 != None:
            self.pos1 = pos1
            self.pos2 = pos2
        else:
            print("Invalid Position")
    def set_color(self, color = None):
        if color != None:
            self.color = color
        else:
            print("Invalid Color")

    def set_sprite(self, spr):
        self.sprite = pygame.image.load(f"./sprites/{spr}")
        self.type = 'sprite'
    def set_sprite_size(self, size = None):
        if type(size) == int:
            self.sprite = pygame.transform.scale(self.sprite,(size, size))
        elif type(size) == tuple:
            self.sprite = pygame.transform.scale(self.sprite, size)
