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

motion = 'STOP'

car1 = car # делаем копию, чтобы не портить исходник
angle = 0
while 1:
    motion = "STOP"
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                angle = 90
                car = pygame.transform.rotate(car1, angle)
                rect.x -= 5
            elif i.key == pygame.K_RIGHT:
                angle = -90
                car = pygame.transform.rotate(car1, angle)
                rect.x += 5
            elif i.key == pygame.K_UP:
                angle = 0
                car = pygame.transform.rotate(car1, angle)
                rect.y -= 5
            elif i.key == pygame.K_DOWN:
                angle = 180
                car = pygame.transform.rotate(car1, angle)
                rect.y += 5
            # поворот машины в зависимости от нажатия на кнопку


    keys = pygame.key.get_pressed()
    # смещение машины (ехать)
    if keys[pygame.K_a]:
        angle = 90
        car = pygame.transform.rotate(car1, angle)
        rect.x -= 5
        motion = 'LEFT'
    elif keys[pygame.K_d]:
        angle = -90
        car = pygame.transform.rotate(car1, angle)
        rect.x += 5
        motion = 'RIGHT'
    elif keys[pygame.K_w]:
        angle = 0
        car = pygame.transform.rotate(car1, angle)
        rect.y -= 5
        motion = 'UP'
    elif keys[pygame.K_s]:
        angle = 180
        car = pygame.transform.rotate(car1, angle)
        rect.y += 5
        motion = "DOWN"

    #rect = car.get_rect()

    sc.fill(WHITE)
    sc.blit(car, rect)

    top_x, top_y = rect.topleft
    left_x, left_y = rect.topleft
    right_x, right_y = rect.topright

    pygame.draw.line(sc, (255, 0, 0), (top_x, top_y), (top_x + rect.width, top_y), 2)
    pygame.draw.line(sc, (0, 255, 0), (left_x, left_y), (left_x, left_y + rect.height), 2)
    pygame.draw.line(sc, (0, 0, 255), (right_x, right_y), (right_x, right_y + rect.height), 2)

    pygame.display.update()

    pygame.time.delay(20)

    if rect.top <= 0 and motion == 'UP':
        rect.top = 0
    elif rect.left <= 0 and motion == 'LEFT':
        rect.left = 0
    elif rect.bottom >= H and motion == 'DOWN':
        rect.bottom = H
    elif rect.right >= W and motion == 'RIGHT':
        rect.right = W