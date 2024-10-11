import os
import pygame
import random

#
# Hra na osazená pole tečky na čtverečkovaném papíru.
#

# Inicializace Pygame
pygame.init()

# Konstanty
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Proměnné
GRID_SIZE_X, GRID_SIZE_Y = 20, 20  # Odpovídá přibližně A4 papíru s mřížkou 5x5 mm

grid = []
current_player = 'human'
scores = {'human': 0, 'ai': 0}
game_state = 'menu'  # 'menu', 'game', 'game_over'

# Inicializace okna
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Čtverečky (Dots Game)")

# Fonty
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Přidáme novou globální proměnnou pro ukládání čar
lines = set()

def calculate_grid_parameters():
    screen_width, screen_height = screen.get_size()
    cell_size = min(screen_width // GRID_SIZE_X, screen_height // GRID_SIZE_Y)
    grid_offset_x = (screen_width - (GRID_SIZE_X - 1) * cell_size) // 2
    grid_offset_y = (screen_height - (GRID_SIZE_Y - 1) * cell_size) // 2
    return cell_size, grid_offset_x, grid_offset_y

def initialize_grid():
    global grid, lines
    grid = [[None for _ in range(GRID_SIZE_Y)] for _ in range(GRID_SIZE_X)]
    lines = set()

def draw_grid():
    cell_size, grid_offset_x, grid_offset_y = calculate_grid_parameters()
    for i in range(GRID_SIZE_X):
        for j in range(GRID_SIZE_Y):
            x = grid_offset_x + i * cell_size
            y = grid_offset_y + j * cell_size
            pygame.draw.line(screen, BLUE, (x, grid_offset_y), (x, grid_offset_y + (GRID_SIZE_Y - 1) * cell_size))
            pygame.draw.line(screen, BLUE, (grid_offset_x, y), (grid_offset_x + (GRID_SIZE_X - 1) * cell_size, y))
            
            if grid[i][j]:
                color = GREEN if grid[i][j] == 'human' else RED
                pygame.draw.circle(screen, color, (x, y), cell_size // 4)
    
    # Vykreslení čar spojujících obklíčené body
    for (x1, y1), (x2, y2) in lines:
        pygame.draw.line(screen, BLACK, 
                         (grid_offset_x + x1 * cell_size, grid_offset_y + y1 * cell_size),
                         (grid_offset_x + x2 * cell_size, grid_offset_y + y2 * cell_size), 2)

def draw_scores():
    human_score = small_font.render(f"Člověk: {scores['human']}", True, BLACK)
    ai_score = small_font.render(f"AI: {scores['ai']}", True, BLACK)
    screen.blit(human_score, (10, screen.get_height() - 60))
    screen.blit(ai_score, (10, screen.get_height() - 30))

def draw_menu():
    screen_width, screen_height = screen.get_size()
    title = font.render("Čtverečky (Dots Game)", True, BLACK)
    instruction = small_font.render("Stiskněte mezerník pro start hry", True, BLACK)
    size_info = small_font.render(f"Velikost herního pole: {GRID_SIZE_X}x{GRID_SIZE_Y}", True, BLACK)
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, screen_height // 3))
    screen.blit(instruction, (screen_width // 2 - instruction.get_width() // 2, screen_height // 2))
    screen.blit(size_info, (screen_width // 2 - size_info.get_width() // 2, screen_height // 2 + 30))

def draw_game_over():
    screen_width, screen_height = screen.get_size()
    game_over_text = font.render("Hra skončila!", True, BLACK)
    if scores['human'] > scores['ai']:
        winner_text = font.render("Člověk vyhrál!", True, BLACK)
    elif scores['ai'] > scores['human']:
        winner_text = font.render("AI vyhrála!", True, BLACK)
    else:
        winner_text = font.render("Remíza!", True, BLACK)
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - 50))
    screen.blit(winner_text, (screen_width // 2 - winner_text.get_width() // 2, screen_height // 2))

def get_clicked_point(pos):
    cell_size, grid_offset_x, grid_offset_y = calculate_grid_parameters()
    x = (pos[0] - grid_offset_x + cell_size // 2) // cell_size
    y = (pos[1] - grid_offset_y + cell_size // 2) // cell_size
    if 0 <= x < GRID_SIZE_X and 0 <= y < GRID_SIZE_Y:
        return x, y
    return None, None

def get_okoli_bodu(x, y):
    return [(x+dx, y+dy) for dx, dy in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
            # filtruje body které jsou mimo rozsah mřížky
            if 0 <= x+dx < GRID_SIZE_X and 0 <= y+dy < GRID_SIZE_Y]

def flood_fill(x, y, player, visited):
    if (x, y) in visited or grid[x][y] != player:
        return set()
    
    visited.add((x, y))
    points = {(x, y)}
    
    # přidání bodů
    for nx, ny in get_okoli_bodu(x, y):
        # rekuze y dal
        points |= flood_fill(nx, ny, player, visited)
    
    return points

def is_surrounded(points, player):
    # print("Seznam ", player, points)
    border_points = set()
    for x, y in points:
        # print("okoli ",get_okoli_bodu(x, y))
        for nx, ny in get_okoli_bodu(x, y):
            # print(grid[nx][ny])
            if grid[nx][ny] is None or grid[nx][ny] == player:
                return False
            if grid[nx][ny] != player:
                border_points.add((nx, ny))
    print("connect_surrounding_points", border_points)
    connect_surrounding_points(border_points)
    # return True
    return False

def has_closed_loop(grid, start_x, start_y, player):
    
    # Směry pro pohyb (nahoru, dolů, doleva, doprava, diagonálně)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # Funkce pro kontrolu platnosti pozice v mřížce
    def is_valid(x, y):
        return 0 <= x < GRID_SIZE_X and 0 <= y < GRID_SIZE_Y

    # DFS funkce pro prohledávání smyčky
    def dfs(x, y, parent_x, parent_y, visited, player, body):     
        visited.add((x, y))
        body.append((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if is_valid(nx, ny) and grid[nx][ny] == player:
                if (nx, ny) in visited:
                    # Pokud je soused navštíven a není to rodičovský vrchol, máme smyčku
                    if (nx, ny) != (parent_x, parent_y):
                        return body[body.index((nx, ny)):]
                else:
                    # Rekurzivní volání DFS pro sousední vrchol
                    result = dfs(nx, ny, x, y, visited, player, body)
                    if result:
                        return result
        body.pop()
        return None

    # body = {(x, y)}        
    os.system("cls")
    # Kontrola uzavřené smyčky z konkrétního bodu
    if grid[start_x][start_y] == player:
        print("None ",grid[start_x][start_y])
        visited = set()
        loop = dfs(start_x, start_y, -1, -1, visited, player, [])
        if loop:
            return loop

    return None


def connect_surrounding_points(points):
    print("line")
    global lines
    sorted_points = sorted(points)
    for i in range(len(sorted_points)):
        for j in range(i+1, len(sorted_points)):
            x1, y1 = sorted_points[i]
            x2, y2 = sorted_points[j]
            # print("line",x1,y1,x2,y2)
            if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:              
                lines.add(((x1, y1), (x2, y2)))

def update_scores(x,y):
    bodyline = has_closed_loop(grid,x,y,current_player)
    print("doplnek ",bodyline)
    if len(bodyline) > 3:
        connect_surrounding_points(bodyline)
    # global scores, grid, lines
    # prázná množina
    visited = set()

    for x in range(GRID_SIZE_X):
        for y in range(GRID_SIZE_Y):
            if grid[x][y] and (x, y) not in visited:
                player = grid[x][y]
                points = flood_fill(x, y, player, visited)
                # print("score ",points)
                # print("doplnek ",grid)
                if is_surrounded(points, player):
                    opponent = 'ai' if player == 'human' else 'human'
                    scores[opponent] += len(points)
                    for px, py in points:
                        grid[px][py] = None

def get_neighbors(x, y):
    neighbors = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE_X and 0 <= ny < GRID_SIZE_Y:
            neighbors.append((nx, ny))
    return neighbors

def count_player_neighbors(x, y, player):
    return sum(1 for nx, ny in get_neighbors(x, y) if grid[nx][ny] == player)

def find_best_move():
    best_score = -1
    best_moves = []
    
    for x in range(GRID_SIZE_X):
        for y in range(GRID_SIZE_Y):
            if grid[x][y] is None:
                # Prioritize moves that surround human player's dots
                human_neighbors = count_player_neighbors(x, y, 'human')
                ai_neighbors = count_player_neighbors(x, y, 'ai')
                
                # Calculate a score for this move
                score = human_neighbors * 2 + ai_neighbors
                
                # Check if this move would complete a square
                if human_neighbors == 3:
                    score += 10
                
                if score > best_score:
                    best_score = score
                    best_moves = [(x, y)]
                elif score == best_score:
                    best_moves.append((x, y))
    
    return best_moves

def make_ai_move():
    global current_player
    best_moves = find_best_move()
    
    if best_moves:
        x, y = random.choice(best_moves)
        if grid[x][y] is None:  # Přidáno ověření, že bod je prázdný
            grid[x][y] = 'ai'
            # print("stroj random ",x,y)
            update_scores(x,y)
            current_player = 'human'
    else:
        available_moves = [(x, y) for x in range(GRID_SIZE_X) for y in range(GRID_SIZE_Y) if grid[x][y] is None]
        if available_moves:
            x, y = random.choice(available_moves)
            grid[x][y] = 'ai'
            print("stroj nejlepsi ",x,y)
            update_scores(x,y)
            current_player = 'human'

def check_game_over():
    return all(all(cell is not None for cell in row) for row in grid)

# Hlavní herní smyčka
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state == 'menu':
                game_state = 'game'
                initialize_grid()
            elif event.key == pygame.K_r and game_state == 'game_over':
                game_state = 'menu'
                scores = {'human': 0, 'ai': 0}
        elif event.type == pygame.MOUSEBUTTONDOWN and game_state == 'game' and current_player == 'human':
            x, y = get_clicked_point(event.pos)
            if x is not None and y is not None and grid[x][y] is None:  # Přidáno ověření, že bod je prázdný
                grid[x][y] = 'human'
                # print("clovek ",x,y)
                update_scores(x,y)
                current_player = 'ai'
                
                if check_game_over():
                    game_state = 'game_over'
    
    screen.fill(WHITE)
    
    if game_state == 'menu':
        draw_menu()
    elif game_state == 'game':
        draw_grid()
        draw_scores()
        if current_player == 'ai':
            make_ai_move()
            if check_game_over():
                game_state = 'game_over'
    elif game_state == 'game_over':
        draw_grid()
        draw_scores()
        draw_game_over()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()