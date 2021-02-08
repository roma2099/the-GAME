import os
import pickle

import pygame

import skeleton
import tile
from goblin import Goblin


def img_load(file_directory, scale=1):
    img = pygame.image.load(file_directory).convert_alpha()
    return pygame.transform.scale(img, (int(scale * img.get_rect().size[0]), int(scale * img.get_rect().size[1])))

def get_files_from_directory(directory):
    files = os.listdir(directory)

    i = 0
    for file in files:
        files[i] = directory + "\\" + file.lower()

        i += 1

    return files
def get_map(directory):
    tiles=get_files_from_directory("sprites/tile/individual")
    for i in tiles:
        tile.Tile.img.append(img_load(i, 2))



    accessories_list = []
    with open("maps/map_1.txt", "rb") as map_file:
        list = pickle.load(map_file)



    return list

def make_dic_images(files, actions, scale=3):
    frame = {}
    for action in actions:
        frame[action] = []
    for asset in files:
        # fuction img_load in main makes the load and scaling
        # 2 IS THE SCALE

        i = img_load(asset, scale)

        for key in frame.keys():
            if key in asset:
                frame[key].append(i)
    return frame

def fix_enemy(enteties_list,entetie_class=None):
    new_list=[]
    x=100
    for entety in enteties_list:
        print(entety.rect.center)
        new_list.append(entetie_class(entety.rect.center))
        x+=100

    return new_list
def draw_backgound(screen, images, camera):
    bg_move = 0
    num = 2
    for image in images:
        for i in range(-1, num):
            screen.blit(image,
                        (i * image.get_width() - int(camera[0] * bg_move), screen.get_height() - image.get_height() ))
        bg_move += 0.05
        num += 1

    return
def draw_live_bar(screen,hp,hp_max,position,camera=(0,0)):

    barra=pygame.Rect(position[0],position[1],400,80)
    conteudo=pygame.Rect(position[0],position[1],int(barra.width*(hp/hp_max)),barra.height)
    pygame.draw.rect(screen, (200, 20, 60, ), conteudo, 0, 6)
    pygame.draw.rect(screen,(200,200,200,200),barra,10,6)





def game_over():
    print("GAME OVER")



