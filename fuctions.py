import os
import pickle

import pygame

import tile

def img_load(file_directory, scale):
    img = pygame.image.load(file_directory).convert_alpha()
    return pygame.transform.scale(img, (scale * img.get_rect().size[0], scale * img.get_rect().size[1]))

def get_files_from_directory(directory):
    files = os.listdir(directory)

    i = 0
    for file in files:
        files[i] = directory + "/" + file.lower()

        i += 1

    return files
def get_map(directory):
    tile.Tile.img.append(img_load("sprites/tiles/Tile_1.png", 2))

    tile_list = []
    enemies_list = []
    accessories_list = []
    with open("maps/map_1.txt", "rb") as map_file:
        list = pickle.load(map_file)

        accessories_list, tile_list, enemies_list = list[0], list[1], list[2]

    return accessories_list, tile_list, enemies_list

def make_dic_images(files, actions):
    frame = {}
    for action in actions:
        frame[action] = []
    for asset in files:
        # fuction img_load in main makes the load and scaling
        # 2 IS THE SCALE

        i = img_load(asset, 3)

        for key in frame.keys():
            if key in asset:
                frame[key].append(i)
    return frame


