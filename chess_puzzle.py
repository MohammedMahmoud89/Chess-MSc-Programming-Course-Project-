import copy
import os.path
import random

def location2index(loc: str) -> tuple[int, int]:
    di={"a": 1,"b":2,"c": 3,"d": 4,"e": 5,"f": 6,"g": 7,"h": 8,"i": 9,"j": 10,"k": 11,"l": 12,"m": 13,"n": 14,"o": 15,"p": 16,"q": 17, "r":18,"s": 19,"t": 20,"u":21,"v": 22,"w": 23,"x": 24,"y": 25,"z": 26}
    x=di[loc[0]]
    y=int(loc[1])

    return (x,y)


def index2location(x: int, y: int) -> str:
    di={"a": 1,"b":2,"c": 3,"d": 4,"e": 5,"f": 6,"g": 7,"h": 8,"i": 9,"j": 10,"k": 11,"l": 12,"m": 13,"n": 14,"o": 15,"p": 16,"q": 17, "r":18,"s": 19,"t": 20,"u":21,"v": 22,"w": 23,"x": 24,"y": 25,"z": 26}
    key_list = list(di.keys())
    val_list = list(di.values())
    pos = val_list.index(x)
    key=key_list[pos]
    op=key+str(y)
    return op

class Piece:
    pos_x : int
    pos_y : int
    side : bool #True for White and False for Black
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values'''
        self.pos_x=pos_X
        self.pos_y=pos_Y
        self.side= side_
    def pos_x (self,pos_X):
        self.pos_x=pos_X
    def pos_y (self,pos_Y):
        self.pos_y=pos_Y
    def side (self,side_):
        self.side=side_
    def __eq__(self, other):
        return self.pos_x == other.pos_x and self.pos_y == other.pos_y and self.side == other.side


#Board = tuple[int, list[Piece]]


def is_piece_at(pos_X : int, pos_Y : int, B) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B'''
    for piece in B[1]:
        if pos_X==piece.pos_x and pos_Y==piece.pos_y:
            return True

    return False

def piece_at(pos_X : int, pos_Y : int, B) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    for piece in B[1]:
        if piece.pos_x==pos_X and piece.pos_y==pos_Y:
            return piece



class Knight(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)

    def can_reach(self, pos_X : int, pos_Y : int, B):
        '''checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule1] and [Rule3] (see section Intro)
        Hint: use is_piece_at
        '''
        #[Rule1] A knight may move two squares vertically and one square horizontally
        #or two squares horizontally and one square vertically. It can jump over other pieces.
        #Rule3] A piece of side X (Black or White) cannot move to a location occupied by a piece of side X.

        if  (abs(pos_X-self.pos_x)==2 and abs(pos_Y-self.pos_y)==1):
            return True

        elif (abs(pos_Y-self.pos_y)==2 and abs(pos_X-self.pos_x)==1):
            return True

        else:
            return False

    def can_move_to(self, pos_X : int, pos_Y : int, B):
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to all chess rules
        Hints:
        - firstly, check [Rule1] and [Rule3] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule4], use is_check on new board
        '''

        B_copy=copy.deepcopy(B)
        B_copy2=copy.deepcopy(B)

        if not(self.can_reach(pos_X,pos_Y, B)):
            return False

        else:
            if is_piece_at(pos_X, pos_Y, B_copy):
                p3=piece_at(pos_X, pos_Y, B_copy)
                if self.side!=p3.side:
                    B_copy[1].remove(p3)

                    self_copy=piece_at(self.pos_x,self.pos_y,B_copy)
                    self_copy.pos_x=pos_X
                    self_copy.pos_y=pos_Y
                    if not is_check(self_copy.side,B_copy):
                        return True
                    else:
                        return False


                else:
                    return False

            else:
                self_copy2=piece_at(self.pos_x,self.pos_y,B_copy2)
                self_copy2.pos_x=pos_X
                self_copy2.pos_y=pos_Y
                if not is_check(self_copy2.side,B_copy2):
                    return True
                else:
                    return False


    def __repr__(self):
        if self.side==True:
            return repr('\u2658')
        if self.side==False:
            return repr('\u265E')


        #[Rule4] A piece of side X cannot make a move, if the configuration resulting from this move is a check for X

       # is_check function(true or false)

    def move_to(self, pos_X : int, pos_Y : int, B):
        '''
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''
        if ((self.can_reach(pos_X, pos_Y, B)) and (self.can_move_to(pos_X, pos_Y, B))):
            if is_piece_at(pos_X, pos_Y, B):
                piece_there=piece_at(pos_X, pos_Y, B)
                B[1].remove(piece_there)
                self.pos_x=pos_X
                self.pos_y=pos_Y
                return B

            else:
                self.pos_x=pos_X
                self.pos_y=pos_Y
                return B









