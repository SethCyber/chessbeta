# Only imports required
import chess
import pygame
import time

# Essential variables
count = 1
pawn_promotion = False
rectangle_count = 0
Move = ""
entry = ""
initialFile = ""
initialBoardRow = ""
finalBoardRow = ""
finalFile = ""
currentLocation = ""
currentDestination = ""
yellow_pieces = ["yellow_king1", "yellow_queen1", "yellow_knight1", "yellow_knight2", "yellow_rook1", "yellow_rook2",
                 "yellow_bishop1", "yellow_bishop2",
                 "yellow_p1", "yellow_p2", "yellow_p3", "yellow_p4", "yellow_p5", "yellow_p6", "yellow_p7",
                 "yellow_p8", ]
red_pieces = ["red_king1", "red_queen1", "red_knight1", "red_knight2", "red_rook1", "red_rook2", "red_bishop1",
              "red_bishop2",
              "red_p1", "red_p2", "red_p3", "red_p4", "red_p5", "red_p6", "red_p7", "red_p8"]
light_brown = (240, 217, 181)
brown = (181, 136, 99)
rectangles = []
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Create the chess board
screen = pygame.display.set_mode((800, 800), pygame.FULLSCREEN)
board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
sq = {
    'a1': (0, 700), 'a2': (0, 600), 'a3': (0, 500), 'a4': (0, 400),
    'a5': (0, 300), 'a6': (0, 200), 'a7': (0, 100), 'a8': (0, 0),
    'b1': (100, 700), 'b2': (100, 600), 'b3': (100, 500), 'b4': (100, 400),
    'b5': (100, 300), 'b6': (100, 200), 'b7': (100, 100), 'b8': (100, 0),
    'c1': (200, 700), 'c2': (200, 600), 'c3': (200, 500), 'c4': (200, 400),
    'c5': (200, 300), 'c6': (200, 200), 'c7': (200, 100), 'c8': (200, 0),
    'd1': (300, 700), 'd2': (300, 600), 'd3': (300, 500), 'd4': (300, 400),
    'd5': (300, 300), 'd6': (300, 200), 'd7': (300, 100), 'd8': (300, 0),
    'e1': (400, 700), 'e2': (400, 600), 'e3': (400, 500), 'e4': (400, 400),
    'e5': (400, 300), 'e6': (400, 200), 'e7': (400, 100), 'e8': (400, 0),
    'f1': (500, 700), 'f2': (500, 600), 'f3': (500, 500), 'f4': (500, 400),
    'f5': (500, 300), 'f6': (500, 200), 'f7': (500, 100), 'f8': (500, 0),
    'g1': (600, 700), 'g2': (600, 600), 'g3': (600, 500), 'g4': (600, 400),
    'g5': (600, 300), 'g6': (600, 200), 'g7': (600, 100), 'g8': (600, 0),
    'h1': (700, 700), 'h2': (700, 600), 'h3': (700, 500), 'h4': (700, 400),
    'h5': (700, 300), 'h6': (700, 200), 'h7': (700, 100), 'h8': (700, 0),
}

# Create pieces and images
yellow_king1 = pygame.image.load('resized//yellow_king.png')
flipped_yellow_king1 = pygame.transform.flip(yellow_king1, False, True)
yellow_queen1 = pygame.image.load('resized//yellow_queen.png')
flipped_yellow_queen1 = pygame.transform.flip(yellow_queen1, False, True)
yellow_knight1 = pygame.image.load('resized//yellow_knight.png')
flipped_yellow_knight1 = pygame.transform.flip(yellow_knight1, False, True)
yellow_knight2 = pygame.image.load('resized//yellow_knight.png')
flipped_yellow_knight2 = pygame.transform.flip(yellow_knight2, False, True)
yellow_rook1 = pygame.image.load('resized//yellow_rook.png')
flipped_yellow_rook1 = pygame.transform.flip(yellow_rook1, False, True)
yellow_rook2 = pygame.image.load('resized//yellow_rook.png')
flipped_yellow_rook2 = pygame.transform.flip(yellow_rook2, False, True)
yellow_bishop1 = pygame.image.load('resized//yellow_bishop.png')
flipped_yellow_bishop1 = pygame.transform.flip(yellow_bishop1, False, True)
yellow_bishop2 = pygame.image.load('resized//yellow_bishop.png')
flipped_yellow_bishop2 = pygame.transform.flip(yellow_bishop2, False, True)
yellow_p1 = pygame.image.load('resized//yellow_pawn.png')
flipped_yellow_p1 = pygame.transform.flip(yellow_p1, False, True)
yellow_p2 = pygame.image.load('resized//yellow_pawn.png')
flipped_yellow_p2 = pygame.transform.flip(yellow_p2, False, True)
yellow_p3 = pygame.image.load('resized//yellow_pawn.png')
flipped_yellow_p3 = pygame.transform.flip(yellow_p3, False, True)
yellow_p4 = pygame.image.load('resized//yellow_pawn.png')
flipped_yellow_p4 = pygame.transform.flip(yellow_p4, False, True)
yellow_p5 = pygame.image.load('resized//yellow_pawn.png')
flipped_yellow_p5 = pygame.transform.flip(yellow_p5, False, True)
yellow_p6 = pygame.image.load('resized//yellow_pawn.png')
flipped_yellow_p6 = pygame.transform.flip(yellow_p6, False, True)
yellow_p7 = pygame.image.load('resized//yellow_pawn.png')
flipped_yellow_p7 = pygame.transform.flip(yellow_p7, False, True)
yellow_p8 = pygame.image.load('resized//yellow_pawn.png')
flipped_yellow_p8 = pygame.transform.flip(yellow_p8, False, True)
red_king1 = pygame.image.load('resized//red_king.png')
flipped_red_king1 = pygame.transform.flip(red_king1, False, True)
red_queen1 = pygame.image.load('resized//red_queen.png')
flipped_red_queen1 = pygame.transform.flip(red_queen1, False, True)
red_knight1 = pygame.image.load('resized//red_knight.png')
flipped_red_knight1 = pygame.transform.flip(red_knight1, False, True)
red_knight2 = pygame.image.load('resized//red_knight.png')
flipped_red_knight2 = pygame.transform.flip(red_knight2, False, True)
red_rook1 = pygame.image.load('resized//red_rook.png')
flipped_red_rook1 = pygame.transform.flip(red_rook1, False, True)
red_rook2 = pygame.image.load('resized//red_rook.png')
flipped_red_rook2 = pygame.transform.flip(red_rook2, False, True)
red_bishop1 = pygame.image.load('resized//red_bishop.png')
flipped_red_bishop1 = pygame.transform.flip(red_bishop1, False, True)
red_bishop2 = pygame.image.load('resized//red_bishop.png')
flipped_red_bishop2 = pygame.transform.flip(red_bishop2, False, True)
red_p1 = pygame.image.load('resized//red_pawn.png')
flipped_red_p1 = pygame.transform.flip(red_p1, False, True)
red_p2 = pygame.image.load('resized//red_pawn.png')
flipped_red_p2 = pygame.transform.flip(red_p2, False, True)
red_p3 = pygame.image.load('resized//red_pawn.png')
flipped_red_p3 = pygame.transform.flip(red_p3, False, True)
red_p4 = pygame.image.load('resized//red_pawn.png')
flipped_red_p4 = pygame.transform.flip(red_p4, False, True)
red_p5 = pygame.image.load('resized//red_pawn.png')
flipped_red_p5 = pygame.transform.flip(red_p5, False, True)
red_p6 = pygame.image.load('resized//red_pawn.png')
flipped_red_p6 = pygame.transform.flip(red_p6, False, True)
red_p7 = pygame.image.load('resized//red_pawn.png')
flipped_red_p7 = pygame.transform.flip(red_p7, False, True)
red_p8 = pygame.image.load('resized//red_pawn.png')
flipped_red_p8 = pygame.transform.flip(red_p8, False, True)
yc = pygame.image.load('yellowcheckmate.png')
yellowcheckmate = pygame.transform.rotate(yc, 90)
rc = pygame.image.load('redcheckmate.png')
redcheckmate = pygame.transform.rotate(rc, 90)
yellow_king1_coordinates = sq['e1']
yellow_knight1_coordinates = sq['b1']
yellow_knight2_coordinates = sq['g1']
yellow_rook1_coordinates = sq['a1']
yellow_rook2_coordinates = sq['h1']
yellow_bishop1_coordinates = sq['c1']
yellow_bishop2_coordinates = sq['f1']
yellow_queen1_coordinates = sq['d1']
yellow_p1_coordinates = sq['a2']
yellow_p2_coordinates = sq['b2']
yellow_p3_coordinates = sq['c2']
yellow_p4_coordinates = sq['d2']
yellow_p5_coordinates = sq['e2']
yellow_p6_coordinates = sq['f2']
yellow_p7_coordinates = sq['g2']
yellow_p8_coordinates = sq['h2']
red_king1_coordinates = sq['e8']
red_knight1_coordinates = sq['b8']
red_knight2_coordinates = sq['g8']
red_rook1_coordinates = sq['a8']
red_rook2_coordinates = sq['h8']
red_bishop1_coordinates = sq['c8']
red_bishop2_coordinates = sq['f8']
red_queen1_coordinates = sq['d8']
red_p1_coordinates = sq['a7']
red_p2_coordinates = sq['b7']
red_p3_coordinates = sq['c7']
red_p4_coordinates = sq['d7']
red_p5_coordinates = sq['e7']
red_p6_coordinates = sq['f7']
red_p7_coordinates = sq['g7']
red_p8_coordinates = sq['h7']

