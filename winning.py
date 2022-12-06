from grid import generate_grid

def win(a, ls):
    global counter
    counter = -1
    #vertical win
    for i in range (a):
        for j in range(a-3):
            if (ls[i][j] == 'X' and ls[i][j+1] == 'X' and ls[i][j+2] == 'X' and ls[i][j+3] == 'X') or (ls[i][j] == 'O' and ls[i][j+1] == 'O' and ls[i][j+2] == 'O' and ls[i][j+3] == 'O'):
                ls[i][j], ls[i][j+1], ls[i][j+2], ls[i][j+3] = '*', '*', '*', '*' 
                generate_grid(a, ls) 
                ls[i][j], ls[i][j+1], ls[i][j+2], ls[i][j+3] = ' ', ' ', ' ', ' '
                counter = 4
                return counter
    
    #horizontal win
    for i in range(a-3):
        for j in range(a):
            if ls[i][j] == 'X' and ls[i+1][j] == 'X' and ls[i+2][j] == 'X' and ls[i+3][j] == 'X': 
                ls[i][j], ls[i+1][j], ls[i+2][j], ls[i+3][j] = '*', '*', '*', '*'
                counter = 4
                if i < a-4 and ls[i+4][j] == 'X':
                    ls[i+4][j] = ' '
                    counter +=1
                    generate_grid(a, ls)
                generate_grid(a, ls)
                ls[i][j], ls[i+1][j], ls[i+2][j], ls[i+3][j] = ' ', ' ', ' ', ' ' 
                return counter
            
            if ls[i][j] == 'O' and ls[i+1][j] == 'O' and ls[i+2][j] == 'O' and ls[i+3][j] == 'O':
                ls[i][j], ls[i+1][j], ls[i+2][j], ls[i+3][j] = '*', '*', '*', '*'
                counter = 4
                if i < a-4 and ls[i+4][j] == 'O':
                    ls[i+4][j] = ' '
                    counter +=1
                    generate_grid(a, ls)
                generate_grid(a, ls)
                ls[i][j], ls[i+1][j], ls[i+2][j], ls[i+3][j] = ' ', ' ', ' ', ' '
                return counter

    #main diagonal win
    for i in range(a-3):
        for j in range(a-3):
            if ls[i][j] == 'X' and ls[i+1][j+1] == 'X' and ls[i+2][j+2] == 'X' and ls[i+3][j+3] == 'X':
                ls[i][j], ls[i+1][j+1], ls[i+2][j+2], ls[i+3][j+3] = '*', '*', '*', '*'
                counter = 4
                if i < a-4 and j< a-4:
                    if ls[i+4][j+4] == 'X':
                        ls[i+4][j+4] = ' '
                        counter +=1
                        generate_grid(a, ls)
                generate_grid(a, ls)
                ls[i][j], ls[i+1][j+1], ls[i+2][j+2], ls[i+3][j+3] = ' ', ' ', ' ', ' '
                return counter
            
            if (ls[i][j] == 'O' and ls[i+1][j+1] == 'O' and ls[i+2][j+2] == 'O' and ls[i+3][j+3] == 'O'):
                ls[i][j], ls[i+1][j+1], ls[i+2][j+2], ls[i+3][j+3] = '*', '*', '*', '*'
                counter = 4
                if i < a-4 and j< a-4:
                    if ls[i+4][j+4] == 'O':
                        ls[i+4][j+4] = ' '
                        counter +=1
                        generate_grid(a, ls)
                generate_grid(a, ls)
                ls[i][j], ls[i+1][j+1], ls[i+2][j+2], ls[i+3][j+3] = ' ', ' ', ' ', ' '
                return counter

    #secondary diagonal win
    for i in range(a-3):
        for j in range(3, a):
            if (ls[i][j] == 'X' and ls[i+1][j-1] == 'X' and ls[i+2][j-2] == 'X' and ls[i+3][j-3] == 'X'):
                ls[i][j], ls[i+1][j-1] , ls[i+2][j-2], ls[i+3][j-3]= '*', '*', '*', '*'
                counter = 4
                if i < a-4 and j > 4:
                    if ls[i+4][j-4] == 'X':
                        ls[i+4][j-4] = ' '
                        counter +=1
                        generate_grid(a, ls)
                generate_grid(a, ls)
                ls[i][j], ls[i+1][j-1] , ls[i+2][j-2], ls[i+3][j-3] = ' ', ' ', ' ', ' '
                return counter
            
            if (ls[i][j] == 'O' and ls[i+1][j-1] == 'O' and ls[i+2][j-2] == 'O' and ls[i+3][j-3] == 'O'):
                ls[i][j], ls[i+1][j-1] , ls[i+2][j-2], ls[i+3][j-3]= '*', '*', '*', '*'
                counter = 4
                if i < a-3 and j > 3:
                    if ls[i+4][j-4] == 'O':
                        ls[i+4][j-4] = ' '
                        counter +=1
                        generate_grid(a, ls)
                generate_grid(a, ls)
                ls[i][j], ls[i+1][j-1] , ls[i+2][j-2], ls[i+3][j-3] = ' ', ' ', ' ', ' '
                return counter

    return -1