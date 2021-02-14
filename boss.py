import pygame,enemy,projectil

class Boss(enemy.Enemy):
    frame={}
    sound = {}

    def __init__(self, position=(0, 0), index=0):
        super(Boss, self).__init__(position)
        self.rect = Boss.frame[self.frame_on][self.frame_index].get_rect(topleft=position)
        self.hit_box = pygame.Rect(position[0], position[1], 19 * 3, 53 * 3)
        self.hit_box.center = self.rect.center
        self.run_speed = 4
        self.reload = 0
        self.reload_max = 20
        self.hp = 500
        self.hp_max = 500
        self.test_mode=False
        self.projectile_list=[]
        self. reload_projectile=0

    def draw(self, screen, camera = (0,0)):
        for projectil in self.projectile_list:

            projectil.draw(screen,camera)

            screen.blit(pygame.transform.flip(Boss.frame[self.frame_on][int(self.frame_index)], self.side_left, False),(self.rect.x - camera[0], self.rect.y - camera[1]))
        rect = pygame.Surface(self.hit_box.size).convert_alpha()
        rect.fill((200, 0, 0, 100))
        if self.test_mode:
            screen.blit(rect, (self.hit_box.x - camera[0], self.hit_box.y - camera[1]))
            if self.attack_on and self.reload==0:
                attack_range = pygame.Rect(10, 10, 100, 100)
                attack_range_surface = pygame.Surface(attack_range.size).convert_alpha()
                attack_range_surface.fill((250, 150, 71, 100))
                if self.side_left:
                    attack_range.midright = self.hit_box.midleft
                else:
                    attack_range.midleft = self.hit_box.midright

                screen.blit(attack_range_surface,(attack_range.x - camera[0], attack_range.y - camera[1]))
        self.draw_live_bar(screen,camera)

    def controle(self, up, down, left, right, jump, k1, k2):
        super(Boss, self).controle( up, down, left, right, jump, k1, k2)
        if k2:

            if self.side_left:
                print("one")
                self.projectile_list.append(projectil.Projectil(self.rect.center,self.side_left,"fireball",[-17,0]))
            else:
                print("two")
                self.projectile_list.append(projectil.Projectil(self.rect.center,self.side_left,"fireball",[17,0]))
    def animation(self):

        self.frame_index += 13*(1/40)
        if len(Boss.frame[self.frame_on]) <= self.frame_index:
            self.frame_index = 0
            return True
        return False
    def set_hit_box(self,rect=None):
        rect = pygame.Rect(self.rect.centerx, self.rect.centery, 28 * 3, 36 * 3)
    def especial_attack(self,player,tile_list):

        for projectile in self.projectile_list:
            projectile.move(player,tile_list)
            if projectile.is_end:

                self.projectile_list.remove(projectile)
                continue

            if projectile.frame_on=="ball" and projectile.colisao(player.hit_box) :

                return True

        return False
    def ai(self,player,list_tile):
        up, down, left, right, jump, k1, k2 = False, False, False, False, False, False, False
        if self.rect.centerx - player.rect.centerx <= 260 and self.rect.centerx - player.rect.centerx >= -260 and self.rect.centery - player.rect.centery <= 60 and self.rect.centery - player.rect.centery >= -60:
            if self.rect.centerx - player.rect.centerx <= 90 and self.rect.centerx - player.rect.centerx >= -90:
                left = False
                right = False
                k1 = True
            elif ((self.rect.centerx - player.rect.centerx <= 260 and self.rect.centerx - player.rect.centerx >= 210 )or (self.rect.centerx - player.rect.centerx >= -260 and self.rect.centerx - player.rect.centerx <= -210)) and self.reload_projectile<=0:

                k2= True
                self.reload_projectile=50
            elif self.rect.centerx - player.rect.centerx > 0:

                left = True
                right = False

            elif self.rect.centerx - player.rect.centerx < 0:

                left = False
                right = True
        else:
            if self.hit_box.right >= self.limits[1]:
                self.side_left = True
            elif self.hit_box.left <= self.limits[0]:
                self.side_left = False

            if self.side_left:
                left = True
                right = False


            else:
                left = False
                right = True
        self.reload_projectile-=2
        self.controle(up, down, left, right, jump, k1, k2)






