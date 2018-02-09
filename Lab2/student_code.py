import random
import konane
import copy

# class for individual player.  student and grader players should be identical except for:
#     - implementation of getMinimaxMove() and getAlphabetaMove(), and
#     - any helper functions and/or members implemented by student
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
        # when first called, we're always the maximizing player
        [m, h] = self.findMax(self.b, self.depth, self.s)
        return m

    def findMax(self, current_board, current_depth, side):
        # if depth = 0, or no more moves (terminal move)
        # then just return the heuristic
        moves = current_board.possibleNextMoves(side)
        if (len(moves) == 0):
            h = self.heuristic(current_board, side)
            return [None, h]
        if (current_depth == 0):
            # at max depth, we return the first move (see piazza)
            poss_moves = current_board.possibleNextMoves(side)
            m = poss_moves[0]
            h = self.heuristic(current_board, side)
            return [m, h]

        # initialize best_h and best_move with placeholders
        best_h = float('-Infinity')
        best_move = moves[0]
        # ie for each child node
        for m in moves:
            # get the board of the child node, ie figure out what
            # the board would look like if we did this move
            childboard = copy.deepcopy(current_board)
            childboard.nextMove(side, m)
            opp = self.opposite(side)
            [poss_move, h] = self.findMin(childboard, current_depth-1, opp)
            # using '>' instead of '>=' or 'max' makes sure if there's
            # a tie, we use the order given by possibleNextMoves
            if (h > best_h):
                best_h = h
                best_move = m
        return [best_move, best_h]

    def findMin(self, current_board, current_depth, side):
        # if depth = 0, or no more moves (terminal move)
        # then just return the heuristic
        moves = current_board.possibleNextMoves(side)
        if (len(moves) == 0):
            h = self.heuristic(current_board, side)
            return [None, h]
        if (current_depth == 0):
            # at max depth, we return the first move (see piazza)
            poss_moves = current_board.possibleNextMoves(side)
            m = poss_moves[0]
            h = self.heuristic(current_board, side)
            return [m, h]

        best_h = float('Infinity')
        best_move = moves[0]
        # ie for each child node
        for m in moves:
            childboard = copy.deepcopy(current_board)
            childboard.nextMove(side, m)
            opp = self.opposite(side)
            [poss_move, h] = self.findMax(childboard, current_depth-1, opp)
            if (h < best_h):
                best_h = h
                best_move = m
        return [best_move, best_h]

    def abMax(self, current_board, current_depth, side, alpha, beta):
        # if depth = 0 or no more moves (terminal node)
        moves = current_board.possibleNextMoves(side)
        if (len(moves) == 0):
            h = self.heuristic(current_board, side)
            return [None, h]
        if (current_depth == 0):
            poss_moves = current_board.possibleNextMoves(side)
            m = poss_moves[0]
            h = self.heuristic(current_board, side)
            return [m, h]

        best_h = float('-Infinity')
        best_move = moves[0]
        # for each child node
        for m in moves:
            childboard = copy.deepcopy(current_board)
            childboard.nextMove(side, m)
            opp = self.opposite(side)
            [poss_move, h] = self.abMin(childboard, current_depth-1, opp, alpha, beta)
            if (h > best_h):
                best_h = h
                best_move = m
            if (best_h > alpha):
                alpha = best_h
            if (beta <= alpha):
                # pruning
                break
        return [best_move, best_h]

    def abMin(self, current_board, current_depth, side, alpha, beta):
        # if depth = 0 or no more moves (terminal node)
        moves = current_board.possibleNextMoves(side)
        if (len(moves) == 0):
            h = self.heuristic(current_board, side)
            return [None, h]
        if (current_depth == 0):
            poss_moves = current_board.possibleNextMoves(side)
            m = poss_moves[0]
            h = self.heuristic(current_board, side)
            return [m, h]

        best_h = float('Infinity')
        best_move = moves[0]
        # for each child node
        for m in moves:
            childboard = copy.deepcopy(current_board)
            childboard.nextMove(side, m)
            opp = self.opposite(side)
            [poss_move, h] = self.abMax(childboard, current_depth-1, opp, alpha, beta)
            if (h < best_h):
                best_h = h
                best_move = m
            if (best_h < beta):
                beta = best_h
            if (beta <= alpha):
                break
        return [best_move, best_h]

    # alphabeta algorithm to be completed by students
    # note: you may add parameters to this function call
    def getAlphaBetaMove(self):
        alpha = float('-Infinity')
        beta = float('Infinity')
        [m, h] = self.abMax(self.b, self.depth, self.s, alpha, beta)
        return m


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
