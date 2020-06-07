
'''You can change the life point to play a game'''
lifepoint = 3
typing = ""
total  = ""
'''You can change the letter here'''
letter_1 = "m"
letter_2 = "a"
letter_3 = "p"
letter_4 = "l"
letter_5 = "e"
guess = ""
round = 0

'''lap_round_the sequence of answer'''
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
        while guess == letter_1 or guess == letter_3 or guess == letter_4:
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

if lifepoint == 0:
    print("The Answer is :", letter_1 + letter_2 + letter_3 + letter_4 + letter_5)























