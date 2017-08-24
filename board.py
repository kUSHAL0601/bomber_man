# CREATED BY MajAK

from subprocess import call
import os
from random import randint
global board


class Board():
    def __init__(self):
        self.pos_dict = {}
        self.pos_dict['bomb_timer'] = 0.0
        self.pos_dict['bomb_plant'] = 0
        self.pos_dict['score'] = 0
        self.pos_dict['lives'] = 3
        self.pos_dict['refresh'] = 0

    def init(self):
        self.pos_dict['bomb_timer'] = 0.0
        self.pos_dict['bomb_plant'] = 0
        self.pos_dict['refresh'] = 0
        self.pos_dict['arr'] = []
        score = str(self.pos_dict['score'])
        lives = str(self.pos_dict['lives'])
        self.pos_dict['arr'] = [[0 for x in range(132)] for y in range(42)]
        for i in range(42):
            for j in range(132):
                if(i == 0 or i == 1 or i == 40 or i == 41):
                    if(i == 0 and j == 50):
                        self.pos_dict['arr'][i][j] = 'S'
                    elif(i == 0 and j == 51):
                        self.pos_dict['arr'][i][j] = 'C'
                    elif(i == 0 and j == 52):
                        self.pos_dict['arr'][i][j] = 'O'
                    elif(i == 0 and j == 53):
                        self.pos_dict['arr'][i][j] = 'R'
                    elif(i == 0 and j == 54):
                        self.pos_dict['arr'][i][j] = 'E'
                    elif(i == 0 and j == 55):
                        self.pos_dict['arr'][i][j] = ':'
                    elif(i == 0 and j > 55 and (j - 55) <= len(score)):
                        self.pos_dict['arr'][i][j] = score[j - 55 - 1]
                    elif(i == 1 and j == 50):
                        self.pos_dict['arr'][i][j] = 'L'
                    elif(i == 1 and j == 51):
                        self.pos_dict['arr'][i][j] = 'I'
                    elif(i == 1 and j == 52):
                        self.pos_dict['arr'][i][j] = 'V'
                    elif(i == 1 and j == 53):
                        self.pos_dict['arr'][i][j] = 'E'
                    elif(i == 1 and j == 54):
                        self.pos_dict['arr'][i][j] = 'S'
                    elif(i == 1 and j == 55):
                        self.pos_dict['arr'][i][j] = ':'
                    elif(i == 1 and j == 56):
                        self.pos_dict['arr'][i][j] = lives[0]
                    else:
                        self.pos_dict['arr'][i][j] = '#'
                else:
                    self.pos_dict['arr'][i][j] = ' '
        count = 0
        while(count <= 50):
            indxj = randint(0, 32)
            indxi = randint(0, 18)
            if(self.pos_dict['arr'][2 * indxi][4 * indxj] == ' ' and indxi != 0 and indxj != 0):
                if((indxi == 0 and indxj == 1 and self.pos_dict['arr'][0][4] != '/') or (indxi == 1 and indxj == 0 and self.pos_dict['arr'][4][0] != '/')):
                    continue
                elif(self.pos_dict['arr'][2 * indxi][4 * indxj] != '/'):
                    self.pos_dict['arr'][2 * indxi][4 * indxj] = '/'
                    self.pos_dict['arr'][2 * indxi][4 * indxj + 1] = '/'
                    self.pos_dict['arr'][2 * indxi][4 * indxj + 2] = '/'
                    self.pos_dict['arr'][2 * indxi][4 * indxj + 3] = '/'
                    self.pos_dict['arr'][2 * indxi + 1][4 * indxj] = '/'
                    self.pos_dict['arr'][2 * indxi + 1][4 * indxj + 1] = '/'
                    self.pos_dict['arr'][2 * indxi + 1][4 * indxj + 2] = '/'
                    self.pos_dict['arr'][2 * indxi + 1][4 * indxj + 3] = '/'
                    count += 1

        count = 0

        while(count <= 4):
            indxj = randint(0, 32)
            indxi = randint(0, 18)
            if(self.pos_dict['arr'][2 * indxi][4 * indxj] == ' ' and indxi != 0 and indxj != 0):
                if((indxi == 0 and indxj == 1 and self.pos_dict['arr'][0][4] != 'E') or (indxi == 1 and indxj == 0 and self.pos_dict['arr'][4][0] != 'E')):
                    continue
                elif(self.pos_dict['arr'][2 * indxi][4 * indxj] != 'E'):
                    self.pos_dict['arr'][2 * indxi][4 * indxj] = 'E'
                    self.pos_dict['arr'][2 * indxi][4 * indxj + 1] = 'E'
                    self.pos_dict['arr'][2 * indxi][4 * indxj + 2] = 'E'
                    self.pos_dict['arr'][2 * indxi][4 * indxj + 3] = 'E'
                    self.pos_dict['arr'][2 * indxi + 1][4 * indxj] = 'E'
                    self.pos_dict['arr'][2 * indxi + 1][4 * indxj + 1] = 'E'
                    self.pos_dict['arr'][2 * indxi + 1][4 * indxj + 2] = 'E'
                    self.pos_dict['arr'][2 * indxi + 1][4 * indxj + 3] = 'E'
                    if(count == 0):
                        self.pos_dict['ecord'] = []
                    self.pos_dict['ecord'].append(
                        {'ic': 2 * indxi, 'jc': 4 * indxj, 'dir': 'l'})
                    count += 1

        for i in range(10):
            for j in range(16):
                if(4 * i + 5 < 40):
                    self.pos_dict['arr'][4 * i + 4][8 * j + 4] = 'X'
                    self.pos_dict['arr'][4 * i + 4][8 * j + 5] = 'X'
                    self.pos_dict['arr'][4 * i + 4][8 * j + 6] = 'X'
                    self.pos_dict['arr'][4 * i + 4][8 * j + 7] = 'X'
                    self.pos_dict['arr'][4 * i + 5][8 * j + 4] = 'X'
                    self.pos_dict['arr'][4 * i + 5][8 * j + 5] = 'X'
                    self.pos_dict['arr'][4 * i + 5][8 * j + 6] = 'X'
                    self.pos_dict['arr'][4 * i + 5][8 * j + 7] = 'X'

        self.pos_dict['posx0'] = 0
        self.pos_dict['posx1'] = 1
        self.pos_dict['posx2'] = 2
        self.pos_dict['posx3'] = 3

        self.pos_dict['posy0'] = 2
        self.pos_dict['posy1'] = 3
        self.pos_dict['arr'][self.pos_dict['posy0']
                             ][self.pos_dict['posx0']] = 'B'
        self.pos_dict['arr'][self.pos_dict['posy0']
                             ][self.pos_dict['posx1']] = 'B'
        self.pos_dict['arr'][self.pos_dict['posy0']
                             ][self.pos_dict['posx2']] = 'B'
        self.pos_dict['arr'][self.pos_dict['posy0']
                             ][self.pos_dict['posx3']] = 'B'
        self.pos_dict['arr'][self.pos_dict['posy1']
                             ][self.pos_dict['posx0']] = 'B'
        self.pos_dict['arr'][self.pos_dict['posy1']
                             ][self.pos_dict['posx1']] = 'B'
        self.pos_dict['arr'][self.pos_dict['posy1']
                             ][self.pos_dict['posx2']] = 'B'
        self.pos_dict['arr'][self.pos_dict['posy1']
                             ][self.pos_dict['posx3']] = 'B'

    def get_dict(self):
        return self.pos_dict

    def set_dict(self, pos_dict):
        self.pos_dict = pos_dict

    def printscr(self):
        pos_dict = self.pos_dict
        arr = pos_dict['arr']
        os.system('clear')
        print("\x1b[8;50;150t")
        for i in range(42):
            print("#####", end='')
            for j in range(132):
                if(pos_dict['arr'][i][j] == 'B'):
                    print("\033[1;34;48m" + 'B' + "\033[0m", end='')
                elif(pos_dict['arr'][i][j] == 'E' and i != 0 and i != 1):
                    print("\033[1;31;48m" + 'E' + "\033[0m", end='')
                elif((pos_dict['arr'][i][j] == '1' or pos_dict['arr'][i][j] == '2' or pos_dict['arr'][i][j] == '0') and i != 0 and i != 1):
                    print("\033[1;32;48m" + pos_dict['arr']
                          [i][j] + "\033[0m", end='')
                elif(pos_dict['arr'][i][j] == 'e'):
                    print("\033[1;33;48m" + 'e' + "\033[0m", end='')
                elif(i == 0 and pos_dict['arr'][i][j] != '#'):
                    print("\033[1;33;48m" + arr[i][j] + "\033[0m", end='')
                elif(i == 1 and pos_dict['arr'][i][j] != '#'):
                    print("\033[1;33;48m" + arr[i][j] + "\033[0m", end='')
                else:
                    print(pos_dict['arr'][i][j], end='')
            print("######", end='')

    def put_bomb(self, x0, x1, x2, x3, y0, y1):
        pos_dict = self.get_dict()
        if(pos_dict['bomb_timer'] >= 2.6):
            pos_dict['arr'][y0][x0] = str(int(pos_dict['bomb_timer']))[0]
            pos_dict['arr'][y0][x1] = str(int(pos_dict['bomb_timer']))[0]
            pos_dict['arr'][y0][x2] = str(int(pos_dict['bomb_timer']))[0]
            pos_dict['arr'][y0][x3] = str(int(pos_dict['bomb_timer']))[0]
            pos_dict['arr'][y1][x0] = str(int(pos_dict['bomb_timer']))[0]
            pos_dict['arr'][y1][x1] = str(int(pos_dict['bomb_timer']))[0]
            pos_dict['arr'][y1][x2] = str(int(pos_dict['bomb_timer']))[0]
            pos_dict['arr'][y1][x3] = str(int(pos_dict['bomb_timer']))[0]
        else:
            pos_dict['arr'][y0][x0] = '1'
            pos_dict['arr'][y0][x1] = '1'
            pos_dict['arr'][y0][x2] = '1'
            pos_dict['arr'][y0][x3] = '1'
            pos_dict['arr'][y1][x0] = '1'
            pos_dict['arr'][y1][x1] = '1'
            pos_dict['arr'][y1][x2] = '1'
            pos_dict['arr'][y1][x3] = '1'
        self.set_dict(pos_dict)

    def update_score_life(self):
        pos_dict = self.get_dict()
        score = str(pos_dict['score'])
        life = str(pos_dict['lives'])
        for i in range(len(score)):
            pos_dict['arr'][0][56 + i] = score[i]
        for i in range(len(life)):
            pos_dict['arr'][1][56 + i] = life[i]
        self.set_dict(pos_dict)


board = Board()
board.init()