# Mouse clicks detection
def screen_input():
    global initialFile, initialBoardRow, finalFile, finalBoardRow, currentLocation, currentDestination, Move, entry, pawn_promotion
    for s in range(len(yellow_pieces)):
        try:
            exec(f"global {yellow_pieces[s]}")
        except:
            print("Absent Yellow Piece")
    for a in range(len(red_pieces)):
        try:
            exec(f"global {red_pieces[a]}")
        except:
            print("Absent Red Piece")
    finalFile = ""
    finalBoardRow = ""
    initialFile = ""
    initialBoardRow = ""
    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                pass
            if event1.type == pygame.MOUSEBUTTONDOWN:
                if event1.button == 1:
                    mouse_position = event1.pos
                    if mouse_position[0] <= 100:
                        initialFile = "a"
                    if 200 >= mouse_position[0] > 100:
                        initialFile = "b"
                    if 300 >= mouse_position[0] > 200:
                        initialFile = "c"
                    if 400 >= mouse_position[0] > 300:
                        initialFile = "d"
                    if 500 >= mouse_position[0] > 400:
                        initialFile = "e"
                    if 600 >= mouse_position[0] > 500:
                        initialFile = "f"
                    if 700 >= mouse_position[0] > 600:
                        initialFile = "g"
                    if 800 >= mouse_position[0] > 700:
                        initialFile = "h"
                    if mouse_position[1] <= 100:
                        initialBoardRow = "8"
                    if 200 >= mouse_position[1] > 100:
                        initialBoardRow = "7"
                    if 300 >= mouse_position[1] > 200:
                        initialBoardRow = "6"
                    if 400 >= mouse_position[1] > 300:
                        initialBoardRow = "5"
                    if 500 >= mouse_position[1] > 400:
                        initialBoardRow = "4"
                    if 600 >= mouse_position[1] > 500:
                        initialBoardRow = "3"
                    if 700 >= mouse_position[1] > 600:
                        initialBoardRow = "2"
                    if 800 >= mouse_position[1] > 700:
                        initialBoardRow = "1"
        if len(initialFile) != 0 and len(initialBoardRow) != 0:
            break
    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.MOUSEBUTTONDOWN:
                if event1.button == 1:
                    mouse_position = event1.pos
                    if mouse_position[0] <= 100:
                        finalFile = "a"
                    if 200 >= mouse_position[0] > 100:
                        finalFile = "b"
                    if 300 >= mouse_position[0] > 200:
                        finalFile = "c"
                    if 400 >= mouse_position[0] > 300:
                        finalFile = "d"
                    if 500 >= mouse_position[0] > 400:
                        finalFile = "e"
                    if 600 >= mouse_position[0] > 500:
                        finalFile = "f"
                    if 700 >= mouse_position[0] > 600:
                        finalFile = "g"
                    if 800 >= mouse_position[0] > 700:
                        finalFile = "h"
                    if mouse_position[1] <= 100:
                        finalBoardRow = "8"
                    if 200 >= mouse_position[1] > 100:
                        finalBoardRow = "7"
                    if 300 >= mouse_position[1] > 200:
                        finalBoardRow = "6"
                    if 400 >= mouse_position[1] > 300:
                        finalBoardRow = "5"
                    if 500 >= mouse_position[1] > 400:
                        finalBoardRow = "4"
                    if 600 >= mouse_position[1] > 500:
                        finalBoardRow = "3"
                    if 700 >= mouse_position[1] > 600:
                        finalBoardRow = "2"
                    if 800 >= mouse_position[1] > 700:
                        finalBoardRow = "1"
        if len(finalBoardRow) != 0 and len(finalFile) != 0:
            break
    currentLocation = str(initialFile + initialBoardRow)
    currentDestination = str(finalFile + finalBoardRow)
    entry = currentLocation + "-" + currentDestination
    for L in range(len(yellow_pieces)):
        temp_piece = str(yellow_pieces[L])
        try:
            exec(f"""
if {temp_piece}_coordinates == sq[currentLocation]:
    entry = yellow_pieces[L][7]+currentLocation+"-"+currentDestination
    if entry[0] == "p" or entry[0] == "P":
        entry = entry[1:]
    if yellow_pieces[L][8] == "n" or yellow_pieces[L][8] == "N":
        entry[0] = "n"
""")
        except:
            pass
    for o in range(len(red_pieces)):
        temp_piece = str(red_pieces[o])
        try:
            exec(f"""
if {temp_piece}_coordinates == sq[currentLocation]:
    entry = red_pieces[L][4]+currentLocation+"-"+currentDestination
    if entry[0] == "p" or entry[0] == "P":
        entry = entry[1:]
    if red_pieces[L][5] == "n" or red_pieces[L][5] == "N":
        entry[0] = "n"
        """)
        except:
            pass
    if len(entry) == 5:
        if currentLocation[1] == "7" and currentDestination[1] == "8":
            pawn_promotion = True
        elif currentLocation[1] == "2" and currentDestination[1] == "1":
            pawn_promotion = True
        else:
            pass
    print("Entry:"+entry)
    if entry[0] == "K" and entry[1] == "e":
        if currentDestination[0] == "c":
            entry = "O-O"
        elif currentDestination[0] == "g":
            entry = "O-O-O"
        else:
            pass
    elif pawn_promotion:
        if count % 2 == 0:
            rect = pygame.Rect(200, 300, 200, 200)
            color = (255, 255, 255)
            pygame.draw.rect(screen, color, rect)
            exec(f"""
screen.blit(pygame.image.load('resized//yellow_queen.png'), (200, 300))
screen.blit(pygame.image.load('resized//yellow_rook.png'), (300, 300))
screen.blit(pygame.image.load('resized//yellow_bishop.png'), (200, 400))
screen.blit(pygame.image.load('resized//yellow_knight.png'), (300, 400))
""")
            pygame.display.update()
            while True:
                for event1 in pygame.event.get():
                    if event1.type == pygame.QUIT:
                        pass
                    if event1.type == pygame.MOUSEBUTTONDOWN:
                        if event1.button == 1:
                            mouse_position = event1.pos
                            if mouse_position[0] >= 200 and mouse_position[0] < 300 and mouse_position[1] >= 300 and mouse_position < 400:
                                entry = entry + "q"
                                break
                            elif mouse_position[0] >= 200 and mouse_position[0] < 300 and mouse_position[1] >= 400 and mouse_position < 500:
                                entry = entry + "b"
                                break
                            elif mouse_position[0] >= 300 and mouse_position[0] < 400 and mouse_position[1] >= 300 and mouse_position < 400:
                                entry = entry + "r"
                                break
                            elif mouse_position[0] >= 300 and mouse_position[0] < 400 and mouse_position[1] >= 400 and mouse_position < 500:
                                entry = entry + "n"
                                break
        else:
            rect = pygame.Rect(200, 300, 200, 200)
            color = (255, 255, 255)
            pygame.draw.rect(screen, color, rect)
            exec(f"""
screen.blit(pygame.image.load('resized//red_queen.png'), (300, 400))
screen.blit(pygame.image.load('resized//red_rook.png'), (200, 400))
screen.blit(pygame.image.load('resized//red_bishop.png'), (200, 300))
screen.blit(pygame.image.load('resized//red_knight.png'), (300, 300))
""")
            pygame.display.update()
            while True:
                for event1 in pygame.event.get():
                    if event1.type == pygame.QUIT:
                        pass
                    if event1.type == pygame.MOUSEBUTTONDOWN:
                        if event1.button == 1:
                            mouse_position = event1.pos
                            if mouse_position[0] >= 200 and mouse_position[0] < 300 and mouse_position[1] >= 300 and mouse_position < 400:
                                entry = entry + "n"
                                break
                            elif mouse_position[0] >= 200 and mouse_position[0] < 300 and mouse_position[1] >= 400 and mouse_position < 500:
                                entry = entry + "q"
                                break
                            elif mouse_position[0] >= 300 and mouse_position[0] < 400 and mouse_position[1] >= 300 and mouse_position < 400:
                                entry = entry + "b"
                                break
                            elif mouse_position[0] >= 300 and mouse_position[0] < 400 and mouse_position[1] >= 400 and mouse_position < 500:
                                entry = entry + "r"
                                break
    try:
        board.push_san(entry)
        board.pop()
    except:
        print("illegal move")
        return screen_input()


