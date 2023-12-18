import pygame
from interface_homme_machine import homme_machine


pygame.init()

# Générer la fenêtre de notre jeu
pygame.display.set_caption("play")
screen = pygame.display.set_mode((400, 400))

# Importer et charger l'arrière-plan de notre jeu
background = pygame.image.load('photo/othello1.jpg')
background = pygame.transform.scale(background, (400, 400))

# Importer ou charger notre bouton pour remporter la partie
play_button = pygame.image.load('photo/bouton2.png')
play_button = pygame.transform.scale(play_button, (150, 50))
play_button_rect = play_button.get_rect(topleft=(50, 300))

running = True

# Boucle tant que cette condition est vraie
while running:
    # Si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # Si l'événement est la fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérification pour savoir si la souris est en collision avec le bouton
            if play_button_rect.collidepoint(event.pos):
                # Mettre le jeu en mode "lancé"
                pygame.quit()
                homme_machine()
    
    screen.blit(background, (0, 0))
    screen.blit(play_button, (50, 300))

    pygame.display.flip()
