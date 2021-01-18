import pygame, caracter


class Enemy(caracter.Caracter):
    frame = {}

    def __init__(self, position=(0, 0),index=0):
        super(Enemy, self).__init__(position)
        self.rect = Enemy.frame[self.frame_on][self.frame_index].get_rect(topleft=position)

        self.attack_on = False
        self.attack_combo = 1
        self.attack_next = False
        self.hit_box = pygame.Rect(7, 8, 20 * 3, 27 * 3)
        self.num_jumps = 0
        print(self.hit_box)


    def draw(self, screen, camera=(0, 0)):
        screen.blit(pygame.transform.flip(Enemy.frame[self.frame_on][self.frame_index], self.side_left, False),(self.rect.x - camera[0], self.rect.y - camera[1]))
        #if self.test_mode:
         #   screen.blit(pygame.Surface(self.hit_box.size), (self.hit_box.x - camera[0], self.hit_box.y - camera[1]))

    def animation(self):

        self.frame_index += 13*(1/40)
        if len(Enemy.frame[self.frame_on]) <= self.frame_index:
            self.frame_index = 0
            return True
        return False