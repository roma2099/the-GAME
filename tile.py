import pygame,enteties
class Tile(enteties.Entetie) :
    img=[]
    def __init__(self,x,y,index):
        self.index = index
        self.rect=pygame.Rect(
            Tile.img[0].get_width() * x,
            Tile.img[0].get_width() * y,
            Tile.img[0].get_width(),
            Tile.img[0].get_height()
        )
        self.index=index

    def draw(self,screen,camera):
        screen.blit(Tile.img[self.index],(self.rect.x-camera[0],self.rect.y-camera[1]))