class King(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)


    def can_reach(self, pos_X : int, pos_Y : int, B) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule2] and [Rule3]'''
        if  (abs(pos_X-self.pos_x)==1 and (pos_Y==self.pos_y)):
            return True

        elif (abs(pos_Y-self.pos_y)==1 and (pos_X==self.pos_x)):
            return True

        elif (abs(pos_Y-self.pos_y)==1 and abs(pos_X-self.pos_x)==1):
            return True

        else:
            return False

    def can_move_to(self, pos_X : int, pos_Y : int, B) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        B_copy=copy.deepcopy(B)
        B_copy2=copy.deepcopy(B)
        #1


        if not(self.can_reach(pos_X,pos_Y, B)):
            return False

        else:
            if is_piece_at(pos_X, pos_Y, B_copy):
                p3=piece_at(pos_X, pos_Y, B_copy)
                if self.side!=p3.side:
                    B_copy[1].remove(p3)


                    self_copy=piece_at(self.pos_x,self.pos_y,B_copy)
                    self_copy.pos_x=pos_X
                    self_copy.pos_y=pos_Y
                    if not is_check(self_copy.side,B_copy):
                        return True
                    else:
                        return False


                else:
                    return False

            else:
                self_copy2=piece_at(self.pos_x,self.pos_y,B_copy2)
                self_copy2.pos_x=pos_X
                self_copy2.pos_y=pos_Y
                if not is_check(self_copy2.side,B_copy2):
                    return True
                else:
                    return False

    def __repr__(self):
        if self.side==True:
            return repr('\u2654')
        if self.side==False:
            return repr('\u265A')

    def move_to(self, pos_X , pos_Y , B):
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''

        #if ((self.can_reach(pos_X, pos_Y, B)) and (self.can_move_to(pos_X, pos_Y, B))):
        if ((self.can_reach(pos_X, pos_Y, B)) and (self.can_move_to(pos_X, pos_Y, B))):
            if is_piece_at(pos_X, pos_Y, B):
                piece_there=piece_at(pos_X, pos_Y, B)
                B[1].remove(piece_there)
                self.pos_x=pos_X
                self.pos_y=pos_Y
                return B

            else:
                self.pos_x=pos_X
                self.pos_y=pos_Y
                return B



def is_check(side: bool, B):
    '''
    checks if configuration of B is check for side
    Hint: use can_reach

    1.find the king of side on board B iterating all over the pieces
    2.use can_reach to see if any of the pieces of another side can go to the position of the king
    '''


    for piece in B[1]:
        if type(piece)==King and piece.side==side:
            our_king=piece

    can_reach_counter=0
    cannot_reach_counter=0
    #2:
    for piece9 in B[1]:
        if piece9.side!=our_king.side:

            if not (piece9.can_reach(our_king.pos_x,our_king.pos_y,B)):
                cannot_reach_counter=+1
            else:
                can_reach_counter=+1

    if can_reach_counter>=1:
        return True

    elif  can_reach_counter==0:
        return False




def is_checkmate(side: bool, B) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints:
    - use is_check
    - use can_reach

    1. verify if the current board is (check) for the side
    2.iterate over all our side pices to see if any move can be done to eliminate the (check situation)
    '''

    if not (is_check(side,B)):
        return False


    for piece in B[1]:
            if piece.side==side:
                for x in range(1, B[0]+1):
                    for y in range(1, B[0]+1):
                        if piece.can_move_to(x,y,B):
                            return False



    return True


def is_stalemate(side: bool, B) -> bool:
    '''
    checks if configuration of B is stalemate for side

    Hints:
    - use is_check
    - use can_move_to
    '''
    side_pieces=[]
    cannot_move_counter=0
    if not(is_check(side,B)):
        for piece in B[1]:
            if piece.side==side:
                side_pieces.append(piece)
                for x in range(1, B[0]+1):
                    for y in range(1, B[0]+1):
                        if not(piece.can_move_to(x,y,B)):
                            cannot_move_counter=+1
        if cannot_move_counter==len(side_pieces):
            return True
        else:
            return False

    else:
        return False


def read_board(filename: str): #-> #Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''
    try:
        f = open(filename, "r")
    except IOError as my_error:
        print("File is not valid :", my_error)


    list_of_pieces = []
    B_strings = f.readlines()
    white_piece_strs = B_strings[1].strip().split(', ')
    for wpiece_str in white_piece_strs:
        if wpiece_str[0] == "K":
            wkcoords = location2index(wpiece_str[1:])
            wnew_king = King(wkcoords[0], wkcoords[1] , True)
            list_of_pieces.append(wnew_king)
        elif wpiece_str[0] == "N":
            wncoords = location2index(wpiece_str[1:])
            wnew_knight = Knight(wncoords[0], wncoords[1] , True)
            list_of_pieces.append(wnew_knight)

    black_piece_strs = B_strings[2].strip().split(', ')
    for bpiece_str in black_piece_strs:
        if bpiece_str[0] == "K":
            bkcoords = location2index(bpiece_str[1:])
            bnew_king = King(bkcoords[0], bkcoords[1] , False)
            list_of_pieces.append(bnew_king)
        elif bpiece_str[0] == "N":
            bncoords = location2index(bpiece_str[1:])
            bnew_knight = Knight(bncoords[0], bncoords[1] , False)
            list_of_pieces.append(bnew_knight)
    f.close()
    B=(int(B_strings[0]), list_of_pieces)

    return B



