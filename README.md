+ This is the basic version of THE BOMBERMAN game in python
+ No external libraries are used here

HOW TO PLAY:
============

+ Simply enter python3 main.py and play

REQUIRMENTS:
============

+ Normal GNOME-TERMINAL
+ Python3 with all inbuilt libraries loaded
+ A player to play :wink:

BASIC CONSTRUCTION:
===================

+ No special libraries are used so it consists of long codes
+ For input **stdin** has been used to get single character.
+ It is made sure that continiously keeping the key pressed doesn't make bomberman to move at a high pace.
+ Basic **OOPS** concepts used
+ **THREADING** has been used which makes all movements happen together.

MODULES:
--------
1. [main.py](./main.py) : File where the main loop is ran
2. [board.py](./board.py) : File with functions to manipulate board
3. [person.py](./person.py) : File with basic layout for *Bomberman* and *Enemies*
4. [bomberman.py](./bomberman.py) :File with functions to manipulate *Bomberman*
5. [enemy.py](./enemy.py) : File with functions to manipulate *Enemy*
6. [bomb.py](./bomb.py) : File with functionality of bomb.

USAGE OF OOPS CONCEPTS:
-----------------------

**Class:**

+ Classes for *board*,*person*,*bomberman*,*enemy* and *bomb* are made.

**Objects:**

+ Objects for *board*,*bomberman*,*enemy* and *bomb* are made.

**Encapsulation:**

+ All the variables except iterators are encapsulated.
+ They all are available in an encapsulated dictionary *pos_dict*.

**Inheritance:**

+ Class for *person* is inherited by *bomberman* and *enemy*.

**Polymorphism:**

+ Methods *move_up*,*move_right*,*move_down* and *move_left* have been overloaded which is a special type od Polymorphism.

**Modularity:**

+ The whole gane is divided in **7 modules** as stated above.

BONUSES WORKED ON:
------------------

+ Giving diffrent colors to diffrent characters.
+ Timer for bomb.

HOW TO PLAY:
============

CONTROLS:
---------

* **w** :Move up
* **a** :Move left
* **w** :Move right
* **d** :Move down
* **b** :Drop bomb
* **q+ctrl+z** :Quit ()

KNOW THE CHARACTERS:
====================

+ **B** :Bomberman(*Blue*)
+ **E** :Enemy(*Red*)
+ **#** :Outer Border
+ **X** :Walls
+ **/** :Bricks
+ **O** :Bomb(*Green*)
+ **e** :Explosion(*Yellow*)

MOTIVE:
=======

+ The motive is to kill the enemies
+ You also get points for breaking bricks

SCORING SCHEME:
===============

+ Killing **Enemy** gets you 100 points
+ Breaking **Brick** gets you 20 points

BEWARE OF:
==========

+ If enemies touch you, you die
+ If explosion touches you, you die
+ If you remain on the bomb, you die
+ You only get 3 lives
+ Enemies are smart enough to be safe from bomb
+ Enemies have random motion

WARNINGS:
=========

+ The game is customised for a full screen UBUNTU-GNOME Terminal with normal size settings
+ It should look something like [this](./Sample.png)
+ It is made sure you continuously don't press a key so some timeout is kept. Avoid loading up your RAM.
+ If it doesn't fit try resizing the terminal and removing line *144* from [board.py](./board.py)

CONTRIBUTORS:
=============

+ **KUSHAL MAJMUNDAR**
+ You can also clone it from [here](https://github.com/kUSHAL0601/bomber_man.git)
+ You can ask queries as issues on same repo.
