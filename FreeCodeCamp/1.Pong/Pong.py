import pygame
import random

pygame.init()

#start Initial beginning Parameters
WIDTH, HEIGHT= 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
run = False
player_1 = player_2 = 0
direction = [0, 1]
angle = [0, 1, 2]