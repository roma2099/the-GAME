import pygame
import pickle
from tile import *
from enemy import *
from accessorie import *

def check_object_in_list(object,object_list):

    for i in object_list:
        if object.rect.topleft == i.rect.topleft:
            return i

def add_and_remove(Entety,entety_list,cousor_entety,camera ):


    cousor_entety.rect.bottomright = (int(pygame.mouse.get_pos()[0] / 32) * 32,
                                 int(pygame.mouse.get_pos()[1] / 32) * 32)

    if pygame.mouse.get_pressed() == (1, 0, 0):
        entety_i = Entety(0, 0, 0)
        entety_i.rect.x = cousor_entety.rect.x+ camera[0]
        entety_i.rect.y = cousor_entety.rect.y+camera[1]

        if check_object_in_list(entety_i, entety_list) == None:
            entety_list.append(entety_i)
        print(entety_list)

    if pygame.mouse.get_pressed() == (0, 0, 1):
        entety_i = Entety(0, 0, 0)
        entety_i.rect.x = cousor_entety.rect.x + camera[0]
        entety_i.rect.y = cousor_entety.rect.y + camera[0]

        obj_remove = check_object_in_list( entety_i,  entety_list)
        if obj_remove != None:
            entety_list.remove(obj_remove)
        print( entety_list)
def main():

    pygame.init()
    screen = pygame.display.set_mode((640, 480))


    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))


    clock = pygame.time.Clock()
    keepGoing = True

    Tile.img.append((pygame.image.load("sprites/tiles/Tile_1.png").convert()))
    Enemy.img.append((pygame.image.load("sprites/Enemies/Idle 1.png").convert_alpha()))
    Enemy.img.append((pygame.image.load("sprites/Enemies/Idle 2.png").convert()))
    #Accessorie.img.append((pygame.image.load("sprites/tiles/Tile_1.png").convert()))
    one_tile=Tile(0,0,0)
    one_enemies = Enemy(0, 0, 0)
   #one_accessories = Accessorie(0, 0, 0)

    tile_list = []
    enemies_list = []
    accessories_list = []

    camera=[0,0]

    choise=1
    k_down = False
    k_up = False
    k_left = False
    k_rigth = False
    while keepGoing:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_DOWN:
                    k_down = False
                if event.key == pygame.K_UP:
                    k_up = False
                if event.key == pygame.K_LEFT:
                    k_left = False
                if event.key == pygame.K_RIGHT:
                    k_rigth = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    k_down = True
                if event.key == pygame.K_UP:
                    k_up = True
                if event.key == pygame.K_LEFT:
                    k_left = True
                if event.key == pygame.K_RIGHT:
                    k_rigth = True

                if event.key == pygame.K_s:
                    with open("maps/map_1.txt","wb") as map_file:

                        for t in tile_list:
                            t.rect.x *= 2
                            t.rect.y *= 2

                        for e in enemies_list:
                            e.rect.x *= 2
                            e.rect.y *= 2

                        for a in accessories_list:
                            a.rect.x *= 2
                            a.rect.y *= 2

                        list=[accessories_list,tile_list,enemies_list]
                        print(list)
                        pickle.dump(list,map_file)
                        keepGoing=False


                if event.key == pygame.K_l:
                    with open("maps/map_1.txt", "rb") as map_file:

                        list = pickle.load(map_file)
                        accessories_list, tile_list, enemies_list = list[0], list[1], list[2]
                        for t in tile_list:
                            t.rect.x *= 0.5
                            t.rect.y *= 0.5

                        for e in enemies_list:
                            e.rect.x *= 0.5
                            e.rect.y *=0.5

                        for a in accessories_list:
                            a.rect.x *= 0.5
                            a.rect.y *= 0.5

                if event.key == pygame.K_1:
                    choise = 1
                if event.key == pygame.K_2:
                    choise = 2


            elif event.type == pygame.MOUSEMOTION:
                if choise==1:
                    add_and_remove(Tile,tile_list,one_tile,camera)
                else:
                    add_and_remove(Enemy, enemies_list, one_enemies,camera)


        if k_up:
            camera[1]+=-4
        if k_down:
            camera[1]+=4
        if k_left:
            camera[0]+=-4
        if k_rigth:
            camera[0]+=4



        screen.blit(background, (0, 0))

        for i in accessories_list:
            i.draw(screen,camera)

        for i in tile_list:
            i.draw(screen,camera)
            #print(i.rect.x,i.rect.y)
        for i in enemies_list:
            i.draw(screen,camera)

        if choise==1:
            one_tile.draw(screen,(0,0))
        else:
            one_enemies.draw(screen,(0,0))

        pygame.display.update()


main()