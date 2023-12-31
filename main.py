import languages as lang
import pygame

pygame.init()
pygame.mixer.music.load('theme.mp3')
pygame.mixer.music.play(-1)


pygame.event.wait()

print('*' * 35)
print('👊 🖐️  ✌️  JO KEN PO 👊 🖐️  ✌️'.center(35))
print('*' * 35)
print()

lang.language()