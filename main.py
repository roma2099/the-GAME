# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame, player, sys, os, tile, enemy, accessorie, pickle, skeleton,mushroom,boss
from particle import *
from fuctions import *
from goblin import *



titulo="Something Something"
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)




def main_menu():
    font = pygame.font.SysFont("fixedsys", 69)
    click = False
    volume=1
    music = pygame.mixer.music.load(
        "sounds/sound track/preview.mp3")
    pygame.mixer.music.play(-1)
    selecionar=pygame.mixer.Sound("sounds/sound efect/menu/select.mp3")
    confirmar = pygame.mixer.Sound("sounds/sound efect/menu/corfimar.mp3")
    cor1=(55, 200, 129)
    cor2=(55, 20, 129)
    while True:

        screen.fill((27, 27, 27))
        draw_text(titulo, font, (255, 255, 255), screen, screen_size[0]/2, 100)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(screen_size[0]/2-200, 200, 400, 100)

        button_2 = pygame.Rect(screen_size[0]/2-200, 400, 400, 100)


        if button_1.collidepoint((mx, my)):
            if cor1!= (129, 20, 55):
                cor1 = (129, 20, 55)
                selecionar.play()

            if click:
                confirmar.play()
                pygame.mixer.fadeout(1000)
                clock.tick(1)
                level_1(volume)
                music = pygame.mixer.music.load(
                    "sounds/sound track/preview.mp3")
                pygame.mixer.music.play(-1)
        else:
            cor1 = (129, 200, 55)

        if button_2.collidepoint((mx, my)):
            if cor2!= (129, 20, 55):
                selecionar.play()
                cor2 = (129, 20, 55)
            cor2 = (129, 20 , 55)
            if click:
                confirmar.play()
                pygame.mixer.fadeout(1000)
                clock.tick(1)
                volume=options(volume)
        else:
            cor2 = (129, 200, 55)

        pygame.draw.rect(screen,cor1 , button_1)
        pygame.draw.rect(screen, cor2, button_2)
        draw_text("Start", font, (255, 255, 255), screen, button_1.center[0], button_1.center[1])
        draw_text("Options", font, (255, 255, 255), screen, button_2.center[0], button_2.center[1])
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        clock.tick(60)

def options(volume):
    font = pygame.font.SysFont("fixedsys", 60)

    click = False

    selecionar=pygame.mixer.Sound("sounds/sound efect/menu/select.mp3")
    confirmar = pygame.mixer.Sound("sounds/sound efect/menu/corfimar.mp3")
    cor1=(55, 200, 129)
    cor2=(55, 20, 129)
    cor3=(0,0,0)
    while True:

        screen.fill((27, 27, 27))
        draw_text(titulo, font, (255, 255, 255), screen, screen_size[0]/2, 100)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(200, 200, 100, 100)

        button_2 = pygame.Rect(screen_size[0]-200, 200, 100, 100)
        exit_button= pygame.Rect(screen_size[0]/2-200, screen_size[1]-200, 400, 100)

        if button_1.collidepoint((mx, my)):
            if cor1!= (129, 20, 55):
                cor1 = (129, 20, 55)
                selecionar.play()

            if click:
                confirmar.play()
                print(pygame.mixer.music.get_volume())
                volume = pygame.mixer.music.get_volume() - 0.1
                if volume < 0:
                    volume = 0
                pygame.mixer.music.set_volume(volume)
                clock.tick(2)
        else:
            cor1 = (129, 200, 55)

        if button_2.collidepoint((mx, my)):
            if cor2!= (129, 20, 55):
                selecionar.play()
                cor2 = (129, 20, 55)
            cor2 = (129, 20 , 55)
            if click:
                confirmar.play()
                print(pygame.mixer.music.get_volume())
                volume=pygame.mixer.music.get_volume() +0.1
                if volume>1:
                    volume=1
                pygame.mixer.music.set_volume(volume)
                clock.tick(2)
        else:
            cor2=(129, 200, 55)

        if exit_button.collidepoint((mx, my)):
            if cor3!= (129, 20, 55):
                selecionar.play()
                cor3 = (129, 20, 55)
            cor3 = (129, 20 , 55)
            if click:
                confirmar.play()

                clock.tick(2)
                return volume
        else:
            cor3 = (129, 200, 55)





        pygame.draw.rect(screen,cor1 , button_1)
        pygame.draw.rect(screen, cor2, button_2)
        pygame.draw.rect(screen,cor3,exit_button)
        draw_text("<", font, (255, 255, 255), screen, button_1.center[0], button_1.center[1])
        draw_text(">", font, (255, 255, 255), screen, button_2.center[0], button_2.center[1])
        draw_text("back", font, (255, 255, 255), screen, exit_button.center[0], exit_button.center[1])
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        clock.tick(60)


