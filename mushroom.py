import enemy,pygame


class Mushroom(enemy.Enemy):
    frame={}
    def __init__(self,position=(0,0)):
        super(Mushroom,self).__init__(position)
        self.rect = Mushroom.frame[self.frame_on][self.frame_index].get_rect(topleft=position)
        self.hit_box = pygame.Rect(position[0],position[1],19*3,36*3)
        self.hit_box.center = self.rect.center
        self.run_speed = 4
    def draw(self, screen, camera = (0,0)):
        screen.blit(pygame.transform.flip(Mushroom.frame[self.frame_on][int(self.frame_index)], self.side_left, False),(self.rect.x - camera[0], self.rect.y - camera[1]-24))
        rect = pygame.Surface(self.hit_box.size).convert_alpha()
        rect.fill((200, 0, 0, 100))
        screen.blit(rect, (self.hit_box.x - camera[0], self.hit_box.y - camera[1]))

    def animation(self):

        self.frame_index += 13*(1/40)
        if len(Mushroom.frame[self.frame_on]) <= self.frame_index:
            self.frame_index = 0
            return True
        return False