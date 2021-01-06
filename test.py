
import pickle
from tile import *
from enemy import *
from accessorie import *
pygame.init()
screen=pygame.display.set_mode((200,200))

Tile.img.append((pygame.image.load("sprites/tiles/Tile_1.png").convert()))
Enemy.img.append((pygame.image.load("sprites/Enemies/Idle 1.png").convert()))
Enemy.img.append((pygame.image.load("sprites/Enemies/Idle 2.png").convert()))
Accessorie.img.append((pygame.image.load("sprites/tiles/Tile_1.png").convert()))

one_tile=Tile(0,0,0)
one_enemies = Enemy(0, 0, 0)
one_accessories = Accessorie(0, 0, 0)

tile_list = [one_tile]
enemies_list = [Enemy(0, 0, 0)]
accessories_list = [one_accessories]
list=[]



with open("maps/map_1.txt","wb") as map_file:

        for t in tile_list:
            t.rect.x *= 2
            t.rect.y *= 2
            list.append(t)

        for e in enemies_list:
            e.rect.x *= 2
            e.rect.y *= 2
            list.append(e)
        for a in accessories_list:
            a.rect.x *= 2
            a.rect.y *= 2
            list.append(a)
        pickle.dump(list, map_file)