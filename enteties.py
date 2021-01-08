import pygame
class Entetie:
    def __init__(self,img,position):
        self.image=img
        self.rect=self.image.get_rect(topleft=position)

        return

    def draw(self, screen, camera=(0, 0)):
        screen.blit(pygame.transform.flip(self.image, self.side_left, False),(self.rect.x - camera[0], self.rect.y - camera[1]))


