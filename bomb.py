# CREATED BY MajAK

import board


class Bomb():
    def init(self):
        pos_dict = board.board.get_dict()
        pos_dict['bomb_timer'] = 2.75
        pos_dict['bomb_plant'] = 1
        pos_dict['bombx0'] = pos_dict['posx0']
        pos_dict['bombx1'] = pos_dict['posx1']
        pos_dict['bombx2'] = pos_dict['posx2']
        pos_dict['bombx3'] = pos_dict['posx3']
        pos_dict['bomby0'] = pos_dict['posy0']
        pos_dict['bomby1'] = pos_dict['posy1']
        board.board.set_dict(pos_dict)

    def blast_bomb(self):
        pos_dict = board.board.get_dict()
        pos_dict['bomb_plant'] = 0
        pos_dict['bomb_timer'] = 0.0
        pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0']] = ' '
        pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx1']] = ' '
        pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx2']] = ' '
        pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3']] = ' '
        pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx0']] = ' '
        pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx1']] = ' '
        pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx2']] = ' '
        pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx3']] = ' '

        if(pos_dict['bomby0'] - 1 != 0 and pos_dict['bomby0'] - 1 != 1 and pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx0']] != '#' and pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx0']] != 'X'):
            pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx0']] = ' '
            pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx1']] = ' '
            pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx2']] = ' '
            pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx3']] = ' '

        if(pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx0']] != '#' and pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx0']] != 'X'):
            pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx0']] = ' '
            pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx1']] = ' '
            pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx2']] = ' '
            pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx3']] = ' '

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 1] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 1] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 1] = ' '
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx0'] - 1] = ' '

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 1] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 1] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 1] = ' '
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx3'] + 1] = ' '

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 2] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 2] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 2] = ' '
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx0'] - 2] = ' '

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 2] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 2] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 2] = ' '
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx3'] + 2] = ' '

        if(pos_dict['bomby0'] - 2 != 0 and pos_dict['bomby0'] - 2 != 1 and pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx0']] != '#' and pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx0']] != 'X'):
            pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx0']] = ' '
            pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx1']] = ' '
            pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx2']] = ' '
            pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx3']] = ' '

        if(pos_dict['arr'][pos_dict['bomby0'] + 2][pos_dict['bombx0']] != '#' and pos_dict['arr'][pos_dict['bomby0'] + 2][pos_dict['bombx0']] != 'X'):
            pos_dict['arr'][pos_dict['bomby1'] + 2][pos_dict['bombx0']] = ' '
            pos_dict['arr'][pos_dict['bomby1'] + 2][pos_dict['bombx1']] = ' '
            pos_dict['arr'][pos_dict['bomby1'] + 2][pos_dict['bombx2']] = ' '
            pos_dict['arr'][pos_dict['bomby1'] + 2][pos_dict['bombx3']] = ' '

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 3] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 3] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 3] = ' '
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx0'] - 3] = ' '

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 3] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 3] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 3] = ' '
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx3'] + 3] = ' '

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 4] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 4] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 4] = ' '
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx0'] - 4] = ' '

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 4] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 4] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 4] = ' '
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx3'] + 4] = ' '

        board.board.set_dict(pos_dict)
        board.board.printscr()
        return

    def level1_explode(self):
        pos_dict = board.board.get_dict()
        if(pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx0']] == 'B'):
            pos_dict['lives'] -= 1
            pos_dict['refresh'] = 1
            board.board.set_dict(pos_dict)
            return
        elif(pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx0']] == 'B'):
            pos_dict['lives'] -= 1
            pos_dict['refresh'] = 1
            board.board.set_dict(pos_dict)
            return
        elif(pos_dict['bombx0'] - 4 > 0 and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 4] == 'B'):
            pos_dict['lives'] -= 1
            pos_dict['refresh'] = 1
            board.board.set_dict(pos_dict)
            return
        elif(pos_dict['bombx0'] + 4 < 132 and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] + 4] == 'B'):
            pos_dict['lives'] -= 1
            pos_dict['refresh'] = 1
            board.board.set_dict(pos_dict)
            return
        elif(pos_dict['bombx0'] == pos_dict['posx0'] and pos_dict['bomby0'] == pos_dict['posy0']):
            pos_dict['lives'] -= 1
            pos_dict['refresh'] = 1
            board.board.set_dict(pos_dict)
            return

        if(pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx0']] == '/'):
            pos_dict['score'] += 20
        if(pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx0']] == '/'):
            pos_dict['score'] += 20
        if(pos_dict['bombx0'] - 4 and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 4] == '/'):
            pos_dict['score'] += 20
        if(pos_dict['bombx0'] + 4 < 132 and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] + 4] == '/'):
            pos_dict['score'] += 20

        if(pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx0']] == 'E'):
            pos_dict['score'] += 100
            left = []
            for i in range(len(pos_dict['ecord'])):
                if(pos_dict['ecord'][i]['ic'] != pos_dict['bomby0'] - 2 or pos_dict['ecord'][i]['jc'] != pos_dict['bombx0']):
                    left.append(pos_dict['ecord'][i])
            pos_dict['ecord'] = left
        if(pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx0']] == 'E'):
            pos_dict['score'] += 100
            left = []
            for i in range(len(pos_dict['ecord'])):
                if(pos_dict['ecord'][i]['ic'] != pos_dict['bomby1'] + 1 or pos_dict['ecord'][i]['jc'] != pos_dict['bombx0']):
                    left.append(pos_dict['ecord'][i])
            pos_dict['ecord'] = left
        if(pos_dict['bombx0'] - 4 > 0 and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 4] == 'E'):
            pos_dict['score'] += 100
            left = []
            for i in range(len(pos_dict['ecord'])):
                if(pos_dict['ecord'][i]['ic'] != pos_dict['bomby0'] or pos_dict['ecord'][i]['jc'] != pos_dict['bombx0'] - 4):
                    left.append(pos_dict['ecord'][i])
            pos_dict['ecord'] = left
        if(pos_dict['bombx0'] + 4 < 132 and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] + 4] == 'E'):
            left = []
            for i in range(len(pos_dict['ecord'])):
                if(pos_dict['ecord'][i]['ic'] != pos_dict['bomby0'] or pos_dict['ecord'][i]['jc'] != pos_dict['bombx0'] + 4):
                    left.append(pos_dict['ecord'][i])
            pos_dict['ecord'] = left
            pos_dict['score'] += 100
        if(len(pos_dict['ecord']) == 0):
            time.sleep(100)
            system.exit(0)

        if(pos_dict['bomby0'] - 1 != 0 and pos_dict['bomby0'] - 1 != 1 and pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx0']] != '#' and pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx0']] != 'X'):
            pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx0']] = 'e'
            pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx1']] = 'e'
            pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx2']] = 'e'
            pos_dict['arr'][pos_dict['bomby0'] - 1][pos_dict['bombx3']] = 'e'
        if(pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx0']] != '#' and pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx0']] != 'X'):
            pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx0']] = 'e'
            pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx1']] = 'e'
            pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx2']] = 'e'
            pos_dict['arr'][pos_dict['bomby1'] + 1][pos_dict['bombx3']] = 'e'

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 1] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 1] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 1] = 'e'
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx0'] - 1] = 'e'

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 1] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 1] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 1] = 'e'
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx3'] + 1] = 'e'

        pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0']] = '0'
        pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx1']] = '0'
        pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx2']] = '0'
        pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3']] = '0'
        pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx0']] = '0'
        pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx1']] = '0'
        pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx2']] = '0'
        pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx3']] = '0'

        board.board.set_dict(pos_dict)
        board.board.printscr()
        return

    def level2_explode(self):
        pos_dict = board.board.get_dict()
        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 2] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 2] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 2] = 'e'
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx0'] - 2] = 'e'

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 2] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 2] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 2] = 'e'
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx3'] + 2] = 'e'

        board.board.set_dict(pos_dict)
        board.board.printscr()
        return

    def level3_explode(self):
        pos_dict = board.board.get_dict()
        if(pos_dict['bomby0'] - 2 != 0 and pos_dict['bomby0'] - 2 != 1 and pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx0']] != '#' and pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx0']] != 'X'):
            pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx0']] = 'e'
            pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx1']] = 'e'
            pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx2']] = 'e'
            pos_dict['arr'][pos_dict['bomby0'] - 2][pos_dict['bombx3']] = 'e'

        if(pos_dict['arr'][pos_dict['bomby1'] + 2][pos_dict['bombx0']] != '#' and pos_dict['arr'][pos_dict['bomby1'] + 2][pos_dict['bombx0']] != 'X'):
            pos_dict['arr'][pos_dict['bomby1'] + 2][pos_dict['bombx0']] = 'e'
            pos_dict['arr'][pos_dict['bomby1'] + 2][pos_dict['bombx1']] = 'e'
            pos_dict['arr'][pos_dict['bomby1'] + 2][pos_dict['bombx2']] = 'e'
            pos_dict['arr'][pos_dict['bomby1'] + 2][pos_dict['bombx3']] = 'e'

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 3] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 3] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 3] = 'e'
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx0'] - 3] = 'e'

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 3] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 3] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 3] = 'e'
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx3'] + 3] = 'e'

        board.board.set_dict(pos_dict)
        board.board.printscr()
        return

    def level4_explode(pos_dict):
        pos_dict = board.board.get_dict()
        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 4] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 4] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx0'] - 4] = 'e'
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx0'] - 4] = 'e'

        if(pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 4] != '#' and pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 4] != 'X'):
            pos_dict['arr'][pos_dict['bomby0']][pos_dict['bombx3'] + 4] = 'e'
            pos_dict['arr'][pos_dict['bomby1']][pos_dict['bombx3'] + 4] = 'e'
        board.board.update_score_life()
        pos_dict = board.board.get_dict()
        board.board.set_dict(pos_dict)
        board.board.printscr()
        return