def save_board(filename: str, B) -> None:
    '''saves board configuration into file in current directory in plain format'''

    j=[]
    whites=[]
    black=[]
    R=str(B[0])

    for piece in B[1]:
        if type(piece)==King and piece.side==True:
            wloc=index2location(piece.pos_x,piece.pos_y)
            piece_name='K'+wloc
            whites.append(piece_name)

        if type(piece)==Knight and piece.side==True:
            wloc=index2location(piece.pos_x,piece.pos_y)
            piece_name='N'+wloc
            whites.append(piece_name)

        if type(piece)==King and piece.side==False:
            bloc=index2location(piece.pos_x,piece.pos_y)
            piece_name='K'+bloc
            black.append(piece_name)

        if type(piece)==Knight and piece.side==False:
            bloc=index2location(piece.pos_x,piece.pos_y)
            piece_name='N'+bloc
            black.append(piece_name)



    whites_s=', '.join(whites)
    black_s=', '.join(black)



    j.append(R)
    j.append(whites_s)
    j.append(black_s)


    with open(filename, 'w') as f:
        for line in j:
            f.write(line)
            f.write('\n')


    f.close()


def find_black_move(B) -> tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules
    assumes there is at least one black piece that can move somewhere

    Hints:
    - use methods of random library
    - use can_move_to
    '''
    black_pieces=[]

    for y in range (1,B[0]+1):
        for x in range (1,B[0]+1):
            for piece in range (len(B[1])):
                if B[1][piece].side==False:
                    if B[1][piece].can_move_to(x,y,B):
                        black_pieces.append((B[1][piece],x,y))

    random_no3 = random.randint(0, len(black_pieces)-1)
    return tuple(black_pieces[random_no3])





def conf2unicode(B) -> str:
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''
    matrix= []
    for y in range(B[0],0,-1):
        a = []
        for x in range(B[0]+1):
                a.append('\u2001')
                if is_piece_at(x, y, B):
                        p6=piece_at(x, y, B)

                        a.append(p6)

        matrix.append(a)


    for i in matrix:
        print ('\u2001'.join(map(str, i)))#making every i in matrix to be string


def main() -> None:
    '''
    runs the play
    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    '''
    filename=input ('File name for initial configuration: ')


    while not (os.path.isfile(filename)):
        if filename=='QUIT':
            break
        filename=input ('This is not a valid file. File name for initial configuration:')
    if os.path.exists(filename):
            B=read_board(filename)
            conf2unicode(B)

            while not (is_checkmate(False,B) or is_checkmate(True,B) or is_stalemate(False,B) or is_stalemate(True,B)):
                next_move=input('Next move of White: ')
                if next_move=='QUIT':
                    save_file_name=input('File name to store the configuration: ')
                    save_board(save_file_name, B)
                    print('The game configuration saved.')
                    break

                while len(next_move)!=4:
                    next_move=input('This is not a valid move. Next move of White: ')


                from_point=location2index(next_move[0:2])
                to_point=location2index(next_move[2:])

                piece=piece_at(from_point[0],from_point[1],B)

                while not(is_piece_at(from_point[0],from_point[1],B)):
                    next_move=input('This is not a valid move. Next move of White: ')
                    if next_move=='QUIT':
                        save_file_name=input('File name to store the configuration: ')
                        save_board(save_file_name, B)
                        print('The game configuration saved.')
                        break
                    from_point=location2index(next_move[0:2])
                    to_point=location2index(next_move[2:])
                    piece=piece_at(from_point[0],from_point[1],B)

                while not(piece.can_move_to(to_point[0],to_point[1],B)):
                    next_move=input('This is not a valid move. Next move of White: ')
                    if next_move=='QUIT':
                        save_file_name=input('File name to store the configuration: ')
                        save_board(save_file_name, B)
                        print('The game configuration saved.')
                        break

                    from_point=location2index(next_move[0:2])
                    to_point=location2index(next_move[2:])
                    piece=piece_at(from_point[0],from_point[1],B)


                while (piece.can_move_to(to_point[0],to_point[1],B)):
                    if next_move=='QUIT':
                        save_file_name=input('File name to store the configuration: ')
                        save_board(save_file_name, B)
                        print('The game configuration saved.')
                        break
                    B= piece.move_to(to_point[0],to_point[1],B)
                    print("The configuration after White's move is:")
                    conf2unicode(B)
                    if is_checkmate(False,B):
                        print ('Game over. White wins.')
                        break
                    elif is_stalemate(False,B):
                        print ('Game over. Stalemate.')
                        break
                    black_move=find_black_move(B)
                    black_from=index2location(black_move[0].pos_x, black_move[0].pos_y)
                    black_to=index2location(black_move[1], black_move[2])
                    valid_black_move=black_from+black_to
                    B= black_move[0].move_to(black_move[1],black_move[2],B)
                    print ('Next move of Black is ', valid_black_move,'The configuration after Black s move is: ')
                    conf2unicode(B)
                    if is_checkmate(True,B):
                        print ('Game over. black wins.')
                        break
                    elif is_stalemate(True,B):
                        print ('Game over. Stalemate.')
                        break


if __name__ == '__main__': #keep this in
   main()
