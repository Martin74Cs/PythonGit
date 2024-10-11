import tensorflow as tf
import numpy as np
import pygame
import sys
import random

class PingPongAI:
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 60
    BALL_SIZE = 10
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Ping Pong AI")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
        self.initialize_game()
        self.initialize_neural_network()

    def initialize_game(self):
        self.ball_x = self.SCREEN_WIDTH // 2
        self.ball_y = self.SCREEN_HEIGHT // 2
        self.reset_ball()
        self.player_paddle_y = self.SCREEN_HEIGHT // 2 - self.PADDLE_HEIGHT // 2
        self.ai_paddle_y = self.SCREEN_HEIGHT // 2 - self.PADDLE_HEIGHT // 2
        self.player_score = 0
        self.ai_score = 0

    def reset_ball(self):
        self.ball_x = self.SCREEN_WIDTH // 2
        self.ball_y = self.SCREEN_HEIGHT // 2
        angle = random.uniform(-np.pi/4, np.pi/4)
        speed = 5
        self.ball_speed_x = speed * np.cos(angle)
        self.ball_speed_y = speed * np.sin(angle)
        if random.choice([True, False]):
            self.ball_speed_x = -self.ball_speed_x

    def initialize_neural_network(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(24, activation='relu', input_shape=(4,)),
            tf.keras.layers.Dense(3)
        ])
        self.model.compile(optimizer='adam', loss='mse')

    def get_game_state(self):
        return np.array([
            self.ball_x / self.SCREEN_WIDTH,
            self.ball_y / self.SCREEN_HEIGHT,
            self.ai_paddle_y / self.SCREEN_HEIGHT,
            self.ball_speed_y
        ])

    def get_ai_action(self):
        state = self.get_game_state().reshape(1, -1)
        q_values = self.model.predict(state)[0]
        return np.argmax(q_values)

    def update_game(self):
        # Aktualizace pozice míčku
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        # Odraz od horní a dolní stěny
        if self.ball_y <= 0 or self.ball_y >= self.SCREEN_HEIGHT - self.BALL_SIZE:
            self.ball_speed_y = -self.ball_speed_y

        # Kontrola kolize s pálkami
        if (self.ball_x <= self.PADDLE_WIDTH and
            self.ball_y + self.BALL_SIZE >= self.player_paddle_y and
            self.ball_y <= self.player_paddle_y + self.PADDLE_HEIGHT):
            self.ball_speed_x = abs(self.ball_speed_x)  # Odraz doprava
            self.ball_speed_y += random.uniform(-1, 1)  # Přidání náhodnosti
        elif (self.ball_x >= self.SCREEN_WIDTH - self.PADDLE_WIDTH - self.BALL_SIZE and
              self.ball_y + self.BALL_SIZE >= self.ai_paddle_y and
              self.ball_y <= self.ai_paddle_y + self.PADDLE_HEIGHT):
            self.ball_speed_x = -abs(self.ball_speed_x)  # Odraz doleva
            self.ball_speed_y += random.uniform(-1, 1)  # Přidání náhodnosti

        # Normalizace rychlosti míčku
        speed = np.sqrt(self.ball_speed_x**2 + self.ball_speed_y**2)
        self.ball_speed_x = self.ball_speed_x / speed * 5
        self.ball_speed_y = self.ball_speed_y / speed * 5

        # Skórování
        if self.ball_x <= 0:
            self.ai_score += 1
            self.reset_ball()
        elif self.ball_x >= self.SCREEN_WIDTH - self.BALL_SIZE:
            self.player_score += 1
            self.reset_ball()

        # Pohyb AI pálky
        action = self.get_ai_action()
        if action == 0 and self.ai_paddle_y > 0:
            self.ai_paddle_y -= 5
        elif action == 1 and self.ai_paddle_y < self.SCREEN_HEIGHT - self.PADDLE_HEIGHT:
            self.ai_paddle_y += 5

    def draw_game(self):
        self.screen.fill(self.BLACK)
        
        # Vykreslení pálek
        pygame.draw.rect(self.screen, self.WHITE, (0, self.player_paddle_y, self.PADDLE_WIDTH, self.PADDLE_HEIGHT))
        pygame.draw.rect(self.screen, self.WHITE, (self.SCREEN_WIDTH - self.PADDLE_WIDTH, self.ai_paddle_y, self.PADDLE_WIDTH, self.PADDLE_HEIGHT))
        
        # Vykreslení míčku
        pygame.draw.rect(self.screen, self.WHITE, (self.ball_x, self.ball_y, self.BALL_SIZE, self.BALL_SIZE))
        
        # Vykreslení skóre
        player_score_text = self.font.render(str(self.player_score), True, self.WHITE)
        ai_score_text = self.font.render(str(self.ai_score), True, self.WHITE)
        self.screen.blit(player_score_text, (self.SCREEN_WIDTH // 4, 20))
        self.screen.blit(ai_score_text, (3 * self.SCREEN_WIDTH // 4, 20))
        
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.player_paddle_y > 0:
                    self.player_paddle_y -= 5
                elif event.key == pygame.K_DOWN and self.player_paddle_y < self.SCREEN_HEIGHT - self.PADDLE_HEIGHT:
                    self.player_paddle_y += 5

    def play_game(self):
        while True:
            self.handle_events()
            self.update_game()
            self.draw_game()
            self.clock.tick(60)  # 60 FPS

if __name__ == "__main__":
    game = PingPongAI()
    game.play_game()