def level_1(volume):
    global goblin_list,skeletom_list,mushroom_list
    mc = player.Player((100, 100))



    # HACK40«

    list = get_map("sprites/tiles")
    barriers = list[0]
    goblin_list = fix_enemy(list[1], Goblin)  # Goblins
    mushroom_list = fix_enemy(list[1], mushroom.Mushroom)
    skeletom_list = fix_enemy(list[1], skeleton.Skeleton)

    # enemies_list =[mushroom.Mushroom(enemies_list[0].rect.center)]

    camera = [0, 0]

    BIRDFLAP = pygame.USEREVENT + 1
    pygame.time.set_timer(BIRDFLAP, 80)

    goblin_1 = Goblin((200, 200))
    goblin_1.hp, goblin_1.hp_max = 5000, 5000

    skeleton_1 = skeleton.Skeleton((800, 200))
    skeleton_1.hp, skeleton_1.hp_max = 5000, 5000

    mushroom_1 = mushroom.Mushroom((1000, 200))
    particles_list = []

    wizard=boss.Boss((1000, 200))
    w_list=[wizard]

    k_left = False
    k_right = False
    k_space = False
    k_down = False
    k_up = False
    k_j = False
    k_k = False
    k_l = False

    k_r = False

    music = pygame.mixer.music.load("sounds/sound track/Yoann Laulan - Dead Cells - Soundtrack Part 1 - 32 Arboretum.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume)
    mushroom_list.append(mushroom_1)
    while True:
        if mc.frame_on=="death"and mc.frame_index >=9:
            return
        k_space = False
        k_j = False
        k_l=False


        # EVENTS------------------------------------------------------------------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == BIRDFLAP:
            #    mc.animation()
            # I whant to now when the animation , so i need to animated inside the controle
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    k_down = True

                if event.key == pygame.K_w:
                    k_up = True

                if event.key == pygame.K_d:
                    k_right = True

                elif event.key == pygame.K_a:
                    k_left = True

                if event.key == pygame.K_k:
                    k_k = True
                if event.key == pygame.K_j:
                    k_j = True

                if event.key == pygame.K_r:
                    mc.hit_box.center = (0, 0)
                    mc.movement = [0, 0]
                    mc.hp = mc.hp_max

                if event.key == pygame.K_SPACE:
                    k_space = True
                if event.key==pygame.K_l:

                    k_l=True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    k_up = False
                if event.key == pygame.K_s:
                    k_down = False
                if event.key == pygame.K_d:
                    k_right = False
                    # maybe it should be just if
                elif event.key == pygame.K_a:
                    k_left = False
                if event.key == pygame.K_k:
                    k_k = False

        # CAMERA ----------------------------------------------------------------------------------------------
        camera[0] += (mc.rect.centerx - camera[0] - screen.get_height()) / 7
        camera[1] += (mc.rect.centery - camera[1] - screen.get_height() * (6 / 10)) / 7

        # ------------------------------------------------------------------------------------------------------

        mc.controle(k_up, k_down, k_left, k_right, k_space, k_j, k_k,k_l)

        mc.move(barriers)

        draw_backgound(screen, bg, camera)

        for barreira in barriers:
            barreira.draw(screen, camera)
        for particle in particles_list:
            if particle.particle_list == []:
                particles_list.remove(particle)
            particle.draw(screen, camera)
        #------------------------------------



        #------------------------------------
        list_list=[w_list]
        for enemy_list in list_list:
            for enemy in enemy_list:

                mc.push(enemy)

                if enemy.attack(mc):
                    mc.damage(50)
                    print(mc.hp)

                if mc.attack(enemy.hit_box):

                    enemy.damage(50)
                    print(enemy.hp)

                enemy.draw(screen, camera)
                enemy.move(barriers)

                enemy.ai(mc, barriers)

                if enemy.hp <= 0:
                    particles_list.append(Particle(enemy.rect.center, 16, (153, 10, 0), 90, 90))
                    particles_list.append(
                        Particle((enemy.rect.center[0], enemy.rect.center[1] - 45), 16, (153, 0, 10), 90, 90))
                    particles_list.append(
                        Particle((enemy.rect.center[0], enemy.rect.center[1] + 45), 16, (153, 4, 18), 90, 90))
                    enemy_list.remove(enemy)
        # for r in enemies_list:

        #     r.draw(screen, camera)
        #    r.move(barriers)

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
        draw_live_bar(screen,mc.hp,mc.hp_max,( 20,20))

        pygame.display.update()
        clock.tick(40)


    # START OF CODE ----------------------------------------------------------


pygame.init()

screen_size = (272 * 4, 160 * 4)
screen = pygame.display.set_mode(screen_size)

bg = []

for i in get_files_from_directory("sprites/background"):
    x = img_load(i, 4)

    bg.append(x)

    ##bg.fill((100, 200, 150))


player.Player.frame= make_dic_images(get_files_from_directory("sprites/player/Hero Knight/individual"),["run", "fall", "death", "hurt", "idle", "crouch", "jump", "attack1", "attack2","attack3","block idli","roll"])
Goblin.frame= make_dic_images(get_files_from_directory("sprites/Enemies/Goblin/individual"), ["idle","run","death","attack","shield","take"])
skeleton.Skeleton.frame= make_dic_images(get_files_from_directory("sprites/Enemies/Skeleton/individual"), ["idle","run","death","attack","shield","take"])
mushroom.Mushroom.frame = make_dic_images (get_files_from_directory("sprites/Enemies/Mushroom/individual"), ["idle","run","death","attack","shield","take"])
boss.Boss.frame= make_dic_images(get_files_from_directory("sprites/Enemies/Boss 2/individual"), ["idle","run","death","attack","shield","take"])
player.Player.sound={"attack1":pygame.mixer.Sound("sounds/sound efect/player/espada 1.mp3"),"attack2":pygame.mixer.Sound("sounds/sound efect/player/espada 2.mp3"),"attack3":pygame.mixer.Sound("sounds/sound efect/player/espada 3.mp3"),"run":pygame.mixer.Sound("sounds/sound efect/player/run1.mp3"),"jump":pygame.mixer.Sound("sounds/sound efect/player/Jump sound effect.mp3")}
#Goblin.sound={"run":pygame.mixer.Sound("sounds/sound efect/goblin/run.mp3"), "attack":pygame.mixer.Sound("sounds/sound efect/goblin/ataque.mp3"), "hurt":pygame.mixer.Sound("sounds/sound efect/goblin/hit.mp3")}
#skeleton.Skeleton.sound={"run":pygame.mixer.Sound("sounds/sound efect/Skeleton/andar.mp3"), "attack":pygame.mixer.Sound("sounds/sound efect/Skeleton/ataque.mp3"),"hurt":pygame.mixer.Sound("sounds/sound efect/Skeleton/hit.mp3")}
mushroom.Mushroom.sound={"run":pygame.mixer.Sound("sounds/sound efect/Mushroom/run.mp3"), "attack":pygame.mixer.Sound("sounds/sound efect/Mushroom/ataque.mp3"), "hurt":pygame.mixer.Sound("sounds/sound efect/Mushroom/hit.mp3")}



clock = pygame.time.Clock()

pygame.mixer.pre_init(44100,-16,2,512)






main_menu()

# GAME LOOP-------------------------------------------------------------------------------


