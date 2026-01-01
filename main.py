import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    td = 0

    while True:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        log_state()

        screen.fill("black")
        pygame.display.flip()
        
        td = clock.tick(60) / 1000.0  # Limit to 60 FPS
        
if __name__ == "__main__":
    main()
