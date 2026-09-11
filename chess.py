import pygame,bot_chess
from sys import exit
import threading,chess_client
import time,ast
pygame.init()
WINDOW_HEIGHT=650
WINDOW_WIDTH=850
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("CHESSSSSSSSSSSSSSSSSS!!!!!!!!!!!!!!!!!")


italic_path="Bodoni_Moda\\italic.ttf"
normal_path="Bodoni_Moda\\normal.ttf"
half_italic_path="Bodoni_Moda\\half.ttf"
medium_italic_path="Bodoni_Moda\\medium_italic.ttf"
board_origin=[85,20]
square_size=75
stalemate=False
LIGHT_SQUARE = (237, 240, 209)
HIGHLIGHT_COLOR_BLACK=(185, 212, 73)
HIGHLIGHT_COLOR_WHITE=(244, 253, 134)
DARK_SQUARE = (120, 156, 87)
BOARD_BG = (60, 60, 60)
row=0
col=0



PAWN_TABLE = [
    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],  
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],  
    [0.10, 0.10, 0.15, 0.20, 0.20, 0.15, 0.10, 0.10],  
    [0.10, 0.10, 0.20, 0.30, 0.30, 0.20, 0.10, 0.10],  
    [0.00, 0.05, 0.20, 0.35, 0.35, 0.20, 0.05, 0.00],  
    [0.00, 0.00, 0.10, 0.25, 0.25, 0.10, 0.00, 0.00],  
    [0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50],  
    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],  
]


KNIGHT_TABLE = [
    [-0.50, -0.40, -0.30, -0.30, -0.30, -0.30, -0.40, -0.50],
    [-0.40, -0.20,  0.00,  0.00,  0.00,  0.00, -0.20, -0.40],
    [-0.30,  0.00,  0.10,  0.15,  0.15,  0.10,  0.00, -0.30],
    [-0.30,  0.05,  0.15,  0.20,  0.20,  0.15,  0.05, -0.30],
    [-0.30,  0.00,  0.15,  0.20,  0.20,  0.15,  0.00, -0.30],
    [-0.30,  0.05,  0.10,  0.15,  0.15,  0.10,  0.05, -0.30],
    [-0.40, -0.20,  0.00,  0.05,  0.05,  0.00, -0.20, -0.40],
    [-0.50, -0.40, -0.30, -0.30, -0.30, -0.30, -0.40, -0.50],
]


BISHOP_TABLE = [
    [-0.20, -0.10, -0.10, -0.10, -0.10, -0.10, -0.10, -0.20],
    [-0.10,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00, -0.10],
    [-0.10,  0.00,  0.05,  0.10,  0.10,  0.05,  0.00, -0.10],
    [-0.10,  0.05,  0.10,  0.15,  0.15,  0.10,  0.05, -0.10],
    [-0.10,  0.00,  0.10,  0.15,  0.15,  0.10,  0.00, -0.10],
    [-0.10,  0.00,  0.05,  0.10,  0.10,  0.05,  0.00, -0.10],
    [-0.10,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00, -0.10],
    [-0.20, -0.10, -0.10, -0.10, -0.10, -0.10, -0.10, -0.20],
]


ROOK_TABLE = [
    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],  # Rank 1
    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],  # Rank 2
    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],  # Rank 3
    [0.00, 0.00, 0.00, 0.05, 0.05, 0.00, 0.00, 0.00],  # Rank 4
    [0.00, 0.00, 0.00, 0.05, 0.05, 0.00, 0.00, 0.00],  # Rank 5
    [0.00, 0.00, 0.00, 0.05, 0.05, 0.00, 0.00, 0.00],  # Rank 6
    [0.10, 0.10, 0.10, 0.15, 0.15, 0.10, 0.10, 0.10],  # Rank 7
    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],  # Rank 8
]


QUEEN_TABLE = [
    [-0.10, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, -0.10],
    [-0.05,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00, -0.05],
    [-0.05,  0.00,  0.05,  0.05,  0.05,  0.05,  0.00, -0.05],
    [-0.05,  0.00,  0.05,  0.10,  0.10,  0.05,  0.00, -0.05],
    [-0.05,  0.00,  0.05,  0.10,  0.10,  0.05,  0.00, -0.05],
    [-0.05,  0.00,  0.05,  0.05,  0.05,  0.05,  0.00, -0.05],
    [-0.05,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00, -0.05],
    [-0.10, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, -0.10],
]


KING_TABLE = [
    [-0.20, -0.10,  0.00,  0.10,  0.10,  0.20,  0.30,  0.20],  
    [-0.10,  0.00,  0.05,  0.10,  0.10,  0.15,  0.20,  0.15],  
    [ 0.00,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00],  
    [-0.10, -0.05,  0.00,  0.00,  0.00,  0.00, -0.05, -0.10],  
    [-0.20, -0.10,  0.00,  0.00,  0.00,  0.00, -0.10, -0.20],  
    [-0.30, -0.20, -0.10, -0.10, -0.10, -0.10, -0.20, -0.30],  
    [-0.40, -0.30, -0.20, -0.20, -0.20, -0.20, -0.30, -0.40],  
    [-0.50, -0.40, -0.30, -0.30, -0.30, -0.30, -0.40, -0.50],  
]
pawn_white=pygame.image.load("pieces\\wP.png").convert_alpha()
pawn_white = pygame.transform.smoothscale(pawn_white, (square_size , square_size ))
pawn_black=pygame.image.load("pieces\\bP.png").convert_alpha()
pawn_black = pygame.transform.smoothscale(pawn_black, (square_size , square_size ))
pygame.display.set_icon(pawn_black)
knight_white=pygame.image.load("pieces\\wN.png").convert_alpha()
knight_white = pygame.transform.smoothscale(knight_white, (square_size , square_size ))
knight_black=pygame.image.load("pieces\\bN.png").convert_alpha()
knight_black = pygame.transform.smoothscale(knight_black, (square_size , square_size ))

bishop_white=pygame.image.load("pieces\\wB.png").convert_alpha()
bishop_white = pygame.transform.smoothscale(bishop_white, (square_size , square_size ))
bishop_black=pygame.image.load("pieces\\bB.png").convert_alpha()
bishop_black = pygame.transform.smoothscale(bishop_black, (square_size , square_size ))

rook_white=pygame.image.load("pieces\\wR.png").convert_alpha()
rook_white = pygame.transform.smoothscale(rook_white, (square_size , square_size ))
rook_black=pygame.image.load("pieces\\bR.png").convert_alpha()
rook_black = pygame.transform.smoothscale(rook_black, (square_size , square_size ))

king_white=pygame.image.load("pieces\\wK.png").convert_alpha()
king_white = pygame.transform.smoothscale(king_white, (square_size , square_size ))
king_black=pygame.image.load("pieces\\bK.png").convert_alpha()
king_black = pygame.transform.smoothscale(king_black, (square_size , square_size ))

queen_white=pygame.image.load("pieces\\wQ.png").convert_alpha()
queen_white = pygame.transform.smoothscale(queen_white, (square_size , square_size ))
queen_black=pygame.image.load("pieces\\bQ.png").convert_alpha()
queen_black = pygame.transform.smoothscale(queen_black, (square_size , square_size ))

availble_mouves_rects=[]
background=pygame.surface.Surface((800,600))
background.fill("black")
squares = [[None]*8 for _ in range(8)]
rects=[[None]*8 for _ in range(8)]
white_pawn_board=0
black_pawn_board=0
font=pygame.font.Font(italic_path,30)
small_font=pygame.font.Font(None,24)
half_italic_font_big=pygame.font.Font(half_italic_path,90)
half_italic_font_medium=pygame.font.Font(half_italic_path,40)
half_italic_font_small=pygame.font.Font(half_italic_path,30)
black_bar_color=(64, 61, 57)
white_bar_color=(255, 255, 255)
medium_italic_font_big=pygame.font.Font(medium_italic_path,90)
medium_italic_font_medium=pygame.font.Font(medium_italic_path,40)
medium_italic_font_small=pygame.font.Font(medium_italic_path,30)
text="White turn"
render_text=font.render(text,False,"white")
letters=["a","b","c","d","e","f","g","h"]
en_passent_mouves_for_white=[]
en_passent_mouves_for_black=[]
white_bishop_board=0
black_bishop_board=0

for_white_passent_board=0
for_black_passent_board=0

white_rook_board=0
black_rook_board=0

white_knight_board=0
black_knight_board=0

white_king_board=0
black_king_board=0

white_queen_board=0
black_queen_board=0

