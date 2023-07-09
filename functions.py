import pygame

def draw_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, (10, 10))
