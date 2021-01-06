import pygame
class Entetie:
    def __init__(self,img,rect):
        self.img=img
        self.rect=rect

        return
    def draw(self,screen,camera):
        screen.blit(self.img,(self.rect.x-camera[0],self.rect.y-camera[1]))


