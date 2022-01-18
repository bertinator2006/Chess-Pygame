import pygame

TILESIZE = 75
WIN = pygame.display.set_mode((8*TILESIZE,8*TILESIZE))
pygame.display.set_caption("Chess")
black_square = (88, 44, 44)
white_square = (128, 76, 60)
board_rect = pygame.Rect(0,0,8*TILESIZE,8*TILESIZE)

piece_file = {
	'-': "empty",
	'P': pygame.image.load(r'assets/w/p.png'),
	'B': pygame.transform.smoothscale(pygame.image.load(r'assets/w/b.png'),(50, 50)),
	'N': pygame.transform.smoothscale(pygame.image.load(r'assets/w/n.png'),(50, 50)),
	'R': pygame.transform.smoothscale(pygame.image.load(r'assets/w/r.png'),(45, 50)),
	'Q': pygame.transform.smoothscale(pygame.image.load(r'assets/w/q.png'),(50, 50)),
	'K': pygame.transform.smoothscale(pygame.image.load(r'assets/w/k.png'),(50, 50)),
	'p': pygame.image.load(r'assets/b/p.png'),
	'b': pygame.transform.smoothscale(pygame.image.load(r'assets/b/b.png'),(50, 50)),
	'n': pygame.transform.smoothscale(pygame.image.load(r'assets/b/n.png'),(50, 50)),
	'r': pygame.transform.smoothscale(pygame.image.load(r'assets/b/r.png'),(45, 50)),
	'q': pygame.transform.smoothscale(pygame.image.load(r'assets/b/q.png'),(50, 50)),
	'k': pygame.transform.smoothscale(pygame.image.load(r'assets/b/k.png'),(50, 50))
}

board_state =  "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"



def fen_to_board(fen):
    board = []
    for row in fen.split('/'):
        brow = []
        for c in row:
            if c == ' ':
                break
            elif c in '12345678':
                brow.extend( ['-'] * int(c) )
            elif c == 'p':
                brow.append( 'p' )
            elif c == 'P':
                brow.append( 'P' )
            elif c > 'Z':
                brow.append( c )
            else:
                brow.append( c )

        board.append( brow )
    return board

#displays board from board_state
def draw_board():
	global board_state
	pygame.draw.rect(WIN, white_square, board_rect)
	act_board = fen_to_board(board_state)
	for y in range(8):
		for x in range(8):
			if (y+x)%2 == 1:
				pygame.draw.rect(WIN, black_square,pygame.Rect(y*TILESIZE,x*TILESIZE,TILESIZE,TILESIZE))
	
	for y in range(len(act_board)):
		for x in range(len(act_board[y])):
			if not act_board[y][x] == "-":
				if act_board[y][x] == 'p' or act_board[y][x] == 'P':
					WIN.blit(piece_file[act_board[y][x]],(x*TILESIZE+20,y*TILESIZE+20))
				else:
					WIN.blit(piece_file[act_board[y][x]],(x*TILESIZE+12.5,y*TILESIZE+12.5))
	pygame.display.update()


run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	draw_board()
	pygame.time.delay(100)

pygame.quit()
