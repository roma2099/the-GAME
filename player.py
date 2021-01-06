import pygame

class Player ():


    def __init__(self,files=[],position=(0,0),movement=0):




        self.movement=[0,0]
        self.hp_max = 50
        self.hp = self.hp_max
        self.img = {"run":[],"fall":[],"die":[],"hurt":[],"idle":[],"jump":[],"attack1":[],"attack2":[],"attack3":[]}

        self.img_index = 0
        self.img_on="idle"

        # maybe u can make the rect_attack evry time o attack
        self.rect_attack = pygame.Rect(0, 0, 50, 150)

        self.attack_on = 0
        self.attack_combo=1
        self.attack_next = 0


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

            for key in self.img.keys():
                if key in asset:
                    self.img[key].append(i)

        self.rect = self.img[self.img_on][self.img_index].get_rect(topleft=(position))
        #\ self.rect.width -= 13
        print (self.img)
        return
    #This funtion is to controle the player movement, changes the side (for the img) , the atribute movement is list where [x_movement , y_movement]


    def animation(self):

        self.img_index+=1
        if len(self.img[self.img_on])<=self.img_index:
            self.img_index=0
            if self.attack_on>0 :
                self.attack_on=0


    def controle(self,up,down,left,right,jump,k1,k2):
        #animation
        if (self.attack_next==1 and self.attack_on== 0) or (self.attack_on!=0 and (self.img_on != "attack1" and self.img_on != "attack2" and self.img_on != "attack3")) :

            if self.attack_next > 0 and self.attack_on==0:
                self.attack_next = 0
                self.attack_on = 1
                self.attack_combo += 1

                if self.attack_combo == 4:
                    self.attack_combo = 1
            else:
                self.attack_combo = 1
                print(1)

            self.img_on = "attack"+str(self.attack_combo)
            print("attack"+str(self.attack_combo))
            self.img_index = 0

        elif self.movement[1] < 0 and self.img_on != "jump" and self.attack_on==0 :
            self.img_on = "jump"
            self.img_index = 0

        elif self.movement[1] > 0 and self.img_on != "fall" and self.attack_on==0:
            self.img_on = "fall"
            self.img_index = 0

        elif (left or right) and self.img_on != "run" and self.num_jumps==0 and self.attack_on==0 :
            self.img_on = "run"
            self.img_index = 0

        elif self.movement[0]==0 and self.movement[1]==0 and self.img_on != "idle" and self.num_jumps == 0 and self.attack_on==0:
            self.img_on = "idle"
            self.img_index = 0





 #       if self.attack_next == 1 :
  #          if self.attack_on==1 :
   #             self.attack_end = 0
    #            self.attack_on=0
     #           self.img_on = "attack"+str(self.attack_combo)
      #          self.attack_combo=+1
       #         if self.attack_combo>3:
        #            self.attack_combo=1




        #if u take the "and down ==False something happends"
        if jump and self.num_jumps<2 and down==False :
            self.movement[1]=-15
            self.num_jumps+=1
        if down and self.movement[1]==0 and self.num_jumps==0:
            self.rect.height=self.rect.height/2
            self.rect.y+=self.rect.height/2
        else:
            self.rect.height = self.img["idle"][0].get_rect(center=(100,100) ).height

        #Side movement
        if right and left :
            self.movement[0]=0
        elif right and left == False and self.attack_on==0:
            self.side_left = False
            self.movement[0]=self.run_speed
        elif right == False and left and self.attack_on==0:
            self.side_left = True
            self.movement[0]=-self.run_speed
        else:
            self.movement[0]=0
        # attack

        if k1:

            self.attack_next=1


        if self.attack_next==1 and self.attack_on==0:

            self.attack_next = 0
            self.attack_on = 1
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

    def draw(self,screen,camera=(0,0)):


        if self.side_left:

            screen.blit(pygame.transform.flip(self.img[self.img_on][self.img_index],True,False), (self.rect.x-camera[0],self.rect.y-camera[1]))
        else:
            screen.blit(self.img[self.img_on][self.img_index],(self.rect.x-camera[0],self.rect.y-camera[1]))



        return

    def die(self):
        if self.hp<=0:
            return True
        return False
