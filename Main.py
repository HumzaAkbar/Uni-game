import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Humza and Adam Game")

Colour = (255,0,225)

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill((Colour)) 

    pygame.quit()

if __name__ == "__main__": 
    main()