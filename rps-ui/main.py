

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kő papír olló")
clock = pygame.time.Clock()

stone =  pygame.image.load("./images/01.png")
paper =  pygame.image.load("./images/02.png")
scissors =  pygame.image.load("./images/03.png")

objects = [stone, paper, scissors]

user_text = user_text.get_rect()

user_select = 0

user_x = 100
user_y = 200

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        user_select += 1
      if event.key == pygame.K_DOWN:
        user_select -= 1

  if user_select > len(objects) - 1:
    user_select = 0
  if user_select < 0:
    user_select = len(objects) - 1

                # R, G, B
  screen.fill((255, 255, 255))

  screen.blit(objects[user_select], (user_x, user_y))
  screen.blit(

  pygame.display.update()
  clock.tick(60)