# Move piece on screen
def move_piece():
    for q in range(len(yellow_pieces)):
        try:
            exec(f"global {yellow_pieces[q]}")
        except:
            print("Absent Yellow Piece")
    for e in range(len(red_pieces)):
        try:
            exec(f"global {red_pieces[e]}")
        except:
            print("Absent Red Piece")
    if count % 2 == 0:
        for f in range(len(yellow_pieces)):
            try:
                exec(f"""if {yellow_pieces[f]}_coordinates == sq[currentLocation]:
                    exec("{yellow_pieces[f]}_coordinates = sq[currentDestination]", globals())""")
            except:
                pass
    else:
        for m in range(len(red_pieces)):
            try:
                exec(f"""if {red_pieces[m]}_coordinates == sq[currentLocation]:
                    exec("{red_pieces[m]}_coordinates = sq[currentDestination]", globals())""")
            except:
                pass


# Behind the scenes logic
def terminal_move():
    global pawn_promotion, entry
    pawn_promotion = False
    if board.is_game_over():
        if count % 2 == 0:
            screen.blit(redcheckmate, (20, 250))
            pygame.display.flip()
            time.sleep(15)
            exit()
        else:
            screen.blit(yellowcheckmate, (20, 250))
            pygame.display.flip()
            time.sleep(15)
            exit()
    else:
        legal_moves = [board.san(move) for move in board.legal_moves]
        if len(legal_moves) == 0:
            if board.is_checkmate():
                if count % 2 == 0:
                    screen.blit(redcheckmate, (200, 400))
                    time.sleep(15)
                    exit()
                else:
                    screen.blit(yellowcheckmate, (200, 400))
                    time.sleep(15)
                    exit()
            elif board.is_stalemate():
                if board.has_insufficient_material(board.turn):
                    print('Draw: Insufficient material')
                else:
                    print('Stalemate!')
        else:
            legal_moves = [board.san(move) for move in board.legal_moves]
            if board.is_check():
                king_square = board.king(board.turn)
                legal_moves = [move for move in legal_moves if str(king_square) in move]
            if board.has_castling_rights(board.turn):
                if board.has_kingside_castling_rights(board.turn):
                    legal_moves.append('O-O')
                if board.has_queenside_castling_rights(board.turn):
                    legal_moves.append('O-O-O')
            print(board)
            screen_input()
            move_piece()
            try:
                move = chess.Move.from_uci(entry)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print('Illegal move')
                    return terminal_move()
            except ValueError:
                try:
                    board.push_san(entry)
                except ValueError:
                    print('Illegal move')
                    return terminal_move()
        if board.is_checkmate():
            print('Mate!')
        elif board.is_stalemate():
            print('Stalemate!')
        elif board.has_insufficient_material(board.turn):
            print('Draw: Insufficient material')


