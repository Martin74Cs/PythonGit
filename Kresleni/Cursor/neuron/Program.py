import pygame
import random
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

# Inicializace Pygame
pygame.init()

# Nastavení obrazovky
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neuronové Pong - Dva AI hráči")

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pálky a míček
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90
BALL_SIZE = 15

class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(4, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.tanh(self.fc4(x))
        return x

class PrioritizedReplayBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.priorities = np.zeros(capacity, dtype=np.float32)
        self.position = 0

    def push(self, state, action, reward, next_state, done):
        max_priority = np.max(self.priorities) if self.buffer else 1.0
        if len(self.buffer) < self.capacity:
            self.buffer.append((state, action, reward, next_state, done))
        else:
            self.buffer[self.position] = (state, action, reward, next_state, done)
        self.priorities[self.position] = max_priority
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size, alpha=0.6, beta=0.4):
        if len(self.buffer) == self.capacity:
            priorities = self.priorities
        else:
            priorities = self.priorities[:self.position]
        
        probs = priorities ** alpha
        probs /= probs.sum()

        indices = np.random.choice(len(self.buffer), batch_size, p=probs)
        samples = [self.buffer[idx] for idx in indices]

        weights = (len(self.buffer) * probs[indices]) ** (-beta)
        weights /= weights.max()

        return samples, indices, weights

    def update_priorities(self, indices, priorities):
        for idx, priority in zip(indices, priorities):
            self.priorities[idx] = priority

    def __len__(self):
        return len(self.buffer)

net_left = NeuralNet()
net_right = NeuralNet()
target_net_left = NeuralNet()
target_net_right = NeuralNet()
target_net_left.load_state_dict(net_left.state_dict())
target_net_right.load_state_dict(net_right.state_dict())

optimizer_left = optim.Adam(net_left.parameters(), lr=0.0005)
optimizer_right = optim.Adam(net_right.parameters(), lr=0.0005)

MEMORY_SIZE = 100000
memory_left = PrioritizedReplayBuffer(MEMORY_SIZE)
memory_right = PrioritizedReplayBuffer(MEMORY_SIZE)

loss_history_left = []
loss_history_right = []

def train_network(net, target_net, optimizer, memory, loss_history):
    if len(memory) < 1000:
        return

    samples, indices, weights = memory.sample(1000)
    states, actions, rewards, next_states, dones = zip(*samples)

    states = torch.FloatTensor(states)
    actions = torch.FloatTensor(actions)
    rewards = torch.FloatTensor(rewards)
    next_states = torch.FloatTensor(next_states)
    dones = torch.FloatTensor(dones)
    weights = torch.FloatTensor(weights)

    current_q_values = net(states).squeeze(1)
    next_q_values = target_net(next_states).squeeze(1)
    expected_q_values = rewards + (1 - dones) * 0.99 * next_q_values

    loss = (current_q_values - expected_q_values.detach()).pow(2) * weights
    priorities = loss + 1e-5
    loss = loss.mean()

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    memory.update_priorities(indices, priorities.detach().numpy())
    loss_history.append(loss.item())

def normalize_input(ball_x, ball_y, ball_dx, ball_dy, paddle_y):
    return [
        ball_x / WIDTH,
        ball_y / HEIGHT,
        ball_dx / 10,
        paddle_y / HEIGHT
    ]

def epsilon_greedy_action(net, input_tensor, epsilon):
    if random.random() < epsilon:
        return random.uniform(-1, 1)
    else:
        with torch.no_grad():
            return net(input_tensor).item()

