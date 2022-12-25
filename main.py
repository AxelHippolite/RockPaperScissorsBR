import pygame
from utils import borderCollision, updateAngle, getPosition, getEntities, getTarget

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('RockPaperScissors BR')

n = 25
win = [(0, 2), (1, 0), (2, 1)] #0 = Rock, 1 = Paper, 2 = Scissors
spawn = [((0, 380), (0, 380)), ((400, 780), (0, 380)), ((200, 580), (400, 780))]
rsp = [pygame.transform.scale(pygame.image.load('assets/rock.png'), (20, 20)),
        pygame.transform.scale(pygame.image.load('assets/paper.png'), (20, 20)),
        pygame.transform.scale(pygame.image.load('assets/scissors.png'), (20, 20))]

target = getTarget(n, len(rsp))
pos = getPosition(n, spawn)
entities = getEntities(n, pos, rsp, target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit(0)

    for entity in entities:  
        if True in borderCollision(entity.pos):
            dir_angle = updateAngle(entity.dir_angle, entity.pos)
            entity.move(dir_angle)
        else:
            entity.move(entity.dir_angle)
        for i in entities:
            if entity != i and entity.collide(i) and (entity.specie, i.specie) in win:
                i.specie, i.image = entity.specie, rsp[entity.specie]

    screen.fill((255, 255, 255))
    
    for entity in entities:
        screen.blit(entity.image, entity.pos)

    pygame.display.flip()