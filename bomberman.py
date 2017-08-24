# CREATED BY MajAK

import board
import person


class Bomberman(person.Person):
    def __init__(self):
        person.Person.__init__(self, 0, 2, "b")

    def put_bomber(self, x0, x1, x2, x3, y0, y1, yconst, xconst):
        pos_dict = board.board.get_dict()
        pos_dict['arr'][y0][x0] = ' '
        pos_dict['arr'][y0][x1] = ' '
        pos_dict['arr'][y0][x2] = ' '
        pos_dict['arr'][y0][x3] = ' '
        pos_dict['arr'][y1][x0] = ' '
        pos_dict['arr'][y1][x1] = ' '
        pos_dict['arr'][y1][x2] = ' '
        pos_dict['arr'][y1][x3] = ' '
        pos_dict['arr'][y0 + yconst][x0 + xconst] = 'B'
        pos_dict['arr'][y0 + yconst][x1 + xconst] = 'B'
        pos_dict['arr'][y0 + yconst][x2 + xconst] = 'B'
        pos_dict['arr'][y0 + yconst][x3 + xconst] = 'B'
        pos_dict['arr'][y1 + yconst][x0 + xconst] = 'B'
        pos_dict['arr'][y1 + yconst][x1 + xconst] = 'B'
        pos_dict['arr'][y1 + yconst][x2 + xconst] = 'B'
        pos_dict['arr'][y1 + yconst][x3 + xconst] = 'B'
        board.board.set_dict(pos_dict)

    def move_right(self):
        pos_dict = board.board.get_dict()
        pos_dict['posx0'] += 4
        pos_dict['posx1'] += 4
        pos_dict['posx2'] += 4
        pos_dict['posx3'] += 4
        if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
            board.board.put_bomb(pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'],
                                 pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
        board.board.printscr()
        board.board.set_dict(pos_dict)

    def move_left(self):
        pos_dict = board.board.get_dict()
        pos_dict['posx0'] -= 4
        pos_dict['posx1'] -= 4
        pos_dict['posx2'] -= 4
        pos_dict['posx3'] -= 4
        if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
            board.board.put_bomb(pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'],
                                 pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
        board.board.printscr()
        board.board.set_dict(pos_dict)

    def move_up(self):
        pos_dict = board.board.get_dict()
        pos_dict['posy0'] -= 2
        pos_dict['posy1'] -= 2
        if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
            board.board.put_bomb(pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'],
                                 pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
        board.board.printscr()
        board.board.set_dict(pos_dict)

    def move_down(self):
        pos_dict = board.board.get_dict()
        pos_dict['posy0'] += 2
        pos_dict['posy1'] += 2
        if(pos_dict['bomb_timer'] != 0.0 and pos_dict['bomb_plant'] == 1):
            board.board.put_bomb(pos_dict['bombx0'], pos_dict['bombx1'], pos_dict['bombx2'],
                                 pos_dict['bombx3'], pos_dict['bomby0'], pos_dict['bomby1'])
        board.board.printscr()
        board.board.set_dict(pos_dict)
