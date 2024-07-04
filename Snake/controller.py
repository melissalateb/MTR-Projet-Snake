import pygame
from model import GameModel
from view import GameView

class GameController:
    def __init__(self, width=500, height=500, cell_size=20):
        # Initialisation du modèle de jeu
        self.model = GameModel(width // cell_size, height // cell_size)
        # Initialisation de la vue de jeu
        self.view = GameView(self.model, width, height, cell_size)
        # Initialisation de l'horloge pour gérer le FPS
        self.clock = pygame.time.Clock()
        self.running = True
        print("Initialisation du contrôleur du jeu")

    def process_events(self):
        # Gestion des événements (clavier, souris, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                print("Événement QUIT détecté, arrêt du jeu")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.model.snake.change_direction((-1, 0))
                    print("Changement de direction vers la gauche")
                elif event.key == pygame.K_RIGHT:
                    self.model.snake.change_direction((1, 0))
                    print("Changement de direction vers la droite")
                elif event.key == pygame.K_UP:
                    self.model.snake.change_direction((0, -1))
                    print("Changement de direction vers le haut")
                elif event.key == pygame.K_DOWN:
                    self.model.snake.change_direction((0, 1))
                    print("Changement de direction vers le bas")

    def run_game(self):
        # Boucle principale du jeu
        while self.running:
            self.process_events()
            if not self.model.update():
                # Si le jeu est terminé, afficher le message de fin de jeu
                self.show_game_over()
            self.view.draw()
            self.clock.tick(12)  # Mettre à jour à chaque tick (15 FPS)
            print("Mise à jour de l'affichage à chaque tick")
        pygame.quit()
        print("Fermeture du jeu")

    def show_game_over(self):
        # Affichage du message de fin de jeu
        self.view.display_message("Game Over! Press R to Restart or Q to Quit")
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Redémarrage du jeu
                        self.model = GameModel(self.view.width // self.view.cell_size, self.view.height // self.view.cell_size)
                        self.view = GameView(self.model, self.view.width, self.view.height, self.view.cell_size)
                        waiting = False
                    elif event.key == pygame.K_q:
                        # Quitter le jeu
                        self.running = False
                        waiting = False
