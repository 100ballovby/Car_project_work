import pygame

pygame.init()
W = 400
H = 400
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))
sc.fill(WHITE)
car = pygame.image.load('car.png').convert_alpha()
rect = car.get_rect(center=(W // 2, H // 2))
sc.blit(car, rect)
pygame.display.update()

car1 = car  # создал копию картинки
rect1 = car1.get_rect()
angle = 0
while 1:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
		if i.type == pygame.KEYDOWN:
			if i.key == pygame.K_LEFT:
				angle = 90
				car = pygame.transform.rotate(car1, angle)
			if i.key == pygame.K_RIGHT:
				angle = -90
				car = pygame.transform.rotate(car1, angle)

	rect = car.get_rect()
	rect.center = W // 2, H // 2

	sc.fill((255, 255, 255))
	sc.blit(car, rect)

	pygame.display.update()
