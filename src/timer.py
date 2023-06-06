import pygame
from colors import get_color

def visualizeTimers(screen, timer_w, timer_b, board):
    font = pygame.font.Font("fonts/PublicPixel.ttf", 15)
    b_seconds = (int(timer_b.time / 60)) % 60
    b_minutes = int(timer_b.time / 3600)
    w_seconds = (int(timer_w.time / 60)) % 60
    w_minutes = int(timer_w.time / 3600)
    if board.Anzahlmoves%2 == 0:  # White player's turn
        # Light this when turn == player
        timer_w.time -= 1
        pygame.draw.rect(screen, get_color("background"),
                         pygame.Rect(128 + 15,
                                     100 + 64 * 8 + 20,
                                     512 - 30, 35))
    else:  # Black player's turn
        # Light this when turn == player
        timer_b.time -= 1
        pygame.draw.rect(screen, get_color("background"),
                         pygame.Rect(128 + 15,
                                     100 - 55,
                                     512 - 30, 35))
    # Print black player's timer
    b_text_surface = font.render("Player Black  ", False, get_color("text"))
    screen.blit(b_text_surface, (155, 55))
    b_timer_surface = font.render(f"00:{b_minutes:02}:{b_seconds:02}", False, get_color("text"))
    screen.blit(b_timer_surface, (355, 55))
    # Print white player's timer
    w_text_surface = font.render("Player White  ", False, get_color("text"))
    screen.blit(w_text_surface, (155, 128 + 64 * 8))
    w_timer_surface = font.render(f"00:{w_minutes:02}:{w_seconds:02}", False, get_color("text"))
    screen.blit(w_timer_surface, (355, 128 + 64 * 8))


class timer:
    def __init__(self):
        self.time = 72000  # 20 Minutes