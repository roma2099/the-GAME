import pygame, enteties


class Tile(enteties.Entetie):
    img = []

    def __init__(self,position,index=4):
        self.index = index
        self.rect = pygame.Rect(
            position[0],
            position[1],
            Tile.img[0].get_width(),
            Tile.img[0].get_height()
        )
        self.midright=self.rect.midright
        self.midleft = self.rect.midleft
        self.index = index

    def draw(self, screen, camera):
        if self.rect.centerx - camera[0] > -100 and self.rect.centerx - camera[0] < 1400 and self.rect.centery - camera[1] > -50 and self.rect.centery - camera[1] < 800:
            screen.blit(Tile.img[self.index], (self.rect.x - camera[0], self.rect.y - camera[1]))
