import random
#fonction qui qui creer la matrix 2x2
def initialiser_plateau():
  a=[['*'for i in range(8)]for j in range(8)]
  a[3][3]="B"
  a[3][4]="N"
  a[4][3]="N"
  a[4][4]="B"
  return a

#fonction qui affiche le tableau de jeux 
def afficher_plateau(a):
  print("  A B C D E F G H")
  for i in range(8):
      print(i+1, end=" ")
      for j in range(8):
          print(a[i][j], end=" ")
      print(" ")


#fonction qui verifie si l'emplacement choisi est valide 
def est_emplacement_valide(plateau, ligne, colonne, joueur):
  if plateau[ligne][colonne] != '*':
      return False
  directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1), (1, 0), (1, 1)]
  adversaire = 'B' if joueur == 'N' else 'N'
  for dr, dc in directions:
      r, c = ligne + dr, colonne + dc
      valide = False
      while 0 <= r < len(plateau) and 0 <= c < len(plateau[0]):
          if plateau[r][c] == '*':
              break
          if plateau[r][c] == adversaire:
              valide = True
          else:
              if valide:
                  return True
              break
          r, c = r + dr, c + dc
  
  return False


#fonction qui positionne le pion et retourne les pions adverse si l'emplacement choisie est valide 
def placer_pion(plateau, ligne, colonne, joueur):
  if not est_emplacement_valide(plateau, ligne, colonne, joueur):
      return False
  
  directions = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1), (1, 0), (1, 1)]
  
  adversaire = 'B' if joueur == 'N' else 'N'
  plateau[ligne][colonne] = joueur
  
  for dr, dc in directions:
      r, c = ligne + dr, colonne + dc
      flip_list = []
      while 0 <= r < len(plateau) and 0 <= c < len(plateau[0]):
          if plateau[r][c] == '*':
              break
          if plateau[r][c] == adversaire:
              flip_list.append((r, c))
          else:
              if len(flip_list) > 0 and plateau[r][c] == joueur:
                  for flip_row, flip_col in flip_list:
                      plateau[flip_row][flip_col] = joueur
                  break
              else:
                  break
          r, c = r + dr, c + dc
  
  return True


#fonction pour compter le nombre de pions
def compter_pions(plateau):
    count_b = sum(row.count('B') for row in plateau)
    count_n = sum(row.count('N') for row in plateau)
    return count_b, count_n

#fonction qui permet à l'ordinateur de jouer en choisissant une position de façon aléatoire parmis les positions possibles
def jouer_ordinateur(board, joueur_actuel):
        moves = [(i, j) for i in range(8) for j in range(8) if est_emplacement_valide(board, i, j, joueur_actuel)]
        if moves:
            return random.choice(moves)
        else:
            return None


#fonction principale du jeux 
def jeu_othello():
  print("-----------------------------------------------")
  print("Bienvenue sur le plateau de jeux othello")
  print("-----------------------------------------------")
  plateau = initialiser_plateau()
  joueur_actuel = 'N'
  while True:
      afficher_plateau(plateau)
      count_b, count_n = compter_pions(plateau)
      print(f'Nombre de pions B: {count_b}, Nombre de pions N: {count_n}')

      if not any(est_emplacement_valide(plateau, i, j, joueur_actuel) for i in range(8) for j in range(8)):
          break

      while True:
          try:
              row = int(input(f'Joueur {joueur_actuel}, Choisissez la ligne (0-7) : '))
              col = int(input(f'Joueur {joueur_actuel}, Choisissez la colonne (0-7) : '))
              if est_emplacement_valide(plateau, row, col, joueur_actuel):
                  break
              else:
                  print("Emplacement invalide. Veuillez choisir à nouveau.")
          except ValueError:
              print("Veuillez entrer un nombre valide.")

      placer_pion(plateau, row, col, joueur_actuel)
      joueur_actuel = 'N' if joueur_actuel == 'B' else 'B'

  count_b, count_n = compter_pions(plateau)
  print("Jeu terminé!")
  print(f'Nombre de pions B: {count_b}, Nombre de pions N: {count_n}')
  if count_b > count_n:
      print("Le joueur B a gagné!")
  elif count_n > count_b:
      print("Le joueur N a gagné!")
  else:
      print("Match nul!")

# Lancer le jeu
#jeu_othello()