dragonBall = True
check_1_D = 0
check_2_D = 0
check_3_D = 0
check_4_D = 0
check_pro_D = False

def guessInput():
    guess = input("guess : ")
    return guess

def guessCorrect():
    print("-------------------------------------")
    print("You guess correctly")
    print("-------------------------------------")

def guessWrong():
    print("-------------------------------------")
    print("Your are incorrect")
    print("-------------------------------------")

def guessAlready():
    print("-------------------------------------------")
    print("You have guessed this letter already")
    print("Please typing again")
    print("-------------------------------------------")

def returnHangmanD():
    print("-----------------------------------------------")
    print("Do you want to continue ")
    print("Please be noted you have to input only 1 or 2")
    print("1) Yes")
    print("2) No")
    returnChoice = int(input(">>> "))
    if returnChoice == 1:
        return  True
    else:
        return  False

def showMenuDragonChoice():
    print("--------------------------------")
    print("Welcome to the Hang-Man game")
    print("--------------------------------")
    print("This game is the name of Dragonball Character")
    print("Select the Number of Problem")
    for x in range(4):
        x += 1
        print(str(x) + ")", "Problem", x)
        if check_1_D == 1 and x == 1:
            print("(--You have clear problem",x,"--)")
        if check_2_D == 1 and x == 2:
            print("(--You have clear problem",x,"--)")
        if check_3_D == 1 and x == 3:
            print("(--You have clear problem", x, "--)")
        if check_4_D == 1 and x == 4:
            print("(--You have clear problem", x, "--)")
    print("5) See the answer but you cannot get the reward")

