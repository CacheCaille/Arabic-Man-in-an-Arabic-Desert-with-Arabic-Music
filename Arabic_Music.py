import pygame

def music():
    pygame.mixer.music.load("data/music/desert_music.mp3")
    pygame.mixer.music.play(-1)