# Nullify Function
def nullify_piece():
    global yellow_king1
    global yellow_queen1
    global yellow_knight1
    global yellow_knight2
    global yellow_rook1
    global yellow_rook2
    global yellow_bishop1
    global yellow_bishop2
    global yellow_p1
    global yellow_p2
    global yellow_p3
    global yellow_p4
    global yellow_p5
    global yellow_p6
    global yellow_p7
    global yellow_p8
    global red_king1
    global red_queen1
    global red_knight1
    global red_knight2
    global red_rook1
    global red_rook2
    global red_bishop1
    global red_bishop2
    global red_p1
    global red_p2
    global red_p3
    global red_p4
    global red_p5
    global red_p6
    global red_p7
    global red_p8
    global red_king1_coordinates
    global red_queen1_coordinates
    global red_knight1_coordinates
    global red_knight2_coordinates
    global red_rook1_coordinates
    global red_rook2_coordinates
    global red_bishop1_coordinates
    global red_bishop2_coordinates
    global red_p1_coordinates
    global red_p2_coordinates
    global red_p3_coordinates
    global red_p4_coordinates
    global red_p5_coordinates
    global red_p6_coordinates
    global red_p7_coordinates
    global red_p8_coordinates
    global yellow_king1_coordinates
    global yellow_queen1_coordinates
    global yellow_knight1_coordinates
    global yellow_knight2_coordinates
    global yellow_rook1_coordinates
    global yellow_rook2_coordinates
    global yellow_bishop1_coordinates
    global yellow_bishop2_coordinates
    global yellow_p1_coordinates
    global yellow_p2_coordinates
    global yellow_p3_coordinates
    global yellow_p4_coordinates
    global yellow_p5_coordinates
    global yellow_p6_coordinates
    global yellow_p7_coordinates
    global yellow_p8_coordinates
    if count % 2 == 0:
        try:
            if yellow_king1_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_king1")

        try:
            if yellow_king1_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_queen1")

        try:
            if yellow_king1_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_knight1")

        try:
            if yellow_king1_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_knight2")

        try:
            if yellow_king1_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_rook1")

        try:
            if yellow_king1_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_rook2")

        try:
            if yellow_king1_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_bishop1")

        try:
            if yellow_king1_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_bishop2")

        try:
            if yellow_king1_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_p1")

        try:
            if yellow_king1_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_p2")

        try:
            if yellow_king1_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_p3")

        try:
            if yellow_king1_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_p4")

        try:
            if yellow_king1_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_p5")

        try:
            if yellow_king1_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_p6")

        try:
            if yellow_king1_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_p7")

        try:
            if yellow_king1_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_king1 capturing red_p8")

        try:
            if yellow_queen1_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_king1")

        try:
            if yellow_queen1_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_queen1")

        try:
            if yellow_queen1_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_knight1")

        try:
            if yellow_queen1_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_knight2")

        try:
            if yellow_queen1_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_rook1")

        try:
            if yellow_queen1_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_rook2")

        try:
            if yellow_queen1_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_bishop1")

        try:
            if yellow_queen1_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_bishop2")

        try:
            if yellow_queen1_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_p1")

        try:
            if yellow_queen1_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_p2")

        try:
            if yellow_queen1_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_p3")

        try:
            if yellow_queen1_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_p4")

        try:
            if yellow_queen1_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_p5")

        try:
            if yellow_queen1_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_p6")

        try:
            if yellow_queen1_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_p7")

        try:
            if yellow_queen1_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_queen1 capturing red_p8")

        try:
            if yellow_knight1_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_king1")

        try:
            if yellow_knight1_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_queen1")

        try:
            if yellow_knight1_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_knight1")

        try:
            if yellow_knight1_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_knight2")

        try:
            if yellow_knight1_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_rook1")

        try:
            if yellow_knight1_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_rook2")

        try:
            if yellow_knight1_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_bishop1")

        try:
            if yellow_knight1_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_bishop2")

        try:
            if yellow_knight1_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_p1")

        try:
            if yellow_knight1_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_p2")

        try:
            if yellow_knight1_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_p3")

        try:
            if yellow_knight1_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_p4")

        try:
            if yellow_knight1_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_p5")

        try:
            if yellow_knight1_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_p6")

        try:
            if yellow_knight1_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_p7")

        try:
            if yellow_knight1_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_knight1 capturing red_p8")

        try:
            if yellow_knight2_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_king1")

        try:
            if yellow_knight2_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_queen1")

        try:
            if yellow_knight2_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_knight1")

        try:
            if yellow_knight2_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_knight2")

        try:
            if yellow_knight2_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_rook1")

        try:
            if yellow_knight2_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_rook2")

        try:
            if yellow_knight2_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_bishop1")

        try:
            if yellow_knight2_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_bishop2")

        try:
            if yellow_knight2_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_p1")

        try:
            if yellow_knight2_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_p2")

        try:
            if yellow_knight2_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_p3")

        try:
            if yellow_knight2_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_p4")

        try:
            if yellow_knight2_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_p5")

        try:
            if yellow_knight2_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_p6")

        try:
            if yellow_knight2_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_p7")

        try:
            if yellow_knight2_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_knight2 capturing red_p8")

        try:
            if yellow_rook1_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_king1")

        try:
            if yellow_rook1_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_queen1")

        try:
            if yellow_rook1_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_knight1")

        try:
            if yellow_rook1_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_knight2")

        try:
            if yellow_rook1_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_rook1")

        try:
            if yellow_rook1_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_rook2")

        try:
            if yellow_rook1_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_bishop1")

        try:
            if yellow_rook1_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_bishop2")

        try:
            if yellow_rook1_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_p1")

        try:
            if yellow_rook1_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_p2")

        try:
            if yellow_rook1_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_p3")

        try:
            if yellow_rook1_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_p4")

        try:
            if yellow_rook1_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_p5")

        try:
            if yellow_rook1_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_p6")

        try:
            if yellow_rook1_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_p7")

        try:
            if yellow_rook1_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_rook1 capturing red_p8")

        try:
            if yellow_rook2_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_king1")

        try:
            if yellow_rook2_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_queen1")

        try:
            if yellow_rook2_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_knight1")

        try:
            if yellow_rook2_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_knight2")

        try:
            if yellow_rook2_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_rook1")

        try:
            if yellow_rook2_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_rook2")

        try:
            if yellow_rook2_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_bishop1")

        try:
            if yellow_rook2_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_bishop2")

        try:
            if yellow_rook2_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_p1")

        try:
            if yellow_rook2_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_p2")

        try:
            if yellow_rook2_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_p3")

        try:
            if yellow_rook2_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_p4")

        try:
            if yellow_rook2_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_p5")

        try:
            if yellow_rook2_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_p6")

        try:
            if yellow_rook2_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_p7")

        try:
            if yellow_rook2_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_rook2 capturing red_p8")

        try:
            if yellow_bishop1_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_king1")

        try:
            if yellow_bishop1_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_queen1")

        try:
            if yellow_bishop1_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_knight1")

        try:
            if yellow_bishop1_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_knight2")

        try:
            if yellow_bishop1_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_rook1")

        try:
            if yellow_bishop1_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_rook2")

        try:
            if yellow_bishop1_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_bishop1")

        try:
            if yellow_bishop1_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_bishop2")

        try:
            if yellow_bishop1_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_p1")

        try:
            if yellow_bishop1_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_p2")

        try:
            if yellow_bishop1_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_p3")

        try:
            if yellow_bishop1_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_p4")

        try:
            if yellow_bishop1_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_p5")

        try:
            if yellow_bishop1_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_p6")

        try:
            if yellow_bishop1_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_p7")

        try:
            if yellow_bishop1_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_bishop1 capturing red_p8")

        try:
            if yellow_bishop2_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_king1")

        try:
            if yellow_bishop2_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_queen1")

        try:
            if yellow_bishop2_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_knight1")

        try:
            if yellow_bishop2_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_knight2")

        try:
            if yellow_bishop2_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_rook1")

        try:
            if yellow_bishop2_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_rook2")

        try:
            if yellow_bishop2_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_bishop1")

        try:
            if yellow_bishop2_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_bishop2")

        try:
            if yellow_bishop2_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_p1")

        try:
            if yellow_bishop2_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_p2")

        try:
            if yellow_bishop2_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_p3")

        try:
            if yellow_bishop2_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_p4")

        try:
            if yellow_bishop2_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_p5")

        try:
            if yellow_bishop2_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_p6")

        try:
            if yellow_bishop2_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_p7")

        try:
            if yellow_bishop2_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_bishop2 capturing red_p8")

        try:
            if yellow_p1_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_king1")

        try:
            if yellow_p1_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_queen1")

        try:
            if yellow_p1_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_knight1")

        try:
            if yellow_p1_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_knight2")

        try:
            if yellow_p1_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_rook1")

        try:
            if yellow_p1_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_rook2")

        try:
            if yellow_p1_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_bishop1")

        try:
            if yellow_p1_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_bishop2")

        try:
            if yellow_p1_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_p1")

        try:
            if yellow_p1_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_p2")

        try:
            if yellow_p1_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_p3")

        try:
            if yellow_p1_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_p4")

        try:
            if yellow_p1_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_p5")

        try:
            if yellow_p1_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_p6")

        try:
            if yellow_p1_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_p7")

        try:
            if yellow_p1_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_p1 capturing red_p8")

        try:
            if yellow_p2_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_king1")

        try:
            if yellow_p2_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_queen1")

        try:
            if yellow_p2_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_knight1")

        try:
            if yellow_p2_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_knight2")

        try:
            if yellow_p2_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_rook1")

        try:
            if yellow_p2_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_rook2")

        try:
            if yellow_p2_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_bishop1")

        try:
            if yellow_p2_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_bishop2")

        try:
            if yellow_p2_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_p1")

        try:
            if yellow_p2_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_p2")

        try:
            if yellow_p2_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_p3")

        try:
            if yellow_p2_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_p4")

        try:
            if yellow_p2_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_p5")

        try:
            if yellow_p2_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_p6")

        try:
            if yellow_p2_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_p7")

        try:
            if yellow_p2_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_p2 capturing red_p8")

        try:
            if yellow_p3_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_king1")

        try:
            if yellow_p3_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_queen1")

        try:
            if yellow_p3_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_knight1")

        try:
            if yellow_p3_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_knight2")

        try:
            if yellow_p3_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_rook1")

        try:
            if yellow_p3_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_rook2")

        try:
            if yellow_p3_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_bishop1")

        try:
            if yellow_p3_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_bishop2")

        try:
            if yellow_p3_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_p1")

        try:
            if yellow_p3_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_p2")

        try:
            if yellow_p3_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_p3")

        try:
            if yellow_p3_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_p4")

        try:
            if yellow_p3_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_p5")

        try:
            if yellow_p3_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_p6")

        try:
            if yellow_p3_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_p7")

        try:
            if yellow_p3_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_p3 capturing red_p8")

        try:
            if yellow_p4_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_king1")

        try:
            if yellow_p4_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_queen1")

        try:
            if yellow_p4_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_knight1")

        try:
            if yellow_p4_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_knight2")

        try:
            if yellow_p4_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_rook1")

        try:
            if yellow_p4_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_rook2")

        try:
            if yellow_p4_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_bishop1")

        try:
            if yellow_p4_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_bishop2")

        try:
            if yellow_p4_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_p1")

        try:
            if yellow_p4_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_p2")

        try:
            if yellow_p4_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_p3")

        try:
            if yellow_p4_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_p4")

        try:
            if yellow_p4_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_p5")

        try:
            if yellow_p4_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_p6")

        try:
            if yellow_p4_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_p7")

        try:
            if yellow_p4_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_p4 capturing red_p8")

        try:
            if yellow_p5_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_king1")

        try:
            if yellow_p5_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_queen1")

        try:
            if yellow_p5_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_knight1")

        try:
            if yellow_p5_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_knight2")

        try:
            if yellow_p5_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_rook1")

        try:
            if yellow_p5_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_rook2")

        try:
            if yellow_p5_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_bishop1")

        try:
            if yellow_p5_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_bishop2")

        try:
            if yellow_p5_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_p1")

        try:
            if yellow_p5_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_p2")

        try:
            if yellow_p5_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_p3")

        try:
            if yellow_p5_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_p4")

        try:
            if yellow_p5_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_p5")

        try:
            if yellow_p5_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_p6")

        try:
            if yellow_p5_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_p7")

        try:
            if yellow_p5_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_p5 capturing red_p8")

        try:
            if yellow_p6_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_king1")

        try:
            if yellow_p6_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_queen1")

        try:
            if yellow_p6_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_knight1")

        try:
            if yellow_p6_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_knight2")

        try:
            if yellow_p6_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_rook1")

        try:
            if yellow_p6_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_rook2")

        try:
            if yellow_p6_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_bishop1")

        try:
            if yellow_p6_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_bishop2")

        try:
            if yellow_p6_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_p1")

        try:
            if yellow_p6_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_p2")

        try:
            if yellow_p6_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_p3")

        try:
            if yellow_p6_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_p4")

        try:
            if yellow_p6_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_p5")

        try:
            if yellow_p6_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_p6")

        try:
            if yellow_p6_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_p7")

        try:
            if yellow_p6_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_p6 capturing red_p8")

        try:
            if yellow_p7_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_king1")

        try:
            if yellow_p7_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_queen1")

        try:
            if yellow_p7_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_knight1")

        try:
            if yellow_p7_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_knight2")

        try:
            if yellow_p7_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_rook1")

        try:
            if yellow_p7_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_rook2")

        try:
            if yellow_p7_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_bishop1")

        try:
            if yellow_p7_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_bishop2")

        try:
            if yellow_p7_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_p1")

        try:
            if yellow_p7_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_p2")

        try:
            if yellow_p7_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_p3")

        try:
            if yellow_p7_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_p4")

        try:
            if yellow_p7_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_p5")

        try:
            if yellow_p7_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_p6")

        try:
            if yellow_p7_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_p7")

        try:
            if yellow_p7_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_p7 capturing red_p8")

        try:
            if yellow_p8_coordinates == red_king1_coordinates:
                del red_king1
                del red_king1_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_king1")

        try:
            if yellow_p8_coordinates == red_queen1_coordinates:
                del red_queen1
                del red_queen1_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_queen1")

        try:
            if yellow_p8_coordinates == red_knight1_coordinates:
                del red_knight1
                del red_knight1_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_knight1")

        try:
            if yellow_p8_coordinates == red_knight2_coordinates:
                del red_knight2
                del red_knight2_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_knight2")

        try:
            if yellow_p8_coordinates == red_rook1_coordinates:
                del red_rook1
                del red_rook1_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_rook1")

        try:
            if yellow_p8_coordinates == red_rook2_coordinates:
                del red_rook2
                del red_rook2_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_rook2")

        try:
            if yellow_p8_coordinates == red_bishop1_coordinates:
                del red_bishop1
                del red_bishop1_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_bishop1")

        try:
            if yellow_p8_coordinates == red_bishop2_coordinates:
                del red_bishop2
                del red_bishop2_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_bishop2")

        try:
            if yellow_p8_coordinates == red_p1_coordinates:
                del red_p1
                del red_p1_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_p1")

        try:
            if yellow_p8_coordinates == red_p2_coordinates:
                del red_p2
                del red_p2_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_p2")

        try:
            if yellow_p8_coordinates == red_p3_coordinates:
                del red_p3
                del red_p3_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_p3")

        try:
            if yellow_p8_coordinates == red_p4_coordinates:
                del red_p4
                del red_p4_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_p4")

        try:
            if yellow_p8_coordinates == red_p5_coordinates:
                del red_p5
                del red_p5_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_p5")

        try:
            if yellow_p8_coordinates == red_p6_coordinates:
                del red_p6
                del red_p6_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_p6")

        try:
            if yellow_p8_coordinates == red_p7_coordinates:
                del red_p7
                del red_p7_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_p7")

        try:
            if yellow_p8_coordinates == red_p8_coordinates:
                del red_p8
                del red_p8_coordinates
        except:
            print("Take failed for yellow_p8 capturing red_p8")
    else:
        try:
            if red_king1_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_king1")

        try:
            if red_king1_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_queen1")

        try:
            if red_king1_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_knight1")

        try:
            if red_king1_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_knight2")

        try:
            if red_king1_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_rook1")

        try:
            if red_king1_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_rook2")

        try:
            if red_king1_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_bishop1")

        try:
            if red_king1_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_bishop2")

        try:
            if red_king1_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_p1")

        try:
            if red_king1_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_p2")

        try:
            if red_king1_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_p3")

        try:
            if red_king1_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_p4")

        try:
            if red_king1_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_p5")

        try:
            if red_king1_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_p6")

        try:
            if red_king1_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_p7")

        try:
            if red_king1_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_king1 capturing yellow_p8")

        try:
            if red_queen1_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_king1")

        try:
            if red_queen1_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_queen1")

        try:
            if red_queen1_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_knight1")

        try:
            if red_queen1_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_knight2")

        try:
            if red_queen1_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_rook1")

        try:
            if red_queen1_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_rook2")

        try:
            if red_queen1_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_bishop1")

        try:
            if red_queen1_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_bishop2")

        try:
            if red_queen1_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_p1")

        try:
            if red_queen1_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_p2")

        try:
            if red_queen1_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_p3")

        try:
            if red_queen1_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_p4")

        try:
            if red_queen1_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_p5")

        try:
            if red_queen1_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_p6")

        try:
            if red_queen1_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_p7")

        try:
            if red_queen1_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_queen1 capturing yellow_p8")

        try:
            if red_knight1_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_king1")

        try:
            if red_knight1_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_queen1")

        try:
            if red_knight1_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_knight1")

        try:
            if red_knight1_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_knight2")

        try:
            if red_knight1_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_rook1")

        try:
            if red_knight1_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_rook2")

        try:
            if red_knight1_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_bishop1")

        try:
            if red_knight1_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_bishop2")

        try:
            if red_knight1_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_p1")

        try:
            if red_knight1_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_p2")

        try:
            if red_knight1_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_p3")

        try:
            if red_knight1_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_p4")

        try:
            if red_knight1_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_p5")

        try:
            if red_knight1_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_p6")

        try:
            if red_knight1_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_p7")

        try:
            if red_knight1_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_knight1 capturing yellow_p8")

        try:
            if red_knight2_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_king1")

        try:
            if red_knight2_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_queen1")

        try:
            if red_knight2_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_knight1")

        try:
            if red_knight2_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_knight2")

        try:
            if red_knight2_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_rook1")

        try:
            if red_knight2_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_rook2")

        try:
            if red_knight2_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_bishop1")

        try:
            if red_knight2_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_bishop2")

        try:
            if red_knight2_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_p1")

        try:
            if red_knight2_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_p2")

        try:
            if red_knight2_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_p3")

        try:
            if red_knight2_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_p4")

        try:
            if red_knight2_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_p5")

        try:
            if red_knight2_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_p6")

        try:
            if red_knight2_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_p7")

        try:
            if red_knight2_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_knight2 capturing yellow_p8")

        try:
            if red_rook1_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_king1")

        try:
            if red_rook1_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_queen1")

        try:
            if red_rook1_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_knight1")

        try:
            if red_rook1_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_knight2")

        try:
            if red_rook1_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_rook1")

        try:
            if red_rook1_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_rook2")

        try:
            if red_rook1_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_bishop1")

        try:
            if red_rook1_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_bishop2")

        try:
            if red_rook1_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_p1")

        try:
            if red_rook1_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_p2")

        try:
            if red_rook1_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_p3")

        try:
            if red_rook1_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_p4")

        try:
            if red_rook1_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_p5")

        try:
            if red_rook1_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_p6")

        try:
            if red_rook1_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_p7")

        try:
            if red_rook1_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_rook1 capturing yellow_p8")

        try:
            if red_rook2_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_king1")

        try:
            if red_rook2_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_queen1")

        try:
            if red_rook2_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_knight1")

        try:
            if red_rook2_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_knight2")

        try:
            if red_rook2_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_rook1")

        try:
            if red_rook2_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_rook2")

        try:
            if red_rook2_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_bishop1")

        try:
            if red_rook2_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_bishop2")

        try:
            if red_rook2_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_p1")

        try:
            if red_rook2_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_p2")

        try:
            if red_rook2_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_p3")

        try:
            if red_rook2_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_p4")

        try:
            if red_rook2_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_p5")

        try:
            if red_rook2_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_p6")

        try:
            if red_rook2_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_p7")

        try:
            if red_rook2_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_rook2 capturing yellow_p8")

        try:
            if red_bishop1_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_king1")

        try:
            if red_bishop1_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_queen1")

        try:
            if red_bishop1_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_knight1")

        try:
            if red_bishop1_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_knight2")

        try:
            if red_bishop1_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_rook1")

        try:
            if red_bishop1_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_rook2")

        try:
            if red_bishop1_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_bishop1")

        try:
            if red_bishop1_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_bishop2")

        try:
            if red_bishop1_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_p1")

        try:
            if red_bishop1_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_p2")

        try:
            if red_bishop1_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_p3")

        try:
            if red_bishop1_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_p4")

        try:
            if red_bishop1_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_p5")

        try:
            if red_bishop1_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_p6")

        try:
            if red_bishop1_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_p7")

        try:
            if red_bishop1_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_bishop1 capturing yellow_p8")

        try:
            if red_bishop2_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_king1")

        try:
            if red_bishop2_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_queen1")

        try:
            if red_bishop2_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_knight1")

        try:
            if red_bishop2_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_knight2")

        try:
            if red_bishop2_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_rook1")

        try:
            if red_bishop2_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_rook2")

        try:
            if red_bishop2_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_bishop1")

        try:
            if red_bishop2_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_bishop2")

        try:
            if red_bishop2_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_p1")

        try:
            if red_bishop2_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_p2")

        try:
            if red_bishop2_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_p3")

        try:
            if red_bishop2_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_p4")

        try:
            if red_bishop2_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_p5")

        try:
            if red_bishop2_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_p6")

        try:
            if red_bishop2_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_p7")

        try:
            if red_bishop2_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_bishop2 capturing yellow_p8")

        try:
            if red_p1_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_king1")

        try:
            if red_p1_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_queen1")

        try:
            if red_p1_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_knight1")

        try:
            if red_p1_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_knight2")

        try:
            if red_p1_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_rook1")

        try:
            if red_p1_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_rook2")

        try:
            if red_p1_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_bishop1")

        try:
            if red_p1_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_bishop2")

        try:
            if red_p1_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_p1")

        try:
            if red_p1_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_p2")

        try:
            if red_p1_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_p3")

        try:
            if red_p1_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_p4")

        try:
            if red_p1_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_p5")

        try:
            if red_p1_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_p6")

        try:
            if red_p1_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_p7")

        try:
            if red_p1_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_p1 capturing yellow_p8")

        try:
            if red_p2_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_king1")

        try:
            if red_p2_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_queen1")

        try:
            if red_p2_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_knight1")

        try:
            if red_p2_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_knight2")

        try:
            if red_p2_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_rook1")

        try:
            if red_p2_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_rook2")

        try:
            if red_p2_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_bishop1")

        try:
            if red_p2_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_bishop2")

        try:
            if red_p2_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_p1")

        try:
            if red_p2_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_p2")

        try:
            if red_p2_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_p3")

        try:
            if red_p2_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_p4")

        try:
            if red_p2_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_p5")

        try:
            if red_p2_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_p6")

        try:
            if red_p2_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_p7")

        try:
            if red_p2_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_p2 capturing yellow_p8")

        try:
            if red_p3_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_king1")

        try:
            if red_p3_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_queen1")

        try:
            if red_p3_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_knight1")

        try:
            if red_p3_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_knight2")

        try:
            if red_p3_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_rook1")

        try:
            if red_p3_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_rook2")

        try:
            if red_p3_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_bishop1")

        try:
            if red_p3_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_bishop2")

        try:
            if red_p3_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_p1")

        try:
            if red_p3_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_p2")

        try:
            if red_p3_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_p3")

        try:
            if red_p3_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_p4")

        try:
            if red_p3_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_p5")

        try:
            if red_p3_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_p6")

        try:
            if red_p3_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_p7")

        try:
            if red_p3_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_p3 capturing yellow_p8")

        try:
            if red_p4_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_king1")

        try:
            if red_p4_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_queen1")

        try:
            if red_p4_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_knight1")

        try:
            if red_p4_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_knight2")

        try:
            if red_p4_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_rook1")

        try:
            if red_p4_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_rook2")

        try:
            if red_p4_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_bishop1")

        try:
            if red_p4_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_bishop2")

        try:
            if red_p4_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_p1")

        try:
            if red_p4_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_p2")

        try:
            if red_p4_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_p3")

        try:
            if red_p4_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_p4")

        try:
            if red_p4_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_p5")

        try:
            if red_p4_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_p6")

        try:
            if red_p4_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_p7")

        try:
            if red_p4_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_p4 capturing yellow_p8")

        try:
            if red_p5_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_king1")

        try:
            if red_p5_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_queen1")

        try:
            if red_p5_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_knight1")

        try:
            if red_p5_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_knight2")

        try:
            if red_p5_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_rook1")

        try:
            if red_p5_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_rook2")

        try:
            if red_p5_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_bishop1")

        try:
            if red_p5_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_bishop2")

        try:
            if red_p5_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_p1")

        try:
            if red_p5_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_p2")

        try:
            if red_p5_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_p3")

        try:
            if red_p5_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_p4")

        try:
            if red_p5_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_p5")

        try:
            if red_p5_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_p6")

        try:
            if red_p5_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_p7")

        try:
            if red_p5_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_p5 capturing yellow_p8")

        try:
            if red_p6_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_king1")

        try:
            if red_p6_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_queen1")

        try:
            if red_p6_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_knight1")

        try:
            if red_p6_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_knight2")

        try:
            if red_p6_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_rook1")

        try:
            if red_p6_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_rook2")

        try:
            if red_p6_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_bishop1")

        try:
            if red_p6_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_bishop2")

        try:
            if red_p6_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_p1")

        try:
            if red_p6_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_p2")

        try:
            if red_p6_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_p3")

        try:
            if red_p6_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_p4")

        try:
            if red_p6_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_p5")

        try:
            if red_p6_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_p6")

        try:
            if red_p6_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_p7")

        try:
            if red_p6_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_p6 capturing yellow_p8")

        try:
            if red_p7_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_king1")

        try:
            if red_p7_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_queen1")

        try:
            if red_p7_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_knight1")

        try:
            if red_p7_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_knight2")

        try:
            if red_p7_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_rook1")

        try:
            if red_p7_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_rook2")

        try:
            if red_p7_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_bishop1")

        try:
            if red_p7_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_bishop2")

        try:
            if red_p7_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_p1")

        try:
            if red_p7_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_p2")

        try:
            if red_p7_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_p3")

        try:
            if red_p7_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_p4")

        try:
            if red_p7_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_p5")

        try:
            if red_p7_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_p6")

        try:
            if red_p7_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_p7")

        try:
            if red_p7_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_p7 capturing yellow_p8")

        try:
            if red_p8_coordinates == yellow_king1_coordinates:
                del yellow_king1
                del yellow_king1_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_king1")

        try:
            if red_p8_coordinates == yellow_queen1_coordinates:
                del yellow_queen1
                del yellow_queen1_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_queen1")

        try:
            if red_p8_coordinates == yellow_knight1_coordinates:
                del yellow_knight1
                del yellow_knight1_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_knight1")

        try:
            if red_p8_coordinates == yellow_knight2_coordinates:
                del yellow_knight2
                del yellow_knight2_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_knight2")

        try:
            if red_p8_coordinates == yellow_rook1_coordinates:
                del yellow_rook1
                del yellow_rook1_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_rook1")

        try:
            if red_p8_coordinates == yellow_rook2_coordinates:
                del yellow_rook2
                del yellow_rook2_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_rook2")

        try:
            if red_p8_coordinates == yellow_bishop1_coordinates:
                del yellow_bishop1
                del yellow_bishop1_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_bishop1")

        try:
            if red_p8_coordinates == yellow_bishop2_coordinates:
                del yellow_bishop2
                del yellow_bishop2_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_bishop2")

        try:
            if red_p8_coordinates == yellow_p1_coordinates:
                del yellow_p1
                del yellow_p1_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_p1")

        try:
            if red_p8_coordinates == yellow_p2_coordinates:
                del yellow_p2
                del yellow_p2_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_p2")

        try:
            if red_p8_coordinates == yellow_p3_coordinates:
                del yellow_p3
                del yellow_p3_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_p3")

        try:
            if red_p8_coordinates == yellow_p4_coordinates:
                del yellow_p4
                del yellow_p4_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_p4")

        try:
            if red_p8_coordinates == yellow_p5_coordinates:
                del yellow_p5
                del yellow_p5_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_p5")

        try:
            if red_p8_coordinates == yellow_p6_coordinates:
                del yellow_p6
                del yellow_p6_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_p6")

        try:
            if red_p8_coordinates == yellow_p7_coordinates:
                del yellow_p7
                del yellow_p7_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_p7")

        try:
            if red_p8_coordinates == yellow_p8_coordinates:
                del yellow_p8
                del yellow_p8_coordinates
        except:
            print("Take failed for red_p8 capturing yellow_p8")


