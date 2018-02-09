import copy
import random
import konane as kb
import student_code as student

boardA = [[' ',' ','x','o'],
          ['o','x','o','x'],
          ['x','o','x','o'],
          ['o','x','o','x']]
ans1 = [((0, 3), (0, 1)), ((2, 3), (0, 3)), ((2, 1), (2, 3))]

game1 = [copy.deepcopy(boardA),ans1,100,5,'First Move','MiniMax','o']
board =     game1[0][:]
gold =      game1[1]
max_moves = game1[2]
depth =     game1[3]
algoS =     game1[4]
algoG =     game1[5]
xo =        game1[6]
# test(board,max_moves,depth,algoS,algoG,xo)
# b = kb.KonaneBoard(copy.deepcopy(boardA))
# kath = student.player(b, 'o', 5, "MiniMax")
# mo = student.player(b, 'x', 5, 'First Move')
# print b
# kp = b.possibleNextMoves(kath.s)
# print "kath has these options:", kp
# print "kath does ((0, 3), (0, 1))"
# kath.makeNextMove(((0, 3), (0, 1)))
# print b
# momove = mo.getFirstMove()
# mo.makeNextMove(momove)
# print "mo does", momove
# print b
# kp = b.possibleNextMoves(kath.s)
# print "kath has these options:", kp
# print kath.s, "kath does ((2, 3), (0, 3))"
# kath.makeNextMove(((2, 3), (0, 3)))
# print b
# momove = mo.getFirstMove()
# mo.makeNextMove(momove)
# print "mo does", momove
# print b
# kp = b.possibleNextMoves(kath.s)
# print "kath has these options:", kp
# print kath.s, "kath does ((2, 1), (2, 3))"
# kath.makeNextMove(((2, 1), (2, 3)))
# print b

## ALPHA BETA GOLD
boardC = [['x','o','x','o','x','o'],
          ['o','x','o','x','o','x'],
          ['x','o','x','o','x','o'],
          ['o','x',' ',' ','o','x'],
          ['x','o','x','o','x','o'],
          ['o','x','o','x','o','x']]
ans3 = [((3, 5), (3, 3)), ((4, 2), (2, 2)),
        ((1, 3), (1, 1)), ((3, 3), (1, 3)),
        ((4, 4), (2, 4)), ((5, 5), (3, 5)),
        ((4, 0), (4, 2)), ((2, 0), (4, 0)),
        ((5, 3), (5, 5)), ((4, 2), (4, 4)),
        ((0, 4), (0, 2)), ((4, 0), (4, 2)),
        ((5, 1), (5, 3)), ((4, 2), (4, 4))]
game3 = [copy.deepcopy(boardC),ans3,100,5,'First Move','AlphaBeta','x']
b = kb.KonaneBoard(copy.deepcopy(boardC))

kath = student.player(b, 'x', 5, 'Alpha Beta')
gr = student.player(b, 'o', 5, 'First Move')
print "starting board", b
kp = b.possibleNextMoves(kath.s)
print "kath has these options:", kp
print "kath does ((3, 5), (3, 3))"
