import random

with open('answords.txt', 'r') as answords:
    answ = [line.rstrip() for line in answords]

with open('guesswords.txt', 'r') as guesswords:
    guew = [line.rstrip() for line in guesswords]

def getinp(turn) -> str:
    uguess = ''
    while len(uguess) != 5:
        if uguess != '':
            print("that wasn't a valid input.  Try again.")
        uguess = input(f"Guess #{turn}. Enter a valid 5 letter word... ")
        if uguess.lower() not in guew:
            uguess = 'bad'
    return uguess.lower()



def guess(g, token, word) -> str:
    gl = list(g)
    for l in gl:
        if l in word:
            for i in range(len(word)):
                if word[i] == l:
                    token[i] += 1
    return ''.join([str(x) for x in token])



if __name__ == "__main__":
    turn = 1
    token = [0,0,0,0,0]
    word = random.choice(answ)
    # you can hardcode words instead
    # word = 'tacos'
    while True:
        wg = getinp(turn)
        t = guess(wg, token, word)
        print(f"{wg} - {t}")
        turn += 1
        if turn == 6:
            answering = True
            while answering:
                ans = input("Time to guess the word... ")
                if ans.lower() in answ:
                    answering = False
                    if ans.lower() == word:
                        print(f"That's right, you guessed {ans.lower()} and it was {word}")
                    else:
                        print(f"I'm sorry, the word was {word}. Better luck next time!")
                    again = input("Another?  (y/n)")
                    if again.lower() == "y":
                        turn = 1
                        token = [0,0,0,0,0]
                        word = random.choice(answ)
                    else:
                        print("Bye!")
                        break
                else:
                    print("That wasn't a valid word, please try again!")
            if turn == 6:
                break