# Main Pygame Loop
def main_loop():
    global rectangle_count, count, pawn_promotion
    clock = pygame.time.Clock()
    pygame.display.update()
    for y in range(8):
        for x in range(8):
            rect = pygame.Rect(x * 100, y * 100, 100, 100)
            rectangles.append(rect)
    while True:
        count += 1
        pawn_promotion = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        for x in range(8):
            line = ''
            for y in range(8):
                if (x + y % 2) % 2 == 0:
                    line += 'X'
                else:
                    line += 'O'
                rect_count = x * 8 + y
                if line[-1] == "X":
                    exec(f"pygame.draw.rect(screen, light_brown, rectangles[{rect_count}])")
                if line[-1] == "O":
                    exec(f"pygame.draw.rect(screen, brown, rectangles[{rect_count}])")
        if board.is_game_over():
            pass
        elif count % 2 == 0:
            for g in range(len(yellow_pieces)):
                try:
                    exec(f"screen.blit({yellow_pieces[g]}, {yellow_pieces[g]}_coordinates)")
                except:
                    pass
            for h in range(len(yellow_pieces)):
                try:
                    exec(f"screen.blit({red_pieces[h]}, {red_pieces[h]}_coordinates)")
                except:
                    pass
        else:
            for g in range(len(yellow_pieces)):
                try:
                    exec(f"screen.blit(flipped_{yellow_pieces[g]}, {yellow_pieces[g]}_coordinates)")
                except:
                    pass
            for h in range(len(yellow_pieces)):
                try:
                    exec(f"screen.blit(flipped_{red_pieces[h]}, {red_pieces[h]}_coordinates)")
                except:
                    pass

        pygame.display.update()
        terminal_move()
        nullify_piece()
        pygame.display.flip()
        clock.tick(60)


main_loop()
