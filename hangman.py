import random
def hangman(word):
    wrong = 0
    stages =["",
             "      ^     ",
             "|    / \    ",
             "|   / | \   ",
             "|  /  O  \  ",
             "| / _/|\_ \ ",
             "|    / \    ",
             ]
    rletters = list(word)
    board =["_"] * len(word)
    win = False
    print("ハングマンやろうぜ!")
    print("残機数は" + str(len(stages)) + "だぜ")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "一文字予想してみてね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち(YOU WIN!)")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は{}.".format(word))
    
correct =["apple","orange","grape"]
correct_num = random.randint(0,2)
hangman(correct[correct_num])
    
