import pygame as p

WIDTH = HEIGHT = 512
DIMENSION = 8
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

    colors = [p.Color("white"), p.Color("black")]
    for c in range(DIMENSION):
        for r in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


'''
Draw de pieces on the board
'''
def drawPieces(screen, pieces):
    pass


if __name__ == "__main__":
    main()
