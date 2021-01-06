import pygame,enteties
class Enemy(enteties.Entetie):
    img=[]

    def __init__(self,x,y,index):



        self.movement=[0,0]
        self.hp_max = 50
        self.hp = self.hp_max

        self.img_index = 0

        # maybe u can make the rect_attack evry time o attack

        self.attack_on = 0
        self.side_left = True
        self.run_speed = 10
        self.num_jumps = 0
        self.hurt = False
        self.rect = pygame.Rect(x,y,53,85)


    #This funtion is to controle the player movement, changes the side (for the img) , the atribute movement is list where [x_movement , y_movement]
    def controle(self,up,down,left,right,jump,k1,k2):
        #Jump
        #if u take the "and down ==False something happends"
        if jump and self.num_jumps<2 and down==False:
            self.movement[1]=-10
            self.num_jumps+=1
        if down and self.movement[1]==0 and self.num_jumps==0:
            self.rect.height=self.rect.height/2
            self.rect.y+=self.rect.height/2
        else:
            self.rect.height = self.img[0].get_rect(center=(100,100) ).height

        #Side movement
        if right and left:
            self.movement[0]=0
        elif right and left == False:
            self.side_left = False
            self.movement[0]=self.run_speed
        elif right == False and left:
            self.side_left = True
            self.movement[0]=-self.run_speed
        else:
            self.movement[0]=0


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


        #I need to know in what side they got hit on

        return self.rect_attack.colliderect(enemy)









    def gravity(self):
        if self.movement[1]<50:
            self.movement[1]+=1
        return
    def draw(self,screen,camera):
        if self.side_left:

            screen.blit(pygame.transform.flip(self.img[self.img_index],True,False), (self.rect.x-camera[0],self.rect.y-camera[1]))
        else:
            screen.blit(self.img[self.img_index],(self.rect.x-camera[0],self.rect.y-camera[1]))
        screen.blit(pygame.Surface(self.rect.size), (self.rect.x - camera[0], self.rect.y - camera[1]))


        return

    def die(self):
        if self.hp<=0:
            return True
        return False
