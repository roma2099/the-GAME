# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame, player, sys, os, tile, enemy, accessorie, pickle
from fuctions import *




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


player.Player.frame=make_dic_images(get_files_from_directory("sprites/Martial artist/individual"),["run", "fall", "die", "hurt", "idle","crouch", "jump", "attack1", "attack2", "attack3"])
enemy.Enemy.frame=make_dic_images(get_files_from_directory("sprites/Enemies"),["idle"])
mc = player.Player( (100, 100))

# HACK


accessories_list, barriers, enemies_list = get_map("sprites/tiles")
for x in enemies_list:
    x.hit_box=x.rect
    x.test_mode=True

print(enemies_list)
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

e=enemy.Enemy((200 ,200))
e.hp,e.hp_max=5000,5000

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
            if event.key == pygame .K_DOWN:
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




    draw_backgound(screen, bg, camera)
    e.draw(screen, camera)
    e.move(barriers)

    if mc.attack(e, screen, camera):
        e.hp -= 1
        print(e.hp)
    for barreira in barriers:
        barreira.draw(screen, camera)
    for r in enemies_list:

        r.draw(screen, camera)
        r.move(barriers)

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
