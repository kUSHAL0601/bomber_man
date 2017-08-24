# CREATED BY MajAK

from subprocess import call
import os
import time
import _thread
import sys
import tty
import termios
from random import randint

import board
import person
import bomberman
import enemy
import bomb

bomber_man = bomberman.Bomberman()
enemy = enemy.Enemy()
bomb = bomb.Bomb()


def input_thread(L):
    pos_dict = board.board.get_dict()
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        board.board.printscr()
        ch = sys.stdin.read(1)
        if(ch == 'd' and pos_dict['posx3'] + 4 < 132 and pos_dict['arr'][pos_dict['posy0']][pos_dict['posx3'] + 4] != '#' and pos_dict['arr'][pos_dict['posy0']][pos_dict['posx3'] + 4] != 'X' and pos_dict['arr'][pos_dict['posy0']][pos_dict['posx3'] + 4] != 'O' and pos_dict['arr'][pos_dict['posy0']][pos_dict['posx3'] + 4] != '/'):
            bomber_man.put_bomber(pos_dict['posx0'], pos_dict['posx1'], pos_dict['posx2'],
                                  pos_dict['posx3'], pos_dict['posy0'], pos_dict['posy1'], 0, 4)
            bomber_man.move_right()
            pos_dict = board.board.get_dict()

        elif(ch == 'a' and pos_dict['posx1'] - 4 > 0 and pos_dict['arr'][pos_dict['posy0']][pos_dict['posx0'] - 4] != '#' and pos_dict['arr'][pos_dict['posy0']][pos_dict['posx0'] - 4] != 'X' and pos_dict['arr'][pos_dict['posy0']][pos_dict['posx0'] - 4] != 'O' and pos_dict['arr'][pos_dict['posy0']][pos_dict['posx0'] - 4] != '/'):
            bomber_man.put_bomber(pos_dict['posx0'], pos_dict['posx1'], pos_dict['posx2'],
                                  pos_dict['posx3'], pos_dict['posy0'], pos_dict['posy1'], 0, -4)
            bomber_man.move_left()
            pos_dict = board.board.get_dict()

        elif(ch == 's' and pos_dict['posy1'] + 1 < 42 and pos_dict['arr'][pos_dict['posy1'] + 1][pos_dict['posx3']] != '#' and pos_dict['arr'][pos_dict['posy1'] + 1][pos_dict['posx3']] != 'X' and pos_dict['arr'][pos_dict['posy1'] + 1][pos_dict['posx3']] != 'O' and pos_dict['arr'][pos_dict['posy1'] + 1][pos_dict['posx3']] != '/'):
            bomber_man.put_bomber(pos_dict['posx0'], pos_dict['posx1'], pos_dict['posx2'],
                                  pos_dict['posx3'], pos_dict['posy0'], pos_dict['posy1'], 2, 0)
            bomber_man.move_down()
            pos_dict = board.board.get_dict()

        elif(ch == 'w' and pos_dict['posy0'] - 1 > 0 and pos_dict['arr'][pos_dict['posy0'] - 1][pos_dict['posx3']] != '#' and pos_dict['arr'][pos_dict['posy0'] - 1][pos_dict['posx3']] != 'X' and pos_dict['arr'][pos_dict['posy0'] - 1][pos_dict['posx3']] != 'O' and pos_dict['arr'][pos_dict['posy0'] - 1][pos_dict['posx3']] != '/'):
            bomber_man.put_bomber(pos_dict['posx0'], pos_dict['posx1'], pos_dict['posx2'],
                                  pos_dict['posx3'], pos_dict['posy0'], pos_dict['posy1'], -2, 0)
            bomber_man.move_up()
            pos_dict = board.board.get_dict()

        elif(ch == 'b' and pos_dict['bomb_timer'] == 0.0 and pos_dict['bomb_plant'] == 0):
            bomb.init()

        elif(ch == 'q'):
            sys.exit(0)

        board.board.set_dict(pos_dict)
        L.append(None)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def do_print():
    L = []
    pos_dict = board.board.get_dict()
    _thread.start_new_thread(input_thread, (L,))
    while 1:
        if(pos_dict['bomb_timer'] != 0.0):
            while(L == []):
                if(pos_dict['refresh'] == 0):
                    if(pos_dict['bomb_timer'] > 2.15):
                        enemy.move()
                        pos_dict = board.board.get_dict()
                        time.sleep(0.01)
                else:
                    time.sleep(0.25)
                pos_dict['bomb_timer'] -= 0.25
                if(pos_dict['bomb_timer'] == 1.25):
                    bomb.level1_explode()
                    pos_dict = board.board.get_dict()
                elif(pos_dict['bomb_timer'] == 1.0 and pos_dict['refresh'] == 0):
                    bomb.level2_explode()
                    pos_dict = board.board.get_dict()
                elif(pos_dict['bomb_timer'] == 0.75 and pos_dict['refresh'] == 0):
                    bomb.level3_explode()
                    pos_dict = board.board.get_dict()
                elif(pos_dict['bomb_timer'] == 0.5 and pos_dict['refresh'] == 0):
                    bomb.level4_explode()
                    pos_dict = board.board.get_dict()
                elif(pos_dict['bomb_timer'] == 0.25 and pos_dict['refresh'] == 0):
                    board.board.printscr()
                if(pos_dict['bomb_plant'] == 1 and pos_dict['bomb_timer'] == 0.0 and pos_dict['refresh'] == 0):
                    bomb.blast_bomb()
                    pos_dict = board.board.get_dict()
                    break
                if(pos_dict['refresh'] == 1):
                    board.board.init()
                    break
        else:
            enemy.move()
            pos_dict = board.board.get_dict()
            if(pos_dict['refresh'] == 1):
                board.board.init()
                pos_dict=board.board.get_dict()
        if L:
            break


while True:
    pos_dict = board.board.get_dict()
    if(pos_dict['lives'] == 0):
        sys.exit(0)
    else:
        do_print()
