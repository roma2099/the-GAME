# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame, player, sys, os, tile, enemy, accessorie, pickle, skeleton,mushroom,particle
from fuctions import *
from goblin import *



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


player.Player.frame= make_dic_images(get_files_from_directory("sprites/player/Hero Knight/individual"),["run", "fall", "die", "hurt", "idle", "crouch", "jump", "attack1", "attack2","attack3"])
Goblin.frame= make_dic_images(get_files_from_directory("sprites/Enemies/Goblin/individual"), ["idle","run","death","attack","shield","take"])
skeleton.Skeleton.frame= make_dic_images(get_files_from_directory("sprites/Enemies/Skeleton/individual"), ["idle","run","death","attack","shield","take"])
mushroom.Mushroom.frame = make_dic_images (get_files_from_directory("sprites/Enemies/Mushroom/individual"), ["idle","run","death","attack","shield","take"])

player.Player.sound={"attack 1":pygame.mixer.Sound("sounds/sound efect/player/espada 1.mp3"),"attack 2":pygame.mixer.Sound("sounds/sound efect/player/espada 2.mp3"),"attack 3":pygame.mixer.Sound("sounds/sound efect/player/espada 3.mp3"),"run":pygame.mixer.Sound("sounds/sound efect/player/andar.mp3")}
Goblin.sound={"run":pygame.mixer.Sound("sounds/sound efect/goblin/run.mp3"), "attack":pygame.mixer.Sound("sounds/sound efect/goblin/ataque.mp3"), "hurt":pygame.mixer.Sound("sounds/sound efect/goblin/hit.mp3")}
skeleton.Skeleton={"run":pygame.mixer.Sound("sounds/sound efect/Skeleton/andar.mp3"), "attack":pygame.mixer.Sound("sounds/sound efect/Skeleton/ataque.mp3"),"hurt":pygame.mixer.Sound("sounds/sound efect/Skeleton/hit.mp3")}
mushroom.Mushroom={"run":pygame.mixer.Sound("sounds/sound efect/Mushroonm/ru.mp3"), "attack":pygame.mixer.Sound("sounds/sound efect/Mushroom/ataque.mp3"), "hurt":pygame.mixer.Sound("sounds/sound efect/Mushroom/hit.mp3")}

mc = player.Player( (100, 100))
mc.test_mode= True
mc.hit_box.height=40 * 3
# HACK40«


accessories_list, barriers, enemies_list = get_map("sprites/tiles")

enemies_list=fix_enemy(enemies_list,mushroom.Mushroom)


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


goblin_1=Goblin((200 ,200))
goblin_1.hp,goblin_1.hp_max=5000,5000
goblin_1.set_test_mode()


skeleton_1=skeleton.Skeleton((800, 200))
skeleton_1.hp,skeleton_1.hp_max=5000,5000


particles_list=[]
pygame.mixer.pre_init(44100,-16,2,512)
hit_sound = pygame.mixer.Sound("sounds/sound efect/quick swing.mp3")

music= pygame.mixer.music.load("sounds/sound track/Yoann Laulan - Dead Cells - Soundtrack Part 1 - 32 Arboretum.mp3")
pygame.mixer.music.play(-1)


mc.test_mode=False




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



    for barreira in barriers:
        barreira.draw(screen, camera)
    for particle in particles_list:
        if particle.particle_list==[]:
            particles_list.remove(particle)
        particle.draw(screen,camera)

    for enemy in enemies_list:
        if mc.attack(enemy, screen, camera):
            hit_sound.play()
            enemy.hp -= 50
            print(enemy.hp)

        enemy.draw(screen, camera)
        enemy.move(barriers)
        enemy.ai(mc,barriers)

        if enemy.hp<=0:
            particles_list.append(particle.Particle(enemy.rect.center,8,(153, 0, 0),90,90))
            particles_list.append(particle.Particle((enemy.rect.center[0],enemy.rect.center[1]-45), 8, (153, 0, 0), 90, 90))
            particles_list.append(particle.Particle((enemy.xxxxxxxrect.center[0],enemy.rect.center[1]+45), 8, (153, 0, 0), 90, 90))
            enemies_list.remove(enemy)
    #for r in enemies_list:


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


    pygame.display.update()
    clock.tick(40)
