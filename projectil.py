import pygame,enteties


class Projectil(enteties.Entetie):
    frames={}
    def __init__(self,  position, side_left,tipo,movment,time=100):
        super(Projectil, self).__init__(None, position)
        self.movement = movment


        self.frame_index = 0
        self.frame_on = "ball"
        self.rect=Projectil.frame["ball"][0].get_rect()
        self.rect.center=position
        self.hit_box=pygame.rect.Rect((self.rect.center),(5,5))

        self.side_left = side_left
        self.time=time
        self.test_mode=True
        self.is_end=False

    def move(self,player,tile_list):

        self.rect.topleft=(self.rect.x+self.movement[0],self.rect.y+self.movement[1])
        self.hit_box.center=self.rect.center
    def draw(self, screen, camera=(0, 0)):
        if self.animation() and self.frame_on=="explosion":
            self.is_end=True

        screen.blit(pygame.transform.flip(Projectil.frame[self.frame_on][int(self.frame_index)-1], self.side_left, False),
                    (self.rect.x - camera[0], self.rect.y - camera[1]))
        rect = pygame.Surface(self.hit_box.size).convert_alpha()
        rect.fill((200, 0, 0, 100))
        if self.test_mode:
            screen.blit(rect, (self.hit_box.x - camera[0], self.hit_box.y - camera[1]))


    def animation(self):

        self.frame_index += 13*(1/40)
        if len(Projectil.frame[self.frame_on]) <= self.frame_index-1:
            self.frame_index = 0
            return True
        return False
    def colisao(self,player):
        if self.rect.colliderect(player):
            self.movement=[0,0]
            self.frame_on="explosion"
            self.frame_index=0
            return True