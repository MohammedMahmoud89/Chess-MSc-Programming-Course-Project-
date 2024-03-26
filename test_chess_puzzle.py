import pytest
from chess_puzzle import *


def test_locatio2index1():
    assert location2index("e2") == (5,2)

def test_locatio2index2():
    assert location2index("e1") == (5,1)

def test_locatio2index3():
    assert location2index("a5") == (1,5)

def test_locatio2index4():
    assert location2index("c3") == (3,3)                

def test_locatio2index5():
    assert location2index("a1") == (1,1) 


def test_index2location1():
    assert index2location(5,2) == "e2"

def test_index2location2():
    assert index2location(5,1) == "e1"

def test_index2location3():
    assert index2location(1,5) == "a5"    

def test_index2location4():
    assert index2location(3,3) == "c3"

def test_index2location5():
    assert index2location(3,2) == "c2"



wn1 = Knight(1,2,True)
wn2 = Knight(5,2,True)
wn3 = Knight(5,4, True)
wk1 = King(3,5, True)

bn1 = Knight(1,1,False)
bk1 = King(2,3, False)
bn2 = Knight(2,4, False)

B1 = (5, [wn1, bn1, wn2, bn2, wn3, wk1, bk1])
'''
  ♔  
 ♞  ♘
 ♚   
♘   ♘
♞    
'''

def test_is_piece_at1():
    assert is_piece_at(2,2, B1) == False

def test_is_piece_at2():
    assert is_piece_at(1,1, B1) == True

def test_is_piece_at3():
    assert is_piece_at(5,5, B1) == False

def test_is_piece_at4():
    assert is_piece_at(2,4, B1) == True

def test_is_piece_at5():
    assert is_piece_at(4,5, B1) == False





def test_piece_at1():
    assert piece_at(1,1, B1) == bn1

def test_piece_at2():
    assert piece_at(2,3, B1) == bk1

def test_piece_at3():
    assert piece_at(5,2, B1) == wn2

def test_piece_at4():
    assert piece_at(2,4, B1) == bn2

def test_piece_at5():
    assert piece_at(5,4, B1) == wn3



def test_can_reach1():
    assert bn1.can_reach(2,2, B1) == False

def test_can_reach2():
    assert bn1.can_reach(2,3, B1) == True

def test_can_reach3():
    assert bk1.can_reach(2,2, B1) == True

def test_can_reach4():
    assert wn2.can_reach(2,2, B1) == False

def test_can_reach5():
    assert wn3.can_reach(4,2, B1) == True



def test_can_move_to1():
    assert wk1.can_move_to(4,5, B1) == False

def test_can_move_to2():
    assert wn1.can_move_to(3,3, B1) == True

def test_can_move_to3():
    assert wn2.can_move_to(4,2, B1) == False

def test_can_move_to4():
    assert wn3.can_move_to(4,4, B1) == False

def test_can_move_to5():
    assert bn1.can_move_to(3,2, B1) == True


def test_move_to1():
    Actual_B = wn1.move_to(2,4, B1)
    wn1a = Knight(2,4,True)
    Expected_B = (5, [wn1a, bn1, wn2, wn3, wk1, bk1]) 
    '''
      ♔   
     ♘  ♘
     ♚   
        ♘
    ♞    
    '''

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found