white_peaces_board=0
black_peaces_board=0
starting=True
waiting_for_pos=False
start_row=0
start_col=0
ready=True
game_mouves=[]
white_turn=True
pieces=0
white_castled=False
black_castled=False
white_king_mouved=False
black_king_mouved=False
white_rook_right=False
white_rook_left=False
black_rook_right=False
took=False
gave_passent_white=False
gave_passent_black=False
promoting=False
idd=None
start_square=[]
end_square=[]
current_position_index=-1
shadow=False
black_rook_left=False
assinged_turn=None
promote_rects=[]
promote_position=[]
game_state="main_menue"
checkmate=False
availble_taking_rects=[]
text_width,tex_height=medium_italic_font_small.size("Play Online")
online_rect=pygame.Rect(0,0,text_width+15,tex_height+8)
text_width,tex_height=medium_italic_font_small.size("Play Offline")
offline_rect=pygame.Rect(0,0,text_width+15,tex_height+8)

boards=[white_pawn_board, white_knight_board, white_bishop_board, white_rook_board, white_queen_board, white_king_board,
        black_pawn_board, black_knight_board, black_bishop_board, black_rook_board, black_queen_board, black_king_board]


advantage=0
# now this is a hard one and i want to make it in a smart way let's say that the evaluation bar's of white and black should be equal to square_size*8
# and we just draw the white bar from a know position wish is board origin[0] and we draw it based on advantage if it is positive it is in the favor of white else in black
# but the way how we get the value of advantage is hard because i don't know how
#ok let me lock in if we know that advantage has an enterval
# nvm mind i'll just ask deepseek for the best idea
#ok so the maximum value of advantage is 10 and the min is -10 
max_val=20
buffer_val=(square_size*4)/max_val

white_bar=pygame.surface.Surface((45,(square_size*4)+advantage*buffer_val))
white_bar_rect=white_bar.get_rect(topleft=(20,board_origin[1]))
white_bar.fill(white_bar_color)
black_bar=pygame.surface.Surface((45,board_origin[1]+(square_size*8)-white_bar_rect.bottom))
black_bar_rect=black_bar.get_rect(topleft=(20,white_bar_rect.bottom))
black_bar.fill(black_bar_color)
def get_piece_index(square_index):
    bit = 1 << square_index
    
    
    if boards[0] & bit:   return 0
    elif boards[6]& bit:   return 6
   
    elif boards[1] & bit: return 1
    elif boards[2] & bit: return 2
    elif boards[3] & bit:   return 3
    elif boards[4] & bit:  return 4
    elif boards[5] & bit:   return 5
    
    
    
    elif boards[7] & bit: return 7
    elif boards[8] & bit: return 8
    elif boards[9] & bit:   return 9
    elif boards[10] & bit:  return 10
    elif boards[11] & bit:   return 11
    else: return None
def get_piece_at(square_index):
    try:
        bit = 1 << square_index
    except:return(None,None)
    
    if boards[0] & bit:   return ["p",0]
    elif boards[6]& bit:   return ["p",1]
   
    elif boards[1] & bit: return ["kn",0]
    elif boards[2] & bit: return ["b",0]
    elif boards[3] & bit:   return ["r",0]
    elif boards[4] & bit:  return ["q",0]
    elif boards[5] & bit:   return "k",0
    
    
    
    elif boards[7] & bit: return ["kn",1]
    elif boards[8] & bit: return ["b",1]
    elif boards[9] & bit:   return ["r",1]
    elif boards[10] & bit:  return ["q",1]
    elif boards[11] & bit:   return ["k",1]
    
    return None,None  # Empty square

def simulate(index,start_col,start_row,end_col,end_row,put,turn):
    global boards,white_peaces_board
    global black_peaces_board,took
    global idd,white_king_board
    global black_king_board
    start_pos=start_row*8+start_col
    end_pos=end_row*8+end_col
    if put:
        
        if turn:
            if index==5:
                white_king_board&=~(1<<start_pos)
                white_king_board|=(1<<end_pos)
            if black_peaces_board&(1<<end_pos):
                black_peaces_board&=~(1<<end_pos)
                for indexx,board in enumerate(boards):
                    if board&(1<<end_pos) and indexx>5:
                        boards[indexx]&=~(1<<end_pos)
                        idd=indexx
                        break
                took=True
            white_peaces_board&=~(1<<start_pos)
            white_peaces_board|=(1<<end_pos)
        else:
            if index==11:
                black_king_board&=~(1<<start_pos)
                black_king_board|=(1<<end_pos)
            if white_peaces_board&(1<<end_pos):
                for indexx,board in enumerate(boards):
                    if board&(1<<end_pos) and indexx<6:
                        boards[indexx]&=~(1<<end_pos)
                        idd=indexx
                        break
                white_peaces_board&=~(1<<end_pos)
                took=True
            black_peaces_board&=~(1<<start_pos)
            black_peaces_board|=(1<<end_pos)
        boards[index]&=~(1<<start_pos)
        boards[index]|=(1<<end_pos)
        
    else:
        if turn:
            if index==5:
                white_king_board&=~(1<<end_pos)
                white_king_board|=(1<<start_pos)
            if took:
                took=False
                boards[idd]|=(1<<end_pos)
                black_peaces_board|=(1<<end_pos)
            white_peaces_board&=~(1<<end_pos)
            white_peaces_board|=(1<<start_pos)
        else:
            if index==11:
                black_king_board&=~(1<<end_pos)
                black_king_board|=(1<<start_pos)
            if took:
                boards[idd]|=(1<<end_pos)
                took=False
                white_peaces_board|=(1<<end_pos)
            black_peaces_board&=~(1<<end_pos)
            black_peaces_board|=(1<<start_pos)
        boards[index]&=~(1<<end_pos)
        boards[index]|=(1<<start_pos)
    
