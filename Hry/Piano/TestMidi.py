import pygame
import pygame.midi
 
# Inicializace Pygame a MIDI
pygame.init()
pygame.midi.init()
 
# Nastavení obrazovky
width, height = 700, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Piano")
 
# Inicializace MIDI výstupu
midi_out = pygame.midi.Output(0)
 
# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
# Definice kláves
white_keys = [pygame.Rect(i * 50, height - 200, 50, 200) for i in range(14) ]
black_keys = [pygame.Rect(35 + i * 50, height - 200, 30, 120)
    for i in range(14) if i % 7 not in (2, 6) ]
 
# Mapování MIDI not
white_notes = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83]
black_notes = [61, 63, 66, 68, 70, 73, 75, 78, 80, 82]
 
# Upravené mapování kláves klávesnice na MIDI noty
keyboard_to_note = {
    pygame.K_a: 60,  # C
    pygame.K_s: 62,  # D
    pygame.K_d: 64,  # E
    pygame.K_f: 65,  # F
    pygame.K_g: 67,  # G
    pygame.K_h: 69,  # A
    pygame.K_j: 71,  # B
    pygame.K_k: 72,  # C (vyšší oktáva)
    pygame.K_l: 74,  # D
    pygame.K_SEMICOLON: 76,  # E
    pygame.K_QUOTE: 77,  # F
    pygame.K_BACKSLASH: 79,  # G
    pygame.K_w: 61,  # C#
    pygame.K_e: 63,  # D#
    pygame.K_t: 66,  # F#
    pygame.K_y: 68,  # G#
    pygame.K_u: 70,  # A#
    pygame.K_o: 73,  # C# (vyšší oktáva)
    pygame.K_p: 75,  # D# (vyšší oktáva)
    pygame.K_LEFTBRACKET: 78,  # F# (vyšší oktáva)
}
 
# Mapování písmen na klávesy
key_labels = {
    60: "A", 62: "S", 64: "D", 65: "F", 67: "G", 69: "H", 71: "J", 72: "K", 74: "L", 76: ";", 77: "'", 79: "\\",
    61: "W", 63: "E", 66: "T", 68: "Y", 70: "U", 73: "O", 75: "P", 78: "["
}
 
# Inicializace fontu
pygame.font.init()
font = pygame.font.Font(None, 24)
 
# Přidejte tuto proměnnou před hlavní smyčku
current_notes = set()
current_note = None
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in keyboard_to_note:
                note = keyboard_to_note[event.key]
                if note not in current_notes:
                    midi_out.note_on(note, 127)
                    current_notes.add(note)
        elif event.type == pygame.KEYUP:
            if event.key in keyboard_to_note:
                note = keyboard_to_note[event.key]
                if note in current_notes:
                    midi_out.note_off(note, 0)
                    current_notes.remove(note)
        elif event.type == pygame.MOUSEBUTTONUP:
            if current_note is not None:
                midi_out.note_off(current_note, 0)
                current_note = None
 
    # Přesunuto mimo smyčku událostí
    if pygame.mouse.get_pressed()[0]:  # Levé tlačítko myši je stisknuto
        pos = pygame.mouse.get_pos()
        new_note = None
        for i, key in enumerate(black_keys):
            if key.collidepoint(pos):
                new_note = black_notes[i]
                break
        if new_note is None:
            for i, key in enumerate(white_keys):
                if key.collidepoint(pos):
                    new_note = white_notes[i]
                    break
       
        if new_note != current_note:
            if current_note is not None:
                midi_out.note_off(current_note, 0)
            if new_note is not None:
                midi_out.note_on(new_note, 127)
            current_note = new_note
 
    # Vykreslení kláves
    screen.fill(WHITE)
    for i, key in enumerate(white_keys):
        color = BLACK if white_notes[i] in current_notes else WHITE
        pygame.draw.rect(screen, color, key)
        pygame.draw.rect(screen, BLACK, key, 2)
        if white_notes[i] in key_labels:
            label = font.render(key_labels[white_notes[i]], True, BLACK if color == WHITE else WHITE)
            screen.blit(label, (key.x + key.width // 2 - label.get_width() // 2, key.y + key.height - 30))
    for i, key in enumerate(black_keys):
        color = WHITE if black_notes[i] in current_notes else BLACK
        pygame.draw.rect(screen, color, key)
        if black_notes[i] in key_labels:
            label = font.render(key_labels[black_notes[i]], True, BLACK if color == WHITE else WHITE)
            screen.blit(label, (key.x + key.width // 2 - label.get_width() // 2, key.y + key.height - 30))
 
    pygame.display.flip()
 
# Ukončení
pygame.midi.quit()
pygame.quit()