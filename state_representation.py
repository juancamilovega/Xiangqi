from gametree import *
from pieces import *

class Gamestate(object):
    def __init__(self,pieces_true,pieces_false,turn,previous_piece,new_piece):
        self.t_pieces=pieces_true#pieces of the true player is an array of Piece objects
        self.turn=turn#defines if it is player True or False's turn,
                      #player True tries to maximize value, False minimizes value
        self.f_pieces=pieces_false
        self.move=(previous_piece,new_piece)#the original piece that was moved
        self.won=self.__pincus_winner__()
        self.grid=self.__make_grid__()
    def successors(self):
        successor=list()
        if self.turn:
            for i in range(len(self.t_pieces)):
                for (possibility,eliminate_name) in self.t_pieces[i].successors(self.grid):
                    new_pieces=self.t_pieces[:]#shallow copy means a new array but
                                                #with pointers to the same old objects
                    new_pieces[i]=possibility
                    f_pieces=self.f_pieces
                    if eliminate !=None:
                        f_pieces=self.f_pieces[:]
                        for piece in f_pieces:
                            if piece.name==eliminate:
                                f_pieces.remove(piece)
                    successor.append(Gamestate(new_pieces,f_pieces,False,self.t_pieces[i],possiblity))
        else:
            for i in range(len(self.f_pieces)):
                for (possibility,eliminate) in self.f_pieces[i].successors(self.grid):
                    new_pieces=self.f_pieces[:]#shallow copy means a new array but
                                                #with pointers to the same old objects
                    if eliminate !=None:
                        t_pieces=self.t_pieces[:]
                        for piece in t_pieces:
                            if piece.name==eliminate:
                                t_pieces.remove(piece)
                    new_pieces[i]=possibility
                    successor.append(Gamestate(t_pieces,new_pieces,True,self.f_pieces[i],possibility))
        return successor
    def value(self):
        #change if we want to add another heuristic
        val_T=0
        val_F=0
        if self.won!=0:
            return self.won*float("inf")
        elif self.won==2:
            return -float("inf")
        for piece in self.t_pieces:
            val_T+=piece.get_value()
        for piece in self.f_pieces:
            val_F+=piece.get_value()
        return val_T/val_F #the more pieces we lose, the more valuable the ones we have
                           #are. The more pieces the oponent loses, the more value the ones he has.
    def __make_grid__(self):
        '''
        makes a GameGrid matrix using all the pieces names
        '''
        grid=[[0]*9]*10
        for piece in self.t_pieces+self.f_pieces:
            grid[piece.pos.x][piece.pos.y]=piece.name
        return grid
    def __pincus_winner__(self):
        #returns 1 if player True won, returns -1 if player False won, returns 0 if
        #game continues
        flag_True=0
        for piece in self.t_pieces:
            if type(piece)==General:
                flag_True=1
                break
        if flag_True==0:
            return -1
        for piece in self.f_pieces:
            if type(piece)==General:
                return 0
        return 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
