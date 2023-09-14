import os
from jgine import obj
import copy
import pygame
from jgine import config
from jgine import additionsls
from pynput import mouse
class scr:
    def __init__(self):
        listener = mouse.Listener(on_click=additionsls.on_click)
        listener.start()
        self.rect = obj.Rect()
        self.rect.set_color(color=(255, 255, 0))
        self.e = 0
        self.s = 0
        self.f = 0
        self.w = 0
        #self.rect.add_event('a',self.roo)
        pygame.mouse.set_visible(False)
        self.curs = obj.Rect(pos1=(10,10), pos2=(11, 11))

    def run(self):
        x, y = pygame.mouse.get_pos()
        self.curs.set_pos(pos1=(x, y))
        self.rect.set_pos(pos1=(self.e, self.s))
        self.rect.set_color(color=(self.f, 255, self.w))
        self.rect.set_sprite(spr="1.png")
        self.rect.set_sprite_size(size=(200, 200))




def run():
    font = pygame.font.Font(None, 42)
    t1 = font.render('JGine 2.1', True, (255, 255, 255))
    fond = pygame.font.Font(None, 24)
    t2 = font.render('Loading Engine Modules', True, (255, 255, 255))
    window_width = 48
    window_height = 330
    # Load the image
    image_name = 'sprites/1.png'
    image_obj = pygame.image.load(image_name).convert()
    # Get the image's size
    image_width, image_height = image_obj.get_size()

    # Calculate the scaling factor
    scale_factor = min(window_width / image_width, window_height / image_height)

    # Calculate the new size of the image
    new_image_width = int(image_width * scale_factor)
    new_image_height = int(image_height * scale_factor)

    # Scale the image
    scaled_image = pygame.transform.scale(image_obj, (new_image_width, new_image_height))

    # Calculate the offsets so image is centered
    offset_x = (window_width - new_image_width) // 2
    offset_y = (window_height - new_image_height) // 2

    # Draw the image on the window
    config.screen.blit(scaled_image, (offset_x, offset_y))
    config.screen.blit(t1, (240-t1.get_size()[0]//2, 140))
    config.screen.blit(t2, (240-t2.get_size()[0]//2, 190))

    pygame.display.update()