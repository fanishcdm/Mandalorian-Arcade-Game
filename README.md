Fanish 2018101021
PYTHON TERMINAL Jetpack Joyride GAME

1. INTRODUCTION
    This is the terminal version of JPJR written in Python. It uses the basic Python libraries and modules.
    Concepts of object oriented
    programming are present within the code and the game simulates a basic version
    of jetpack joyride.

2. STRUCTURES AND FEATURES
    The game application exhibits the OOP concepts of Inheritance, Encapsulation, Polymorphism, Abstraction along with Function Overloading.

    2.1 The Engine of the game is defined Engine class, which contains crucial functions necesssary for the running of the game. The engine of the game is responsible for the various updates and rendering of the objects onto the terminal screen. The main game loop is a function of the Engine class.

    2.2 Every Player or Enemy is derived from Person class.

     The Base class Person has basic functionalities common among all the moving entities in the game.
     The Player(Mario) class inherits from the Person Base Class and has overloaded the functions of the Base class to respond to the environment and the keypress from the Player.
     The Enemy class inherits from the class Person as well and has the move functions overloaded differently than Mario.
     Mario has his motion subjected to a gravitational simulation.

    2.3 Every Obstacle or Item ( Coins, Flag, Bricks, etc. ) is derived from the Item class.

     The moving entities in the game are all subjected to a possible with the map objects like coins, firebeams, magnets, etc. and change their course of direction or respond to the event of collision accordingly.

    2.4 The Game Screen has its own class which generates the game map and can blit object, players and enemies onto the screen.

    The game has a pre-generated level map which is rendered during the run time and is updated according to Mario's position in the game.

3. RUNNING THE GAME
    Run using :
        Python3 run.py

4. BASIC CONTROLS
    w/s for up/down
    a/d for left/right
    space for bullets
    q for quit
