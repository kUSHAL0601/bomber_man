# CREATED BY MajAK

import board
import person
from random import randint
import time


class Enemy(person.Person):
    def __init__(self):
        person.Person.__init__(self, 18, 61, "e")

    def move(self):
        pos_dict = board.board.get_dict()
        count = 0
        for i in pos_dict['ecord']:
            icord = i['ic']
            jcord = i['jc']
            direc = i['dir']
            rnd_dir = []
            if(direc == 'r'):
                if(jcord + 4 < 132 and (pos_dict['arr'][icord][jcord + 4] == ' ' or pos_dict['arr'][icord][jcord + 4] == 'B')):
                    if(pos_dict['arr'][icord][jcord + 4] == 'B'):
                        pos_dict['lives'] -= 1
                        pos_dict['refresh'] = 1
                        break
                    self.move_right(icord, jcord)
                    pos_dict = board.board.get_dict()
                    ((pos_dict['ecord'])[count])['jc'] += 4
                    if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                        board.board.put_bomb(pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'],
                                             pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                    time.sleep(0.125)
                else:
                    if(jcord - 4 > 0 and (pos_dict['arr'][icord][jcord - 4] == ' ' or pos_dict['arr'][icord][jcord - 4] == 'B')):
                        if(pos_dict['arr'][icord][jcord - 4] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('l')
                    if(icord + 2 < 42 and (pos_dict['arr'][icord + 2][jcord + 3] == ' ' or pos_dict['arr'][icord + 2][jcord + 3] == 'B')):
                        if(pos_dict['arr'][icord + 2][jcord + 3] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('d')
                    if(icord - 2 > 0 and (pos_dict['arr'][icord - 2][jcord + 3] == ' ' or pos_dict['arr'][icord - 2][jcord + 3] == ' ')):
                        if(pos_dict['arr'][icord - 2][jcord + 3] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('u')
                    if(len(rnd_dir) == 0):
                        count += 1
                        continue
                    else:
                        ri = randint(0, len(rnd_dir) - 1)
                        if(rnd_dir[ri] == 'l'):
                            self.move_left(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['jc'] -= 4
                            ((pos_dict['ecord'])[count])['dir'] = 'l'
                            direc = 'l'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
                        if(rnd_dir[ri] == 'd'):
                            self.move_down(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['ic'] += 2
                            ((pos_dict['ecord'])[count])['dir'] = 'd'
                            direc = 'd'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
                        if(rnd_dir[ri] == 'u'):
                            self.move_up(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['ic'] -= 2
                            ((pos_dict['ecord'])[count])['dir'] = 'u'
                            direc = 'u'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
            elif(direc == 'l'):
                if(jcord - 4 > 0 and (pos_dict['arr'][icord][jcord - 4] == ' ' or pos_dict['arr'][icord][jcord - 4] == 'B')):
                    if(pos_dict['arr'][icord][jcord - 4] == 'B'):
                        pos_dict['lives'] -= 1
                        pos_dict['refresh'] = 1
                        break
                    self.move_left(icord, jcord)
                    pos_dict = board.board.get_dict()
                    ((pos_dict['ecord'])[count])['jc'] -= 4
                    if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                        board.board.put_bomb(pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'],
                                             pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                    time.sleep(0.125)
                else:
                    if(jcord + 4 < 132 and (pos_dict['arr'][icord][jcord + 4] == ' ' or pos_dict['arr'][icord][jcord + 4] == 'B')):
                        if(pos_dict['arr'][icord][jcord + 4] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('r')
                    if(icord + 2 < 42 and (pos_dict['arr'][icord + 2][jcord + 3] == ' ' or pos_dict['arr'][icord + 2][jcord + 3] == 'B')):
                        if(pos_dict['arr'][icord + 2][jcord + 3] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('d')
                    if(icord - 2 > 0 and (pos_dict['arr'][icord - 2][jcord + 3] == ' ' or pos_dict['arr'][icord - 2][jcord + 3] == 'B')):
                        if(pos_dict['arr'][icord - 2][jcord + 3] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('u')
                    if(len(rnd_dir) == 0):
                        count += 1
                        continue
                    else:
                        ri = randint(0, len(rnd_dir) - 1)
                        if(rnd_dir[ri] == 'r'):
                            self.move_right(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['jc'] += 4
                            ((pos_dict['ecord'])[count])['dir'] = 'r'
                            direc = 'r'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
                        if(rnd_dir[ri] == 'd'):
                            self.move_down(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['ic'] += 2
                            ((pos_dict['ecord'])[count])['dir'] = 'd'
                            direc = 'd'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
                        if(rnd_dir[ri] == 'u'):
                            self.move_up(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['ic'] -= 2
                            ((pos_dict['ecord'])[count])['dir'] = 'u'
                            direc = 'u'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
            elif(direc == 'd'):
                if(icord + 2 < 42 and (pos_dict['arr'][icord + 2][jcord + 3] == ' ' or pos_dict['arr'][icord + 2][jcord + 3] == 'B')):
                    if(pos_dict['arr'][icord + 2][jcord + 3] == 'B'):
                        pos_dict['lives'] -= 1
                        pos_dict['refresh'] = 1
                        break
                    self.move_down(icord, jcord)
                    pos_dict = board.board.get_dict()
                    ((pos_dict['ecord'])[count])['ic'] += 2
                    if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                        board.board.put_bomb(pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'],
                                             pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                    time.sleep(0.125)
                else:
                    if(jcord - 4 > 0 and (pos_dict['arr'][icord][jcord - 4] == ' ' or pos_dict['arr'][icord][jcord - 4] == 'B')):
                        if(pos_dict['arr'][icord][jcord - 4] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('l')
                    if(jcord + 4 < 132 and (pos_dict['arr'][icord][jcord + 4] == ' ' or pos_dict['arr'][icord][jcord + 4] == 'B')):
                        if(pos_dict['arr'][icord][jcord + 4] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('r')
                    if(icord - 2 > 0 and (pos_dict['arr'][icord - 2][jcord + 3] == ' ' or pos_dict['arr'][icord - 2][jcord + 3] == ' ')):
                        if(pos_dict['arr'][icord - 2][jcord + 3] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('u')
                    if(len(rnd_dir) == 0):
                        count += 1
                        continue
                    else:
                        ri = randint(0, len(rnd_dir) - 1)
                        if(rnd_dir[ri] == 'l'):
                            self.move_left(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['jc'] -= 4
                            ((pos_dict['ecord'])[count])['dir'] = 'l'
                            direc = 'l'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
                        if(rnd_dir[ri] == 'r'):
                            self.move_right(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['jc'] += 4
                            ((pos_dict['ecord'])[count])['dir'] = 'r'
                            direc = 'r'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
                        if(rnd_dir[ri] == 'u'):
                            self.move_up(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['ic'] -= 2
                            ((pos_dict['ecord'])[count])['dir'] = 'u'
                            direc = 'u'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
            elif(direc == 'u'):
                if(icord - 2 > 0 and (pos_dict['arr'][icord - 2][jcord + 3] == ' ' or pos_dict['arr'][icord - 2][jcord + 3] == 'B')):
                    if(pos_dict['arr'][icord - 2][jcord + 3] == 'B'):
                        pos_dict['lives'] -= 1
                        pos_dict['refresh'] = 1
                        break
                    self.move_up(icord, jcord)
                    pos_dict = board.board.get_dict()
                    ((pos_dict['ecord'])[count])['ic'] -= 2
                    if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                        board.board.put_bomb(pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'],
                                             pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                    time.sleep(0.125)
                else:
                    if(jcord - 4 > 0 and (pos_dict['arr'][icord][jcord - 4] == ' ' or pos_dict['arr'][icord][jcord - 4] == 'B')):
                        if(pos_dict['arr'][icord][jcord - 4] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('l')
                    if(jcord + 4 < 132 and (pos_dict['arr'][icord][jcord + 4] == ' ' or pos_dict['arr'][icord][jcord + 4] == 'B')):
                        if(pos_dict['arr'][icord][jcord + 4] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('r')
                    if(icord + 2 < 42 and (pos_dict['arr'][icord + 2][jcord + 3] == ' ' or pos_dict['arr'][icord + 2][jcord + 3] == 'B')):
                        if(pos_dict['arr'][icord + 2][jcord + 3] == 'B'):
                            pos_dict['lives'] -= 1
                            pos_dict['refresh'] = 1
                            break
                        rnd_dir.append('d')
                    if(len(rnd_dir) == 0):
                        count += 1
                        continue
                    else:
                        ri = randint(0, len(rnd_dir) - 1)
                        if(rnd_dir[ri] == 'l'):
                            self.move_left(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['jc'] -= 4
                            ((pos_dict['ecord'])[count])['dir'] = 'l'
                            direc = 'l'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
                        if(rnd_dir[ri] == 'r'):
                            self.move_right(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['jc'] += 4
                            ((pos_dict['ecord'])[count])['dir'] = 'r'
                            direc = 'r'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
                        if(rnd_dir[ri] == 'd'):
                            self.move_down(icord, jcord)
                            pos_dict = board.board.get_dict()
                            ((pos_dict['ecord'])[count])['ic'] += 2
                            ((pos_dict['ecord'])[count])['dir'] = 'd'
                            direc = 'd'
                            if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
                                board.board.put_bomb(
                                    pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'], pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
                            time.sleep(0.125)
            count += 1

        board.board.printscr()
        time.sleep(0.125)
        board.board.set_dict(pos_dict)

    def move_right(self, icord, jcord):
        pos_dict = board.board.get_dict()
        pos_dict['arr'][icord][jcord] = ' '
        pos_dict['arr'][icord][jcord + 1] = ' '
        pos_dict['arr'][icord][jcord + 2] = ' '
        pos_dict['arr'][icord][jcord + 3] = ' '
        pos_dict['arr'][icord + 1][jcord] = ' '
        pos_dict['arr'][icord + 1][jcord + 1] = ' '
        pos_dict['arr'][icord + 1][jcord + 2] = ' '
        pos_dict['arr'][icord + 1][jcord + 3] = ' '
        pos_dict['arr'][icord][jcord + 4] = 'E'
        pos_dict['arr'][icord][jcord + 1 + 4] = 'E'
        pos_dict['arr'][icord][jcord + 2 + 4] = 'E'
        pos_dict['arr'][icord][jcord + 3 + 4] = 'E'
        pos_dict['arr'][icord + 1][jcord + 4] = 'E'
        pos_dict['arr'][icord + 1][jcord + 1 + 4] = 'E'
        pos_dict['arr'][icord + 1][jcord + 2 + 4] = 'E'
        pos_dict['arr'][icord + 1][jcord + 3 + 4] = 'E'
        board.board.set_dict(pos_dict)

    def move_left(self, icord, jcord):
        pos_dict = board.board.get_dict()
        pos_dict['arr'][icord][jcord] = ' '
        pos_dict['arr'][icord][jcord + 1] = ' '
        pos_dict['arr'][icord][jcord + 2] = ' '
        pos_dict['arr'][icord][jcord + 3] = ' '
        pos_dict['arr'][icord + 1][jcord] = ' '
        pos_dict['arr'][icord + 1][jcord + 1] = ' '
        pos_dict['arr'][icord + 1][jcord + 2] = ' '
        pos_dict['arr'][icord + 1][jcord + 3] = ' '
        pos_dict['arr'][icord][jcord - 4] = 'E'
        pos_dict['arr'][icord][jcord + 1 - 4] = 'E'
        pos_dict['arr'][icord][jcord + 2 - 4] = 'E'
        pos_dict['arr'][icord][jcord + 3 - 4] = 'E'
        pos_dict['arr'][icord + 1][jcord - 4] = 'E'
        pos_dict['arr'][icord + 1][jcord + 1 - 4] = 'E'
        pos_dict['arr'][icord + 1][jcord + 2 - 4] = 'E'
        pos_dict['arr'][icord + 1][jcord + 3 - 4] = 'E'
        board.board.set_dict(pos_dict)

    def move_down(self, icord, jcord):
        pos_dict = board.board.get_dict()
        pos_dict['arr'][icord][jcord] = ' '
        pos_dict['arr'][icord][jcord + 1] = ' '
        pos_dict['arr'][icord][jcord + 2] = ' '
        pos_dict['arr'][icord][jcord + 3] = ' '
        pos_dict['arr'][icord + 1][jcord] = ' '
        pos_dict['arr'][icord + 1][jcord + 1] = ' '
        pos_dict['arr'][icord + 1][jcord + 2] = ' '
        pos_dict['arr'][icord + 1][jcord + 3] = ' '
        pos_dict['arr'][icord + 2][jcord] = 'E'
        pos_dict['arr'][icord + 2][jcord + 1] = 'E'
        pos_dict['arr'][icord + 2][jcord + 2] = 'E'
        pos_dict['arr'][icord + 2][jcord + 3] = 'E'
        pos_dict['arr'][icord + 1 + 2][jcord] = 'E'
        pos_dict['arr'][icord + 1 + 2][jcord + 1] = 'E'
        pos_dict['arr'][icord + 1 + 2][jcord + 2] = 'E'
        pos_dict['arr'][icord + 1 + 2][jcord + 3] = 'E'
        board.board.set_dict(pos_dict)

    def move_up(self, icord, jcord):
        pos_dict = board.board.get_dict()
        pos_dict['arr'][icord][jcord] = ' '
        pos_dict['arr'][icord][jcord + 1] = ' '
        pos_dict['arr'][icord][jcord + 2] = ' '
        pos_dict['arr'][icord][jcord + 3] = ' '
        pos_dict['arr'][icord + 1][jcord] = ' '
        pos_dict['arr'][icord + 1][jcord + 1] = ' '
        pos_dict['arr'][icord + 1][jcord + 2] = ' '
        pos_dict['arr'][icord + 1][jcord + 3] = ' '
        pos_dict['arr'][icord - 2][jcord] = 'E'
        pos_dict['arr'][icord - 2][jcord + 1] = 'E'
        pos_dict['arr'][icord - 2][jcord + 2] = 'E'
        pos_dict['arr'][icord - 2][jcord + 3] = 'E'
        pos_dict['arr'][icord + 1 - 2][jcord] = 'E'
        pos_dict['arr'][icord + 1 - 2][jcord + 1] = 'E'
        pos_dict['arr'][icord + 1 - 2][jcord + 2] = 'E'
        pos_dict['arr'][icord + 1 - 2][jcord + 3] = 'E'
        board.board.set_dict(pos_dict)
