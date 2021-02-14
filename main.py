# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import  player, sys, os, tile, enemy, accessorie, pickle, skeleton,mushroom,boss,projectil,goblin
import pygame

from particle import *
from fuctions import *
from goblin import *



titulo="Death Souls"


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)




def main_menu():


    font = pygame.font.SysFont("courier", 69)
    font_titulo =  pygame.font.SysFont("courier", 90,True)
    click = False
    volume=1
    music = pygame.mixer.music.load(
        "sounds/sound track/preview.mp3")
    pygame.mixer.music.play(-1)
    selecionar=pygame.mixer.Sound("sounds/sound efect/menu/select.mp3")
    confirmar = pygame.mixer.Sound("sounds/sound efect/menu/corfimar.mp3")
    cor1=(55, 200, 129)
    cor2=(55, 20, 129)
    cor3=(55, 200,129)
    while True:

        screen.fill((27, 27, 27))
        draw_text(titulo, font_titulo, (255, 255, 255), screen, screen_size[0]/2, 100)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(screen_size[0]/2-200, 200, 400, 100)

        button_2 = pygame.Rect(screen_size[0]/2-200, 350, 400, 100)

        button_3 = pygame.Rect(screen_size[0] / 2 - 200, 500, 400, 100)


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
                selecionar.set_volume(volume)
                confirmar.set_volume(volume)
        else:
            cor2 = (129, 200, 55)

        if button_3.collidepoint((mx, my)):
            if cor3!= (129, 20, 55):
                selecionar.play()
                cor3 = (129, 20, 55)
            cor3 = (129, 20 , 55)
            if click:
                confirmar.play()
                pygame.mixer.fadeout(1000)
                clock.tick(1)
                quit()
        else:
            cor3 = (129, 200, 55)

        pygame.draw.rect(screen,cor1 , button_1,5,20)
        pygame.draw.rect(screen, cor2, button_2,5,20)
        pygame.draw.rect(screen, cor3, button_3, 5, 20)
        draw_text("Start", font, (240, 240, 240), screen, button_1.center[0], button_1.center[1])
        draw_text("Options", font, (240, 240, 240), screen, button_2.center[0], button_2.center[1])
        draw_text("Exit", font, (240, 240, 240), screen, button_3.center[0], button_3.center[1])
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
    font = pygame.font.SysFont("courier", 69)
    font_titulo = pygame.font.SysFont("courier", 90, True)

    click = False

    selecionar=pygame.mixer.Sound("sounds/sound efect/menu/select.mp3")
    confirmar = pygame.mixer.Sound("sounds/sound efect/menu/corfimar.mp3")
    cor1=(55, 200, 129)
    cor2=(55, 20, 129)
    cor3=(0,0,0)
    while True:

        screen.fill((27, 27, 27))
        draw_text("Options", font_titulo, (255, 255, 255), screen, screen_size[0]/2, 100)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(200, 200, 100, 100)
        button_2 = pygame.Rect(screen_size[0]-200-100, 200, 100, 100)
        barra=pygame.Rect(320,225,700,20)
        circulo=pygame.Rect(320,225,40,100)
        barra.center=(screen_size[0]/2,250)
        circulo.center =(350 + 660*volume,250)
        exit_button= pygame.Rect(screen_size[0]/2-200, screen_size[1]-200, 400, 100)

        if button_1.collidepoint((mx, my)):
            if cor1!= (129, 20, 55):
                cor1 = (129, 20, 55)
                selecionar.set_volume(volume)
                selecionar.play()

            if click:
                confirmar.set_volume(volume)
                confirmar.play()
                print(pygame.mixer.music.get_volume())
                volume = pygame.mixer.music.get_volume() - 0.05
                if volume < 0:
                    volume = 0
                pygame.mixer.music.set_volume(volume)
                clock.tick(2)
        else:
            cor1 = (129, 200, 55)

        if button_2.collidepoint((mx, my)):
            if cor2!= (129, 20, 55):
                selecionar.set_volume(volume)
                selecionar.play()
                cor2 = (129, 20, 55)
            cor2 = (129, 20 , 55)
            if click:
                confirmar.set_volume(volume)
                confirmar.play()
                print(pygame.mixer.music.get_volume())
                volume=pygame.mixer.music.get_volume() +0.05
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





        pygame.draw.rect(screen,cor1 , button_1,5,30)
        pygame.draw.rect(screen, cor2, button_2,5,30)
        pygame.draw.rect(screen,cor3,exit_button,5,20)

        pygame.draw.rect(screen, (129, 200, 55), barra, 0, 20)
        pygame.draw.rect(screen,  (55, 129, 200), circulo, 0, 20)



        draw_text("-", font, (255, 255, 255), screen, button_1.center[0], button_1.center[1])
        draw_text("+", font, (255, 255, 255), screen, button_2.center[0], button_2.center[1])
        draw_text("Back", font, (255, 255, 255), screen, exit_button.center[0], exit_button.center[1])
        click = False
        selecionar.set_volume(volume)
        confirmar.set_volume(volume)
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


