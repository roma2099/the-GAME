import pygame
class Accessorie:
    img=[]
    def __init__(self,x,y,index):
        self.index = index
        self.rect=pygame.Rect(
            Accessorie.img[0].get_width() * x,
            Accessorie.img[0].get_width() * y,
            Accessorie.img[0].get_width(),
            Accessorie.img[0].get_height()
        )

        self.index=index

    def draw(self,screen):
        screen.blit( Accessorie.img[self.index],self.rect)