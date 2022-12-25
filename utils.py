import math
import random
from entity import Entity

def getTarget(n, indentity):
    return [[random.randint(0, 780), random.randint(0, 780)] for i in range(n * indentity)]

def getPosition(n, spawn):
    pos = []
    for s in spawn:
        for i in range(n):
            pos.append([random.randint(s[0][0], s[0][1]), random.randint(s[1][0], s[1][1])])
    return pos

def getEntities(n, pos, rsp, target):
    entities = []
    for i in range(len(rsp)):
        for j in range(n):
            entities.append(Entity(rsp[i], pos[j], 1, i, direction(pos[j], target[j])))
        del pos[:n]
        del target[:n]
    return entities

def direction(pos, target):
    distance_x = target[0] - pos[0]
    distance_y = target[1] - pos[1]
    if distance_x != 0 or distance_y != 0:
        return math.atan2(distance_y, distance_x)

def borderCollision(pos):
    return [pos[0] <= 0, pos[0] >= 800 - 20, pos[1] <= 0, pos[1] >= 800 - 20]

def updateAngle(dir_angle, pos):
    index = borderCollision(pos).index(True)
    if index == 0 or index == 1:
        return math.pi - dir_angle
    else:
        return -dir_angle