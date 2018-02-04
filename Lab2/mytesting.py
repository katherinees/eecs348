import copy
import random
import konane as kb

class player:
    def __init__(self, b,s,depth,algo):
        self.b = b                  # board to be played for test
        self.s = s                  # save 'x' or 'o' designation
        self.depth = depth          # maximum depth for search (in number fo plies)
        self.algo = algo            # name of algorithm for player
        self.prior_move = 'L'       # helper variable for first/last deterministic player algo

    # should not be needed for autograder, but include to help development
    def makeFirstMove(self,r,c):
        self.b.firstMove(self.s,r,c)

    # returns list of available moves for player as list of [[x_from][y_from],[x_to][y_to]] items
    def getNextMoves(self):
        return(self.b.possibleNextMoves(self.s))

    # makes move specified by move expressed as [[x_from][y_from],[x_to][y_to]]
    def makeNextMove(self,move):
        self.b.nextMove(self.s,move)

    ######
    # next few methods get the next move for each of the available algorithms

    # get the first move of the list of available moves
    def getFirstMove(self):
        moves = self.b.possibleNextMoves(self.s)
        return moves[0]

    # alternative between taking the first and last available move
    def getFirstLastMove(self):
        moves = self.b.possibleNextMoves(self.s)
        if self.prior_move == 'L':
            move = moves[0]
            self.prior_move = 'F'
        else:
            move = moves[len(moves)-1]
            self.prior_move = 'L'
        return move

    # randomly choose one of the available moves
    def getRandomMove(self):
        moves = self.b.possibleNextMoves(self.s)
        selected = random.randint(0,len(moves)-1)
        return moves[selected]

    # ask a human player for a move
    def getHumanMove(self):
        print "Possible moves:" , self.b.possibleNextMoves(self.s)
        origin = self._promptForPoint("Choose a piece to move (in the format 'row column'): ")
        destination = self._promptForPoint("Choose a destination for (%s, %s) -> " % (origin[0], origin[1]))
        if (origin, destination) in self.b.possibleNextMoves(self.s):
            return (origin, destination)
        else:
            print "Invalid move.", (origin, destination)
            return self.getHumanMove()

    # help for prompting human player
    def _promptForPoint(self, prompt):
        raw = raw_input(prompt)
        (r, c) = raw.split()
        return (int(r), int(c))

    # minimax algorithm to be completed by students
    # note: you may add parameters to this function call
    def getMinimaxMove(self):
        ######################
        ##  Put codes here  ##
        ######################
        return



    # alphabeta algorithm to be completed by students
    # note: you may add parameters to this function call
    def getAlphaBetaMove(self):
        ######################
        ##  Put codes here  ##
        ######################
        return


    def opposite(self,s):
        if s == 'x':
            return 'o'
        else:
            return 'x'

    def heuristic(self, board, player):
        score = len(board.possibleNextMoves(self.s)) - len(board.possibleNextMoves(self.opposite(self.s))) + \
            int(board.state[0][0]==self.s) + \
            int(board.state[0][board.size-1]==self.s) + \
            int(board.state[board.size-1][0]==self.s) + \
            int(board.state[board.size-1][board.size-1]==self.s)
        #print "heuristic", board, player, score
        return score

    # member function called by test() which specifies move to be made for player's turn, with move
    # expressed as [[x_from][y_from],[x_to][y_to]]
    # if no moves available, return Python 'None' value
    def takeTurn(self):
        moves = self.b.possibleNextMoves(self.s)

        # return Python 'None' if no moves available
        if len(moves) == 0:
            return [True,None]

        if self.algo == 'First Move':  # select first avaliable move
            move = self.getFirstMove()

        if self.algo == 'First/Last Move':  # alternate first and last moves
            move = self.getFirstLastMove()

        if self.algo == 'Random':  # select random move Note: not determinisic, just used to exercise code
            move = self.getRandomMove()

        if self.algo == 'MiniMax':  # player must select best move based upon MiniMax algorithm
            move = self.getMinimaxMove()

        if self.algo == 'AlphaBeta':  # player must select best move based upon AlphaBeta algorithm
            move = self.getAlphaBetaMove()

        if self.algo == 'Human':
            move = self.getHumanMove()

        # makes move on board being used for evaluation
        self.makeNextMove(move)
        return [False,move]

# sample boards used for evaluation of student implementations

