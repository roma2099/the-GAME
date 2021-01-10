# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame, player, sys, os, tile, enemy, accessorie, pickle


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


def img_load(file_directory, scale):
    img = pygame.image.load(file_directory).convert_alpha()
    return pygame.transform.scale(img, (scale * img.get_rect().size[0], scale * img.get_rect().size[1]))


def get_map(directory):
    tile.Tile.img.append(img_load("sprites/tiles/Tile_1.png", 2))

    tile_list = []
    enemies_list = []
    accessories_list = []
    with open("maps/map_1.txt", "rb") as map_file:
        list = pickle.load(map_file)

        accessories_list, tile_list, enemies_list = list[0], list[1], list[2]

    return accessories_list, tile_list, enemies_list


def draw_backgound(screen, images, camera):
    bg_move = 0
    num = 1
    for image in images:
        for i in range(0, num):
            screen.blit(image,
                        (i * image.get_width() - int(camera[0] * bg_move), screen.get_height() - image.get_height()))
        bg_move += 0.05
        num += 1

    return


def get_files_from_directory(directory):
    files = os.listdir(directory)

    i = 0
    for file in files:
        files[i] = directory + "/" + file
        i += 1

    return files


def game_over():
    print("GAME OVER")

    # START OF CODE ----------------------------------------------------------


pygame.init()

screen_size = (272 * 4, 160 * 4)
screen = pygame.display.set_mode(screen_size)

bg = []

for i in get_files_from_directory("sprites/background"):
    x = img_load(i, 4)

    bg.append(x)

    ##bg.fill((100, 200, 150))
frame = make_dic_images(get_files_from_directory("sprites/Individual Sprites"),
                        ["run", "fall", "die", "hurt", "idle","crouch", "jump", "attack1", "attack2", "attack3"])

mc = player.Player(frame, (100, 100))

# HACK
mc.movement = [0, 0]

accessories_list, barriers, enemies_list = get_map("sprites/tiles")

camera = [0, 0]

clock = pygame.time.Clock()

k_left = False
k_right = False
k_space = False
k_down = False
k_up = False
k_x = False
k_y = False
k_r = False

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 80)

# GAME LOOP-------------------------------------------------------------------------------

while True:
    k_space = False
    k_x = False

    # EVENTS------------------------------------------------------------------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == BIRDFLAP:
        #    mc.animation()
        # I whant to now when the animation , so i need to animated inside the controle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                k_down = True

            if event.key == pygame.K_UP:
                k_up = True

            if event.key == pygame.K_RIGHT:
                k_right = True

            elif event.key == pygame.K_LEFT:
                k_left = True

            if event.key == pygame.K_x:
                k_x = True

            if event.key == pygame.K_r:
                mc.hit_box.center = (0, 0)
                mc.movement = [0, 0]
                mc.hp = mc.hp_max

            if event.key == pygame.K_SPACE:
                k_space = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                k_up = False
            if event.key == pygame.K_DOWN:
                k_down = False
            if event.key == pygame.K_RIGHT:
                k_right = False
                # maybe it should be just if
            elif event.key == pygame.K_LEFT:
                k_left = False

    # CAMERA ----------------------------------------------------------------------------------------------
    camera[0] += (mc.rect.centerx - camera[0] - screen.get_height()) / 7
    camera[1] += (mc.rect.centery - camera[1] - screen.get_height() * (6 / 10)) / 7

    # ------------------------------------------------------------------------------------------------------
    mc.controle(k_up, k_down, k_left, k_right, k_space, k_x, False)

    mc.move(barriers)
    for enemy in enemies_list:
        enemy.move(barriers)
    draw_backgound(screen, bg, camera)

    for barreira in barriers:
        barreira.draw(screen, camera)

        #      if k_x :
        #         for enemy in enemys:
        #            if mc.attack(enemy.rect):
        #               enemy.hp-=5
        #              print(enemy.hp)
        # for enemy in enemys:
        #     if enemy.die():
        #         enemys.remove(enemy)
        #     enemy.draw_player(screen,(255, 50, 50))
    #    for enemy in enemies_list:
    #       enemy.draw(screen,camera)
    mc.update()
    mc.draw(screen, camera)

    pygame.display.update()
    clock.tick(40)