def is_square_attacked(start_row,start_col,turn,):
    global boards,black_peaces_board
    global white_peaces_board
    
    
    
    
    col_row=[start_col,start_row]
    
    for index,board in enumerate(boards):
        
        if turn :
            if index>5:

                for pos in range(64):
                    if board&(1<<pos) :
                        piece=get_piece_at(pos)
                        
                        mouves=get_legal_mouves(piece[0],pos//8,pos%8,not turn,False)
                        
                        if col_row in mouves:
                            
                            return True
        else:
            if index<6:
                for pos in range(64):
                    if board&(1<<pos) :
                        piece=get_piece_at(pos)
                        
                        mouves=get_legal_mouves(piece[0],pos//8,pos%8,not turn,False)
                        if col_row in mouves:
                            
                            return True
    
    return False

def is_king_checked(turn):
    if turn:king_board=white_king_board
    else:king_board=black_king_board
    for i in range(64):
        if king_board&(1<<i):
            king_row=i//8
            king_col=i%8
            break
    return is_square_attacked(king_row,king_col,turn)
    

def receive_position():
    global start_square,end_square
    global white_turn
    request=chess_client.recv()
    request=ast.literal_eval(request)
    request[0][1]=7-request[0][1]
    request[1][1]=7-request[1][1]
    request[0][0]=7-request[0][0]
    request[1][0]=7-request[1][0]
    
    start_square=request[0]
    end_square=request[1]
    
    moove_piece(request[0][1],request[0][0],request[1][1],request[1][0])
    
    
def evaluet(peaces_board):
    global advantage
    
    queen_points=4
    pawn_points=1
    knight_points=2
    bishop_points=2
    rook_points=3

    white_points=0
    black_points=0
    white_points+=(white_queen_board.bit_count())*queen_points
    black_points-=(black_queen_board.bit_count())*queen_points

    white_points+=(white_rook_board.bit_count())*rook_points
    black_points-=(black_rook_board.bit_count())*rook_points

    white_points+=(white_bishop_board.bit_count())*bishop_points
    black_points-=(black_bishop_board.bit_count())*bishop_points

    white_points+=(white_pawn_board.bit_count())*pawn_points
    black_points-=(black_pawn_board.bit_count())*pawn_points

    white_points+=(white_knight_board.bit_count())*knight_points
    black_points-=(black_knight_board.bit_count())*knight_points

    for pos in range(64):
        for index,board in enumerate(peaces_board):
            if board&(1<<pos):
                pos_row=pos//8
                pos_col=pos%8
                if index==0 :
                    white_points+=PAWN_TABLE[7-pos_row][pos_col]
                elif index==6:
                    black_points-=PAWN_TABLE[pos_row][pos_col]

                elif index==1 :
                    white_points+=KNIGHT_TABLE[7-pos_row][pos_col]
                elif index==7:
                    black_points-=KNIGHT_TABLE[pos_row][pos_col]


                elif index==2 :
                    white_points+=BISHOP_TABLE[7-pos_row][pos_col]
                elif index==8:
                    black_points-=BISHOP_TABLE[pos_row][pos_col]


                elif index==3 :
                    white_points+=ROOK_TABLE[7-pos_row][pos_col]
                elif index==9:
                    black_points-=ROOK_TABLE[pos_row][pos_col]

                elif index==4 :
                    white_points+=QUEEN_TABLE[7-pos_row][pos_col]
                elif index==10:
                    black_points-=QUEEN_TABLE[pos_row][pos_col]

                elif index==5 :
                    white_points+=KING_TABLE[7-pos_row][pos_col]
                elif index==11:
                    black_points-=KING_TABLE[pos_row][pos_col]


    old_advantage=advantage
    advantage=white_points+black_points
    if -1*max_val<advantage<max_val:
        return advantage
    else:
        advantage=old_advantage
        return old_advantage
    


def update_bars(adv):
    global black_bar,black_bar_rect
    global white_bar_rect,white_bar

    white_bar=pygame.surface.Surface((45,(square_size*4)+adv*buffer_val))
    white_bar_rect=white_bar.get_rect(topleft=(20,board_origin[1]))
    white_bar.fill(white_bar_color)
    black_bar=pygame.surface.Surface((45,board_origin[1]+(square_size*8)-white_bar_rect.bottom))
    black_bar_rect=black_bar.get_rect(topleft=(20,white_bar_rect.bottom))
    black_bar.fill(black_bar_color)

def get_legal_mouves(piece,start_row,start_col,turn,checking):
    global white_peaces_board,black_peaces_board
    global boards,white_king_mouved
    global black_king_mouved,white_passent_board
    global black_passent_board,en_passent_mouves
    global white_rook_right,white_rook_left
    legal_mouve=[]
    num=None
    start_postion=start_row*8+start_col
    blocked_pawn_right=False
    blocked_pawn_left=False
    white_start_row=6
    black_start_row=1
    taking_multi=1
    if turn:
        value=-1
        
        team_peaces=white_peaces_board
        peacess=black_peaces_board
        king_mouved=white_king_mouved
        rook_right=white_rook_right
        rook_left=white_rook_left
    else:
        value=1
        rook_right=black_rook_right
        rook_left=black_rook_left
        peacess=white_peaces_board
        team_peaces=black_peaces_board
        king_mouved=black_king_mouved
    blocked=False
    king_castle_positions=[[6,7],[6,0],[2,7],[2,0]]
    rook_l=rook_left
    rook_r=rook_right
    if game_state=="playing_online" and not assinged_turn:
        value*=-1
        black_start_row=7-black_start_row
        white_start_row=7-white_start_row
        rook_l=rook_right
        rook_r=rook_left
        taking_multi=-1
        for i in range(len(king_castle_positions)):
            king_castle_positions[i][0]=7-king_castle_positions[i][0]
            king_castle_positions[i][1]=7-king_castle_positions[i][1]
        
    if piece=="p":
        
        
        if turn:
            num=0
            
            
            taking_right_col=start_col+1
            taking_right_row=start_row+value
            taking_left_col=start_col-1
            taking_left_row=start_row+value
            if 0<=taking_right_col<8 and 0<=taking_right_row<8 :taking_right=taking_right_row*8+taking_right_col
            else: blocked_pawn_right=True
            if 0<=taking_left_col<8 and 0<=taking_left_row<8 :taking_left=taking_left_row*8+taking_left_col
            else:blocked_pawn_left=True
            
        else:
            
            num=6
            taking_right_col=start_col+1
            taking_right_row=start_row+value
            taking_left_col=start_col-1
            taking_left_row=start_row+value
            if 0<=taking_right_col<8 and 0<=taking_right_row<8 :taking_right=taking_right_row*8+taking_right_col
            else: blocked_pawn_right=True
            if 0<=taking_left_col<8 and 0<=taking_left_row<8 :taking_left=taking_left_row*8+taking_left_col
            else:blocked_pawn_left=True

        double_mouve_block=False
        for indexx,board in enumerate(boards):
            if  0<=start_row+value<8:
                if board&(1<<((start_row+value)*8+start_col)):
                    blocked=True
            if  0<=start_row+value*2<8:
                if board&(1<<((start_row+value*2)*8+start_col)):
                    double_mouve_block=True
            if checking:
                if turn and indexx>5:
                    if not blocked_pawn_right:
                        if black_peaces_board&(1<<taking_right) or for_white_passent_board&(1<<taking_right):legal_mouve.append([taking_right_col,taking_right_row])
                    if not blocked_pawn_left:
                        if black_peaces_board&(1<<taking_left) or for_white_passent_board&(1<<taking_left):legal_mouve.append([taking_left_col,taking_left_row])
                    
                elif not turn and indexx<6:
                    if not blocked_pawn_right:
                        if white_peaces_board&(1<<taking_right) or for_black_passent_board&(1<<taking_right):legal_mouve.append([taking_right_col,taking_right_row])
                    if not blocked_pawn_left:
                        if white_peaces_board&(1<<taking_left) or for_black_passent_board&(1<<taking_left):legal_mouve.append([taking_left_col,taking_left_row])
                
            else:
                
                legal_mouve.append([taking_right_col,taking_right_row])
                legal_mouve.append([taking_left_col,taking_left_row])
        
        
            
        if not blocked:
        
            legal_mouve.append([start_col,start_row+value])
            str_roow=white_start_row if turn else black_start_row

            if not double_mouve_block and start_row==str_roow:
                legal_mouve.append([start_col,start_row+value*2])
                    
            
    elif piece=="kn":
        mouves=[]

        if turn:num=1
        else:num=7
        
        up_right_row=start_row-2
        up_right_col=start_col+1
        if 0<=up_right_row<8 and 0<=up_right_col<8:
            up_right=up_right_row*8+up_right_col
            mouves.append(up_right)

        up_left_row=start_row-2
        up_left_col=start_col-1
        
        if 0<=up_left_row<8 and 0<=up_left_col<8:
            up_left=up_left_row*8+up_left_col
            mouves.append(up_left)

        down_right_row=start_row+2
        down_right_col=start_col+1
        
        if 0<=down_right_row<8 and 0<=down_right_col<8:
            down_right=down_right_row*8+down_right_col
            mouves.append(down_right)

        down_left_row=start_row+2
        down_left_col=start_col-1
        
        if 0<=down_left_row<8 and 0<=down_left_col<8:
            down_left=down_left_row*8+down_left_col
            mouves.append(down_left)
        
        up_right_row1=start_row-1
        up_right_col1=start_col+2
        
        if 0<=up_right_row1<8 and 0<=up_right_col1<8:
            up_right_1=up_right_row1*8+up_right_col1
            mouves.append(up_right_1)

        up_left_row1=start_row-1
        up_left_col1=start_col-2
        
        if 0<=up_left_row1<8 and 0<=up_left_col1<8:
            up_left1=up_left_row1*8+up_left_col1
            mouves.append(up_left1)

        down_right_row1=start_row+1
        down_right_col1=start_col+2
        if 0<=down_right_row1<8 and 0<=down_right_col1<8:
            down_right1=down_right_row1*8+down_right_col1        
            mouves.append(down_right1)
        
            
        

        down_left_row1=start_row+1
        down_left_col1=start_col-2
        
        if 0<=down_left_row1<8 and 0<=down_left_col1<8:
            down_left1=down_left_row1*8+down_left_col1
            mouves.append(down_left1)
        
       
        
        
        
        for i,mouve in enumerate(mouves):
            if 0<=mouve<64:
                row=mouve//8
                col=mouve%8
                if checking:

                    if not team_peaces&(1<<(mouve)):legal_mouve.append([col,row])
                else:
                    legal_mouve.append([col,row])
    elif piece=="r":
        if turn:num=3
        else:num=9
        blocked_right=False
        blocked_top=False
        blocked_bottom=False
        blocked_left=False
        for i in range(1,8):
            col_right=start_col+i
            col_left=start_col-i
            row_up=start_row-i
            row_down=start_row+i

            if col_right>7 or blocked_right:blocked_right=True
            else:
                position=start_row*8+col_right
                if peacess&(1<<position):
                    legal_mouve.append([col_right,start_row])
                    blocked_right=True
                elif team_peaces&(1<<position):
                    if checking:blocked_right=True
                    else:
                        legal_mouve.append([col_right,start_row])
                        blocked_right=True
                else:legal_mouve.append([col_right,start_row])

            if col_left<0 or blocked_left:blocked_left=True
            else:
                position=start_row*8+col_left
                if peacess&(1<<position):
                    legal_mouve.append([col_left,start_row])
                    blocked_left=True
                elif team_peaces&(1<<position):
                    if checking:blocked_left=True
                    else:
                        blocked_left=True
                        legal_mouve.append([col_left,start_row])
                else:legal_mouve.append([col_left,start_row])

            if row_up<0 or blocked_top:blocked_top=True
            else:
                position=row_up*8+start_col
                if peacess&(1<<position):
                    legal_mouve.append([start_col,row_up])
                    blocked_top=True
                    
                elif team_peaces&(1<<position):
                    if checking:blocked_top=True
                    else:
                        legal_mouve.append([start_col,row_up])
                        blocked_top=True
                else:legal_mouve.append([start_col,row_up])


            if row_down>7 or blocked_bottom:blocked_bottom=True
            else:
                position=row_down*8+start_col
                if peacess&(1<<position):
                    legal_mouve.append([start_col,row_down])
                    blocked_bottom=True
                elif team_peaces&(1<<position):
                    if checking:blocked_bottom=True
                    else:
                        blocked_bottom=True
                        legal_mouve.append([start_col,row_down])
                else:legal_mouve.append([start_col,row_down])
            if blocked_right and blocked_top and blocked_bottom and blocked_left:
                break
    elif piece=="b":
        
        if turn:num=2
        else:num=8
        
        blocked_top_right=False
        blocked_bottom_right=False
        blocked_top_left=False
        blocked_bottom_left=False
        blocked_top=False
        blocked_bottom=False
        for i in range(1,8):
            up_row=start_row-i
            down_row=start_row+i
            right=start_col+i
            left=start_col-i
            
            if up_row<0 :
                blocked_top_left=True 
                blocked_top_right=True
                blocked_top=True
                
            if right>7: 
                blocked_top_right=True
                blocked_bottom_right=True
                
            if left<0: 
                blocked_top_left=True
                blocked_bottom_left=True
                
            if down_row>7: 
                blocked_bottom_right=True
                blocked_bottom_left=True
                blocked_bottom=True

            if not blocked_top:
                if not blocked_top_right:
                    position=up_row*8+right
                    if peacess&(1<<position):
                        
                        legal_mouve.append([right,up_row])
                        blocked_top_right=True
                    elif team_peaces&(1<<position):
                        
                        if checking:blocked_top_right=True
                        else:
                            legal_mouve.append([right,up_row])
                            blocked_top_right=True
                    else:legal_mouve.append([right,up_row])
                if not blocked_top_left:
                    position=up_row*8+left
                    if peacess&(1<<position):
                        legal_mouve.append([left,up_row])
                        blocked_top_left=True
                    elif team_peaces&(1<<position):
                        if checking:blocked_top_left=True
                        else:
                            legal_mouve.append([left,up_row])
                            blocked_top_left=True
                    else:legal_mouve.append([left,up_row])
            if not blocked_bottom:
                if not blocked_bottom_right:
                    position=down_row*8+right
                    if peacess&(1<<position):
                        legal_mouve.append([right,down_row])
                        blocked_bottom_right=True
                    elif team_peaces&(1<<position):
                        if checking:blocked_bottom_right=True
                        else:
                            blocked_bottom_right=True
                            legal_mouve.append([right,down_row])
                    else:legal_mouve.append([right,down_row])
                if not blocked_bottom_left:
                    position=down_row*8+left
                    if peacess&(1<<position):
                        legal_mouve.append([left,down_row])
                        blocked_bottom_left=True
                    elif team_peaces&(1<<position):
                        if checking:blocked_bottom_left=True
                        else:
                            blocked_bottom_left=True
                            legal_mouve.append([left,down_row])
                    else:legal_mouve.append([left,down_row])
            if blocked_top_right and blocked_bottom_right and blocked_top_left and blocked_bottom_left:
                break
        

    elif piece=="q":
        if turn:num=4
        else:num=10
        blocked_top_right=False
        blocked_bottom_right=False
        blocked_top_left=False
        blocked_bottom_left=False
        blocked_top=False
        blocked_bottom=False
        for i in range(1,8):
            up_row=start_row-i
            down_row=start_row+i
            right=start_col+i
            left=start_col-i
            
            if up_row<0 :
                blocked_top_left=True 
                blocked_top_right=True
                blocked_top=True
                
            if right>7: 
                blocked_top_right=True
                blocked_bottom_right=True
                
            if left<0: 
                blocked_top_left=True
                blocked_bottom_left=True
                
            if down_row>7: 
                blocked_bottom_right=True
                blocked_bottom_left=True
                blocked_bottom=True

            if not blocked_top:
                if not blocked_top_right:
                    position=up_row*8+right
                    if peacess&(1<<position):
                        
                        legal_mouve.append([right,up_row])
                        blocked_top_right=True
                    elif team_peaces&(1<<position):
                        
                        if checking:blocked_top_right=True
                        else:
                            legal_mouve.append([right,up_row])
                            blocked_top_right=True
                    else:legal_mouve.append([right,up_row])
                if not blocked_top_left:
                    position=up_row*8+left
                    if peacess&(1<<position):
                        legal_mouve.append([left,up_row])
                        blocked_top_left=True
                    elif team_peaces&(1<<position):
                        if checking:blocked_top_left=True
                        else:
                            legal_mouve.append([left,up_row])
                            blocked_top_left=True
                    else:legal_mouve.append([left,up_row])
            if not blocked_bottom:
                if not blocked_bottom_right:
                    position=down_row*8+right
                    if peacess&(1<<position):
                        legal_mouve.append([right,down_row])
                        blocked_bottom_right=True
                    elif team_peaces&(1<<position):
                        if checking:blocked_bottom_right=True
                        else:
                            blocked_bottom_right=True
                            legal_mouve.append([right,down_row])
                    else:legal_mouve.append([right,down_row])
                if not blocked_bottom_left:
                    position=down_row*8+left
                    if peacess&(1<<position):
                        legal_mouve.append([left,down_row])
                        blocked_bottom_left=True
                    elif team_peaces&(1<<position):
                        if checking:blocked_bottom_left=True
                        else:
                            blocked_bottom_left=True
                            legal_mouve.append([left,down_row])
                    else:legal_mouve.append([left,down_row])
            if blocked_top_right and blocked_bottom_right and blocked_top_left and blocked_bottom_left:
                break

        blocked_right=False
        blocked_top=False
        blocked_bottom=False
        blocked_left=False
        for i in range(1,8):
            col_right=start_col+i
            col_left=start_col-i
            row_up=start_row-i
            row_down=start_row+i

            if col_right>7 or blocked_right:blocked_right=True
            else:
                position=start_row*8+col_right
                if peacess&(1<<position):
                    legal_mouve.append([col_right,start_row])
                    blocked_right=True
                elif team_peaces&(1<<position):
                    if checking:blocked_right=True
                    else:
                        legal_mouve.append([col_right,start_row])
                        blocked_right=True
                else:legal_mouve.append([col_right,start_row])

            if col_left<0 or blocked_left:blocked_left=True
            else:
                position=start_row*8+col_left
                if peacess&(1<<position):
                    legal_mouve.append([col_left,start_row])
                    blocked_left=True
                elif team_peaces&(1<<position):
                    if checking:blocked_left=True
                    else:
                        blocked_left=True
                        legal_mouve.append([col_left,start_row])
                else:legal_mouve.append([col_left,start_row])

            if row_up<0 or blocked_top:blocked_top=True
            else:
                position=row_up*8+start_col
                if peacess&(1<<position):
                    legal_mouve.append([start_col,row_up])
                    blocked_top=True
                    
                elif team_peaces&(1<<position):
                    if checking:blocked_top=True
                    else:
                        legal_mouve.append([start_col,row_up])
                        blocked_top=True
                else:legal_mouve.append([start_col,row_up])


            if row_down>7 or blocked_bottom:blocked_bottom=True
            else:
                position=row_down*8+start_col
                if peacess&(1<<position):
                    legal_mouve.append([start_col,row_down])
                    blocked_bottom=True
                elif team_peaces&(1<<position):
                    if checking:blocked_bottom=True
                    else:
                        blocked_bottom=True
                        legal_mouve.append([start_col,row_down])
                else:legal_mouve.append([start_col,row_down])
            if blocked_right and blocked_top and blocked_bottom and blocked_left:
                break


        for inde,mouve in enumerate(legal_mouve[:]):
            for ind,second_mouve in enumerate(legal_mouve[:]):
                if inde!=ind:
                    if mouve==second_mouve:legal_mouve.remove(second_mouve)
    elif piece=="k":
        if turn:num=5
        else:num=11
        king_mouves=[[start_col+1,start_row],[start_col+1,start_row+1],[start_col+1,start_row-1],[start_col,start_row-1],
                     [start_col,start_row+1],[start_col-1,start_row],[start_col-1,start_row+1],[start_col-1,start_row-1]]
        

        for i,king_mouve in enumerate(king_mouves):
            poss=king_mouve[1]*8+king_mouve[0]
            
            if 0<=king_mouve[0]<8 and 0<=king_mouve[1]<8:
                if checking:
                    if not team_peaces&(1<<poss):legal_mouve.append(king_mouve)
                else:legal_mouve.append(king_mouve)

        if king_mouved==False :
            
            if checking:
                if not is_king_checked(turn):
                    if not rook_r:
                        if not team_peaces&(1<<(start_row*8+(start_col+1*taking_multi))) and not team_peaces&(1<<(start_row*8+(start_col+2*taking_multi))):
                            if not is_square_attacked(start_row,start_col+1*taking_multi,turn) and not is_square_attacked(start_row,start_col+2*taking_multi,turn):
                                if turn:legal_mouve.append(king_castle_positions[0])
                                else:legal_mouve.append(king_castle_positions[1])
                    if not rook_l:
                        if not team_peaces&(1<<(start_row*8+(start_col-1*taking_multi))) and not team_peaces&(1<<(start_row*8+(start_col-2*taking_multi))) :
                            if not is_square_attacked(start_row,start_col-1*taking_multi,turn) and not is_square_attacked(start_row,start_col-2*taking_multi,turn):
                                if turn:legal_mouve.append(king_castle_positions[2])
                                else:legal_mouve.append(king_castle_positions[3])

                

    if checking:
  
        for mouve in legal_mouve[:]:
            
            
            simulate(num,start_col,start_row,mouve[0],mouve[1],True,turn)

            if is_king_checked(turn):
                legal_mouve.remove(mouve)
            simulate(num,start_col,start_row,mouve[0],mouve[1],False,turn)
        
            
        
    return(legal_mouve)


def promote(turn,piece):
    global boards,promote_position
    pawn_index=0 if turn else 6
    if piece=="q":
        piece_index=4 if turn else 10
        
        promote_pos=promote_position[1]*8+promote_position[0]
        boards[pawn_index]&=~(1<<promote_pos)
        boards[piece_index]|=(1<<promote_pos)
    elif piece=="b":
        piece_index=2 if turn else 8
        
        promote_pos=promote_position[1]*8+promote_position[0]
        boards[pawn_index]&=~(1<<promote_pos)
        boards[piece_index]|=(1<<promote_pos)
    elif piece=="k":
        piece_index=1 if turn else 7
        
        promote_pos=promote_position[1]*8+promote_position[0]
        boards[pawn_index]&=~(1<<promote_pos)
        boards[piece_index]|=(1<<promote_pos)
    elif piece=="r":
        piece_index=3 if turn else 9
        
        promote_pos=promote_position[1]*8+promote_position[0]
        boards[pawn_index]&=~(1<<promote_pos)
        boards[piece_index]|=(1<<promote_pos)
    promote_position=[]
    update_boards(True)


def look(direction):
    
    global shadow,current_position_index
    global game_mouves,boards
    global white_turn,white_peaces_board
    global for_white_passent_board,for_black_passent_board
    global black_peaces_board,white_rook_right
    global white_rook_left,black_rook_right
    global black_rook_left,white_king_mouved
    global black_king_mouved
    
    current_position_index+=direction
    if 0<=current_position_index<len(game_mouves):
        
       
        shadow=True
        current_game_mouve=game_mouves[current_position_index]
        
        boards=current_game_mouve["boards"][:]
        white_turn=current_game_mouve["turn"]
        for_white_passent_board=current_game_mouve["en_passent_for_white"]
        for_black_passent_board=current_game_mouve["en_passent_for_black"]
        white_peaces_board=current_game_mouve["white_peaces_board"]
        black_peaces_board=current_game_mouve["black_peaces_board"]
        white_king_mouved=current_game_mouve["white_king_mouved"]
        black_king_mouved=current_game_mouve["black_king_mouved"]
        white_rook_right=current_game_mouve["rook_mouved"][0]
        white_rook_left=current_game_mouve["rook_mouved"][1]
        black_rook_right=current_game_mouve["rook_mouved"][2]
        black_rook_left=current_game_mouve["rook_mouved"][3]
        if current_position_index==len(game_mouves)-1:
            shadow=False
            
        
    else:current_position_index-=direction
    
def show_mouves(legal_mouves):
    global availble_mouves_rects,availble_taking_rects
    if len(legal_mouves)!=0:
        for mouve in legal_mouves:
            
                
                if mouve!=None:
                    board=white_peaces_board if not white_turn else black_peaces_board
                    if board &(1<<((mouve[1]*8)+mouve[0])):
                        availble_taking_rects.append([mouve[0],mouve[1]])
                    else:
                        availble_mouves_rects.append([mouve[0],mouve[1]])
                
            
def update_boards(reverse):
    global boards
    global white_pawn_board,black_pawn_board
    global white_knight_board,black_knight_board
    global white_bishop_board,black_bishop_board
    global white_queen_board,black_queen_board
    global white_king_board,black_king_board
    global white_rook_board,black_rook_board

    if not reverse:
        boards[0]=white_pawn_board
        boards[1]=white_knight_board
        boards[2] = white_bishop_board
        boards[3] = white_rook_board
        boards[4] = white_queen_board
        boards[5] = white_king_board
        boards[6] = black_pawn_board
        boards[7] = black_knight_board
        boards[8] = black_bishop_board
        boards[9] = black_rook_board
        boards[10] = black_queen_board
        boards[11] = black_king_board
    else:
        white_pawn_board=boards[0]
        white_knight_board=boards[1]
        white_bishop_board=boards[2]
        white_rook_board=boards[3]
        white_queen_board=boards[4]
        white_king_board=boards[5]
        black_pawn_board=boards[6]
        black_knight_board=boards[7]
        black_bishop_board=boards[8]
        black_rook_board=boards[9]
        black_queen_board=boards[10]
        black_king_board=boards[11]

def castle(start_col,start_row,end_row,end_col,turn):
    global black_king_mouved,white_king_mouved
    global white_rook_board,black_rook_board
    global white_king_board,black_king_board
    if turn:white_king_mouved=True
    else:black_king_mouved=True

    
    if turn:
        
        if end_col>4:
            rook_position=end_col-1
            rook_start_position=7
        else:
            rook_start_position=0
            rook_position=end_col+1
        white_king_board&=~(1<<((start_row*8)+start_col))
        white_king_board|=(1<<((end_row*8)+end_col))
        white_rook_board&=~(1<<(start_row*8+rook_start_position))
        white_rook_board|=(1<<(start_row*8+rook_position))
    else:
        
        if end_col>4:
            rook_position=end_col-1
            rook_start_position=7
        else:
            rook_start_position=0
            rook_position=end_col+1
        black_king_board&=~(1<<((start_row*8)+start_col))
        black_king_board|=(1<<((end_row*8)+end_col))
        black_rook_board&=~(1<<(start_row*8+rook_start_position))
        black_rook_board|=(1<<(start_row*8+rook_position))
    
        

def moove_piece(start_row,start_col,end_row,end_col):
    global white_pawn_board, black_pawn_board
    global white_bishop_board, black_bishop_board
    global white_rook_board, black_rook_board
    global white_knight_board, black_knight_board
    global white_king_board, black_king_board
    global white_queen_board,black_queen_board
    global pieces, boards
    global white_turn,white_king_mouved
    global black_king_mouved,for_white_passent_board
    global white_peaces_board, black_peaces_board
    global for_black_passent_board,en_passent_mouves_for_white
    global en_passent_mouves_for_black,white_castled
    global black_castled,white_rook_right
    global white_rook_left,black_rook_right
    global black_rook_left,gave_passent_white
    global gave_passent_black,start_square
    global end_square,game_mouves
    global current_position_index,promoting
    global promote_position,checkmate
    global stalemate
    end_square
    played=False
    position=start_row*8+start_col
    end_position=end_row*8+end_col
    piece,h=get_piece_at(position)
    piece_at_end_postion,hh=get_piece_at(end_position)
    
    end_square.clear()
    if not gave_passent_white:
        for_white_passent_board=0
        en_passent_mouves_for_white.clear()
    elif not gave_passent_black:
        for_black_passent_board=0
        en_passent_mouves_for_black.clear()

    
    if white_turn:
        castledd=white_castled
        king_mouvedd=white_king_mouved
        val=1
        board=white_peaces_board
        if gave_passent_white:gave_passent_white=False
        taken_board=black_peaces_board
        rook_rightt=white_rook_right
        rook_leftt=white_rook_left
    else:
        castledd=black_castled
        king_mouvedd=black_king_mouved
        rook_rightt=black_rook_right
        val=-1
        rook_leftt=black_rook_left
        if gave_passent_black==True:
            gave_passent_black=False
        board=black_peaces_board
        taken_board=white_peaces_board

    str_row=6
    ed_row=4
    king_castle_positions=[[6,7],[6,0],[2,7],[2,0]]
    if game_state=="playing_online" and not assinged_turn:
        str_row=7-str_row
        ed_row=7-ed_row
        val*=-1
        for i in range(len(king_castle_positions)):
            king_castle_positions[i][0]=7-king_castle_positions[i][0]
            king_castle_positions[i][1]=7-king_castle_positions[i][1]
    if (not board&(1<<end_position)) and board&(1<<position):


        if piece=="p":
            legal_mouves=get_legal_mouves(piece,start_row,start_col,white_turn,True)
            
            row_col=[end_col,end_row]
            if row_col in legal_mouves:


                if white_turn and end_row==ed_row and start_row==str_row:
                    
                    en_passent_mouves_for_black.append([end_col,end_row+val])
                    gave_passent_black=True
                    
                    for_black_passent_board|=(1<<(end_row+val)*8+end_col)
                elif not white_turn and end_row==7-ed_row and start_row==7-str_row:
                    gave_passent_white=True
                    
                    for_white_passent_board|=(1<<(end_row+val)*8+end_col)
                    en_passent_mouves_for_white.append([end_col,end_row+val])
                    
                
                if white_turn:
                    white_pawn_board&=~(1<<position)
                    white_pawn_board|=(1<<end_position)
                else:
                    black_pawn_board&=~(1<<position)
                    black_pawn_board|=(1<<end_position)
                white_turn=not white_turn

                played=True
        elif piece=="q":
            legal_mouves=get_legal_mouves(piece,start_row,start_col,white_turn,True)                                                                                                                                                                 
            
            row_col=[end_col,end_row]
            if row_col in legal_mouves:
                if white_turn:
                    white_queen_board&=~(1<<position)
                    white_queen_board|=(1<<end_position)
                else:
                    black_queen_board&=~(1<<position)
                    black_queen_board|=(1<<end_position)
                white_turn=not white_turn
        
                played=True           
        elif piece=="kn":
            legal_mouves=get_legal_mouves(piece,start_row,start_col,white_turn,True)
            
            row_col=[end_col,end_row]
            
            if row_col in legal_mouves:
                if white_turn:
                    white_knight_board&=~(1<<position)
                    white_knight_board|=(1<<end_position)
                else:
                    black_knight_board&=~(1<<position)
                    black_knight_board|=(1<<end_position)
                white_turn=not white_turn
        
                played=True
        elif piece=="b":
            
            legal_mouves=get_legal_mouves(piece,start_row,start_col,white_turn,True)
           
            row_col=[end_col,end_row]
            
            if row_col in legal_mouves:
                if white_turn:
                    white_bishop_board&=~(1<<position)
                    white_bishop_board|=(1<<end_position)
                else:
                    black_bishop_board&=~(1<<position)
                    black_bishop_board|=(1<<end_position)
                white_turn=not white_turn
        
                played=True
        elif piece=="k":
            legal_mouves=get_legal_mouves(piece,start_row,start_col,white_turn,True)
            
            row_col=[end_col,end_row]
            
            if row_col in legal_mouves:
                if row_col in king_castle_positions and not castledd and (not rook_rightt or not rook_leftt) and not king_mouvedd:
                    castle(start_col,start_row,end_row,end_col,white_turn)
                    castled=True
                    if white_turn:white_king_mouved=True
                    else:black_king_mouved=True
                else:
                    if white_turn:
                        white_king_mouved=True
                        white_king_board&=~(1<<position)
                        white_king_board|=(1<<end_position)
                    else:
                        black_king_mouved=True
                        black_king_board&=~(1<<position)
                        black_king_board|=(1<<end_position)
                white_turn=not white_turn
        
                played=True

        
        elif piece=="r":

            legal_mouves=get_legal_mouves(piece,start_row,start_col,white_turn,True)
            
            row_col=[end_col,end_row]
            
            if row_col in legal_mouves:
                if white_turn:
                    if start_row==7 and start_col==7:white_rook_right=True
                    elif start_row==7 and start_col==0:white_rook_left=True
                    white_rook_board&=~(1<<position)
                    white_rook_board|=(1<<end_position)
                else:
                    if start_row==0 and start_col==7:white_rook_right=True
                    elif start_row==0 and start_col==0:white_rook_left=True
                    black_rook_board&=~(1<<position)
                    black_rook_board|=(1<<end_position)
                white_turn=not white_turn
        
                played=True
    else:("can't take you'r own peace")

    if played and game_state=="playing_online" and white_turn!= assinged_turn:
        chess_client.send("sending_mouve")
        confirmation=chess_client.recv()
        chess_client.send([start_col,start_row])
        confimation=chess_client.recv()
        chess_client.send([end_col,end_row])
    

    

    if white_turn:
        black_castled=castledd
        if for_black_passent_board&(1<<end_position):
            for_black_passent_board&=~(1<<end_position)
            white_pawn_board&=~(1<<((end_row+val)*8+end_col))
        

    else:
        if for_white_passent_board&(1<<end_position):
            black_pawn_board&=~(1<<((end_row+val)*8+end_col))
            
            for_white_passent_board&=~(1<<end_position)
        white_castled=castledd
    update_boards(False)
    if played and (end_row==0 or end_row==7) and piece=="p":
        promoting=True
        promote_position=[end_col,end_row]

    if piece_at_end_postion is not None   and played:
            
            if white_turn:
                for index,current_board in enumerate(boards):
                    if current_board &(1<<end_position) and index<6:
                        boards[index]&=~(1<<end_position)
                        

                        if current_board==white_pawn_board:
                            white_pawn_board&=~(1<<end_position)
                        
                        elif current_board==white_knight_board:
                            white_knight_board&=~(1<<end_position)
                        elif current_board==white_bishop_board:
                            white_bishop_board&=~(1<<end_position)
                        elif current_board==white_rook_board:
                            white_rook_board&=~(1<<end_position)
                            if end_col==7 :white_rook_right=True
                            elif end_col==0 :white_rook_left=True
                        elif current_board==white_queen_board:
                            white_queen_board&=~(1<<end_position)
                        elif current_board==white_king_board :
                            white_king_board&=~(1<<end_position)
                        
                        break
                
                        
            else:
                for index,current_board in enumerate(boards):
                    
                    if current_board &(1<<end_position) and index>5:
                        boards[index]&=~(1<<end_position)
                        
                        if current_board==black_pawn_board:
                            black_pawn_board&=~(1<<end_position)
                        
                        elif current_board==black_knight_board:
                            black_knight_board&=~(1<<end_position)
                        elif current_board==black_bishop_board:
                            black_bishop_board&=~(1<<end_position)
                        elif current_board==black_rook_board:
                            black_rook_board&=~(1<<end_position)
                            if end_col==7 :black_rook_right=True
                            elif end_col==0 :black_rook_left=True
                        elif current_board==black_queen_board:
                            black_queen_board&=~(1<<end_position)
                        elif current_board==black_king_board :
                            black_king_board&=~(1<<end_position)
                        
                        break

    white_peaces_board=0
    black_peaces_board=0
    for i in range(6):
        white_peaces_board|=boards[i]
        black_peaces_board|=boards[i+6]
    if played:
        
        update_bars(evaluet(boards))
        end_square=[end_col,end_row]
        
        snapshot={
            "turn":white_turn,
            "boards":boards[:],
            "rook_mouved":[white_rook_right,white_rook_left,black_rook_right,black_rook_left],
            "en_passent_for_white":for_white_passent_board,
            "en_passent_for_black":for_black_passent_board,
            "white_peaces_board":white_peaces_board,
            "black_peaces_board":black_peaces_board,
            "white_king_mouved":white_king_mouved,
            "black_king_mouved":black_king_mouved
        }      
        game_mouves.append(snapshot)
        current_position_index+=1
        
    else:
        start_square=[]
    checkmate=is_checkmated(white_turn)
    stalemate=is_stalemate(white_turn)
    
    pieces=boards[0]|boards[1]|boards[2]|boards[3]|boards[4]|boards[5]|boards[6]|boards[7]|boards[8]|boards[9]|boards[10]|boards[11]
def spawn_peaces():
    global white_pawn_board, black_pawn_board
    global white_bishop_board, black_bishop_board
    global white_rook_board, black_rook_board
    global white_knight_board, black_knight_board
    global white_king_board, black_king_board
    global white_queen_board, black_queen_board
    global white_peaces_board, black_peaces_board
    global boards, pieces,game_mouves
    global current_position_index
    placement_row=6
    if game_state=="playing_online" and not assinged_turn:
        placement_row=1
    
    for colu in range(8):
        
        position = placement_row * 8 + colu
        white_pawn_board |= 1 << position
        

        placement_row = 7-placement_row
        
        position = placement_row * 8 + colu
        black_pawn_board |= 1 << position
        placement_row=7-placement_row
    placement_row=0
    white_back_rank = [
        rook_white, knight_white, bishop_white, queen_white,
        king_white, bishop_white, knight_white, rook_white
    ]
    black_back_rank = [
        rook_black, knight_black, bishop_black, queen_black,
        king_black, bishop_black, knight_black, rook_black
    ]
    if game_state=="playing_online" and not assinged_turn:
        placement_row=7
        holder=black_back_rank[4]
        black_back_rank[4]=black_back_rank[3]
        black_back_rank[3]=holder
        holder=white_back_rank[4]
        white_back_rank[4]=white_back_rank[3]
        white_back_rank[3]=holder
    
    for colu,piece in enumerate(black_back_rank):
        
        if piece==rook_black:
            position=placement_row*8+colu
            black_rook_board|=1<<position
        elif piece==knight_black:
            position=placement_row*8+colu
            black_knight_board|=1<<position
        elif piece==bishop_black:
            position=placement_row*8+colu
            black_bishop_board|=1<<position
        elif piece==king_black:
            position=placement_row*8+colu
            black_king_board|=1<<position
        elif piece==queen_black:
            position=placement_row*8+colu
            black_queen_board|=1<<position
    placement_row=7-placement_row
    for colu,piece in enumerate(white_back_rank):
        
        


        if piece==rook_white:
            position=placement_row*8+colu
            white_rook_board|=1<<position
        elif piece==knight_white:
            position=placement_row*8+colu
            white_knight_board|=1<<position
        elif piece==bishop_white:
            position=placement_row*8+colu
            white_bishop_board|=1<<position
        elif piece==king_white:
            position=placement_row*8+colu
            white_king_board|=1<<position
        elif piece==queen_white:
            position=placement_row*8+colu
            white_queen_board|=1<<position
    white_peaces_board=white_pawn_board|white_bishop_board|white_rook_board|white_knight_board|white_king_board|white_queen_board
    black_peaces_board=black_pawn_board|black_bishop_board|black_rook_board|black_knight_board|black_king_board|black_queen_board
    pieces=white_peaces_board|black_peaces_board
    boards[0] = white_pawn_board
    boards[1] = white_knight_board
    boards[2] = white_bishop_board
    boards[3] = white_rook_board
    boards[4] = white_queen_board
    boards[5] = white_king_board
    boards[6] = black_pawn_board
    boards[7] = black_knight_board
    boards[8] = black_bishop_board
    boards[9] = black_rook_board
    boards[10] = black_queen_board
    boards[11] = black_king_board


def is_checkmated(turn):
    mate=True
    if is_king_checked(turn):
        
        for i in range(64):
            piece_index=get_piece_index(i)
            if piece_index !=None:
                if piece_index<6 and turn:
                    legal_mouve=get_legal_mouves(get_piece_at(i)[0],i//8,i%8,turn,True)
                    
                    if len(legal_mouve)>0:

                        mate=False
                        return mate
                elif piece_index>5 and not turn:
                    legal_mouve=get_legal_mouves(get_piece_at(i)[0],i//8,i%8,turn,True)
                    
                    if len(legal_mouve)>0:

                        mate=False
                        return mate
        return mate
    return False

def is_stalemate(turn):
    stale_mate=True
    if turn and not is_king_checked(turn):
        for i in range(64):
            piece_index=get_piece_index(i)
            if piece_index !=None:
                if piece_index<6:
                    legal_mouve=get_legal_mouves(get_piece_at(i)[0],i//8,i%8,white_turn,True)
                    
                    if len(legal_mouve)>0:
                        stale_mate=False
                        return stale_mate
        return stale_mate

    if white_peaces_board.bit_count()==black_peaces_board.bit_count()==1:
        return True
    return False

def spawn_board():
    
    current_x,current_y=board_origin
    white=True
    for y in range(1,9):
        
        for x in range(1,9):
            if(white):
                color=DARK_SQUARE
                white=False
            else:
                color=LIGHT_SQUARE
                white=True
            surface=pygame.surface.Surface((square_size,square_size))
            surface.fill(color)
            rect=surface.get_rect(topleft=(current_x,current_y))
            squares[y-1][x-1]=surface
            rects[y-1][x-1]=rect
            screen.blit(surface,rect)
            current_x+=square_size
            if x==8:
                white=not white
        
        current_x=board_origin[0]
        current_x=board_origin[0]
        current_y+=square_size
def hovered_square():
    mouse_x,mouse_y=pygame.mouse.get_pos()

    col=(mouse_x//(square_size))
    row=mouse_y//(square_size)
    if board_origin[0]!=0:
        col-=board_origin[0]//square_size
    if board_origin[1]!=0:
        row-=board_origin[1]//square_size
    pos=row*8+col
    if get_piece_at(pos)!=(None,None):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    if 0<=col<8 and 0<=row<8:return(row,col)
    return None,None

def render():
    
    global start_square,end_square
    screen.blit(black_bar,black_bar_rect)
    screen.blit(white_bar,white_bar_rect)
    white=True
    screen.blit(white_bar,white_bar_rect)
    
    for y in range(8):
        for x in range(8):
            
            if(white):
                highlit_color=HIGHLIGHT_COLOR_WHITE
                color=LIGHT_SQUARE
                text_color=DARK_SQUARE
                white=False
            else:
                highlit_color=HIGHLIGHT_COLOR_BLACK
                text_color=LIGHT_SQUARE
                color=DARK_SQUARE
                white=True


            
            if len(start_square)!=0:
                if x==start_square[0] and y == start_square[1]:
                    square=squares[y][x]
                    square.fill(highlit_color)
                    screen.blit(square,rects[y][x])
                
                else:
                    squares[y][x].fill(color)
                    screen.blit(squares[y][x],rects[y][x])
            if len(end_square)!=0:
                if x==end_square[0] and y == end_square[1]:
                    square=squares[y][x]
                    square.fill(highlit_color)
                    screen.blit(square,rects[y][x])
                elif x!=end_square[0] and y != end_square[1] and x!=start_square[0] and y != start_square[1]:
                    squares[y][x].fill(color)
                    screen.blit(squares[y][x],rects[y][x])
            if len(start_square)==0 and len(end_square)==0:
                squares[y][x].fill(color)
                screen.blit(squares[y][x],rects[y][x])
            if x==7:
                white=not white
    white=False
    if game_state=="playing_offline":
        for i in range(8):
            if white:
                text_color=DARK_SQUARE
                
            else:
                text_color=LIGHT_SQUARE
            white=not white
            letter=small_font.render(letters[i],True,text_color)
            letter_rect=letter.get_rect(center=(board_origin[0]+68+square_size*i , board_origin[1]+ square_size*8-10))
            screen.blit(letter,letter_rect)
        white=False
        for i in range(7,-1,-1):
            if white:text_color=DARK_SQUARE
            else:text_color=LIGHT_SQUARE
            white=not white
            number=small_font.render(f"{8-i}",True,text_color)
            number_rect=number.get_rect(center=(5+board_origin[0],board_origin[1]+ square_size*i+10))
            screen.blit(number,number_rect)
    elif game_state=="playing_online" and not assinged_turn:
        for i in range(8):
            if white:
                text_color=DARK_SQUARE
                
            else:
                text_color=LIGHT_SQUARE
            white=not white
            letter=small_font.render(letters[7-i],True,text_color)
            letter_rect=letter.get_rect(center=(board_origin[0]+68+square_size*i,board_origin[1]+ square_size*8-10))
            screen.blit(letter,letter_rect)
        white=False
        for i in range(7,-1,-1):
            if white:text_color=DARK_SQUARE
            else:text_color=LIGHT_SQUARE
            white=not white
            number=small_font.render(f"{i+1}",True,text_color)
            number_rect=number.get_rect(center=(5+board_origin[0],board_origin[1]+square_size*i+10))
            screen.blit(number,number_rect)

    for board in boards:
        
        for pos in range(64):
            if board &(1<<pos):
                column= pos%8
                rowe=pos//8
                if board==boards[0]:
                    screen.blit(pawn_white, (board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))
                elif board==boards[1]:
                    screen.blit(knight_white, (board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))
                elif board==boards[2]:
                    screen.blit(bishop_white, (board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))
                elif board==boards[3]:
                    screen.blit(rook_white, (board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))
                elif board==boards[4]:
                    screen.blit(queen_white, (board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))
                elif board==boards[5]:
                    screen.blit(king_white, (board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))
                elif board==boards[6]:
                    screen.blit(pawn_black, (board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))
                elif board==boards[7]:
                    screen.blit(knight_black, (board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))
                elif board==boards[8]:
                    screen.blit(bishop_black,(board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))
                elif board==boards[9]:
                    screen.blit(rook_black, (board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))
                elif board==boards[10]:
                    screen.blit(queen_black, (board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))
                elif board==boards[11]:
                    screen.blit(king_black, (board_origin[0]+ (square_size * column), board_origin[1]+(square_size * rowe)))

    if len(availble_mouves_rects)!=0:
        for rect in availble_mouves_rects:
            pygame.draw.circle(screen,(191, 191, 191),(board_origin[0]+(square_size/2+rect[0]*square_size), board_origin[1]+(square_size/2+rect[1]*square_size)),19,25)
    if len(availble_taking_rects)!=0:
        for rect in availble_taking_rects:
            pygame.draw.circle(screen,(225, 165, 165),(board_origin[0]+(square_size/2+rect[0]*square_size),board_origin[1]+(square_size/2+rect[1]*square_size)),square_size/2,8)
    
def draw_menue():
    global online_rect,offline_rect
    global text_width,tex_height
    NORMAL_STATE=(108,94,79)
    HOEVERED_STATE=(104,92,79)
    color=NORMAL_STATE
    screen.fill((140,107,79))
    game_name=half_italic_font_big.render("Chess",True,(215,207,191))
    game_name_rect=game_name.get_rect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/4))

    
    text_width,tex_height=medium_italic_font_small.size("Play Online")
    online_rect=pygame.Rect(0,0,text_width+15,tex_height+8)
    
    online_rect.center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
    
    play_online_text=medium_italic_font_small.render("Play Online",True,(215,207,191))
    play_online_rect=play_online_text.get_rect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

    

    offline_rect=pygame.Rect(0,0,text_width+15,tex_height+8)
    
    offline_rect.center=(WINDOW_WIDTH/2,(WINDOW_HEIGHT/2)+75)
    
    play_offline_text=medium_italic_font_small.render("Play Offline",True,(215,207,191))
    play_offline_rect=play_offline_text.get_rect(center=(WINDOW_WIDTH/2,75+(WINDOW_HEIGHT/2)))
    
    

    mouse_position=pygame.mouse.get_pos()
    if play_offline_rect.collidepoint(mouse_position):
        play_offline_text=medium_italic_font_small.render("Play Offline",True,(178,169,159))
        color=HOEVERED_STATE
    pygame.draw.rect(screen,NORMAL_STATE,offline_rect,border_radius=10)
    screen.blit(play_offline_text,play_offline_rect)
    color=NORMAL_STATE
    if play_online_rect.collidepoint(mouse_position):
        play_online_text=medium_italic_font_small.render("Play Online",True,(178,169,159))
        color=HOEVERED_STATE
    
    pygame.draw.rect(screen,NORMAL_STATE,online_rect,border_radius=10)
    screen.blit(play_online_text,play_online_rect)
    
    screen.blit(game_name,game_name_rect)

can_play=False

if __name__ == "__main__":
    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if game_state=="main_menue":
                    mouse_pos=pygame.mouse.get_pos()
                
                    if offline_rect.collidepoint(mouse_pos):
                        game_state="playing_offline"
                        spawn_board()
                        spawn_peaces()
                        can_play=True
                        
                        update_bars(evaluet(boards))
                    elif online_rect.collidepoint(mouse_pos):
                        game_state="playing_online"
                        threading.Thread(target=chess_client.start).start()
                        time.sleep(0.5)
                        chess_client.send("ok")
                        assinged_turn=chess_client.recv()
                        assinged_turn=bool(int(assinged_turn))
                    
                        can_play=True
                        waiting_for_pos=True
                        spawn_board()
                        spawn_peaces()
                        
                        update_bars(evaluet(boards))

            
                if can_play:
                    if promoting:
                        for ind,promote_rect in enumerate(promote_rects):
                            if promote_rect.collidepoint(pygame.mouse.get_pos()):
                                promote(not white_turn,promote_pieces[ind])
                                promoting=False
                    elif event.button == 1 and ready and not shadow and not promoting and (game_state=="playing_offline" or game_state=="playing_online"): 
                            row,col=hovered_square()
                            ready=False
                            if row is not None and col is not None:
                                if white_turn:
                                    peaces=white_peaces_board
                                else:peaces=black_peaces_board
                                if starting :
                                    position=row*8+col
                                    if(get_piece_at(position) is not None) and peaces&(1<<position):
                                        starting=False
                                        start_row=row
                                        start_col=col
                                        end_square=[]
                                        start_square=[start_col,start_row]
                                        show_mouves(get_legal_mouves(get_piece_at(position)[0],start_row,start_col,white_turn,True))
                                    
                                else:
                                
                                    starting=True
                                
                                    moove_piece(start_row,start_col,row,col)
                                    availble_taking_rects.clear()
                                    availble_mouves_rects.clear()
            elif event.type == pygame.MOUSEBUTTONUP and (game_state=="playing_offline"or game_state=="playing_online"):
                if event.button == 1 and not shadow:
                    ready=True
            elif event.type==pygame.KEYDOWN :
                if game_state=="playing_offline" or game_state=="playing_online" or game_state=="game_over":
                    if event.key==pygame.K_l:
                        look(1)
                    elif event.key==pygame.K_j:
                        look(-1)
                    elif event.key==pygame.K_ESCAPE:
                        game_state="main_menue"


        screen.fill((48,46,43))

        if   white_turn==assinged_turn and game_state=="playing_online":
            can_play=True
            waiting_for_pos=True
        elif   white_turn!=assinged_turn and game_state=="playing_online":
            can_play=False
                
                
            if  waiting_for_pos:
            
                get_value=threading.Thread(target=receive_position)
                get_value.daemon=True
                get_value.start()
                waiting_for_pos=False

        if game_state=="playing_offline" or game_state=="playing_online":
            row, col = hovered_square()
        
            screen.fill((48, 46, 43))
            render()
            # if white_turn:
            #     text="White turn"
            #     background.fill("black")
            #     render_text=font.render(text,True,"white")
            # else:
            #     text="Black turn"
            #     background.fill("white")
            #     render_text=font.render(text,True,"black")
            # screen.blit(render_text,(610,0))

            if promoting:
                promote_rects.clear()
                backgroundd=pygame.surface.Surface((75*8,600))
                backgroundd.fill("black")
                backgroundd.set_alpha(150)
                promote_text=font.render("Promote",True,"white")
                promote_text_rect=promote_text.get_rect(center=((75*8)/2,300-100))
                screen.blit(backgroundd,(0,0))
                screen.blit(promote_text,promote_text_rect)
                bishop=bishop_white if not white_turn else bishop_black
                knight=knight_white if not white_turn else knight_black
                queen=queen_white if not white_turn else queen_black
                rook=rook_white if not white_turn else rook_black
                bishop_rect=bishop.get_rect(topleft=(3*75,4*75))
                knight_rect=knight.get_rect(topleft=(4*75,4*75))
                queen_rect=queen.get_rect(topleft=(3*75,3*75))
                rook_rect=rook.get_rect(topleft=(4*75,3*75))
                promote_rects.append(bishop_rect)
                promote_rects.append(knight_rect)
                promote_rects.append(rook_rect)
                promote_rects.append(queen_rect)
                promote_pieces=["b","k","r","q"]
                screen.blit(bishop,bishop_rect)
                screen.blit(queen,queen_rect)
                screen.blit(rook,rook_rect)
                screen.blit(knight,knight_rect)
            if checkmate:
                game_over_text="Black won" if white_turn else "White won"
                render_text=font.render(game_over_text,True,"black" if not white_turn else "white")
                screen.blit(render_text,(75*8+20,75*4))
            
            elif stalemate:
                game_over_text="stalemate" 
                render_text=font.render(game_over_text,True,"black" if not white_turn else "white")
                screen.blit(render_text,(75*8+20,75*4))
                can_play=False
        elif game_state=="main_menue":
            draw_menue()
    
        pygame.display.update()
        clock.tick(60)

