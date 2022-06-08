import random
import string
al = string.ascii_lowercase
word_list = ('python', 'java', 'swift', 'javascript')
lives = 1
wonscore = 0
lostscore = 0

print("H A N G M A N  # 8 attempts")
mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
while mode not in ('play', 'results', 'exit'):
    mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
while mode == 'play' or mode == 'results':
    if mode == 'results':
        print('You won: ' + str(wonscore) + ' times.')
        print('You lost: ' + str(lostscore) + ' times.')
        mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        while mode not in ('play', 'results', 'exit'):
            mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    elif mode == 'play':
        answer = word_list[random.randint(0, len(word_list) - 1)]
        ans_list = set(answer)
        show = len(answer) * '-'
        showplus = show
        print(show)
        while lives > 0:
            if show != answer:
                a = input('Input a letter:')
                if len(a) != 1:
                    print("Please, input a single letter.")
                    print()
                    print(show)
                elif a not in al:
                    print("Please, enter a lowercase letter from the English alphabet.")
                    print()
                    print(show)

                else:
                    if a in showplus:
                        print("You've already guessed this letter.")
                        print()
                    else:
                        if a in ans_list:
                            j = 0
                            for char in answer:
                                j = j + 1
                                if char == a:
                                    before = show[0:j - 1]
                                    after = show[j:]
                                    show = show[0:j - 1] + a + show[j:]
                            showplus = showplus + a
                            print()
                        else:
                            print("That letter doesn't appear in the word.")
                            showplus = showplus + a
                            print()
                            lives = lives - 1
                    if show != answer:
                        print(show)
            else:
                print("You guessed the word " + show + "!")
                print("You survived!")
                wonscore += 1
                break
        else:
            if show == answer:
                print("You guessed the word " + show + "!")
                print("You survived!")
            else:
                print("You Lost!")
                lostscore += 1

        mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        while mode not in ('play', 'results', 'exit'):
            mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    elif mode == 'exit':
        print('exit')
        break
    else:
        mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')