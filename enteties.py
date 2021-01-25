import pygame


class Entetie(pygame.sprite.Sprite):
    def __init__(self, img, position, side_left=False):
        pygame.sprite.Sprite.__init__(self)
        self.test_mode = False
        if img != None:

            self.image = img
            self.rect = self.image.get_rect(topleft=position)
        self.side_left=False
        return
    def set_test_mode(self):
        if self.test_mode == False:
            self.test_mode = True
        else:
            self.test_mode = False


    def draw(self, screen, camera=(0, 0)):
        self.rect.center = self.hit_box.center
        screen.blit(pygame.transform.flip(self.image, self.side_left, False),
                    (self.rect.x - camera[0], self.rect.y - camera[1]))
        if self.test_mode:
            a=pygame.Surface(self.hit_box.size), (self.hit_box.x - camera[0], self.hit_box.y - camera[1])
            a.fill((220,60,30,50))
            screen.blit()