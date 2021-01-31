import enemy,pygame

class Skeleton(enemy.Enemy):
    frame={}
    sound={}
    def __init__(self,position=(0,0),index=0):
        super(Skeleton, self).__init__(position)
        self.rect = Skeleton.frame[self.frame_on][self.frame_index].get_rect(topleft=position)
        self.hit_box = pygame.Rect(position[0], position[1], 28 * 3, 48 * 3)
        self.hit_box.center = self.rect.center
        self.run_speed=8
        self.test_mode=False
        self.hp=250

    def draw(self, screen, camera=(0, 0)):

        screen.blit(pygame.transform.flip(Skeleton.frame[self.frame_on][int(self.frame_index)], self.side_left, False),(self.rect.x - camera[0], self.rect.y - camera[1]))
        if self.test_mode:
            rect = pygame.Surface(self.hit_box.size).convert_alpha()
            rect.fill((200, 0, 0, 100))
            screen.blit(rect, (self.hit_box.x - camera[0], self.hit_box.y - camera[1]))

    def animation(self):

        self.frame_index += 13*(1/40)
        if len(Skeleton.frame[self.frame_on]) <= self.frame_index:
            self.frame_index = 0
            return True
        return False