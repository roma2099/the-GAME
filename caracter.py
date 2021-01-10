import pygame, enteties


class Caracter(enteties.Entetie):

    def __init__(self, frames={}, position=(0, 0), movement=0):

        self.movement = [0, 0]
        self.hp_max = 50
        self.hp = self.hp_max

        self.frame = frames
        self.frame_index = 0
        self.frame_on = "idle"

        self.side_left = True
        self.run_speed = 10

        self.hurt = False

        super(Caracter, self).__init__(self.frame[self.frame_on][self.frame_index], position)

    def animation(self):

        self.frame_index += 0.4
        if len(self.frame[self.frame_on]) <= self.frame_index:
            self.frame_index = 0
            return True
        return False

    def update(self):

        self.image = self.frame[self.frame_on][int(self.frame_index)]

    def move(self, barreiras):
        # Mudar depois, pq se colidir em duas barreiras do mesmo lado, por exemplo a direita e detectar primeiro a menos aa direita a posisao sera atualizada para a barreiramais a direita, assim atravesando a menos a direita!!!

        # gravidade talvez fique no controle

        self.gravity()

        # mover no y
        self.hit_box.y += self.movement[1]
        # lista das barreiras que colidio

        collisinons = self.move_collision(barreiras)
        for barreira in collisinons:
            if self.movement[1] < 0:
                self.hit_box.top = barreira.bottom
                self.movement[1] = 0
            if self.movement[1] > 0:
                self.hit_box.bottom = barreira.top
                self.movement[1] = 0
                self.num_jumps = 0

        # mover no x
        self.hit_box.x += self.movement[0]
        # lista das barreiras que colidio
        collisinons = self.move_collision(barreiras)
        for barreira in collisinons:
            if self.movement[0] < 0:
                self.hit_box.left = barreira.right
            if self.movement[0] > 0:
                self.hit_box.right = barreira.left
        self.rect.midbottom = self.hit_box.midbottom

        return

    def move_collision(self, barreiras):
        collision = []

        for barreira in barreiras:

            if self.hit_box.colliderect(barreira.rect):
                collision.append(barreira.rect)
        return collision

    # Should I use just the rect of the enemy or the hole class
    #
    def gravity(self):
        if self.movement[1] < 50:
            self.movement[1] += 1
        return

    def die(self):
        if self.hp <= 0:
            return True
        return False

    def attack(self, enemy):
        return
