def generate_grid(a, ls):
    """
    >>> ls = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    >>> generate_grid(5, ls)
    >>>     1    2    3    4    5
        -------------------------
        A|    |    |    |    |    |
        B|    |    |    |    |    |
        C|    |    |    |    |    |
        D|    |    |    |    |    |
        E|    |    |    |    |    |
        -------------------------
    """
    for i in range(1,a+1):
        print(3*' ', i, end="")

    print('\n', end="")
    print(5*a*'-')
    
    for i in range(1, 1+a):
        
        print(str(chr(i+96).upper()), end="")
        
        for j in range(1,a+1):
           print('|'+ 2*' ', ls[j-1][i-1], end="")
        print('|')
    
    print(5*a*'-')