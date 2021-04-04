import random

def hangman(word):
    #間違えの回数を数える
    wrong = 0
    #間違えるたびに1行ずつ絵を書く
    stages = ["",
              "_____     ",
              "|         ",
              "|     |   ",
              "|     o   ",
              "|    /|\  ",
              "|    / \  ",
              "|         "
              ]
    #wordの文字を分解してリストにする
    #残りの文字数を覚えておくのに使う
    rletters = list(word)
    #文字列のリスト。プレイヤー2に見せるヒントを記録する
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    #ステージの長さに達したら負け。
    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字予想してね:"
        char = input(msg)
        #
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
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}".format(word))

#word_list = ["shark", "piano", "cat", "dog"]
#hangman(word_list[random.randint(0, len(word_list)-1)])

my_word = "zuruchan"
hangman(my_word)