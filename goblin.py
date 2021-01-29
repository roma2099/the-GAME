import  pygame,enemy

class Goblin(enemy.Enemy):
    frame ={}
    sound={}
    def __init__(self,position=(0,0),index=0):
        super(Goblin, self).__init__(position)
        self.rect = Goblin.frame[self.frame_on][self.frame_index].get_rect(topleft=position)
        self.hit_box=pygame.Rect(position[0],position[1],28*3,36*3)

        self.hit_box.center=self.rect.center

    def draw(self, screen, camera=(0, 0)):

        screen.blit(pygame.transform.flip(Goblin.frame[self.frame_on][int(self.frame_index)], self.side_left, False),(self.rect.x - camera[0], self.rect.y - camera[1]-21))

        if self.test_mode :
            rect = pygame.Surface(self.hit_box.size).convert_alpha()
            rect.fill((200, 0, 0, 100))
            screen.blit(rect, (self.hit_box.x - camera[0], self.hit_box.y - camera[1]))

    def animation(self):

        self.frame_index += 13*(1/40)
        if len(Goblin.frame[self.frame_on]) <= self.frame_index:
            self.frame_index = 0
            return True
        return False
    def set_hit_box(self,rect=None):
        rect = pygame.Rect(self.rect.centerx, self.rect.centery, 28 * 3, 36 * 3)
