from final_console import est_emplacement_valide,placer_pion,compter_pions,initialiser_plateau
import pygame
import sys

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
# Taille de la fenêtre et du carré
SCREEN_SIZE = (400, 450)
SQUARE_SIZE = SCREEN_SIZE[0] // 8

#chargement image et son
#icon="photo/othello3.jpg"
#musique_pions="musique/click.ogg"

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Othello")
#pygame_icon=pygame.image.load(icon)
#pygame.display.set_icon(pygame_icon)

def draw_board(board):
        screen.fill(GREEN)
        for row in range(8):
            for col in range(8):
                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
                if board[row][col] == 'B':
                    pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 2)
                elif board[row][col] == 'N':
                    pygame.draw.circle(screen, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 2)

board=initialiser_plateau()
joueur_actuel = 'B'
game_over = False

while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_pos = pygame.mouse.get_pos()
                row = mouse_pos[1] // SQUARE_SIZE
                col = mouse_pos[0] // SQUARE_SIZE

                if est_emplacement_valide(board, row, col, joueur_actuel):
                    placer_pion(board, row, col, joueur_actuel)
                    joueur_actuel = 'N' if joueur_actuel == 'B' else 'B'
        draw_board(board)
        pygame.display.flip()

pygame.quit()
sys.exit()