import pygame,enteties


class Accessorie(enteties.Entetie):
    img = []

    def __init__(self, x, y, index=0):
        self.index = index
        self.rect = pygame.Rect(
            Accessorie.img[0].get_width() * x,
            Accessorie.img[0].get_width() * y,
            Accessorie.img[0].get_width(),
            Accessorie.img[0].get_height()
        )

        self.index = index

    def draw(self, screen):
        screen.blit(Accessorie.img[self.index], self.rect)
