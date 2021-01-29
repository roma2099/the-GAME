import pygame
import pickle

from fuctions import *
from tile import *
from goblin import *
from accessorie import *




def check_object_in_list(object, object_list):
    for i in object_list:
        if object.rect.topleft == i.rect.topleft:
            return i


def add_and_remove(Entety, entety_list, cousor_entety, camera):
    cousor_entety.rect.bottomright = (int(pygame.mouse.get_pos()[0] / 32) * 32,
                                      int(pygame.mouse.get_pos()[1] / 32) * 32)

    if pygame.mouse.get_pressed() == (1, 0, 0):
        entety_i = Entety((0, 0), 0)
        entety_i.rect.x = cousor_entety.rect.x + int(camera[0] / 32) * 32
        entety_i.rect.y = cousor_entety.rect.y + int(camera[1] / 32) * 32

        if check_object_in_list(entety_i, entety_list) == None:
            entety_list.append(entety_i)


    if pygame.mouse.get_pressed() == (0, 0, 1):
        entety_i = Entety((0, 0), 0)
        entety_i.rect.x = cousor_entety.rect.x + camera[0]
        entety_i.rect.y = cousor_entety.rect.y + camera[0]

        obj_remove = check_object_in_list(entety_i, entety_list)
        if obj_remove != None:
            entety_list.remove(obj_remove)



def editor():
    pygame.init()
    screen = pygame.display.set_mode((640*2, 380*2))

    background = pygame.Surface((640*2, 380*2))
    background.fill((27, 27, 27))




    clock = pygame.time.Clock()
    keepGoing = True

    Tile.img.append((pygame.image.load("sprites/tiles/Tile_1.png").convert()))
    Goblin.frame= {'idle':[img_load("sprites/Enemies/Goblin/individual/goblin-idle-0.png",1.5)]}

    # Accessorie.img.append((pygame.image.load("sprites/tiles/Tile_1.png").convert()))
    one_tile = Tile((0, 0), 0)
    one_enemy = Goblin((0, 0),0)

    # one_accessories = Accessorie((0, 0), 0)
    tile_list = []
    enemies_list = []
    accessories_list = []
#-----------------------------
    tipo=[one_tile, one_enemy]
    tipo_list=[tile_list,enemies_list]
    tipo_class=[Tile,     Goblin ]




    camera = [0, 0]

    choise = 1
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
                    with open("maps/map_1.txt", "wb") as map_file:
                        for list in tipo_list:
                          for element in list:
                              element.rect.x *= 2
                              element.rect.y *= 2
                              element.rect.height *= 2
                              element.rect.width *= 2



                        tipo_list = [accessories_list, tile_list, enemies_list]
                        pickle.dump(tipo_list, map_file)
                        keepGoing = False

                if event.key == pygame.K_l:
                    with open("maps/map_1.txt", "rb") as map_file:

                        tipo_list = pickle.load(map_file)

                        for list in tipo_list:
                            for element in list:
                                element.rect.x *= 0.5
                                element.rect.y *= 0.5
                                element.rect.height *= 0.5
                                element.rect.width *= 0.5
                if event.key == pygame.K_1 and choise<len(tipo)-1:
                    choise +=1
                if event.key == pygame.K_2 and choise>0:
                    choise -= 1


            elif event.type == pygame.MOUSEMOTION:
                    add_and_remove(tipo_class[choise], tipo_list[choise], tipo[choise], camera)

        if k_up:
            camera[1] += -4
        if k_down:
            camera[1] += 4
        if k_left:
            camera[0] += -4
        if k_rigth:
            camera[0] += 4

        screen.blit(background,(0,0))

        for list in tipo_list:
            for element in list:
                element.draw(screen, camera)





        tipo[choise].draw(screen, (-camera[0] % 32, -camera[1] % 32))


        pygame.display.update()



editor()