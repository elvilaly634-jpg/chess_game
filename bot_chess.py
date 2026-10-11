import chess


def search(depth,ai_turn,boards):
    
    
    
    total_legal_mouves=[]
    
    for i in range (64):
        for board in boards:
            if board&(1<<i):
                peace=chess.get_piece_at(i)[0]
                
                total_legal_mouves.append(chess.get_legal_mouves(peace,i//8,i%8,ai_turn,True))
                print(peace)
    
    