def test_move_to2():
    Actual_B2 = wn2.move_to(4,4, B1)
    wn2a = Knight(4,4,True)
    Expected_B2 = (5, [wn2a, bn1, wn3, wk1, bk1, bn2, wn1]) 
    
    #check if actual board has same contents as expected 
    assert Actual_B2[0] == 5
    for piece1 in Actual_B2[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B2[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found
    for piece in Expected_B2[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B2[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found

def test_move_to3():
    Actual_B3 = wk1.move_to(2,5, B1)
    wk1a = King(2,5,True)
    Expected_B3 = (5, [wk1a, bn1, wn3, wn2, bk1, bn2, wn1]) 
   
    #check if actual board has same contents as expected 
    assert Actual_B3[0] == 5
    for piece1 in Actual_B3[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B3[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found
    for piece in Expected_B3[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B3[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found

def test_move_to4():
    Actual_B4 = wn3.move_to(3,3, B1)
    wn3a = Knight(3,3,True)
    Expected_B4 = (5, [wn3a, bn1, wn2, bk1, bn2, wn1, wk1]) 
    
    #check if actual board has same contents as expected 
    assert Actual_B4[0] == 5
    for piece1 in Actual_B4[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B4[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found
    for piece in Expected_B4[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B4[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found













def test_is_check1():
    wk1a = King(4,5,True)
    B2 = (5, [wn1, bn1, wn2, bn2, wn3, wk1a, bk1])
    '''
       ♔  
     ♞  ♘
     ♚   
    ♘   ♘
    ♞    
    '''
    
    assert is_check(True, B2) == True


def test_is_check2():
    wk1a = King(3,2,True)
    B2 = (5, [wn1, bn1, wn2, bn2, wn3, wk1a, bk1])
    '''
       
     ♞  ♘
     ♚   
    ♘ ♔  ♘
    ♞    
    '''
    assert is_check(True, B2) == True


def test_is_check3():
    wk1a = King(2,4,True)
    B2 = (5, [wn1, bn1, wn2, wn3, wk1a, bk1])
    '''
       
     ♔  ♘
     ♚   
    ♘   ♘
    ♞    
    '''
    assert is_check(True, B2) == True


def test_is_check4():
    wk1 = King(3,5,True)
    wn2a = Knight(3,3,True)
    bk1a = King(3,4,False)
    B2 = (5, [wn1, bn1, wn2a, bn2, wn3, wk1, bk1a])
    '''
      ♔  
     ♞♚  ♘
      ♘  
    ♘   
    ♞    
    '''    
    assert is_check(True, B2) == True


def test_is_check5():
    wk1a = King(2,5,True)
    B2 = (5, [wn1, bn1, wn2, bn2, wn3, wk1a, bk1])
    '''
     ♔  
     ♞  ♘
     ♚   
    ♘   ♘
    ♞    
    '''
    assert is_check(True, B2) == False



def test_is_checkmate1():
    wk1a = King(1,5,True)
    bn2a = Knight(3,4, False)
    bn3 = Knight(4,4,False)
    B2 = (5, [wn1, wn2, wn3, wk1a, bn1, bk1, bn2a, bn3])
  
    '''
    ♔    
      ♞♞♘
     ♚   
    ♘   ♘
    ♞    
    '''
    assert is_checkmate(True, B2) == True



def test_is_checkmate2():
    wn1b = Knight(2,5,True)
    wn2b = Knight(1,4,True)
    wn3b = Knight(1,2, True)
    wk1b = King(5,5, True)
    bn1b = Knight(1,5,False)
    bk1b = King(4,3, False)
    bn2b = Knight(3,4, False)    
    bn3b = Knight(2,4,False)
    B2 = (5, [wn1b, wn2b, wn3b, wk1b, bn1b, bk1b, bn2b, bn3b])
    '''
           ♔    
   ♘ ♞♞ ♚      
   ♘     ♘
           ♞    
    '''
    assert is_checkmate(True, B2) == True

def test_is_checkmate3():
    wn1b = Knight(1,5,True)
    wn2b = Knight(1,4,True)
    wn3b = Knight(5,4, True)
    wk1b = King(5,1, True)
    bn1b = Knight(3,2,False)
    bk1b = King(4,3, False)
    bn2b = Knight(4,5, False)    
    bn3b = Knight(2,2,False)
    B2 = (5, [wn1b, wn2b, wn3b, wk1b, bn1b, bk1b, bn2b, bn3b])
    '''
   ♘    ♞         
   ♘       ♘
         ♚      
     ♞♞  
            ♔       
    '''
    assert is_checkmate(True, B2) == True


def test_is_checkmate4():
    wn1b = Knight(1,5,True)
    wn2b = Knight(1,4,True)
    wn3b = Knight(5,5, True)
    wk1b = King(1,1, True)
    bn1b = Knight(4,5,False)
    bk1b = King(2,3, False)
    bn2b = Knight(3,2, False)    
    bn3b = Knight(4,2,False)
    B2 = (5, [wn1b, wn2b, wn3b, wk1b, bn1b, bk1b, bn2b, bn3b])
    '''
   ♘   ♞  ♘       
   ♘       
    ♚      
      ♞♞  
   ♔       
    '''
    assert is_checkmate(True, B2) == True



def test_is_checkmate5():
    wn1b = Knight(1,5,True)
    wn2b = Knight(1,4,True)
    wn3b = Knight(5,5, True)
    wk1b = King(1,1, True)
    bn1b = Knight(4,5,False)
    bk1b = King(2,3, False)
    bn2b = Knight(4,2, False)    
    bn3b = Knight(5,2,False)
    B2 = (5, [wn1b, wn2b, wn3b, wk1b, bn1b, bk1b, bn2b, bn3b])
    '''
   ♘   ♞  ♘       
   ♘       
    ♚      
      ♞♞  
   ♔       
    '''
    assert is_checkmate(True, B2) == False





def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5

    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found



def test_read_board2():
    wn1 = Knight(5,1,True)
    wn2 = Knight(3,1,True)
    wn3 = Knight(4,3, True)
    wk1 = King(1,5, True)

    bn1 = Knight(2,3,False)
    bk1 = King(5,5, False)
    bn2 = Knight(3,5, False)

    B1 = (5, [wn1, bn1, wn2, bn2, wn3, wk1, bk1])
    
    B = read_board("board_examp2.txt")
    assert B[0] == 5

    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found


def test_read_board3():
    wn1 = Knight(5,1,True)
    wn2 = Knight(3,1,True)
    wn3 = Knight(4,3, True)
    wk1 = King(1,1, True)

    bn1 = Knight(2,3,False)
    bk1 = King(3,3, False)
    bn2 = Knight(3,5, False)

    B1 = (5, [wn1, bn1, wn2, bn2, wn3, wk1, bk1])
    
    B = read_board("board_examp3.txt")
    assert B[0] == 5

    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found


def test_read_board4():
    wn1 = Knight(5,1,True)
    wn2 = Knight(4,5,True)
    wn3 = Knight(4,3, True)
    wk1 = King(1,1, True)

    bn1 = Knight(1,5,False)
    bk1 = King(3,3, False)
    bn2 = Knight(3,5, False)

    B1 = (5, [wn1, bn1, wn2, bn2, wn3, wk1, bk1])
    
    B = read_board("board_examp4.txt")
    assert B[0] == 5

    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found



def test_read_board5():
    wn1 = Knight(1,3,True)
    wn2 = Knight(5,4,True)
    wn3 = Knight(4,1, True)
    wk1 = King(2,1, True)

    bn1 = Knight(4,3,False)
    bk1 = King(3,3, False)
    bn2 = Knight(3,1, False)

    B1 = (5, [wn1, bn1, wn2, bn2, wn3, wk1, bk1])
    
    B = read_board("board_examp5.txt")
    assert B[0] == 5

    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
                assert found


def test_is_stalemate1():
    
    wk1 = King(1,1, True)
    bn1 = Knight(4,2,False)
    bk1 = King(2,3, False)
    B1 = (5, [bn1, wk1, bk1])
    assert is_stalemate(True, B1) == True

def test_is_stalemate2():
    
    wk1 = King(5,5, True)
    bn1 = Knight(2,4,False)
    bk1 = King(4,3, False)
    B1 = (5, [bn1, wk1, bk1])
    assert is_stalemate(True, B1) == True


def test_is_stalemate3():
    
    wk1 = King(3,1, True)
    bn1 = Knight(1,3,False)
    bk1 = King(3,3, False)
    bn2 = Knight(5,3,False)
    B1 = (5, [bn1, wk1, bk1, bn2])
    assert is_stalemate(True, B1) == True

def test_is_stalemate4():
    
    wk1 = King(3,2, True)
    bn1 = Knight(1,3,False)
    bk1 = King(3,5, False)
    bn2 = Knight(5,3,False)
    B1 = (5, [bn1, wk1, bk1, bn2])
    assert is_stalemate(True, B1) == False


def test_is_stalemate5():
    
    wk1 = King(2,1, True)
    bn1 = Knight(1,3,False)
    bk1 = King(1,5, False)
    B1 = (5, [bn1, wk1, bk1])
    assert is_stalemate(True, B1) == False     