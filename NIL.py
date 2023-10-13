'''
1       5   6   7
1 2     5   6   7
1   3   5   6   7
1     4 5   6   7
1       5   6   7 8 9 0
'''

for row in range(5):
    for column in range(12):
        if ((column ==0 or column==4 or row==column or column==6 or column==8) or
             ((column==9 and row==4) or (column==10 and row==4) or (column==11 and row==4))):
            print('*',end=' ')
        else:
            print(' ',end=' ')  
    print()