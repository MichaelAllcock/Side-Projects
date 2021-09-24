# Name: Michael Allcock
# Date: 8/19/21
# Description: Tic Tac Toe game using a gui with numpy and pygame.

import pygame
import sys
import numpy as np

pygame.init()

# Initialize Game
player = 1
game_over = False

# Board Constants
Width = 600
Height = 600
Line_Width = 15
Board_Rows = 3
Board_Cols = 3
Circle_Radius = 60
Circle_Width = 15
X_Width = 15
Space = 45

# Colors in RGB format
BG_Color = (28, 170, 156)
Line_Color = (23, 145, 135)
Circle_Color = (0, 0, 0)
X_Color = (255, 255, 255)
Win_Color = (0, 0, 0)

# Set up pygame Screen
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_Color)

# Board
board = np.zeros((Board_Rows, Board_Cols))


# Functions ---------------------------------------------------------------
def draw_lines():
    """Function to draw the lines for the tic tac toe board"""
    # Horizontal Line 1:
    pygame.draw.line(screen, Line_Color, (0, 200), (600, 200), Line_Width)
    # Horizontal Line 2:
    pygame.draw.line(screen, Line_Color, (0, 400), (600, 400), Line_Width)

    # Vertical Line 1:
    pygame.draw.line(screen, Line_Color, (200, 0), (200, 600), Line_Width)
    # Vertical Line 2:
    pygame.draw.line(screen, Line_Color, (400, 0), (400, 600), Line_Width)


def mark_squares(row, col, player):
    """Function to mark squares on the board"""
    board[row][col] = player


def available_square(row, col):
    """Function to check which squares have not been marked. True if available, False if not."""
    if board[row][col] == 0:
        return True
    else:
        return False


def is_board_full():
    """Function to check if the board is completely full. Returns True if Full"""
    for row in range(Board_Rows):
        for col in range(Board_Cols):
            if board[row][col] == 0:
                return False

    return True


def draw_figures():
    """Function to draw figure for the correct player on the board"""
    for row in range(Board_Rows):
        for col in range(Board_Cols):
            # If player 1 has marked a square
            if board[row][col] == 1:
                pygame.draw.circle(screen, Circle_Color, (int(col * 200 + 100), int(row * 200 + 100)), Circle_Radius, Circle_Width)
                # Position: X Coor = width of screen / 3. Y Coor = height of screen / 6

            elif board[row][col] == 2:
                pygame.draw.line(screen, X_Color, (col * 200 + Space, row * 200 + 200 - Space), (col * 200 + 200 - Space, row * 200 + Space), X_Width)
                pygame.draw.line(screen, X_Color, (col * 200 + Space, row * 200 + Space), (col * 200 + 200 - Space, row * 200 + 200 - Space), X_Width)


def check_win(player):
    """Function checks if a player has won the game"""
    # Vertical win check
    for col in range(Board_Cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # Horizontal win check
    for row in range(Board_Rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # Asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # Desc Diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    """Function that draws the vertical winning line"""
    posX = col * 200 + 100

    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = X_Color

    pygame.draw.line(screen, color, (posX, 15), (posX, Height - 15), 15)


def draw_horizontal_winning_line(row, player):
    """Function that draws the horizontal winning line"""
    posY = row * 200 + 100

    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = X_Color

    pygame.draw.line(screen, color, (15, posY), (Width - 15, posY), 15)


def draw_asc_diagonal(player):
    """Function draws an ascending winning line"""
    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = X_Color

    pygame.draw.line(screen, color, (15, Height - 15), (Width - 15, 15), 15)


def draw_desc_diagonal(player):
    """Function draws descending winning line"""
    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = X_Color

    pygame.draw.line(screen, color, (15, 15), (Width - 15, Height - 15), 15)


def restart():
    """Function to restart the game"""
    screen.fill(BG_Color)
    draw_lines()
    player = 1
    for row in range(Board_Rows):
        for col in range(Board_Cols):
            board[row][col] = 0


def text_objects(text, font):
    """Sets the text objects to be displayed"""
    text_Surface = font.render(text, True, Win_Color, X_Color)
    return text_Surface, text_Surface.get_rect()


def message_display(text):
    """Function to display the message on the screen"""
    large_Text = pygame.font.Font('freesansbold.ttf', 32)
    TextSurf, TextRect = text_objects(text, large_Text)
    TextRect.center = (Width // 2, Height // 2)
    screen.blit(TextSurf, TextRect)


draw_lines()

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# Link screen board with console board
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouse_X = event.pos[0]  # x coordinate
            mouse_Y = event.pos[1]  # y coordinate

            clicked_row = int(mouse_Y // 200)
            clicked_col = int(mouse_X // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_squares(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2

                elif player == 2:
                    mark_squares(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1

                draw_figures()

# Display text
            if check_win(1):
                message_display('Player 1 Wins!')

            elif check_win(2):
                message_display('Player 2 Wins!')

            elif is_board_full() is True:
                message_display('Draw! Press "r" to restart.')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()
