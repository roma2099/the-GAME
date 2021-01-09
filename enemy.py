import pygame,caracter
class Enemy(caracter.Caracter):
    frame=dict()
    def __init__(self, frame_input={}, position=(0, 0)) :

        if Enemy.frame=={}:
            Enemy.frame=frame_input

        super(Enemy, self).__init__(None, position, movement)
        self.rect=Enemy.frame[self.frame_on][self.frame_index].get_rect(topleft=position)

    def draw(self, screen, camera=(0, 0)):
        screen.blit(pygame.transform.flip(Enemy.frame[self.frame_on][self.frame_index], self.side_left, False),(self.rect.x - camera[0], self.rect.y - camera[1]))




















