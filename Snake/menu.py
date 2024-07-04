import pygame
from controller import GameController

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

class Menu:
    def __init__(self, width=500, height=500, background_image='icons/background1.jpg'):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Game Menu')
        self.running = True
        # Couleurs pastel
        green_pastel = (170, 197, 63)
        light_green_pastel = (160, 185, 55)
        self.buttons = [
            Button("Start", (self.width // 4 - 75, 100), (150, 50), green_pastel, light_green_pastel, self.start_game),
            Button("Quit", (3 * self.width // 4 - 75, 100), (150, 50), green_pastel, light_green_pastel, self.quit_game)
        ]
        # Charger l'image de fond
        self.background_image = pygame.image.load(background_image)
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

    def draw_text(self, text, color, rect):
        font = pygame.font.SysFont("bahnschrift", 50)
        label = font.render(text, True, color)
        self.screen.blit(label, rect)

    def start_game(self):
        print("Démarrage du jeu")
        game_controller = GameController()
        game_controller.run_game()
        self.running = False

    def quit_game(self):
        self.running = False
        print("Quitter le jeu")

    def run(self):
        while self.running:
            self.screen.blit(self.background_image, (0, 0))  # Dessiner l'image de fond

            for button in self.buttons:
                button.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    print("Événement QUIT détecté, arrêt du jeu")
                for button in self.buttons:
                    if button.is_clicked(event):
                        button.action()

        pygame.quit()

if __name__ == "__main__":
    pygame.init()
    menu = Menu()
    menu.run()
