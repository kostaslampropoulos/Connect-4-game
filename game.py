from operator import *
from math import *
import csv
from grid import generate_grid
from winning import win, counter

print('Welcome to the game (Connect 4) !')
start = input('Do you wish for a new game (Y) or to load an existing one (S); ')


if start == 'Y':
    while True:
        try:
            a = int(input('Give the number of columns of the game: (5-10): '))
            break
        except ValueError:
            pass

    while a>10 or a<5:
        print('Wrong input!')
        a = int(input('Give the number of columns of the game: (5-10): '))

        """
        >>> 11
        >>> Wrong input!
        >>> 4
        >>> Wrong input!
        >>> 100000
        >>> Wrong input!
        """

    ls = []
    p = []

    for i in range(a):
        for j in range(a):
            p.append(' ')
        ls.append(p)
        p = []
elif start == 'S':
    file_name = input('What is the name of the file? : ')
    file_name += '.csv'
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        ls = list(reader)
    
    score_X = ls[-1][0]
    score_O = ls[-2][0]
    a = len(ls[0])

def shift(a, ls):
    for k in range(a):
        for i in range(a):
            for j in range(1, a):
                if ls[i][j] == ' ' and ls[i][j-1] != ' ' and ls[i][j-1] != '*':
                    ls[i][j] = ls[i][j-1]
                    ls[i][j-1] = ' '

generate_grid(a, ls)

score_O = 0
score_X = 0

check = 'n'

k=0
while k < a**2:
    
    print('Player '+str(k%2 + 1)+': Choose a column for your pawn: ', end="")
    b = int(input())
    
    while b>a or b<1:
        print('Wring input')
        print('Choose a column for your pawn: 1 - ', a,': ' ,end="")
        b = int(input())

    while ls[b-1][0] != ' ':
        print('This column is full!:','Try again!')
        print('Player', k%2 + 1, end="")
        b = int(input(': Choose a column for your pawn:'))

    for i in range(a):
        if i+1 == a or ls[b-1][i+1] == 'X' or ls[b-1][i+1] == 'O':
            if k%2==0:
                ls[b-1][i] = 'O'
            else:
                ls[b-1][i] = 'X'
            break
    
    generate_grid(a, ls)

    if win(a, ls) != -1:
        if k%2 == 0:
            score_O = score_O + counter
        else:
            score_X = score_X + counter
        choice = input('ANd we have a winner! Do you wish to continue: N (for Yes) και O (for No): ')
        if choice == 'N':
            shift(a, ls)
            k = k - counter
        else:
            break
    
    if k%2 != 0:
        check = input('To pause and store the game into a file press "s": ')
    
    if check == 's':
        file_name = input('What name would you like the file to have? : ')
        file_name += '.csv'
        break
             
    k+=1

if check == 's':
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(ls)
        writer.writerow(str(score_O))
        writer.writerow(str(score_X))
    print('The current game was stored successfully !')
else:
    print('The score for P1 and P2: ',end="")
    print(score_O, score_X)
    print('End of the game, thanks for playing!!!')
    jkrhdg 

    