import pygame,enteties

class Player (enteties.Entetie):


    def __init__(self,files=[],position=(0,0),movement=0):




        self.movement=[0,0]
        self.hp_max = 50
        self.hp = self.hp_max

        self.frame = {"run":[],"fall":[],"die":[],"hurt":[],"idle":[],"jump":[],"attack1":[],"attack2":[],"attack3":[]}
        self.frame_index = 0
        self.frame_on="idle"


        # maybe u can make the rect_attack evry time o attack
        self.rect_attack = pygame.Rect(0, 0, 50, 150)

        self.attack_on = False
        self.attack_combo=1
        self.attack_next = False


        self.side_left = True
        self.run_speed = 10
        self.num_jumps = 0
        self.hurt = False


        for asset in files:
            #fuction img_load in main makes the load and scaling
            #2 IS THE SCALE
            i = pygame.image.load(asset).convert_alpha()
            i= pygame.transform.scale(i, (2 * i.get_rect().size[0], 2 * i.get_rect().size[1]))

            i = pygame.transform.scale(pygame.image.load(asset), (150,111)).convert_alpha()

            for key in self.frame.keys():
                if key in asset:
                    self.frame[key].append(i)
        super(Player, self).__init__(self.frame[self.frame_on][self.frame_index], position)

        #\ self.rect.width -= 13

        return
    #This funtion is to controle the player movement, changes the side (for the img) , the atribute movement is list where [x_movement , y_movement]


    def animation(self):

        self.frame_index+=0.4
        if len(self.frame[self.frame_on])<=self.frame_index:
            self.frame_index=0
            return True
        return False
    def update(self):
        print(self.frame_on + "___"+str(int(self.frame_index)))
        self.image = self.frame[self.frame_on][int(self.frame_index)]

    def controle(self, up, down, left, right, jump, k1, k2):
        # animation
        if self.animation():
            self.attack_on=False
        if (self.attack_next == True and self.attack_on == False) or (self.attack_on != False and (self.frame_on != "attack1" and self.frame_on != "attack2" and self.frame_on != "attack3")):
            if self.attack_next ==True and self.attack_on==False:
                if right and not left:
                    self.side_left=False
                elif not right and  left:
                    self.side_left=True
            if (self.attack_next == True) and self.attack_on == False:
                self.attack_next = False
                self.attack_on = True
                self.attack_combo += 1

                if self.attack_combo == 4:
                    self.attack_combo = 1
            else:
                self.attack_combo = 1
                print(1)

            self.frame_on = "attack" + str(self.attack_combo)
            print("attack" + str(self.attack_combo))
            self.frame_index = 0

        elif self.movement[1] < 0 and self.frame_on != "jump" and self.attack_on == False:
            self.frame_on = "jump"
            self.frame_index = 0

        elif self.movement[1] > 0 and self.frame_on != "fall" and self.attack_on == False:
            self.frame_on = "fall"
            self.frame_index = 0

        elif (left or right) and self.frame_on != "run" and self.num_jumps == 0 and self.attack_on == False:
            self.frame_on = "run"
            self.frame_index = 0

        elif self.movement[0] == 0 and self.movement[
            1] == 0 and self.frame_on != "idle" and self.num_jumps == 0 and self.attack_on == False:
            self.frame_on = "idle"
            self.frame_index = 0

        #       if self.attack_next == 1 :
        #          if self.attack_on==1 :
        #             self.attack_end = 0
        #            self.attack_on=0
        #           self.img_on = "attack"+str(self.attack_combo)
        #          self.attack_combo=+1
        #         if self.attack_combo>3:
        #            self.attack_combo=1

        # if u take the "and down ==False something happends"
        if jump and self.num_jumps < 2 and down == False:
            self.movement[1] = -15
            self.num_jumps += 1
        if down and self.movement[1] == 0 and self.num_jumps == 0:
            self.rect.height = self.rect.height / 2
            self.rect.y += self.rect.height / 2
        else:
            self.rect.height = self.frame["idle"][0].get_rect(center=(100, 100)).height

        # Side movement
        if right and left:
            self.movement[0] = 0
        elif right and left == False and self.attack_on == False:
            self.side_left = False
            self.movement[0] = self.run_speed
        elif right == False and left and self.attack_on == False:
            self.side_left = True
            self.movement[0] = -self.run_speed
        else:
            self.movement[0] = 0
        # attack

        if k1:
            self.attack_next = True

        if self.attack_next == True and self.attack_on == False:
            self.attack_next = False
            self.attack_on = True
        return


    def move(self,barreiras):
        #Mudar depois, pq se colidir em duas barreiras do mesmo lado, por exemplo a direita e detectar primeiro a menos aa direita a posisao sera atualizada para a barreiramais a direita, assim atravesando a menos a direita!!!

        #gravidade talvez fique no controle

        self.gravity()

        # mover no y
        self.rect.y += self.movement[1]
        # lista das barreiras que colidio

        collisinons = self.move_collision(barreiras)
        for barreira in collisinons:
            if self.movement[1] < 0:
                self.rect.top = barreira.bottom
                self.movement[1] = 0
            if self.movement[1] > 0:
                self.rect.bottom = barreira.top
                self.movement[1] = 0
                self.num_jumps = 0

        #mover no x
        self.rect.x+=self.movement[0]
        #lista das barreiras que colidio
        collisinons=self.move_collision(barreiras)
        for barreira in collisinons:
            if self.movement[0]<0:
                self.rect.left=barreira.right
            if self.movement[0] > 0:
                self.rect.right = barreira.left



        return
    def move_collision(self,barreiras):
        collision=[]

        for barreira in barreiras:

            if self.rect.colliderect(barreira.rect):
                collision.append(barreira.rect)
        return collision


    #Should I use just the rect of the enemy or the hole class
    #
    def attack(self,enemy):
        self.attack_on=10
        if self.side_left:
            self.rect_attack.midright=self.rect.midleft
            print(self.side_left)
        else:
            self.rect_attack.midleft = self.rect.midright
            print(self.side_left)

        #I need to know in what side they got hit on

        return self.rect_attack.colliderect(enemy)






    def __getattr__(self, item):
            return


    def gravity(self):
        if self.movement[1]<50:
            self.movement[1]+=1
        return









    def die(self):
        if self.hp<=0:
            return True
        return False
