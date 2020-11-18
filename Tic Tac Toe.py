user_input = "_________"
# print(user_input)
theBoard = {}
j = 1
for i in user_input:
    # print(i)
    theBoard[str(j)] = i
    j += 1
    # print(theBoard)

# print(theBoard)

def printBoard(board):
    print("---------")
    print('|', board['1'], board['2'], board['3'], '|')
    # print('-+-+-')
    print('|', board['4'], board['5'], board['6'], '|')
    # print('-+-+-')
    print('|', board['7'], board['8'], board['9'], '|')
    print("---------")

printBoard(theBoard)
i = 1
for i in range(10):
    if int(i) % 2 != 0:
        turn = "X"
    if i % 2 == 0:
        turn = "O"
    user_in = input().split()
    for i in range(0, len(user_in)):
        user_in[i] = int(user_in[i])

# print(user_in)
# print([user_in[0], user_in[1]])
    if type(int(user_in[0])) != int or type(user_in[1]) != int:
        print("You should enter numbers!")
        continue

    elif user_in[0] < 1 or user_in[0]> 3 or user_in[1] < 1 or user_in[1]> 3:
        print("Coordinates should be from 1 to 3!")
        continue

    elif user_in == [1, 3]: #theBoard["1"]
        if theBoard["1"] == "_":
            theBoard["1"] = turn
        else:
            print("This cell is occupied! Choose another one!")
            continue


    elif user_in == [2, 3]: #theBoard["2"]
        if theBoard["2"] == "_":
            theBoard["2"] = turn
        else:
            print("This cell is occupied! Choose another one!")
            continue

    elif [user_in[0], user_in[1]] == [3, 3]: #theBoard["3"]
        if theBoard["3"] == "_":
            theBoard["3"] = turn
        else:
            print("This cell is occupied! Choose another one!")
            continue

    elif [user_in[0], user_in[1]] == [1, 2]: #theBoard["4"]
        if theBoard["4"] == "_":
            theBoard["4"] = turn
        else:
            print("This cell is occupied! Choose another one!")
            continue

    elif [user_in[0], user_in[1]] == [2, 2]: #theBoard["5"]
        if theBoard["5"] == "_":
            theBoard["5"] = turn
        else:
            print("This cell is occupied! Choose another one!")
            continue

    elif [user_in[0], user_in[1]] == [3, 2]: #theBoard["6"]
        if theBoard["6"] == "_":
            theBoard["6"] = turn
        else:
            print("This cell is occupied! Choose another one!")
            continue

    elif [user_in[0], user_in[1]] == [3, 2]: #theBoard["6"]
        if theBoard["6"] == "_":
            theBoard["6"] = turn
        else:
            print("This cell is occupied! Choose another one!")
            continue

    elif [user_in[0], user_in[1]] == [1, 1]: #theBoard["7"]
        # print([user_in[0], user_in[1]]== [1, 1])
        # print(theBoard["7"])
        if theBoard["7"] == "_":
            # print(theBoard["7"] == "_")
            theBoard["7"] = turn
        else:
            print("This cell is occupied! Choose another one!")
            continue

    elif [user_in[0], user_in[1]] == [2, 1]: #theBoard["8"]
        if theBoard["8"] == "_":
            theBoard["8"] = turn
        else:
            print("This cell is occupied! Choose another one!")
            continue

    elif [user_in[0], user_in[1]] == [3, 1]: #theBoard["9"]
        if theBoard["9"] == "_":
            theBoard["9"] = turn
        else:
            print("This cell is occupied! Choose another one!")
            continue
    printBoard(theBoard)
    # win conditions
    x_check = bool
    o_check = bool
    if theBoard["1"] == theBoard["2"] == theBoard["3"] !="_":
        if theBoard["1"] == "X":
            print("X wins")
            x_check = True
            break
        elif theBoard["1"] == "O":
            print("O wins")
            o_check = True
            break
    if theBoard["4"] == theBoard["5"] == theBoard["6"] !="_":
        if theBoard["4"] == "X":
            print("X wins")
            x_check = True
            break
        elif theBoard["4"] == "O":
            print("O wins")
            o_check = True
            break
    if theBoard["7"] == theBoard["8"] == theBoard["9"] !="_":
        if theBoard["7"] == "X":
            print("X wins")
            x_check = True
            break
        elif theBoard["7"] == "O":
            print("O wins")
            o_check = True
            break
    if theBoard["1"] == theBoard["4"] == theBoard["7"] !="_":
        if theBoard["1"] == "X":
            print("X wins")
            x_check = True
            break
        elif theBoard["1"] == "O":
            print("O wins")
            o_check = True
            break
    if theBoard["2"] == theBoard["5"] == theBoard["8"] !="_":
        if theBoard["2"] == "X":
            print("X wins")
            x_check = True
            break
        elif theBoard["2"] == "O":
            print("O wins")
            o_check = True
            break
    if theBoard["3"] == theBoard["6"] == theBoard["9"] !="_":
        if theBoard["3"] == "X":
            print("X wins")
            x_check = True
            break
        elif theBoard["3"] == "O":
            print("O wins")
            o_check = True
            break
    if theBoard["1"] == theBoard["5"] == theBoard["9"] !="_":
        if theBoard["1"] == "X":
            print("X wins")
            x_check = True
            break
        elif theBoard["1"] == "O":
            print("O wins")
            o_check = True
            break
    if theBoard["7"] == theBoard["5"] == theBoard["3"] !="_":
        if theBoard["7"] == "X":
            print("X wins")
            x_check = True
            break
        elif theBoard["7"] == "O":
            print("O wins")
            o_check = True
            break
    # draw case
    if "_" not in theBoard.values() and x_check != True and o_check != True:
        print("Draw")
        break
    # impossible condition
    # print(x_check)
    # print(o_check)
    num_x = []
    num_o = []
    for k, v in theBoard.items():
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
    i += 1
