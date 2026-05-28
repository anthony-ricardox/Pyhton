#Faça um programa em ýthon que abra e reproduza um audio

import pygame
pygame.init()

pygame.mixer.music.load('curso/desafio/mp3.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


