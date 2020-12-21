import random

def printBoard(board):
    print("---------")
    print('|', board['1'], board['2'], board['3'], '|')
    # print('-+-+-')
    print('|', board['4'], board['5'], board['6'], '|')
    # print('-+-+-')
    print('|', board['7'], board['8'], board['9'], '|')
    print("---------")

def board_check(theBoard, user_in):
    coordinate = [[1,1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
    for index, cord in enumerate(coordinate):
        if cord == user_in: # board position loop through
            if theBoard[str(index + 1)] == "_":
                result = True
            else:
                result = False
    return result

def board_update(theBoard, user_in, turn):
    coordinate = [[1,1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
    for index, cord in enumerate(coordinate):
        if cord == user_in: # board position loop through
            theBoard[str(index + 1)] = turn

    return theBoard

def win_condition(theBoard):
    # win conditions
    x_check = bool
    o_check = bool
    if theBoard["1"] == theBoard["2"] == theBoard["3"] !="_":
        if theBoard["1"] == "X":
            print("X wins")
            x_check = True

        elif theBoard["1"] == "O":
            print("O wins")
            o_check = True

    elif theBoard["4"] == theBoard["5"] == theBoard["6"] !="_":
        if theBoard["4"] == "X":
            print("X wins")
            x_check = True

        elif theBoard["4"] == "O":
            print("O wins")
            o_check = True


    elif theBoard["7"] == theBoard["8"] == theBoard["9"] !="_":
        if theBoard["7"] == "X":
            print("X wins")
            x_check = True

        elif theBoard["7"] == "O":
            print("O wins")
            o_check = True

    elif theBoard["1"] == theBoard["4"] == theBoard["7"] !="_":
        if theBoard["1"] == "X":
            print("X wins")
            x_check = True

        elif theBoard["1"] == "O":
            print("O wins")
            o_check = True

    elif theBoard["2"] == theBoard["5"] == theBoard["8"] !="_":
        if theBoard["2"] == "X":
            print("X wins")
            x_check = True
        elif theBoard["2"] == "O":
            print("O wins")
            o_check = True

    elif theBoard["3"] == theBoard["6"] == theBoard["9"] !="_":
        if theBoard["3"] == "X":
            print("X wins")
            x_check = True

        elif theBoard["3"] == "O":
            print("O wins")
            o_check = True

    elif theBoard["1"] == theBoard["5"] == theBoard["9"] !="_":
        if theBoard["1"] == "X":
            print("X wins")
            x_check = True

        elif theBoard["1"] == "O":
            print("O wins")
            o_check = True

    elif theBoard["7"] == theBoard["5"] == theBoard["3"] !="_":
        if theBoard["7"] == "X":
            print("X wins")
            x_check = True

        elif theBoard["7"] == "O":
            print("O wins")
            o_check = True
        
    # draw case
    if "_" not in theBoard.values() and x_check != True and o_check != True:
        print("Draw")
    
    if x_check == True or o_check == True:
        return True

    num_x = []
    num_o = []
    for _, v in theBoard.items():
        if v == "X":
            num_x.append(v)
        elif v == "O":
            num_o.append(v)
    # print(len(num_x))
    # print(len(num_o))
    # print(abs(len(num_x) - len(num_o)))
    if abs(len(num_x) - len(num_o)) > 1 or x_check == True and o_check == True:
        print("Impossible")
    elif "_" in theBoard.values() and x_check != True and o_check != True:
        print("Game not finished")

def win_condition_inside(theBoard):
    # win conditions
    x_check = bool
    o_check = bool
    outcome = None
    if theBoard["1"] == theBoard["2"] == theBoard["3"] !="_":
        if theBoard["1"] == "X":
            x_check = True

        elif theBoard["1"] == "O":
            o_check = True

    elif theBoard["4"] == theBoard["5"] == theBoard["6"] !="_":
        if theBoard["4"] == "X":
            x_check = True

        elif theBoard["4"] == "O":
            o_check = True


    elif theBoard["7"] == theBoard["8"] == theBoard["9"] !="_":
        if theBoard["7"] == "X":
            x_check = True

        elif theBoard["7"] == "O":
            o_check = True

    elif theBoard["1"] == theBoard["4"] == theBoard["7"] !="_":
        if theBoard["1"] == "X":
            x_check = True

        elif theBoard["1"] == "O":
            o_check = True

    elif theBoard["2"] == theBoard["5"] == theBoard["8"] !="_":
        if theBoard["2"] == "X":
            x_check = True
        elif theBoard["2"] == "O":
            o_check = True

    elif theBoard["3"] == theBoard["6"] == theBoard["9"] !="_":
        if theBoard["3"] == "X":
            x_check = True

        elif theBoard["3"] == "O":
            o_check = True

    elif theBoard["1"] == theBoard["5"] == theBoard["9"] !="_":
        if theBoard["1"] == "X":
            x_check = True

        elif theBoard["1"] == "O":
            o_check = True

    elif theBoard["7"] == theBoard["5"] == theBoard["3"] !="_":
        if theBoard["7"] == "X":
            x_check = True

        elif theBoard["7"] == "O":
            o_check = True
        
    # draw case
    if "_" not in theBoard.values() and x_check != True and o_check != True:
        outcome = "draw"
    
    if o_check == True:
        outcome = "robot_win"
    
    if x_check == True:
        outcome = "robot_lose"
    
    return outcome

def move_check(tempBoard, move, turn):
    coordinate = [[1,1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
    for index, cord in enumerate(coordinate):
        if cord == move: # board position loop through
            tempBoard[str(index + 1)] = turn
    
    if win_condition_inside(tempBoard) == "robot_win":
        return "robot_win"

    elif win_condition_inside(tempBoard) == "robot_lose":
        return "robot_lose"

def isTerminal(theBoard):
    
    if win_condition_inside(theBoard) == None:
        return False
    else:
        return True

def minimax(theBoard, turn):
    """ this has to return the utility value, move."""     

    if isTerminal(theBoard):
        if win_condition_inside(theBoard) == "robot_win":  # the turn that created theBoard is "X", but what fed into minimax is the potential next turn
            return -10, 0  # if it's terminal, and the move that got us to terminal is O, it means x lost, thus -1

        elif win_condition_inside(theBoard) == "robot_lose":
            return 10, 0

        elif win_condition_inside(theBoard) == "draw":
            return 0, 0
    
    move_list = []  # this will be all possible moves robot can make
    for k, v in theBoard.items():
        if v == "_":
            move_list.append(k)

    coordinate_conversion = {"1": [1,1], "2": [1, 2], "3": [1, 3], "4": [2, 1], "5": [2, 2], "6": [2, 3], "7": [3, 1], "8": [3, 2], "9": [3, 3]}
    all_possible_move_cord = []  # contain all possible move in x, y coordinates
    for item in move_list:
        all_possible_move_cord.append(coordinate_conversion[str(item)])

    # construct a nested list of utility value, move
    utility_score = {}
    for move in all_possible_move_cord:
        tempBoard = theBoard.copy()  # every recursive call theBoard changes to tempBoard and tempboard updates it to new tempboard
        next_board = board_update(tempBoard, move, turn)  # this gives me the updated board for each possible move, we then update u_val based on whose turn it is
        if turn == "X":
            u_val, p = minimax(next_board, "O")
            utility_score[str(u_val)] = move

        if turn == "O":
            u_val, p = minimax(next_board, "X")
            utility_score[str(u_val)] = move
    
    if turn == "X":
        max_utility = max(list(map(int, utility_score.keys())))
        for k, v in utility_score.items():
            if int(k) == max_utility:
                robot_in = v
                return max_utility, robot_in
    
    if turn == "O":
        min_utility = min(list(map(int, utility_score.keys())))
        for k, v in utility_score.items():
            if int(k) == min_utility:
                robot_in = v
                return min_utility, robot_in
                
class Robot():
    def __init__(self, level):
        self.level = level  # this attribute of the Robot class can be assigned to instances of robot and thus define behavior

    def robot_move(self, theBoard, turn):
        if self.level == "easy":
            robot_in = [random.randint(1, 3), random.randint(1, 3)]
            print('Making move level "easy"')
            return robot_in
        
        elif self.level == "medium":
            move_list = []  # this will be all possible moves robot can make
            for k, v in theBoard.items():
                if v == "_":
                    move_list.append(k)

            corners_set =  ("1", "3", "7", "9")
            corners_set = set(corners_set)
            center_set = ("5")
            center_set = set(center_set)
            edge_set =  ("2", "4", "6", "8")
            edge_set = set(edge_set)

            # I HAVE A LOT OF USELESS CONVERSIONS HERE THAT I REGRET!!!

            # convert to coordinates
            coordinate_conversion = {"1": [1,1], "2": [1, 2], "3": [1, 3], "4": [2, 1], "5": [2, 2], "6": [2, 3], "7": [3, 1], "8": [3, 2], "9": [3, 3]}
            all_possible_move_cord = []  # contain all possible move in x, y coordinates
            for item in move_list:
                all_possible_move_cord.append(coordinate_conversion[str(item)])

            robot_win_cord = []  # all moves that allow robot to win right away
            robot_lose_cord = [] # all moves that prevent player from winning right away

            # these serve as a move classifiers

            for move in all_possible_move_cord:
                tempBoard = theBoard.copy()  # every loop a copy of the original board dict is created to be used to check if move will cause a win or loss
                if move_check(tempBoard, move, "O") == "robot_win":
                    robot_win_cord.append(move)
                
                tempBoard_2 = theBoard.copy()
                if move_check(tempBoard_2, move, "X") == "robot_lose":
                    robot_lose_cord.append(move)
                
            robot_win_set = set()
            for i in robot_win_cord:
                for k, v in coordinate_conversion.items():
                    if i == v:
                        robot_win_set.add(k)

            robot_lose_set = set()
            for i in robot_lose_cord:
                for k, v in coordinate_conversion.items():
                    if i == v:
                        robot_lose_set.add(k)

            all_possible_move_set = set()
            for i in all_possible_move_cord:
                for k, v in coordinate_conversion.items():
                    if i == v:
                        all_possible_move_set.add(k)

            other_move_set = all_possible_move_set - robot_win_set - robot_lose_set
            corner_move_set = other_move_set.intersection(corners_set)
            center_move_set = other_move_set.intersection(center_set)
            edge_move_set = other_move_set.intersection(edge_set)

            # convert to coordinates again
            corner_move_cord = []
            center_move_cord = []
            edge_move_cord = []
            for item in corner_move_set:
                corner_move_cord.append(coordinate_conversion[str(item)])
            for item in center_move_set:
                center_move_cord.append(coordinate_conversion[str(item)])
            for item in edge_move_set:
                edge_move_cord.append(coordinate_conversion[str(item)])

            # I now have 5 lists
            # 1) robot_win_cord contains all moves that allow robot to win right away - this is priority 1
            # 2) robot_lose_cord contains all moves that allow robot to lose right away - this is priority 2
            # 3) center_move_cord contains the center coordinate, which takes priority 3
            # 4) corner_move_cord contains 4 corners, which is better move, priority 4
            # 5) edge_move_cord is the least important, contains 4 edges on the 3x3 block
            # I HAVE A LOT OF USELESS CONVERSIONS HERE THAT I REGRET!!!
            
            if len(robot_win_cord) != 0:
                robot_in = robot_win_cord[0]
            elif len(robot_lose_cord) !=0:
                robot_in = robot_lose_cord[0]
            elif len(center_move_cord) != 0:
                robot_in = center_move_cord[0]
            elif len(corner_move_cord) != 0:
                robot_in = corner_move_cord[0]
            elif len(edge_move_cord) != 0:
                robot_in = edge_move_cord[0]
            else:
                robot_in = random.choice(all_possible_move_cord)
            print('Making move level "medium"')
            return robot_in
        
        elif self.level == "hard":  #minimax algorithm
            u_val, robot_in = minimax(theBoard, turn)
            print('Making move level "hard"')
            return robot_in
        
def start_board():
    user_input = "_________"
    count = 0  # count is used to stop the while loop after 9 valid entries from users
    # user_input = input()  # create original board
    for i in user_input:
        if i == "O" or i == "X":
            count += 1  # this allows count value to start at the number of X or O in the original input, 
            # and then program counts up further until it reaches 9 or a winner is determined
    theBoard = {}
    j = 1
    for i in user_input:
        theBoard[str(j)] = i
        j += 1
    printBoard(theBoard)
    return theBoard, count

def user_AI(robot_easy, theBoard, count, turn="X"):
    while True:
        checker = 0  # checker is used to stop count += 1 when invalid input are provided
        try:
            if turn == "O":
                user_in = robot_easy.robot_move(theBoard, turn)
            else:
                user_in = list(map(int, input().split()))
        except ValueError:
            print("You should enter numbers!")
            continue
        except EOFError:
            break
        else:
            if user_in[0] < 1 or user_in[0] > 3 or user_in[1] < 1 or user_in[1] > 3:
                    print("Coordinates should be from 1 to 3!")
                    checker = 1  # if coordiante isn't entered correctly, program also returns to start of while loop without progressing
            
            elif not board_check(theBoard, user_in):
                print("This cell is occupied! Choose another one!")
                checker = 1  # if the board spot isn't empty, checker = 1 ensures that program returns to start of while loop asking to reenter input
                
            if checker == 0:
                count += 1
            else:
                continue  # go to beginning of while loop without raising count and without defining turn
        
        theBoard = board_update(theBoard, user_in, turn)
        printBoard(theBoard)
        
        if count % 2 != 0:
            turn = "O"
        if count % 2 == 0:
            turn = "X"
        
        if win_condition(theBoard):
            break

        if count == 9:
            win_condition(theBoard)
            break

def user_user(theBoard, count):
    while True:
        checker = 0  # checker is used to stop count += 1 when invalid input are provided
        try:
            user_in = list(map(int, input("Enter the coordinates", ).split()))
        except ValueError:
            print("You should enter numbers!")
            continue
        except EOFError:
            break
        else:
            if user_in[0] < 1 or user_in[0] > 3 or user_in[1] < 1 or user_in[1] > 3:
                    print("Coordinates should be from 1 to 3!")
                    checker = 1  # if coordiante isn't entered correctly, program also returns to start of while loop without progressing
            
            elif not board_check(theBoard, user_in):
                print("This cell is occupied! Choose another one!")
                checker = 1  # if the board spot isn't empty, checker = 1 ensures that program returns to start of while loop asking to reenter input
                
            if checker == 0:
                count += 1
            else:
                continue  # go to beginning of while loop without raising count and without defining turn

        if count % 2 != 0:
            turn = "X"
        if count % 2 == 0:
            turn = "O"

        updated_board = board_update(theBoard, user_in, turn)
        printBoard(updated_board)
        
        if win_condition(updated_board):
            break

        if count == 9:
            win_condition(updated_board)
            break

def AI_AI(robot_1, robot_2, theBoard, count, turn="X"):
    while True:
        checker = 0  # checker is used to stop count += 1 when invalid input are provided
        try:
            if turn == "O":
                user_in = robot_1.robot_move(theBoard, turn)
            else:
                user_in = robot_2.robot_move(theBoard, turn)
        except ValueError:
            print("You should enter numbers!")
            continue
        except EOFError:
            break
        else:
            if user_in[0] < 1 or user_in[0] > 3 or user_in[1] < 1 or user_in[1] > 3:
                    print("Coordinates should be from 1 to 3!")
                    checker = 1  # if coordiante isn't entered correctly, program also returns to start of while loop without progressing
            
            elif not board_check(theBoard, user_in):
                print("This cell is occupied! Choose another one!")
                checker = 1  # if the board spot isn't empty, checker = 1 ensures that program returns to start of while loop asking to reenter input
                
            if checker == 0:
                count += 1
            else:
                continue  # go to beginning of while loop without raising count and without defining turn
        
        theBoard = board_update(theBoard, user_in, turn)
        printBoard(theBoard)
        
        if count % 2 != 0:
            turn = "O"
        if count % 2 == 0:
            turn = "X"
        
        if win_condition(theBoard):
            break

        if count == 9:
            win_condition(theBoard)
            break

def main():
    theBoard, count = start_board()
    robot_1 = Robot("easy")
    robot_2 = Robot("medium")
    robot_3 = Robot("hard")
    while True:
        theBoard_copy = theBoard.copy()
        inp_command = input()
        if inp_command == "start easy user":  # AI vs user
            user_AI(robot_1, theBoard_copy, count)  # play AI with easy robot, count starts at some value based on board state, turn starts at X since user is X start

        elif inp_command == "start user user":  # 2 users
            user_user(theBoard_copy, count)

        elif inp_command == "start easy easy":  # 2 AI
            AI_AI(robot_1, robot_1, theBoard_copy, count)
        
        elif inp_command == "start user medium":
            user_AI(robot_2, theBoard_copy, count)

        elif inp_command == "start medium user":
            user_AI(robot_2, theBoard_copy, count)

        elif inp_command == "start medium medium":
            AI_AI(robot_2, robot_2, theBoard_copy, count)

        elif inp_command == "start hard hard":
            AI_AI(robot_3, robot_3, theBoard_copy, count)

        elif inp_command == "start hard user":
            user_AI(robot_3, theBoard_copy, count)

        elif inp_command == "start user hard":
            user_AI(robot_3, theBoard_copy, count)
        
        elif inp_command == "start hard medium":
            AI_AI(robot_3, robot_2, theBoard_copy, count)

        elif inp_command == "exit":
            break

        else:
            print("Bad parameters")
         
if __name__ == "__main__":
    main()