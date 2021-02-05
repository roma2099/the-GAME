import pygame,enemy

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
        self.hp = 200
        self.hp_max = 5000
        self.test_mode=False

    def draw(self, screen, camera = (0,0)):
        screen.blit(pygame.transform.flip(Boss.frame[self.frame_on][int(self.frame_index)], self.side_left, False),(self.rect.x - camera[0], self.rect.y - camera[1]-46))
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

    def animation(self):

        self.frame_index += 13*(1/40)
        if len(Boss.frame[self.frame_on]) <= self.frame_index:
            self.frame_index = 0
            return True
        return False
    def set_hit_box(self,rect=None):
        rect = pygame.Rect(self.rect.centerx, self.rect.centery, 28 * 3, 36 * 3)