def draw_enemy_count(screen, param, enemy_num):
    global font_count

    textobj = font_count.render(("Enemies:"+str(enemy_num)+"/"+str(param)), 1, (255,255,255))
    textrect = textobj.get_rect()
    textrect.center = (1150,40)
    screen.blit(textobj, textrect)



def level_1(volume):
    projectil.Projectil.frame = make_dic_images(get_files_from_directory("sprites/projectile/individual"),
                                                ["ball", "explosion"])
    player.Player.frame = make_dic_images(get_files_from_directory("sprites/player/Hero Knight/individual"),
                                          ["run", "fall", "death", "hurt", "idle", "crouch", "jump", "attack1",
                                           "attack2", "attack3", "block idli", "roll", "grab"])
    Goblin.frame = make_dic_images(get_files_from_directory("sprites/Enemies/Goblin/individual"),
                                   ["idle", "run", "death", "attack", "shield", "take"])
    skeleton.Skeleton.frame = make_dic_images(get_files_from_directory("sprites/Enemies/Skeleton/individual"),
                                              ["idle", "run", "death", "attack", "shield", "take"])
    mushroom.Mushroom.frame = make_dic_images(get_files_from_directory("sprites/Enemies/Mushroom/individual"),
                                              ["idle", "run", "death", "attack", "shield", "take"])
    boss.Boss.frame = make_dic_images(get_files_from_directory("sprites/Enemies/Boss 2/individual"),
                                      ["idle", "run", "death", "attack", "shield", "take"])
    player.Player.sound = {"attack1": pygame.mixer.Sound("sounds/sound efect/player/espada 1.mp3"),
                           "attack2": pygame.mixer.Sound("sounds/sound efect/player/espada 2.mp3"),
                           "attack3": pygame.mixer.Sound("sounds/sound efect/player/espada 3.mp3"),
                           "run": pygame.mixer.Sound("sounds/sound efect/player/run1.mp3"),
                           "jump": pygame.mixer.Sound("sounds/sound efect/player/Jump sound effect.mp3"),
                           "block idli": pygame.mixer.Sound("sounds/sound efect/player/Gravação (5).mp3")}
    Goblin.sound = {"run": pygame.mixer.Sound("sounds/sound efect/goblin/run.mp3"),
                    "attack": pygame.mixer.Sound("sounds/sound efect/goblin/ataque.mp3"),
                    "hurt": pygame.mixer.Sound("sounds/sound efect/goblin/hit.mp3")}
    # skeleton.Skeleton.sound={"run":pygame.mixer.Sound("sounds/sound efect/Skeleton/andar.mp3"), "attack":pygame.mixer.Sound("sounds/sound efect/Skeleton/ataque.mp3"),"hurt":pygame.mixer.Sound("sounds/sound efect/Skeleton/hit.mp3")}
    mushroom.Mushroom.sound = {"run": pygame.mixer.Sound("sounds/sound efect/Mushroom/run.mp3"),
                               "attack": pygame.mixer.Sound("sounds/sound efect/Mushroom/ataque.mp3"),
                               "hurt": pygame.mixer.Sound("sounds/sound efect/Mushroom/hit.mp3")}

    global goblin_list,skeletom_list,mushroom_list
    mc = player.Player((100, -300))

    font = pygame.font.SysFont("courier", 69)
    font_titulo = pygame.font.SysFont("courier", 90, True)

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
    w_list=[boss.Boss((3577,772)),goblin.Goblin((3097,-60)),mushroom.Mushroom((1069,-60))]

    k_left = False
    k_right = False
    k_space = False
    k_down = False
    k_up = False
    k_j = False
    k_k = False
    k_l = False

    k_r = False

    list_list = [w_list,goblin_list,mushroom_list]

    music = pygame.mixer.music.load("sounds/sound track/Yoann Laulan - Dead Cells - Soundtrack Part 1 - 32 Arboretum.mp3")
    for m in mushroom.Mushroom.sound.values():
        m.set_volume(volume)
    for m in player.Player.sound.values():
        m.set_volume(volume)
    for m in goblin.Goblin.sound.values():
        m.set_volume(volume)

    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume)
    mushroom_list.append(mushroom_1)
    enemy_list = []

    #background = pygame.Surface(screen.get_size())

    #for r in skeletom_list:
    #    enemy_list.append(r)
    for r in mushroom_list:
        enemy_list.append(r)
    for r in goblin_list:
        enemy_list.append(r)

    enemy_list.append(wizard)

    win_time= 25
    enemy_num=len (enemy_list)


    while True:
        pygame.display.set_caption(titulo+"("+str(int(clock.get_fps()))+")")
       # screen.blit(background, (0,0))





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
        camera[1] += (mc.rect.centery - camera[1]-10 - screen.get_height() * (6 / 10)) / 7

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


        mc_attack=pygame.Rect(10, 10, 100, 100)
        mc.attack(mc_attack)
        if mc.side_left:
            mc_attack.midright=mc.hit_box.midleft
        else:
            mc_attack.midleft=mc.hit_box.midright

        for enemy in enemy_list:
            if (enemy.rect.centerx - camera[0] > -100 and enemy.rect.centerx - camera[0] < 1400 and enemy.rect.centery -camera[1] > -50 and enemy.rect.centery - camera[1] < 800) or enemy == wizard:
                mc.push(enemy)

                if enemy.attack(mc) or enemy.especial_attack(mc, barriers):
                    mc.damage(50)
                    print(mc.hp)

                if mc_attack.colliderect(enemy.hit_box) and mc.reload == 0 and mc.attack_on:
                    enemy.damage(50)
                    print(enemy.hp)

                enemy.draw(screen, camera)
                enemy.move(barriers)

                enemy.ai(mc, barriers)

                if enemy.hp <= 0 or enemy.hit_box.y>4500:
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
        if enemy_list==[]:
            mc.enemy=mc
        else:
            mc.enemy=mc.closer_enemy(enemy_list)

        mc.draw(screen, camera)
        draw_live_bar(screen,mc.hp,mc.hp_max,( 20,20))
        draw_enemy_count(screen,len(enemy_list),enemy_num)

        #-----------------------------------------------------------------------------
        #Condiçoes para terminar o jogo

        if (mc.frame_on=="death"and mc.frame_index >=9 )or mc.hit_box.y>4500:
            barra = pygame.Rect(320, 225, 700, 60)
            pygame.draw.rect(screen, (27, 27, 27), barra, 0, 20)
            draw_text("Game Over", font, (255, 255, 255), screen, barra.center[0], barra.center[1])
            pygame.display.update()
            clock.tick(0.3)
            return
        k_space = False
        k_j = False
        k_l=False
        if enemy_list==[]:
            win_time-=1
            if win_time==0:
                barra = pygame.Rect(320, 225, 700, 60)
                pygame.draw.rect(screen, (27, 27, 27), barra, 0, 20)
                draw_text("You Win", font, (255, 255, 255), screen, barra.center[0], barra.center[1])
                pygame.display.update()
                clock.tick(0.3)
                return


        #------------------------------------------------------
        pygame.display.update()
        clock.tick(40)


    # START OF CODE ----------------------------------------------------------


pygame.init()

screen_size = (340 * 4, 190 * 4)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(titulo)

bg = []

for i in get_files_from_directory("sprites/background/brown"):
    x = img_load(i, 3)

    bg.append(x)

    ##bg.fill((100, 200, 150))




clock = pygame.time.Clock()

pygame.mixer.pre_init(44100,-16,2,512)

font = pygame.font.SysFont("courier", 69)
font_count = pygame.font.SysFont("courier", 50)







main_menu()

# GAME LOOP-------------------------------------------------------------------------------


