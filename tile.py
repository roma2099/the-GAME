import pygame, enteties


class Tile(enteties.Entetie):
    img = []

    def __init__(self,position,index=4):
        self.index = index
        self.rect = pygame.Rect(
            Tile.img[0].get_width() * position[0],
            Tile.img[0].get_width() * position[1],
            Tile.img[0].get_width(),
            Tile.img[0].get_height()
        )
        self.midright=self.rect.midright
        self.midleft = self.rect.midleft
        self.index = index

    def draw(self, screen, camera):
        screen.blit(Tile.img[self.index], (self.rect.x - camera[0], self.rect.y - camera[1]))
