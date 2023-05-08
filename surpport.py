from os import walk
import pygame
def import_folder(path):
    surface_list = []
    
    for _, __, img_f in walk(path):
        for img in img_f:
            full_path = path + '\\' +img
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list 