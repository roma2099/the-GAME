import pygame,enteties

class Spikes(enteties.Entetie):
    frames=[]

    def __init__(self, position, index=4):
        self.index = index
        self.rect = pygame.Rect(
            Spikes.frames[0].get_width() * position[0],
            Spikes.frames[0].get_width() * position[1],
            Spikes.frames[0].get_width(),
            Spikes.frames[0].get_height()
        )
        self.midright = self.rect.midright
        self.midleft = self.rect.midleft
        self.index = index
        self.hit_box=pygame.rect.Rect.copy(self.rect)
    def draw(self, screen, camera):
        if self.rect.centerx - camera[0] > -100 and self.rect.centerx - camera[0] < 1400 and self.rect.centery - camera[1] > -50 and self.rect.centery - camera[1] < 800:
            screen.blit(Spikes.frames[self.index], (self.rect.x - camera[0], self.rect.y - camera[1]))


