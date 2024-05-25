import pygame
pygame.init()
W = 400
H = 400
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))
sc.fill(WHITE)
car = pygame.image.load('car.png').convert_alpha()
rect = car.get_rect(center=(W//2, H//2))
sc.blit(car, rect)
pygame.display.update()

car1 = car # делаем копию, чтобы не портить исходник
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            pass
            # поворот машины в зависимости от нажатия на кнопку
    keys = pygame.key.get_pressed()
    # смещение машины (ехать)

    sc.fill(WHITE)
    sc.blit(car1, rect)
    pygame.display.update()

    pygame.time.delay(20)