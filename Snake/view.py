import pygame
import logging

# Couleurs
blanc = (255, 255, 255)
jaune = (255, 255, 102)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (2, 112, 21)
bleu = (50, 153, 213)
mauve = (229, 202, 255)

class GameView:
    def __init__(self, model, width=500, height=500, cell_size=10):
        # Référence au modèle de jeu
        self.model = model
        # Dimensions de la fenêtre de jeu
        self.width = width
        self.height = height
        # Taille d'une cellule (segment du serpent ou nourriture)
        self.cell_size = cell_size
        # Initialisation de la fenêtre de jeu
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Python')
        # Police pour l'affichage du score
        self.font = pygame.font.SysFont("bahnschrift", 20)
        # Charger l'image de la pomme
        self.apple_image = pygame.image.load("icons/apple.png")
        # Redimensionner l'image de la pomme pour qu'elle corresponde à la taille de la cellule
        self.apple_image = pygame.transform.scale(self.apple_image, (self.cell_size, self.cell_size))
        # Charger l'image de fond et de game over
        self.background_image = pygame.image.load("icons/background.png")
        self.background_gameover = pygame.image.load("icons/gameover.jpg")
        # Redimensionner l'image de fond et de game over pour qu'elle corresponde à la taille de la fenêtre
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        self.background_gameover = pygame.transform.scale(self.background_gameover, (self.width, self.height))
        logging.info(f"Initialisation de la vue du jeu : {self.width}x{self.height}, taille des cellules : {self.cell_size}")

    def draw(self):
        # Dessiner l'image de fond
        self.screen.blit(self.background_image, (0, 0))
        
        # Dessin de la tête du serpent
        head = self.model.snake.body[0]
        head_x = head[0] * self.cell_size
        head_y = head[1] * self.cell_size
        pygame.draw.ellipse(self.screen, vert, [
            head_x, head_y,
            self.cell_size, self.cell_size
        ])
        logging.debug(f"Affichage de la tête du serpent à : {head_x}, {head_y}")
        
        # Dessiner les yeux du serpent
        eye_radius = self.cell_size // 10
        eye_offset_x = self.cell_size // 4
        eye_offset_y = self.cell_size // 4
        pygame.draw.circle(self.screen, noir, (head_x + eye_offset_x, head_y + eye_offset_y), eye_radius)
        pygame.draw.circle(self.screen, noir, (head_x + self.cell_size - eye_offset_x, head_y + eye_offset_y), eye_radius)
        
        # Dessin des segments du corps du serpent
        for segment in self.model.snake.body[1:]:
            pygame.draw.ellipse(self.screen, vert, [
                segment[0] * self.cell_size, segment[1] * self.cell_size,
                self.cell_size, self.cell_size
            ])
            logging.debug(f"Affichage du segment du serpent à : {segment[0] * self.cell_size}, {segment[1] * self.cell_size}")
        
        # Dessin de la nourriture en utilisant l'image de la pomme
        food_x = self.model.food.position[0] * self.cell_size
        food_y = self.model.food.position[1] * self.cell_size
        self.screen.blit(self.apple_image, (food_x, food_y))
        logging.debug(f"Affichage de la nourriture à : {food_x}, {food_y}")

        # Affichage du score
        score_text = self.font.render("Score: " + str(self.model.score), True, noir)
        self.screen.blit(score_text, [0, 0])
        pygame.display.flip()
        logging.info(f"Affichage du score : {self.model.score}")

    def display_message(self, message):
        # Affichage d'un message au centre de l'écran
        font = pygame.font.SysFont("bahnschrift", 35)
        message_text = font.render(message, True, (255, 255, 255))
        self.screen.blit(message_text, [self.width // 6, self.height // 2])
        pygame.display.flip()

class Button:
    def __init__(self, text, pos, size, color, hover_color, action):
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.font = pygame.font.SysFont("bahnschrift", 35)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        rect = pygame.Rect(self.pos, self.size)
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, rect, border_radius=15)
        else:
            pygame.draw.rect(screen, self.color, rect, border_radius=15)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (rect.x + (rect.width - text_surface.get_width()) // 2,
                                   rect.y + (rect.height - text_surface.get_height()) // 2))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(self.pos, self.size).collidepoint(event.pos):
                return True
        return False

class GameOverView:
    def __init__(self, width, height, background_image='icons/background1.jpg', background_gameover='icons/gameover.jpg'):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Game Over')
        self.running = True
        self.restart = False

        # Couleurs pastel
        green_pastel = (170, 197, 63)
        light_green_pastel = (160, 185, 55)

        # Boutons
        self.buttons = [
            Button("Restart", (self.width // 4 - 75, 100), (150, 50), green_pastel, light_green_pastel, self.restart_game),
            Button("Quit", (3 * self.width // 4 - 75, 100), (150, 50), green_pastel, light_green_pastel, self.quit_game)
        ]

        # Charger l'image de fond
        self.background_image = pygame.image.load(background_image)
        self.background_gameover = pygame.image.load(background_gameover)
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        self.background_gameover = pygame.transform.scale(self.background_gameover, (self.width, self.height))

    def draw_text(self, text, color, rect):
        font = pygame.font.SysFont("bahnschrift", 50)
        label = font.render(text, True, color)
        self.screen.blit(label, rect)

    def restart_game(self):
        self.restart = True
        self.running = False

    def quit_game(self):
        self.running = False

    def run(self):
        while self.running:
            self.screen.blit(self.background_gameover, (0, 0))

            for button in self.buttons:
                button.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                for button in self.buttons:
                    if button.is_clicked(event):
                        button.action()

        pygame.quit()
