import pygame
import logging
from model import GameModel
from view import GameView, GameOverView

# Configuration du logger
logging.basicConfig(
    filename='snake_game.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'  # 'w' pour écrire à nouveau chaque début du jeu
)

class GameController:
    def __init__(self, width=500, height=500, cell_size=20):
        # Initialisation du modèle de jeu
        self.model = GameModel(width // cell_size, height // cell_size)
        # Initialisation de la vue de jeu
        self.view = GameView(self.model, width, height, cell_size)
        # Initialisation de l'horloge pour gérer le FPS
        self.clock = pygame.time.Clock()
        self.running = True
        logging.info("Initialisation du contrôleur du jeu")

    def process_events(self):
        # Gestion des événements (clavier, souris, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                logging.info("Événement QUIT détecté, arrêt du jeu")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.model.snake.change_direction((-1, 0))
                    logging.info("Changement de direction vers la gauche")
                elif event.key == pygame.K_RIGHT:
                    self.model.snake.change_direction((1, 0))
                    logging.info("Changement de direction vers la droite")
                elif event.key == pygame.K_UP:
                    self.model.snake.change_direction((0, -1))
                    logging.info("Changement de direction vers le haut")
                elif event.key == pygame.K_DOWN:
                    self.model.snake.change_direction((0, 1))
                    logging.info("Changement de direction vers le bas")

    def run_game(self):
        # Boucle principale du jeu
        while self.running:
            self.process_events()
            if not self.model.update():
                # Si le jeu est terminé, afficher le message de fin de jeu
                self.show_game_over()
            self.view.draw()
            self.clock.tick(12)  # Mettre à jour à chaque tick (12 FPS)
            logging.debug("Mise à jour de l'affichage à chaque tick")
        pygame.quit()
        logging.info("Fermeture du jeu")

    def show_game_over(self):
        # Afficher la vue de fin de jeu
        game_over_view = GameOverView(self.view.width, self.view.height)
        self.running = False
        game_over_view.run()
        if game_over_view.restart:
            # Redémarrage du jeu
            pygame.init()  # Réinitialiser Pygame
            self.model = GameModel(self.view.width // self.view.cell_size, self.view.height // self.view.cell_size)
            self.view = GameView(self.model, self.view.width, self.view.height, self.view.cell_size)
            self.running = True
            self.run_game()
