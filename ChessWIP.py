# Forrest Richardson
# note: white uses capital letters, black uses lowercase
# 

class Board:
    def __init__(self):
        self.blackPieces = ["w" ,"r", "n", "b", "q", "k"]
        self.whitePieces = ["M" ,"R", "N", "B", "Q", "K"]
        
        self.board = [
                    ["R","M","_","_","_","_","w","r"],
                    ["N","M","_","_","_","_","w","n"],
                    ["B","M","_","_","_","_","w","b"],
                    ["Q","M","_","_","_","_","w","q"],
                    ["K","M","_","_","_","_","w","k"],
                    ["B","M","_","_","_","_","w","b"],
                    ["N","M","_","_","_","_","w","n"],
                    ["R","M","_","_","_","_","w","r"]
                    ]
    def getBoard(self):
        print("----------------------------------------")
        for i in self.board:
            print(i)
        print("----------------------------------------")        

    def move(self,src,dst):
       
        # src and dst are tuples
        piece = self.board[src[0]][src[1]]
        target = self.board[dst[0]][dst[1]]
        
        
        
        # Are src and dst on the board?
        if src[0] not in range(8) and src[1] not in range(8) and dst[0] not in range(8) and dst[1] not in range(8):
            print("error: src or dst not on board")
            return -1
         
        # is src a piece?
        elif piece == "_":
            print("error: src not a piece")
            return -1
        #TODO check further legality
        
        # pawns
        if piece == "M" or piece == "w":
            return self.movePawn(src, dst)
            
        elif piece == "B" or piece == "b":
            return self.moveBishop(src, dst)
            
        elif piece == "R" or piece == "r":
            return self.moveRook(src, dst)
            
        elif piece == "N" or piece == "n":
            return self.moveKnight(src, dst)
            
        elif piece == "Q" or piece == "q":
            return self.moveQueen(src, dst)
            
        elif piece == "K" or piece == "k":
            return self.moveKing(src, dst)

    def movePawn(self, src, dst):
        
        piece = self.board[src[0]][src[1]]
        target = self.board[dst[0]][dst[1]]
        if piece == "M":
            color = 1
        elif piece == "w":
            color = -1
            
        # vertical move
        if dst[0] == src[0]:
            
            # one square forward
            if dst[1] == src[1] + color and target == "_":
                return self.legalMove(src, dst)
                
            # two squares forward
            if dst[1] == src[1] + color*2:
                if  self.board[src[0]][src[1] + color] == "_" and target == "_":
                    if src[1] == 1 and color == 1 or src[1] == 6 and color == -1:
                        return self.legalMove(src,dst)
            
            print("error: collision")    
            return(-1)
        
        # diagonal capture
        if src[1] + color == dst[1]:
            if abs(dst[0] - src[0]) == 1:
                if color == 1:
                    if target in self.blackPieces:
                        return self.legalMove(src, dst)
                elif color == -1:
                    if target in self.whitePieces:
                        return self.legalMove(src, dst)
    
    def moveBishop(self, src, dst):
        
        piece = self.board[src[0]][src[1]]
        target = self.board[dst[0]][dst[1]]
        if piece == "B":
            color = 1
        elif piece == "b":
            color = -1
        # get xy change    
        dx = dst[0] - src[0]
        dy = dst[1] - src[1]
        
        dxSign =  int(dx / abs(dx))
        dySign = int(dy / abs(dy))
        
        #chaeck if diagonal move
        if abs(dx) != abs(dy):
            print("error: make a diagonal move")    
            return -1
            
          
        else:

            # check for collisions  
            temp = 1
            while temp < abs(dx):
                
                tempTgt = self.board[src[0]+dxSign*temp][src[1]+dySign*temp]
                
                if tempTgt == "_":
                    temp += 1
                else:
                    # collision
                    print("error: collision")
                    return -1
                    
            if target == "_":
                return self.legalMove(src, dst)       
            elif color == 1:
                if target in self.blackPieces:
                    return self.legalMove(src, dst)
            elif color == -1:
                if target in self.whitePieces:
                    return self.legalMove(src, dst)
            else:
                print("error: unknown move; try again")
                return -1
            
            
    def moveRook(self, src, dst):
        piece = self.board[src[0]][src[1]]
        target = self.board[dst[0]][dst[1]]
        if piece == "R":
            color = 1
        elif piece == "r":
            color = -1
        # get xy change
        dx = dst[0] - src[0]
        dy = dst[1] - src[1]
       
        if dx == 0:
            dxSign = 0
        else:
            dxSign =  int(dx / abs(dx))
            
        if dy == 0:
            dySign = 0
        else:
            dySign = int(dy / abs(dy))
        
        #chaeck if diagonal move
        if abs(dx) < abs(dy)+abs(dx) and abs(dy) < abs(dy)+abs(dx):
            print("error: make a perpindicular move")    
            return -1
            
          
        else:

            # check for collisions
            temp = 1
            while temp < abs(dx):
                
                tempTgt = self.board[src[0]+dxSign*temp][src[1]+dySign*temp]
                
                if tempTgt == "_":
                    temp += 1
                else:
                    # collision
                    print("error: collision")
                    return -1
                 
            if target == "_":
                return self.legalMove(src, dst) 
            
            elif color == 1:
                
                if target in self.blackPieces:
                    return self.legalMove(src, dst)
            elif color == -1:
                if target in self.whitePieces:
                    return self.legalMove(src, dst)
            
            else:
                print("error: unknown move; try again")
                return -1
                
    def moveKnight(self, src, dst):
        piece = self.board[src[0]][src[1]]
        target = self.board[dst[0]][dst[1]]
        if piece == "N":
            color = 1
        elif piece == "n":
            color = -1

        # get xy change
        dx = dst[0] - src[0]
        dy = dst[1] - src[1]
       
        if abs(dx) + abs(dy) != 3:
            print("error: illegal move")
            return -1
        if dx == 0 or dy == 0:
            print("error: illegal move")
            return -1
        
        if target == "_":
            return self.legalMove(src, dst) 
        elif color == 1:
            if target in self.blackPieces:
                return self.legalMove(src, dst)
            else:
                print("error: illegal move")
                return -1
        elif color == -1:
            if target in self.whitePieces:
                return self.legalMove(src, dst)
            else:
                print("error: illegal move")
                return -1
        else:
            print("error: unknown move; try again")
            return -1    
                
                
    def moveQueen(self, src, dst):
        pass
    def moveKing(self, src, dst):
        pass

    def legalMove(self, src, dst):
        # update board state to reflect the move
        if self.board[dst[0]][dst[1]] != "_":
            print("Capture")
        else:
            print("Legal move")
        
        self.board[dst[0]][dst[1]] = self.board[src[0]][src[1]]
        self.board[src[0]][src[1]] = "_"
        return 1
                
