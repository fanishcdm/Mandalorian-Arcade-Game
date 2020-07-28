'''Person Class Definition'''
import random
from colorama import Fore,Style,Back
from config import MAP_COMPONENTS as mp
from items import bossbullet
from utilities import superimpose
import time
class Person:
    '''A class to define general characteristic of the players and enemies in the game'''

    def __init__(self, x, y, height, width, dx, dy, gravity, board):
        self.__x = x
        self.__y = y
        self.__height = height
        self.__width = width
        self.__dx = dx
        self.__dy = dy
        self.__init_gravity = gravity
        self.__gravity = 0
        self.__matrix = []

    def get_x(self):
        return self.__x
    def set_x(self,x):
        self.__x = x
    x = property(get_x,set_x)
    def get_y(self):
        return self.__y
    def set_y(self,x):
        self.__y = x
    y = property(get_y,set_y)
    def get_he(self):
        return self.__height
    def set_he(self,x):
        self.__height = x
    height = property(get_he,set_he)
    def get_wi(self):
        return self.__width
    def set_wi(self,x):
        self.__width = x
    width = property(get_wi,set_wi)
    def get_mat(self):
        return self.__matrix
    def set_mat(self,x):
        self.__matrix = x
    matrix = property(get_mat,set_mat)
    def get_matrix(self):
        '''Function to return the matrix
        representation of the person
        '''
        return self.matrix

    def check_right_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element from the right
        '''
        for i in range(self.y, self.y + self.height):
            if board.matrix[i][self.__x + self.width + 1] in mp:
                return True

    def check_left_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element from the left
        '''
        for i in range(self.y, self.y + self.height):
            if board.matrix[i][self.__x - 1] in mp:
                return True

    def check_bottom_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element from the bottom
        '''
        for i in range(self.__x, self.__x + self.width):
            if board.matrix[self.y + self.height][i] in mp:
                return True
        return False

    def check_top_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element from the top
        '''
        for i in range(self.__x, self.__x + self.width):
            if board.matrix[self.y - 1][i] in mp:
                return True
        return False

    def check_side_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element in the horizontal directions
        '''
        if self.check_left_collision_with_map(
                board) or self.check_right_collision_with_map(board):
            return True
        return False

    def check_up_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element in the vertical directions
        '''
        if self.check_top_collision_with_map(
                board) or self.check_bottom_collision_with_map(board):
            return True
        return False

    def check_left_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item from the left
        '''
        if self.__x in range(item.x, item.x + item.width):
            return True
        return False

    def check_right_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item from the right
        '''
        if self.__x + self.width in range(item.x, item.x + item.width):
            return True
        return False

    def check_top_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item from the top
        '''
        if self.y in range(item.y, item.y + item.height):
            return True
        return False

    def check_bottom_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item from the bottom
        '''
        if self.y + self.height in range(item.y, item.y + item.height):
            return True
        return False

    def check_up_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item in the vertical directions
        '''
        if self.check_top_collision_with_item(
                item) and self.check_bottom_collision_with_item(item):
            return True
        return False

    def check_side_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item in the horizontal directions
        '''
        if self.check_left_collision_with_item(
                item) and self.check_right_collision_with_item(item):
            return True
        return False

    def check_complete_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item.
        '''
        if self.check_side_collision_with_item(
                item) and self.check_up_collision_with_item(item):
            return True
        return False

    def check_overlap_with_item(self, item):
        '''Function to check if the person has
        overlapped with an item.
        '''
        if self.__x < (
                item.x +
                item.width) and (
                self.__x +
                self.width) > item.x and self.y < (
                item.y +
                item.height) and (
                    self.y +
                self.height) > item.y:
            return True
        return False


class Mario(Person):
    '''Class to define the main player of the game.
    Initilized Mario with its size, matrix and velocities.
    '''

    def __init__(self, x, y, height, width, dx, dy, gravity, board):
        super().__init__(x, y, height, width, dx, dy, gravity, board)
        self.__height = 3
        self.__lives = 3
        self.__width = 6
        self.__dx = 3
        self.__dy = 1
        self.__jump = 4
        self.__height_at_jump = 0
        self.__score = 0
        self.__killed = 0
        self.__gravity = 1
        self.__coins = 0
        self.__mario_boss_life = 100
        self.__win = False
        self.__matrix = [
            ['[', '[', 'f', 'j', ']', ']'],
            ['o', '-', '|', '|', '-', 'o'],
            [' ', '/', '/', '\\', '\\', ' '],
        ]
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] is 'f' or self.matrix[i][j] is 'j':
                    self.matrix[i][j] = Fore.CYAN + \
                        self.matrix[i][j] + Fore.RESET
                elif self.matrix[i][j] is ']' or self.matrix[i][j] is '[':
                    self.matrix[i][j] = Fore.YELLOW + \
                        self.matrix[i][j] + Fore.RESET
                elif self.matrix[i][j] is '-' or self.matrix[i][j] is '/' or self.matrix[i][j] is '\\':
                    self.matrix[i][j] = Fore.MAGENTA + \
                        self.matrix[i][j] + Fore.RESET
                else:
                    self.matrix[i][j] = Fore.RED + \
                        self.matrix[i][j] + Fore.RESET

    def get_dx(self):
        return self.__dx
    def set_dx(self,x):
        self.__dx = x
    dx = property(get_dx,set_dx)
    def get_dy(self):
        return self.__dy
    def set_dy(self,x):
        self.__dy = x
    dy = property(get_dy,set_dy)
    def get_win(self):
        return self.__win
    def set_win(self,x):
        self.__win = x
    def get_win(self):
        return self.__win
    def set_win(self,x):
        self.__win = x
    win = property(get_win,set_win)
    def get_killed(self):
        return self.__killed
    def set_killed(self,x):
        self.__killed = x
    killed = property(get_killed,set_killed)
    def get_score(self):
        return self.__score
    def set_score(self,x):
        self.__score = x
    score = property(get_score,set_score)
    def get_mbl(self):
        return self.__mario_boss_life
    def set_mbl(self,x):
        self.__mario_boss_life = x
    mario_boss_life = property(get_mbl,set_mbl)
    def get_coins(self):
        return self.__coins
    def set_coins(self,x):
        self.__coins = x
    coins = property(get_coins,set_coins)
    def get_lives(self):
        return self.__lives
    def set_lives(self,x):
        self.__lives = x
    lives = property(get_lives,set_lives)
    def get_mat(self):
        return self.__matrix
    def set_mat(self,x):
        self.__matrix = x
    matrix = property(get_mat,set_mat)
    def get_he(self):
        return self.__height
    def set_he(self,x):
        self.__height = x
    height = property(get_he,set_he)
    def get_wi(self):
        return self.__width
    def set_wi(self,x):
        self.__width = x
    width = property(get_wi,set_wi)
    def mario_jump(self):
        '''Function to initialize the players jump
        '''
        self.height_at_jump = 0

    def mario_update_y(self, board):
        '''Function to update the player's y co-ordinates and
        instill the effect of gravity
        '''
        if self.height_at_jump <= self.jump:
            self.dy = -1
            self.height_at_jump += 1
            if self.check_top_collision_with_map(board):
                self.height_at_jump += 5
                self.dy = 1
        else:
            self.dy = 1

        if not self.check_bottom_collision_with_map(board):
            self.y += self.dy

    def shield(self,screen):
        new_matrix = screen.get_matrix()
        # new_matrix[self.y-1][self.__x+6]=Fore.CYAN + Style.BRIGHT + '\\' + Style.RESET_ALL + Fore.RESET
        # new_matrix[self.y-2][self.__x+5]=Fore.CYAN + Style.BRIGHT + '-' + Style.RESET_ALL + Fore.RESET
        new_matrix[self.y][self.x+7]=Fore.CYAN + Style.BRIGHT + '|' + Style.RESET_ALL + Fore.RESET
        new_matrix[self.y+1][self.x+7]=Fore.CYAN + Style.BRIGHT + '|' + Style.RESET_ALL + Fore.RESET
        new_matrix[self.y+2][self.x+7]=Fore.CYAN + Style.BRIGHT + '|' + Style.RESET_ALL + Fore.RESET
        # new_matrix[self.y+3][self.x+6]=Fore.CYAN + Style.BRIGHT + '/' + Style.RESET_ALL + Fore.RESET
        screen.update_matrix(new_matrix)

class Boss(Person):

    def __init__(self, x, y, height, width, dx, dy, gravity, board):
        super().__init__(x, y, height, width, dx, dy, gravity, board)
        self.__height = 3
        self.__life = 100
        self.__width = 6
        self.__dx = 3
        self.__dy = -1
        self.__jump = 4
        self.__height_at_jump = 0
        self.__score = 0
        self.__killed = 0
        self.__gravity = 1
        self.__win = False
        self.__bossspecialvar = 0
        self.__bullet = []
        self.__matrix = [
            ['[', 'B', 'O', 'S', 'S', ']'],
            ['o', '-', '|', '|', '-', 'o'],
            [' ', '/', '/', '\\', '\\', ' '],
        ]
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] is 'B' or self.matrix[i][j] is 'O' or self.matrix[i][j] is 'S':
                    self.matrix[i][j] = Fore.CYAN + \
                        self.matrix[i][j] + Fore.RESET
                elif self.matrix[i][j] is ']' or self.matrix[i][j] is '[':
                    self.matrix[i][j] = Fore.YELLOW + \
                        self.matrix[i][j] + Fore.RESET
                elif self.matrix[i][j] is '-' or self.matrix[i][j] is '/' or self.matrix[i][j] is '\\':
                    self.matrix[i][j] = Fore.MAGENTA + \
                        self.matrix[i][j] + Fore.RESET
                else:
                    self.matrix[i][j] = Fore.RED + \
                        self.matrix[i][j] + Fore.RESET

    def get_bsv(self):
        return self.__bossspecialvar
    def set_bsv(self,x):
        self.__bossspecialvar = x
    bossspecialvar = property(get_bsv,set_bsv)
    def get_dx(self):
        return self.__bullet
    def set_dx(self,x):
        self.__bullet = x
    bullet = property(get_dx,set_dx)
    def get_life(self):
        return self.__life
    def set_life(self,x):
        self.__life = x
    life = property(get_life,set_life)
    def get_mat(self):
        return self.__matrix
    def set_mat(self,x):
        self.__matrix = x
    matrix = property(get_mat,set_mat)
    def get_he(self):
        return self.__height
    def set_he(self,x):
        self.__height = x
    height = property(get_he,set_he)
    def get_wi(self):
        return self.__width
    def set_wi(self,x):
        self.__width = x
    width = property(get_wi,set_wi)

    def update(self,mario,screen):
        if mario.y < self.y :
            self.y -= min (self.y - mario.y, 3)
        elif mario.y > self.y :
            self.y += min(mario.y - self.y , 3)
        # acc to mario's arrow boss changes its y coordinates
        if screen.matrix[self.y][self.x - 2] == '>':
            if(self.y + 2 < 32) :
                self.y += 2
            elif self.y - 2 > 3:
                self.y -= 2
        if mario.y + mario.height == screen.height - 3:
            self.y = 5
            self.bullet.append(bossbullet(self.x -1,mario.y + 1,None,None,None))
        elif mario.y <= 5:
            self.y = screen.height - 7
            self.bullet.append(bossbullet(self.x -1,mario.y + 1,None,None,None))
        if self.bossspecialvar < 4  :
            self.bossspecialvar += 1
            for bull in self.bullet:
                bull.move_bullet()
        else :
            self.bossspecialvar = 0
            for bull in self.bullet:
                bull.move_bullet_fast()
        for bull in self.bullet :
                superimpose(bull,screen)
    def bossshoot(self):
        self.bullet.append(bossbullet(self.x -1,self.y + 1,None,None,None))
