"""
井字棋玩家
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    返回棋盘的初始状态。
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    返回棋盘上该轮到哪个玩家。
    """
    count_x = 0
    count_o = 0
    for row in board:
        for cell in row:
            if cell == X:
                count_x += 1
            elif cell == O:
                count_o += 1

    if count_x == count_o:
        return X
    else:
        return O


def actions(board):
    """
    返回棋盘上所有可能的动作 (i, j) 集合。
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    返回在棋盘上执行动作 (i, j) 后的棋盘状态。
    """
    i, j = action
    if i < 0 or i > 2 or j < 0 or j > 2 or board[i][j] != EMPTY:
        raise ValueError("Invalid action")

    new_board = copy.deepcopy(board)
    current_player = player(board)
    new_board[i][j] = current_player
    return new_board


def winner(board):
    """
    如果游戏有胜者，则返回胜者。
    """
    # 检查行
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
    # 检查列
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]
    # 检查对角线
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    如果游戏结束则返回 True，否则返回 False。
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False  # 棋盘未满且无赢家
    return True  # 棋盘已满


def utility(board):
    """
    如果 X 获胜则返回 1，如果 O 获胜则返回 -1，否则返回 0。
    """
    win_player = winner(board)
    if win_player == X:
        return 1
    elif win_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    返回当前玩家在棋盘上的最优动作。
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    else:  # current_player == O
        best_score = math.inf
        best_action = None
        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action
        return best_action

def max_value(board):
    """
    Helper function for minimax: returns the max utility for the current board.
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    """
    Helper function for minimax: returns the min utility for the current board.
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
