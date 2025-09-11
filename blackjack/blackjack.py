import pygame
import random
import os

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)

# Fonts
font = pygame.font.SysFont(None, 36)

# Load card images (expects files like 'cards/2_of_hearts.png')
suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'jack': 10, 'queen': 10, 'king': 10, 'ace': 11
}

card_images = {}
for suit in suits:
    for rank in ranks:
        path = os.path.join("cards", f"{rank}_of_{suit}.png")
        if os.path.exists(path):
            card_images[(rank, suit)] = pygame.image.load(path)

# Functions
def calculate_hand(hand):
    value = sum(values[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == 'ace')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def deal_card(deck):
    return deck.pop()

def draw_hand(hand, x, y):
    for i, card in enumerate(hand):
        if card in card_images:
            screen.blit(card_images[card], (x + i * 80, y))
        else:
            pygame.draw.rect(screen, BLACK, (x + i * 80, y, 70, 100))

def blackjack():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    running = True
    player_turn = True
    result = None

    while running:
        screen.fill(GREEN)

        # Draw hands
        draw_hand(player_hand, 100, 400)
        draw_hand(dealer_hand, 100, 100)

        # Show values
        player_value = calculate_hand(player_hand)
        dealer_value = calculate_hand(dealer_hand)

        player_text = font.render(f"Player: {player_value}", True, WHITE)
        screen.blit(player_text, (100, 350))

        if not player_turn:
            dealer_text = font.render(f"Dealer: {dealer_value}", True, WHITE)
            screen.blit(dealer_text, (100, 220))

        # Show result if game ended
        if result:
            result_text = font.render(result, True, WHITE)
            screen.blit(result_text, (WIDTH//2 - 80, HEIGHT//2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and player_turn:
                if event.key == pygame.K_h:  # Hit
                    player_hand.append(deal_card(deck))
                    if calculate_hand(player_hand) > 21:
                        result = "Player busts! Dealer wins."
                        player_turn = False
                elif event.key == pygame.K_s:  # Stand
                    player_turn = False
                    while calculate_hand(dealer_hand) < 17:
                        dealer_hand.append(deal_card(deck))
                    dealer_value = calculate_hand(dealer_hand)
                    if dealer_value > 21 or player_value > dealer_value:
                        result = "Player wins!"
                    elif dealer_value > player_value:
                        result = "Dealer wins!"
                    else:
                        result = "It's a tie!"

    pygame.quit()

if __name__ == "__main__":
    blackjack()
