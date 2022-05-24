import pygame as p

WIDTH = HEIGHT = 600
DIMENSION = 20
MAX_FPS = 20
SQUARE_SIZE = HEIGHT // DIMENSION


'''
Main function. Handles initializing application and updating graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameSate(screen)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsible for drawing the board and pieces (to implement)
'''
def drawGameSate(screen):

    drawBoard(screen)  # draw squares of chess board

    # drawPieces(screen, pieces)


'''
Draw de squares on the board (top left is always white)
'''
def drawBoard(screen):

    square_color = p.Color("white")
    lines_color = p.Color("black")
    for c in range(DIMENSION):
        for r in range(DIMENSION):
            p.draw.rect(screen, square_color, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)

    for l in range(DIMENSION):
        p.draw.lines(screen, lines_color, True, [(0, l*SQUARE_SIZE), (DIMENSION*SQUARE_SIZE, l*SQUARE_SIZE)])
        p.draw.lines(screen, lines_color, True, [(l*SQUARE_SIZE, 0), (l*SQUARE_SIZE, DIMENSION*SQUARE_SIZE)])


'''
Draw de pieces on the board
'''
def drawPieces(screen, pieces):
    pass


if __name__ == "__main__":
    main()