def guess_5_letter_word():
    lifepoint = 5
    guess = ""
    round = 0
    lap_1_1 = 0
    lap_1_2 = 0
    lap_1_3 = 0
    lap_1_4 = 0
    lap_1_5 = 0
    lap_2_12 = 0
    lap_2_13 = 0
    lap_2_14 = 0
    lap_2_15 = 0
    lap_2_23 = 0
    lap_2_24 = 0
    lap_2_25 = 0
    lap_2_34 = 0
    lap_2_35 = 0
    lap_2_45 = 0
    lap_2_123 = 0
    lap_2_234 = 0
    lap_2_345 = 0
    lap_2_124 = 0
    lap_2_125 = 0
    lap_2_134 = 0
    lap_2_135 = 0
    lap_2_145 = 0
    lap_2_235 = 0
    lap_2_245 = 0
    lap_3_1234 = 0
    lap_3_2345 = 0
    lap_3_1245 = 0
    lap_3_1345 = 0
    lap_3_1235 = 0


    print("(----Please be noted input an only one low-case letter----)")
    print("_____")
    while guess != letter_1 and guess != letter_2 and guess != letter_3 and guess != letter_4 and guess != letter_5:
        guess = input("guess : ")
        if guess != letter_1 and guess != letter_2 and guess != letter_3 and guess != letter_4 and guess != letter_5:
            guessWrong()
            print("_____")
            lifepoint -= 1
            print("Your life is ", lifepoint)
            if lifepoint <= 0:
                print("-------------------------------------")
                print("Game over")
                break

    if lifepoint > 0 and guess == letter_1 and round == 0:
        guessCorrect()
        print(letter_1+"____")
        while guess != letter_2 and guess != letter_3 and guess != letter_4 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_1:
                guessAlready()
                print(letter_1 + "____")
                guess = guessInput()
            if guess != letter_2 and guess != letter_3 and guess != letter_4 and guess != letter_5:
                guessWrong()
                print(letter_1+"____")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_1_1 = 1
        round = 1

    if lifepoint > 0 and guess == letter_2 and round == 0:
        guessCorrect()
        print("_"+letter_2+"___")
        while guess != letter_1 and guess != letter_3 and guess != letter_4 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_2:
                guessAlready()
                print("_" + letter_2 + "___")
                guess = guessInput()
            if guess != letter_1 and guess != letter_3 and guess != letter_4 and guess != letter_5:
                guessWrong()
                print("_"+letter_2+"___")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_1_2 = 1
        round = 1

    if lifepoint > 0 and guess == letter_3 and round == 0:
        guessCorrect()
        print("__"+letter_3+"__")
        while guess != letter_1 and guess != letter_2 and guess != letter_4 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_3:
                guessAlready()
                print("__" + letter_3 + "__")
                guess = guessInput()
            if guess != letter_1 and guess != letter_2 and guess != letter_4 and guess != letter_5:
                guessWrong()
                print("__"+letter_3+"__")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_1_3 = 1
        round = 1

    if lifepoint > 0 and guess == letter_4 and round == 0:
        guessCorrect()
        print("___"+letter_4+"_")
        while guess != letter_1 and guess != letter_2 and guess != letter_3 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_4:
                guessAlready()
                print("___" + letter_4 + "_")
                guess = guessInput()
            if guess != letter_1 and guess != letter_2 and guess != letter_3 and guess != letter_5:
                guessWrong()
                print("___"+letter_4+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_1_4 = 1
        round = 1

    if lifepoint > 0 and guess == letter_5 and round == 0:
        guessCorrect()
        print("____"+letter_5)
        while guess != letter_1 and guess != letter_2 and guess != letter_3 and guess != letter_4:
            guess = input("guess : ")
            while guess == letter_5:
                guessAlready()
                print("____" + letter_5)
                guess = guessInput()
            if guess != letter_1 and guess != letter_2 and guess != letter_3 and guess != letter_4:
                guessWrong()
                print("____"+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_1_5 = 1
        round = 1

    '''--------------------------Here finish all lap_1---------------------------------'''

    if lifepoint > 0 and lap_1_1 == 1 and guess == letter_2 and round == 1:
        guessCorrect()
        print(letter_1+letter_2+"___")
        while guess != letter_3 and guess != letter_4 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_2:
                guessAlready()
                print(letter_1 + letter_2 + "___")
                guess = guessInput()
            if guess != letter_3 and guess != letter_4 and guess != letter_5:
                guessWrong()
                print(letter_1+letter_2+"___")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_12 = 1
        lap_2_123 = 1
        lap_2_124 = 1
        lap_2_125 = 1
        round = 2

    if lifepoint > 0 and lap_1_1 == 1 and guess == letter_3 and round == 1:
        guessCorrect()
        print(letter_1+"_"+letter_3+"__")
        while guess != letter_2 and guess != letter_4 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_3:
                guessAlready()
                print(letter_1+"_"+letter_3+"__")
                guess = guessInput()
            if guess != letter_2 and guess != letter_4 and guess != letter_5:
                guessWrong()
                print(letter_1+"_"+letter_3+"__")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_13 = 1
        lap_2_123 = 1
        lap_2_134 = 1
        lap_2_135 = 1
        round = 2

    if lifepoint > 0 and lap_1_1 == 1 and guess == letter_4 and round == 1:
        guessCorrect()
        print(letter_1+"__"+letter_4+"_")
        while guess != letter_2 and guess != letter_3 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_4:
                guessAlready()
                print(letter_1+"__"+letter_4+"_")
                guess = guessInput()
            if guess != letter_2 and guess != letter_3 and guess != letter_5:
                guessWrong()
                print(letter_1+"__"+letter_4+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_14 = 1
        lap_2_124 = 1
        lap_2_134 = 1
        lap_2_145 = 1
        round = 2

    if lifepoint > 0 and lap_1_1 == 1 and guess == letter_5 and round == 1:
        guessCorrect()
        print(letter_1+"___"+letter_5)
        while guess != letter_2 and guess != letter_3 and guess != letter_4:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_5:
                guessAlready()
                print(letter_1+"___"+letter_5)
                guess = guessInput()
            if guess != letter_2 and guess != letter_3 and guess != letter_4:
                guessWrong()
                print(letter_1+"___"+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_15 = 1
        lap_2_125 = 1
        lap_2_135 = 1
        lap_2_145 = 1
        round = 2

    if lifepoint > 0 and lap_1_2 == 1 and guess == letter_1 and round == 1:
        guessCorrect()
        print(letter_1+letter_2+"___")
        while guess != letter_3 and guess != letter_4 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_2 or guess == letter_1:
                guessAlready()
                print(letter_1+letter_2+"___")
                guess = guessInput()
            if guess != letter_3 and guess != letter_4 and guess != letter_5:
                guessWrong()
                print(letter_1+letter_2+"___")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_12 = 1
        lap_2_123 = 1
        lap_2_124 = 1
        lap_2_125 = 1
        round = 2

    if lifepoint > 0 and lap_1_2 == 1 and guess == letter_3 and round == 1:
        guessCorrect()
        print("_"+letter_2+letter_3+"__")
        while guess != letter_1 and guess != letter_4 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_2 or guess == letter_3:
                guessAlready()
                print("_"+letter_2+letter_3+"__")
                guess = guessInput()
            if guess != letter_1 and guess != letter_4 and guess != letter_5:
                guessWrong()
                print("_"+letter_2+letter_3+"__")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_23 = 1
        lap_2_123 = 1
        lap_2_234 = 1
        lap_2_235 = 1
        round = 2

    if lifepoint > 0 and lap_1_2 == 1 and guess == letter_4 and round == 1:
        guessCorrect()
        print("_"+letter_2+"_"+letter_4+"_")
        while guess != letter_1 and guess != letter_3 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_2 or guess == letter_4:
                guessAlready()
                print("_"+letter_2+"_"+letter_4+"_")
                guess = guessInput()
            if guess != letter_1 and guess != letter_3 and guess != letter_5:
                guessWrong()
                print("_"+letter_2+"_"+letter_4+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_24 = 1
        lap_2_234 = 1
        lap_2_124 = 1
        lap_2_245 = 1
        round = 2

    if lifepoint > 0 and lap_1_2 == 1 and guess == letter_5 and round == 1:
        guessCorrect()
        print("_"+letter_2+"__"+letter_5)
        while guess != letter_1 and guess != letter_3 and guess != letter_4:
            guess = input("guess : ")
            while guess == letter_2 or guess == letter_5:
                guessAlready()
                print("_"+letter_2+"__"+letter_5)
                guess = guessInput()
            if guess != letter_1 and guess != letter_3 and guess != letter_4:
                guessWrong()
                print("_"+letter_2+"__"+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_25 = 1
        lap_2_125 = 1
        lap_2_245 = 1
        lap_2_235 = 1
        round = 2

    if lifepoint > 0 and lap_1_3 == 1 and guess == letter_1 and round == 1:
        guessCorrect()
        print(letter_1+"_"+letter_3+"__")
        while guess != letter_2 and guess != letter_4 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_3:
                guessAlready()
                print(letter_1+"_"+letter_3+"_")
                guess = guessInput()
            if guess != letter_2 and guess != letter_4 and guess != letter_5:
                guessWrong()
                print(letter_1+"_"+letter_3+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_13 = 1
        lap_2_123 = 1
        lap_2_134 = 1
        lap_2_135 = 1
        round = 2

    if lifepoint > 0 and lap_1_3 == 1 and guess == letter_2 and round == 1:
        guessCorrect()
        print("_"+letter_2+letter_3+"__")
        while guess != letter_1 and guess != letter_4 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_2 or guess == letter_3:
                guessAlready()
                print("_"+letter_2+letter_3+"__")
                guess = guessInput()
            if guess != letter_1 and guess != letter_4 and guess != letter_5:
                guessWrong()
                print("_"+letter_2+letter_3+"__")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_23 = 1
        lap_2_123 = 1
        lap_2_234 = 1
        lap_2_235 = 1
        round = 2

    if lifepoint > 0 and lap_1_3 == 1 and guess == letter_4 and round == 1:
        guessCorrect()
        print("__"+letter_3+letter_4+"_")
        while guess != letter_1 and guess != letter_2 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_3 or guess == letter_4:
                guessAlready()
                print("__"+letter_3+letter_4+"_")
                guess = guessInput()
            if guess != letter_1 and guess != letter_2 and guess != letter_5:
                guessWrong()
                print("__"+letter_3+letter_4+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_34 = 1
        lap_2_234 = 1
        lap_2_345 = 1
        lap_2_134 = 1
        round = 2

    if lifepoint > 0 and lap_1_3 == 1 and guess == letter_5 and round == 1:
        guessCorrect()
        print("__"+letter_3+"_"+letter_5)
        while guess != letter_1 and guess != letter_2 and guess != letter_4:
            guess = input("guess : ")
            while guess == letter_3 or guess == letter_5:
                guessAlready()
                print("__"+letter_3+"_"+letter_5)
                guess = guessInput()
            if guess != letter_1 and guess != letter_2 and guess != letter_4:
                guessWrong()
                print("__"+letter_3+"_"+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_35 = 1
        lap_2_345 = 1
        lap_2_135 = 1
        lap_2_235 = 1
        round = 2

    if lifepoint > 0 and lap_1_4 == 1 and guess == letter_1 and round == 1:
        guessCorrect()
        print(letter_1+"__"+letter_4+"_")
        while guess != letter_2 and guess != letter_3 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_4:
                guessAlready()
                print(letter_1+"__"+letter_4+"_")
                guess = guessInput()
            if guess != letter_2 and guess != letter_3 and guess != letter_5:
                guessWrong()
                print(letter_1+"__"+letter_4+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_14 = 1
        lap_2_124 = 1
        lap_2_134 = 1
        lap_2_145 = 1
        round = 2

    if lifepoint > 0 and lap_1_4 == 1 and guess == letter_2 and round == 1:
        guessCorrect()
        print("_"+letter_2+"_"+letter_4+"_")
        while guess != letter_1 and guess != letter_3 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_2 or guess == letter_4:
                guessAlready()
                print("_"+letter_2+"_"+letter_4+"_")
                guess = guessInput()
            if guess != letter_1 and guess != letter_3 and guess != letter_5:
                guessWrong()
                print("_"+letter_2+"_"+letter_4+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_24 = 1
        lap_2_234 = 1
        lap_2_124 = 1
        lap_2_245 = 1
        round = 2

    if lifepoint > 0 and lap_1_4 == 1 and guess == letter_3 and round == 1:
        guessCorrect()
        print("__"+letter_3+letter_4+"_")
        while guess != letter_1 and guess != letter_2 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_3 or guess == letter_4:
                guessAlready()
                print("__"+letter_3+letter_4+"_")
                guess = guessInput()
            if guess != letter_1 and guess != letter_2 and guess != letter_5:
                guessWrong()
                print("__"+letter_3+letter_4+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_34 = 1
        lap_2_234 = 1
        lap_2_345 = 1
        lap_2_134 = 1
        round = 2

    if lifepoint > 0 and lap_1_4 == 1 and guess == letter_5 and round == 1:
        guessCorrect()
        print("___"+letter_4+letter_5)
        while guess != letter_1 and guess != letter_2 and guess != letter_3:
            guess = input("guess : ")
            while guess == letter_4 or guess == letter_5:
                guessAlready()
                print("___"+letter_4+letter_5)
                guess = guessInput()
            if guess != letter_1 and guess != letter_2 and guess != letter_3:
                guessWrong()
                print("___"+letter_4+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_45 = 1
        lap_2_345 = 1
        lap_2_145 = 1
        lap_2_245 = 1
        round = 2

    if lifepoint > 0 and lap_1_5 == 1 and guess == letter_1 and round == 1:
        guessCorrect()
        print(letter_1+"___"+letter_5)
        while guess != letter_2 and guess != letter_3 and guess != letter_4:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_5:
                guessAlready()
                print(letter_1+"___"+letter_5)
                guess = guessInput()
            if guess != letter_2 and guess != letter_3 and guess != letter_4:
                guessWrong()
                print(letter_1+"___"+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_15 = 1
        lap_2_125 = 1
        lap_2_135 = 1
        lap_2_145 = 1
        round = 2

    if lifepoint > 0 and lap_1_5 == 1 and guess == letter_2 and round == 1:
        guessCorrect()
        print("_"+letter_2+"__"+letter_5)
        while guess != letter_1 and guess != letter_3 and guess != letter_4:
            guess = input("guess : ")
            while guess == letter_2 or guess == letter_5:
                guessAlready()
                print("_"+letter_2+"__"+letter_5)
                guess = guessInput()
            if guess != letter_1 and guess != letter_3 and guess != letter_4:
                guessWrong()
                print("_"+letter_2+"__"+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_25 = 1
        lap_2_125 = 1
        lap_2_245 = 1
        lap_2_235 = 1
        round = 2

    if lifepoint > 0 and lap_1_5 == 1 and guess == letter_3 and round == 1:
        guessCorrect()
        print("__"+letter_3+"_"+letter_5)
        while guess != letter_1 and guess != letter_2 and guess != letter_4:
            guess = input("guess : ")
            while guess == letter_3 or guess == letter_5:
                guessAlready()
                print("__"+letter_3+"_"+letter_5)
                guess = guessInput()
            if guess != letter_1 and guess != letter_2 and guess != letter_4:
                guessWrong()
                print("__"+letter_3+"_"+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_35 = 1
        lap_2_345 = 1
        lap_2_135 = 1
        lap_2_235 = 1
        round = 2

    if lifepoint > 0 and lap_1_5 == 1 and guess == letter_4 and round == 1:
        guessCorrect()
        print("___"+letter_4+letter_5)
        while guess != letter_1 and guess != letter_2 and guess != letter_3:
            guess = input("guess : ")
            while guess == letter_4 or guess == letter_5:
                guessAlready()
                print("___"+letter_4+letter_5)
                guess = guessInput()
            if guess != letter_1 and guess != letter_2 and guess != letter_3:
                guessWrong()
                print("___"+letter_4+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_2_45 = 1
        lap_2_345 = 1
        lap_2_145 = 1
        lap_2_245 = 1
        round = 2

    '''----------------------------------Here finish all lap_2--------------------------------'''

    if (lifepoint > 0 and lap_2_123 == 1  and round == 2) and (guess != letter_4 and guess != letter_5):
        guessCorrect()
        print(letter_1+letter_2+letter_3+"__")
        while  guess != letter_4 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_2 or guess == letter_3:
                guessAlready()
                print(letter_1+letter_2+letter_3+"__")
                guess = guessInput()
            if  guess != letter_4 and guess != letter_5:
                guessWrong()
                print(letter_1+letter_2+letter_3+"__")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_3_123 = 1
        lap_3_1234 = 1
        lap_3_1235 = 1
        round = 3

    if (lifepoint > 0 and lap_2_234 == 1  and round == 2) and (guess != letter_1 and guess != letter_5):
        guessCorrect()
        print("_"+letter_2+letter_3+letter_4+"_")
        while  guess != letter_1 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_2 or guess == letter_3 or guess == letter_4:
                guessAlready()
                print("_"+letter_2+letter_3+letter_4+"_")
                guess = guessInput()
            if  guess != letter_1 and guess != letter_5:
                guessWrong()
                print("_"+letter_2+letter_3+letter_4+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_3_234 = 1
        lap_3_1234 = 1
        lap_3_2345 = 1
        round = 3

    if (lifepoint > 0 and lap_2_345 == 1  and round == 2) and (guess != letter_1 and guess != letter_2):
        guessCorrect()
        print("__"+letter_3+letter_4+letter_5)
        while  guess != letter_1 and guess != letter_2:
            guess = input("guess : ")
            while guess == letter_3 or guess == letter_4 or guess == letter_5:
                guessAlready()
                print("__"+letter_3+letter_4+letter_5)
                guess = guessInput()
            if  guess != letter_1 and guess != letter_2:
                guessWrong()
                print("__"+letter_3+letter_4+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_3_345 = 1
        lap_3_2345 = 1
        lap_3_1345 = 1
        round = 3

    if (lifepoint > 0 and lap_2_124 == 1  and round == 2) and (guess != letter_3 and guess != letter_5):
        guessCorrect()
        print(letter_1+letter_2+"_"+letter_4+"_")
        while  guess != letter_3 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_2 or guess == letter_4:
                guessAlready()
                print(letter_1+letter_2+"_"+letter_4+"_")
                guess = guessInput()
            if  guess != letter_3 and guess != letter_5:
                guessWrong()
                print(letter_1+letter_2+"_"+letter_4+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_3_124 = 1
        lap_3_1234 = 1
        lap_3_1245 = 1
        round = 3

    if (lifepoint > 0 and lap_2_125 == 1  and round == 2) and (guess != letter_3 and guess != letter_4):
        guessCorrect()
        print(letter_1+letter_2+"__"+letter_5)
        while  guess != letter_3 and guess != letter_4:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_2 or guess == letter_5:
                guessAlready()
                print(letter_1+letter_2+"__"+letter_5)
                guess = guessInput()
            if  guess != letter_3 and guess != letter_4:
                guessWrong()
                print(letter_1+letter_2+"__"+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_3_125 = 1
        lap_3_1245 = 1
        lap_3_1235 = 1
        round = 3

    if (lifepoint > 0 and lap_2_134 == 1  and round == 2) and (guess != letter_2 and guess != letter_5):
        guessCorrect()
        print(letter_1+"_"+letter_3+letter_4+"_")
        while  guess != letter_2 and guess != letter_5:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_3 or guess == letter_4:
                guessAlready()
                print(letter_1+"_"+letter_3+letter_4+"_")
                guess = guessInput()
            if  guess != letter_2 and guess != letter_5:
                guessWrong()
                print(letter_1+"_"+letter_3+letter_4+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_3_134 = 1
        lap_3_1234 = 1
        lap_3_1345 = 1
        round = 3

    if (lifepoint > 0 and lap_2_135 == 1  and round == 2) and (guess != letter_2 and guess != letter_4):
        guessCorrect()
        print(letter_1+"_"+letter_3+"_"+letter_5)
        while  guess != letter_2 and guess != letter_4:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_3 or guess == letter_5:
                guessAlready()
                print(letter_1+"_"+letter_3+"_"+letter_5)
                guess = guessInput()
            if  guess != letter_2 and guess != letter_4:
                guessWrong()
                print(letter_1+"_"+letter_3+"_"+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_3_135 = 1
        lap_3_1345 = 1
        lap_3_1235 = 1
        round = 3

    if (lifepoint > 0 and lap_2_145 == 1  and round == 2) and (guess != letter_2 and guess != letter_3):
        guessCorrect()
        print(letter_1+"__"+letter_4+letter_5)
        while  guess != letter_2 and guess != letter_3:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_4 or guess == letter_5:
                guessAlready()
                print(letter_1+"__"+letter_4+letter_5)
                guess = guessInput()
            if  guess != letter_2 and guess != letter_3:
                guessWrong()
                print(letter_1+"__"+letter_4+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_3_145 = 1
        lap_3_1245 = 1
        lap_3_1345 = 1
        round = 3

    if (lifepoint > 0 and lap_2_245 == 1  and round == 2) and (guess != letter_1 and guess != letter_3):
        guessCorrect()
        print("_"+letter_2+"_"+letter_4+letter_5)
        while  guess != letter_1 and guess != letter_3:
            guess = input("guess : ")
            while guess == letter_2 or guess == letter_4 or guess == letter_5:
                guessAlready()
                print("_"+letter_2+"_"+letter_4+letter_5)
                guess = guessInput()
            if  guess != letter_1 and guess != letter_3:
                guessWrong()
                print("_"+letter_2+"_"+letter_4+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_3_245 = 1
        lap_3_2345 = 1
        lap_3_1245 = 1
        round = 3

    if (lifepoint > 0 and lap_2_235 == 1  and round == 2) and (guess != letter_1 and guess != letter_4):
        guessCorrect()
        print("_"+letter_2+letter_3+"_"+letter_5)
        while  guess != letter_1 and guess != letter_4:
            guess = input("guess : ")
            while guess == letter_2 or guess == letter_3 or guess == letter_5:
                guessAlready()
                print("_"+letter_2+letter_3+"_"+letter_5)
                guess = guessInput()
            if  guess != letter_1 and guess != letter_4:
                guessWrong()
                print("_"+letter_2+letter_3+"_"+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_3_235 = 1
        lap_3_2345 = 1
        lap_3_1235 = 1
        round = 3

    '''--------------------------------Here Finish all lap 3----------------------------------'''
    if (lifepoint > 0 and lap_3_1234 == 1  and round == 3) and (guess != letter_5):
        guessCorrect()
        print(letter_1+letter_2+letter_3+letter_4+"_")
        while  guess != letter_5:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_2 or guess == letter_3 or guess == letter_4:
                guessAlready()
                print(letter_1+letter_2+letter_3+letter_4+"_")
                guess = guessInput()
            if  guess != letter_5:
                guessWrong()
                print(letter_1+letter_2+letter_3+letter_4+"_")
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_4_1234 = 1
        round = 4

    if (lifepoint > 0 and lap_3_2345 == 1  and round == 3) and (guess != letter_1):
        guessCorrect()
        print("_"+letter_2+letter_3+letter_4+letter_5)
        while  guess != letter_1:
            guess = input("guess : ")
            while guess == letter_2 or guess == letter_3 or guess == letter_4 or guess == letter_5:
                guessAlready()
                print("_"+letter_2+letter_3+letter_4+letter_5)
                guess = guessInput()
            if  guess != letter_1:
                guessWrong()
                print("_"+letter_2+letter_3+letter_4+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_4_2345 = 1
        round = 4

    if (lifepoint > 0 and lap_3_1245 == 1  and round == 3) and (guess != letter_3):
        guessCorrect()
        print(letter_1+letter_2+"_"+letter_4+letter_5)
        while  guess != letter_3:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_2 or guess == letter_4 or guess == letter_5:
                guessAlready()
                print(letter_1+letter_2+"_"+letter_4+letter_5)
                guess = guessInput()
            if  guess != letter_3:
                guessWrong()
                print(letter_1+letter_2+"_"+letter_4+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_4_1245 = 1
        round = 4

    if (lifepoint > 0 and lap_3_1345 == 1  and round == 3) and (guess != letter_2):
        guessCorrect()
        print(letter_1+"_"+letter_3+letter_4+letter_5)
        while  guess != letter_2:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_3 or guess == letter_4 or guess == letter_5:
                guessAlready()
                print(letter_1+"_"+letter_3+letter_4+letter_5)
                guess = guessInput()
            if  guess != letter_2:
                guessWrong()
                print(letter_1+"_"+letter_3+letter_4+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_4_1345 = 1
        round = 4

    if (lifepoint > 0 and lap_3_1235 == 1  and round == 3) and (guess != letter_4):
        guessCorrect()
        print(letter_1+letter_2+letter_3+"_"+letter_5)
        while  guess != letter_4:
            guess = input("guess : ")
            while guess == letter_1 or guess == letter_2 or guess == letter_3 or guess == letter_5:
                guessAlready()
                print(letter_1+letter_2+letter_3+"_"+letter_5)
                guess = guessInput()
            if  guess != letter_4:
                guessWrong()
                print(letter_1+letter_2+letter_3+"_"+letter_5)
                lifepoint -= 1
                print("Your life is ", lifepoint)
                if lifepoint <= 0:
                    print("Game over")
                    break
        lap_4_1235 = 1
        round = 4

    '''-----------------------------Here finish all lap 4-------------------------------------------'''

    if lifepoint > 0:
        guessCorrect()
        print("The Answer is :",letter_1+letter_2+letter_3+letter_4+letter_5)
        print("----------------You won--------------------")
        return 1

    if lifepoint == 0:
        return 0

while dragonBall == True:
    showMenuDragonChoice()
    if check_1_D == 1 and check_2_D == 1 and check_3_D == 1 and check_4_D == 1 and check_pro_D == False:
        print("------------------------------------------------")
        print("Congratulations!!!!!!!!!!!")
        print("You are very genius")
        print("Behalf of the God_Shin")
        print("I will give you a reward")
        print("https://www.pinterest.com/manbeast6964849/mr-satan/")
        print("This reward is appropriate for the guy who can answer all question in the Dragonball part")
        print("--------------------------------------------------")
    problemSelect = float(input("Selcet Choice : "))
    if problemSelect == 1:
        letter_1 = "b"
        letter_2 = "u"
        letter_3 = "l"
        letter_4 = "m"
        letter_5 = "a"
        if guess_5_letter_word() == 1:
            check_1_D = 1
        else:
            check_1_D = 0
        if returnHangmanD() == True:
            dragonBall = True
        else:
            dragonBall = False

    if problemSelect == 2:
        letter_1 = "g"
        letter_2 = "o"
        letter_3 = "h"
        letter_4 = "a"
        letter_5 = "n"
        if guess_5_letter_word() == 1:
            check_2_D = 1
        else:
            check_2_D = 0
        if returnHangmanD() == True:
            dragonBall = True
        else:
            dragonBall = False

    if problemSelect == 3:
        letter_1 = "v"
        letter_2 = "i"
        letter_3 = "d"
        letter_4 = "e"
        letter_5 = "l"
        if guess_5_letter_word() == 1:
            check_3_D = 1
        else:
            check_3_D = 0
        if returnHangmanD() == True:
            dragonBall = True
        else:
            dragonBall = False

    if problemSelect == 4:
        letter_1 = "b"
        letter_2 = "r"
        letter_3 = "o"
        letter_4 = "l"
        letter_5 = "y"
        if guess_5_letter_word() == 1:
            check_4_D = 1
        else:
            check_4_D = 0
        if returnHangmanD() == True:
            dragonBall = True
        else:
            dragonBall = False

    if problemSelect == 5:
        print("The answer of problem 1 : bulma")
        print("The answer of problem 2 : gohan")
        print("The answer of problem 3 : videl")
        print("The answer of problem 4 : broly")
        check_pro_D = True
        if returnHangmanD() == True:
            dragonBall = True
        else:
            dragonBall = False

    if problemSelect < 1 or problemSelect >= 6:
        print("-----------------------")
        print("You have selected incorrectly")


print("---------------Thank you for playing---------------------")
print("You can contact me at https://github.com/leoshingkung1122")


























