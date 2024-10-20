import pygame

pygame.init()
pygame.display.set_mode(())

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT():
      import sys
      sys.exit()