def main():
    clock = pygame.time.Clock()
    left_paddle = pygame.Rect(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 25, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

    ball_dx, ball_dy = 5 * random.choice((1, -1)), 5 * random.choice((1, -1))
    left_speed = right_speed = 0

    epsilon = 1.0
    epsilon_decay = 0.9995
    epsilon_min = 0.01

    running = True
    frame_count = 0
    left_hits = right_hits = 0
    while running:
        frame_count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # AI pohyb pro levou pálku
        state_left = normalize_input(ball.x, ball.y, ball_dx, ball_dy, left_paddle.centery)
        input_tensor = torch.FloatTensor(state_left)
        left_action = epsilon_greedy_action(net_left, input_tensor, epsilon)
        left_speed = 15 * left_action

        left_paddle.y += left_speed
        left_paddle.clamp_ip(screen.get_rect())

        # AI pohyb pro pravou pálku
        state_right = normalize_input(WIDTH - ball.x, ball.y, -ball_dx, ball_dy, right_paddle.centery)
        input_tensor = torch.FloatTensor(state_right)
        right_action = epsilon_greedy_action(net_right, input_tensor, epsilon)
        right_speed = 15 * right_action

        right_paddle.y += right_speed
        right_paddle.clamp_ip(screen.get_rect())

        # Pohyb míčku
        old_ball_x, old_ball_y = ball.x, ball.y
        ball.x += ball_dx
        ball.y += ball_dy

        # Kolize s horní a dolní hranou
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy *= -1

        # Kolize s pálkami
        left_hit = right_hit = False
        if ball.colliderect(left_paddle):
            ball_dx *= -1
            left_hits += 1
            left_hit = True
        elif ball.colliderect(right_paddle):
            ball_dx *= -1
            right_hits += 1
            right_hit = True

        # Skórování
        left_scored = right_scored = False
        if ball.left <= 0:
            right_scored = True
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_dx = 5 * random.choice((1, -1))
            ball_dy = 5 * random.choice((1, -1))
        elif ball.right >= WIDTH:
            left_scored = True
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_dx = 5 * random.choice((1, -1))
            ball_dy = 5 * random.choice((1, -1))

        # Výpočet odměn
        reward_left = 0.1 if left_hit else (-1 if right_scored else 0)
        reward_right = 0.1 if right_hit else (-1 if left_scored else 0)

        # Uložení zkušeností
        next_state_left = normalize_input(ball.x, ball.y, ball_dx, ball_dy, left_paddle.centery)
        next_state_right = normalize_input(WIDTH - ball.x, ball.y, -ball_dx, ball_dy, right_paddle.centery)
        
        memory_left.push(state_left, left_action, reward_left, next_state_left, left_scored or right_scored)
        memory_right.push(state_right, right_action, reward_right, next_state_right, left_scored or right_scored)

        if frame_count % 4 == 0:  # Trénujeme každé 4 snímky
            train_network(net_left, target_net_left, optimizer_left, memory_left, loss_history_left)
            train_network(net_right, target_net_right, optimizer_right, memory_right, loss_history_right)

        if frame_count % 1000 == 0:  # Aktualizujeme cílové sítě každých 1000 snímků
            target_net_left.load_state_dict(net_left.state_dict())
            target_net_right.load_state_dict(net_right.state_dict())

        # Snižování epsilon
        epsilon = max(epsilon * epsilon_decay, epsilon_min)

        # Vykreslení
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

        # Zobrazení skóre
        font = pygame.font.Font(None, 36)
        left_score = font.render(str(left_hits), True, WHITE)
        right_score = font.render(str(right_hits), True, WHITE)
        screen.blit(left_score, (WIDTH//4, 10))
        screen.blit(right_score, (3*WIDTH//4, 10))

        pygame.display.flip()
        clock.tick(600)

    pygame.quit()

    # Vizualizace průběhu učení
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(loss_history_left)
    plt.title('Průběh učení levé neuronové sítě')
    plt.xlabel('Počet trénovacích iterací')
    plt.ylabel('Ztráta')
    
    plt.subplot(1, 2, 2)
    plt.plot(loss_history_right)
    plt.title('Průběh učení pravé neuronové sítě')
    plt.xlabel('Počet trénovacích iterací')
    plt.ylabel('Ztráta')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()