boardA = [[' ',' ','x','o'],
          ['o','x','o','x'],
          ['x','o','x','o'],
          ['o','x','o','x']]

boardB = [['x','o','x','o'],
          ['o',' ',' ','x'],
          ['x','o','x','o'],
          ['o','x','o','x']]

boardC = [['x','o','x','o','x','o'],
          ['o','x','o','x','o','x'],
          ['x','o','x','o','x','o'],
          ['o','x',' ',' ','o','x'],
          ['x','o','x','o','x','o'],
          ['o','x','o','x','o','x']]

# 'gold' sequences of moves that students' implementations must match

ans1 = [((2, 1), (0, 1)), ((2, 3), (2, 1))]

ans2 = [((3, 5), (3, 3)), ((4, 2), (2, 2)),
        ((1, 3), (1, 1)), ((4, 4), (2, 4)),
        ((5, 5), (3, 5)), ((5, 3), (5, 5)),
        ((5, 1), (5, 3)), ((4, 0), (4, 2)),
        ((3, 1), (1, 1)), ((4, 2), (2, 2)),
        ((2, 2), (2, 0))]

ans3 = [((3, 5), (3, 3)), ((4, 2), (2, 2)),
        ((1, 3), (1, 1)), ((4, 4), (2, 4)),
        ((5, 5), (3, 5)), ((5, 3), (5, 5)),
        ((3, 1), (1, 1)), ((4, 0), (4, 2)),
        ((4, 2), (2, 2)), ((2, 2), (2, 0)),
        ((2, 4), (2, 2)), ((2, 2), (2, 4))]

# specification of boards, gold sequences and game parameters used to test student code
game1 = [copy.deepcopy(boardA),ans1,100,5,'First Move','MiniMax','o']
game2 = [copy.deepcopy(boardC),ans2,100,5,'First Move','MiniMax','x']
game3 = [copy.deepcopy(boardC),ans2,100,5,'First Move','AlphaBeta','x']
game4 = [copy.deepcopy(boardC),ans3,100,7,'First Move','AlphaBeta','x']

verbose = True # flag to control level of debugging output

def test(board,max_moves,depth,algoG,algoS,student_xo):

    moves_x = []
    moves_o = []

    b = kb.KonaneBoard(board)

    # instantiates student and grader players based upon students' 'x' or 'o' designation
    if student_xo == 'x':
        player_x = player(b,'x',depth,algoS)
        player_o = player(b,'o',depth,algoG)
    else:
        player_o = player(b,'o',depth,algoS)
        player_x = player(b,'x',depth,algoG)

    # displays paramters of specific game used for evaluation
    if verbose:
        print('Konane Test Game')
        print('  Grader Algorithm:   %s' % algoG)
        print('  Student Algorithm:  %s' % algoS)
        print('  Student Playing as: %s' % student_xo)
        print('  Maximum Moves:      %d' % max_moves)
        print('  Maximum Depth:      %d' % depth)
        print('  Boards:')
        print(b)

    # players continue to alternate turns until gameover or maximum moves reached
    done = False
    while not done and len(moves_o) < max_moves:
        [done,move] = player_x.takeTurn()
        moves_x.append(move)
        if done:
            if verbose:
                print 'PlayerX moved', move
                print(b)
                print('PlayerO WINS!!!')
        else:
            if verbose:
                print 'PlayerX moved', move
                print(b)
            [done,move] = player_o.takeTurn()
            moves_o.append(move)
            if done:
                if verbose:
                    print 'PlayerO moved', move
                    print(b)
                    print('PlayerX WINS!!!')
            else:
                if verbose:
                    print 'PlayerO moved', move
                    print(b)

    if verbose:
        print('Game Over.')

    # returns appropriate list of moves based upon player's 'x' or 'o' designation
    if student_xo == 'x':
        return(moves_x)
    else:
        return(moves_o)

game1 = [copy.deepcopy(boardA),ans1,100,5,'First Move','MiniMax','o']
board =     game1[0][:]
gold =      game1[1]
max_moves = game1[2]
depth =     game1[3]
algoS =     game1[4]
algoG =     game1[5]
xo =        game1[6]
# test(board,max_moves,depth,algoS,algoG,xo)
b = kb.KonaneBoard(copy.deepcopy(boardA))
kath = player(b, 'x', 5, "MiniMax")
li = kath.getNextMoves()
print li[0]
foo = kath.heuristic(b, 'x')
print foo
kath.makeNextMove(li[0])
print b
