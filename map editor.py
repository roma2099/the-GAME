import pygame
import pickle
import skeleton,mushroom,random,templates,spikes
from fuctions import *
from tile import *
from goblin import *
from accessorie import *




def generate_level(tile_list):
    # Creating the solution path list
    tile_list.clear()
    level = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    row = 0
    # Placing the entrance randomly
    col = random.randint(0, 3)

    level[row][col] = 1
    while True:
        direction = random.randint(1, 5)

        previous = (row, col)

        if direction == 1 or direction == 2:
            col -= 1
        elif direction == 3 or direction == 4:
            col += 1
        else:
            row += 1

        if col < 0:
            col += 1
            row += 1

        if col > 3:
            col -= 1
            row += 1

        if row > 3:
            break

        if previous[0] < row:
            level[previous[0]][previous[1]] = 2
            level[row][col] = 3
        elif level[row][col] == 0:
            level[row][col] = 1


    for rows in range(0,len(level)):

        for cols in range(0,len(level[rows])):
            # Switching to the correct template
            if cols == 0:
                current_template = templates.templates_all[random.randrange(0, len(templates.templates_all))]
            if cols == 1:
                current_template = templates.templates_lr[random.randrange(0, len(templates.templates_lr))]
            elif cols == 2:
                current_template = templates.templates_tlbr[random.randrange(0, len(templates.templates_tlbr))]
            elif cols == 3:
                current_template = templates.templates_tlr[random.randrange(0, len(templates.templates_tlr))]



            # Randomly flip the template
            if random.randint(0, 1) == 1:
                for flip in current_template:
                    flip.reverse()
            level[rows][cols]=current_template


            for temp_rows in range(0,len(current_template)):

                for temp_cols in range(0,len(current_template[temp_rows])):
                    if current_template[temp_rows][temp_cols] == 1:
                        new_tile = Tile((16+temp_cols*32+cols*16*32,16+temp_rows*32+rows*16*32), 0)
                        tile_list.append(new_tile)


    return level


def fixe_tiles(tile_list):

    for tile in tile_list:
        up = False
        down = False
        left = False
        right = False
        for neibor in tile_list:
            if neibor.rect.center== (tile.rect.center[0],tile.rect.center[1]-tile.rect.height):
                up=True
            if neibor.rect.center == (tile.rect.center[0], tile.rect.center[1] + tile.rect.height):
                down=True
            if neibor.rect.center == (tile.rect.center[0]- tile.rect.width, tile.rect.center[1] ):
                left=True
            if neibor.rect.center == (tile.rect.center[0]+ tile.rect.width, tile.rect.center[1]):
                right=True

        if up and down and left and right:
            tile.index=0
        elif not up and down and not left and right:
            tile.index=4
        elif up and down and not left and right:
            tile.index=1
        elif up and not down and not left and right:
            tile.index=2
        elif  not up and  down and left and right:
            tile.index=5
        elif up and not down and left and right:
            tile.index=7
        elif not up and down and left and not right:
            tile.index=10
        elif  up and down and left and not right:
            tile.index=11
        elif up and not down and left and not  right:
            tile.index=12
        elif not up and down and not left and not right:
            tile.index=15
        elif  up and down and not left and not right:
            tile.index=16
        elif up and not down and not left and not right:
            tile.index=17
        elif  left and right:
            tile.index=5
        elif not left and right:
            tile.index=4
        elif  left and not right:
            tile.index=10
        else :
            tile.index=15





def check_object_in_list(object, object_list):
    for i in object_list:
        if object.rect.topleft == i.rect.topleft:
            return i


def add_and_remove(Entety, entety_list, cousor_entety, camera):
    cousor_entety.rect.center = (int(pygame.mouse.get_pos()[0] / 32) * 32,
                                      int(pygame.mouse.get_pos()[1] / 32) * 32)

    if pygame.mouse.get_pressed() == (1, 0, 0):
        entety_i = Entety((0, 0), 0)
        entety_i.rect.x = cousor_entety.rect.x + int(camera[0] / 32) * 32
        entety_i.rect.y = cousor_entety.rect.y + int(camera[1] / 32) * 32

        if check_object_in_list(entety_i, entety_list) == None:
            entety_list.append(entety_i)


    if pygame.mouse.get_pressed() == (0, 0, 1):
        entety_i = Entety((0, 0), 4)
        entety_i.rect.x = cousor_entety.rect.x + int(camera[0] / 32) * 32
        entety_i.rect.y = cousor_entety.rect.y + int(camera[1] / 32) * 32

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

    tiles = get_files_from_directory("sprites/tile/individual")
    for i in tiles:
        tile.Tile.img.append(img_load(i, 1))

    Goblin.frame= {'idle':[img_load("sprites/Enemies/Goblin/individual/goblin-idle-00.png",1.5)]}
    skeleton.Skeleton.frame = {'idle': [img_load("sprites/Enemies/Skeleton/individual/skeleton-idle-0.png", 1.5)]}
    mushroom.Mushroom.frame = {'idle': [img_load("sprites/Enemies/Mushroom/individual/mushroom-idle-00.png", 1.5)]}
    spikes.Spikes.frames=[img_load("sprites/Spikes/spikes6.png",1)]
    # Accessorie.img.append((pygame.image.load("sprites/tiles/Tile_1.png").convert()))
    one_tile = Tile((0, 0), 0)
    one_goblin = Goblin((0, 0),0)
    one_mushroom=mushroom.Mushroom((0,0),0)
    one_skeleton = skeleton.Skeleton((0, 0), 0)
    one_spike= spikes.Spikes((0,0),0)

    # one_accessories = Accessorie((0, 0), 0)
    spike_list=[]
    tile_list = []
    goblin_list = []
    skeleton_list = []
    mushroom_list =[]
    accessories_list = []
#-----------------------------
    tipo=[one_tile, one_goblin,one_mushroom,one_skeleton,one_spike]
    tipo_list=[tile_list,goblin_list,mushroom_list,skeleton_list,spike_list]
    tipo_class=[Tile,     Goblin ,mushroom.Mushroom,skeleton.Skeleton,spikes.Spikes]




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
                if event.key == pygame.K_f:
                    fixe_tiles(tile_list)
            #-------------------------------------------------
                if event.key == pygame.K_g:
                    print (generate_level(tile_list))

                if event.key == pygame.K_s:
                    with open("maps/map_1.txt", "wb") as map_file:
                        for list in tipo_list:
                          for element in list:
                              element.rect.x *= 2
                              element.rect.y *= 2
                              element.rect.height *= 2
                              element.rect.width *= 2
                              print (element.rect.center)



                        tipo_list=[tile_list,goblin_list,mushroom_list,skeleton_list]
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
                                print(element.rect.center)
                if event.key == pygame.K_1 and choise<len(tipo)-1:
                    choise +=1
                if event.key == pygame.K_2 and choise>0:
                    choise -= 1


            elif event.type == pygame.MOUSEMOTION:
                    add_and_remove(tipo_class[choise], tipo_list[choise], tipo[choise], camera)

        if k_up:
            camera[1] += -32
        if k_down:
            camera[1] += 32
        if k_left:
            camera[0] += -32
        if k_rigth:
            camera[0] += 32

        screen.blit(background,(0,0))

        for list in tipo_list:
            for element in list:
                if type (element) is not Tile:
                    element.hit_box.center=element.rect.center
                element.draw(screen, camera)






        tipo[choise].draw(screen, (-camera[0]/32 , -camera[1]/32 ))


        pygame.display.update()



editor()