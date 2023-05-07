import random
import pygame

# pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kő papír olló")
clock = pygame.time.Clock()

# images
ko = pygame.image.load("./images/01.png")
papir = pygame.image.load("./images/02.png")
ollo = pygame.image.load("./images/03.png")

# colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)

# texts
font = pygame.font.Font('freesansbold.ttf', 32)

user_text = font.render('Te', True, white, black)
user_text_rect = user_text.get_rect()
user_text_rect.center = (100, 100)
komputer_text = font.render('Komputer', True, white, black)
komputer_text_rect = komputer_text.get_rect()
komputer_text_rect.center = (400, 100)

winner_text = font.render('Győztes', True, white, black)
winner_text_rect = winner_text.get_rect()
winner_text_rect.center = (300, 50)

# globals

szabaly =[
  {id: 0, "name": "kő", "beats": [2], "image": ko},
  {id: 1, "name": "papír", "beats": [0], "image": papir},
  {id: 2, "name": "olló", "beats": [1], "image": ollo}
]

gyoztest_mutasd = False
komputer_valasztasa = 0
felh_valasztasa = 0
running = True

# functions

def gyoztes():
  if felh_valasztasa == komputer_valasztasa:
    return "Döntetlen!"
  else:
    if komputer_valasztasa in szabaly[felh_valasztasa]["beats"]:
      return "Te győztél!"
    else:
      return "Komputer győzőtt!"

# main
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE or event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_UP:
        gyoztest_mutasd = False
        felh_valasztasa += 1
        if felh_valasztasa > 2:
          felh_valasztasa = 0
      if event.key == pygame.K_DOWN:
        gyoztest_mutasd = False
        felh_valasztasa -= 1
        if felh_valasztasa < 0:
          felh_valasztasa = 2
      if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or  event.key == pygame.K_KP_ENTER:
        komputer_valasztasa = random.randint(0, 2)
        ki_a_gyoztes = gyoztes()
        winner_text = font.render(ki_a_gyoztes, True, white, black)
        gyoztest_mutasd = True

  screen.fill((0, 0, 0))

  if gyoztest_mutasd:
    screen.blit(winner_text, winner_text_rect)

  screen.blit(user_text, user_text_rect)
  screen.blit(szabaly[felh_valasztasa]["image"], (100, 250))

  screen.blit(komputer_text, komputer_text_rect)
  screen.blit(szabaly[komputer_valasztasa]["image"], (400, 250))

  pygame.display.update()
  clock.tick(60)

pygame.quit()
quit()