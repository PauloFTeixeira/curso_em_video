"""
Faça um programa em Python que abra e reproduza um arquivo Mp3

"""
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()