def pawnTest(x):
         
    b = Board()
    
    if x == 1:
        print("white pawn move 1 forward, 3 times")
        b.getBoard()
        b.move((3,1),(3,2))
        b.getBoard()
        b.move((3,2),(3,3))
        b.getBoard()
        b.move((3,3),(3,4))
        b.getBoard()
        
    if x == 2:
        print("white pawn double move")
        b.getBoard()
        b.move((3,1),(3,3))
        b.getBoard()
        
    if x == 3:
        print("false white pawn double move")
        b.getBoard()
        b.move((3,1),(3,2))
        b.getBoard()
        b.move((3,2),(3,4))
        b.getBoard()
        
    if x == 4:
        print("pawn collision test")
        b.getBoard()
        b.move((3,1),(3,3))
        b.getBoard()
        b.move((3,6),(3,4))
        b.getBoard() 
        b.move((3,3),(3,4))
        b.getBoard()  
        
    if x == 5:
        print("valid capture test")
        b.getBoard()
        b.move((3,1),(3,3))
        b.getBoard()
        b.move((4,6),(4,4))
        b.getBoard()
        b.move((3,3),(4,4))
        b.getBoard()  
  
#pawnTest(5)

def bishopTest(x):
         
    b = Board()
    
    if x == 1:
        print("bishop move one spot three times")
        b.getBoard()
        b.move((3,1),(3,2))
        b.getBoard()
        b.move((2,0),(3,1))
        b.getBoard()
        b.move((3,1),(4,2))
        b.getBoard()
        b.move((4,2),(5,3))
        b.getBoard()
        
    if x == 2:
        print("bishop move 3 spots")
        b.getBoard()
        b.move((3,1),(3,2))
        b.getBoard()
        b.move((2,0),(5,3))
        b.getBoard()
    
    if x == 3:
        print("bishop move 3 spots")
        b.getBoard()
        b.move((4,1),(4,2))
        b.getBoard()
        b.move((5,0),(1,4))
        b.getBoard()
        
        
    if x == 4:
        print("bishop capture test")
        b.getBoard()
        b.move((4,1),(4,2))
        b.getBoard()
        b.move((1,6),(1,4))
        b.getBoard()
        b.move((5,0),(1,4))
        b.getBoard()
        
        
#bishopTest(4)

def rookTest(x):
         
    b = Board()
    
    if x == 1:
        print("rook move up")
        b.getBoard()
        b.move((0,1),(0,3))
        b.getBoard()
        b.move((0,0),(0,2))
        b.getBoard()  
        
    if x == 2:
        print("rook collision test")
        b.getBoard()
        b.move((0,1),(0,3))
        b.getBoard()
        b.move((0,0),(0,3))
        b.getBoard()     
        
    if x == 3:
        print("rook move up then out")
        b.getBoard()
        b.move((0,1),(0,3))
        b.getBoard()
        b.move((0,0),(0,2))
        b.getBoard()      
        b.move((0,2),(7,2))
        b.getBoard()  
        
    if x == 4:
        print("rook capture test")
        b.getBoard()
        b.move((0,1),(0,3))
        b.getBoard()
        b.move((0,0),(0,2))
        b.getBoard()      
        b.move((0,2),(7,2))
        b.getBoard()  
        b.move((7,2),(7,6))
        b.getBoard()  
          
    
       
#rookTest(4)

def knightTest(x):
         
    b = Board()
    
    if x == 1:
        print("knight move out")
        b.getBoard()
        b.move((1,0),(2,2))
        b.getBoard()
        b.move((2,2),(4,3))
        b.getBoard()
        
    if x == 2:
        print("collision test")
        b.getBoard()
        b.move((1,0),(2,2))
        b.getBoard()
        b.move((2,2),(4,1))
        b.getBoard()
        
    if x == 3:
        print("capture test")
        b.getBoard()
        b.move((1,0),(2,2))
        b.getBoard()
        b.move((2,2),(4,3))
        b.getBoard()
        b.move((3,6),(3,5))
        b.getBoard()
        b.move((4,3),(3,5))
        b.getBoard()
        
        
knightTest(3)



            

