import enteties,pygame,random,math

class Particle(enteties.Entetie):
    def __init__(self,position,num_particle,cor=(255,255,255),angle=0,openig_angle=0):
        self.cor=cor
        self.position =position
        self. particle_list=[]
        for i in range (0,num_particle):
            #                            pos_x        pos_y                      speed_x        speed_y              time to disapear
            self.particle_list.append([[position[0],position[1]], [random.randint(-10, 10) , random.randint(-10, 10)], random.randint(10, 15)])


    def draw(self, screen, camera=(0, 0)):

        for particle in self.particle_list:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.7
            particle[1][1] += 0.1
            pygame.draw.circle(screen, self.cor, [int(particle[0][0])-camera[0], int(particle[0][1])-camera[1]], int(particle[2]))
            if particle[2] <= 0:
                self.particle_list.remove(particle)
