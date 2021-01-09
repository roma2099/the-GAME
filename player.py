import pygame,caracter

class Player (caracter.Caracter):


    def __init__(self,files=[],position=(0,0),movement=0):



        # maybe u can make the rect_attack evry time o attack


        self.attack_on = False
        self.attack_combo=1
        self.attack_next = False

        self.num_jumps = 0
        
        super(Player, self).__init__(files,position,movement)

        #\ self.rect.width -= 13

        return
    #This funtion is to controle the player movement, changes the side (for the img) , the atribute movement is list where [x_movement , y_movement]



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


