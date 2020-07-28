from colorama import Fore,Back,Style
class Item:
    '''General item class to define various
    obstacles and objects
    '''

    def __init__(self, x, y, height, width, board):
        self.__x = x
        self.__y = y
        self.__height = height
        self.__width = width
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
        '''
        return self.matrix

    def check_overlap(self, item):
        '''Function to check overlap with another item
        or person
        '''
        if self.x < (
                item.x +
                item.width) and (
                self.x +
                self.width) > item.x and self.y < (
                item.y +
                item.height) and (
                    self.y +
                self.height) > item.y:
            return True
        else:
            return False


class Coin(Item):
    '''Class for Coin item
    '''

    def __init__(self, x, y, height, width, board):
        super().__init__(x, y, height, width, board)
        self.__height = 1
        self.__width = 3
        self.__matrix = [
            [ '$', '$', '$']
        ]
        for i in range(self.height):
            for j in range(self.width):
                self.matrix[i][j] = Style.BRIGHT + Fore.BLACK + \
                    Back.WHITE + self.matrix[i][j] + Style.RESET_ALL+ Back.RESET + Fore.RESET

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
    def check_collected(self, player):
        '''Function to check if the coin is
        collected by the player
        '''
        if self.check_overlap(player):
            return True
        return False

class bossbullet(Item):
    def __init__(self,x,y,height,width,board):
        super().__init__(x,y,height,width,board)
        self.__matrix = [
           [ 'o' ]
        ]
        self.__height = 1
        self.__width = 1
        for i in range(self.height):
            for j in range (self.width):
                self.matrix[i][j] = Fore.RED + Back.BLACK + Style.BRIGHT + self.matrix[i][j] + Back.RESET +Style.RESET_ALL + Fore.RESET

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
    def move_bullet(self):
        self.x -= 2
    def move_bullet_fast(self):
        self.x -= 4

class bullet(Item):
    def __init__(self,x,y,height,width,board):
        super().__init__(x,y,height,width,board)
        self.__matrix = [
           [ '>','>','-','-','-','-','>']
        ]
        self.__height = 1
        self.__width = 7
        for i in range(self.height):
            for j in range (self.width):
                self.matrix[i][j] = Fore.WHITE + Style.BRIGHT + self.matrix[i][j] + Style.RESET_ALL +Fore.RESET

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
    def move_bullet(self):
        self.x += 15

class magnet(Item):
    def __init__(self,x,y,height,width,board):
        super().__init__(x,y,height,width,board)
        self.__matrix = [
            ['|',' ',' ',' ','|'],
            ['|',' ',' ',' ','|'],
            [' ','\\','_','/',' ']
        ]
        self.__height = 3
        self.__width = 5
        for i in range(self.height):
            for j in range(self.width):
                self.matrix[i][j] = Fore.MAGENTA + Style.BRIGHT + self.matrix[i][j] + Style.RESET_ALL + Fore.RESET

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
    def attract(self,mario):
        if mario.x + mario.width < self.x :
            if mario.y < self.y :
                mario.y += min(self.y - mario.y,2)
            else :
                mario.y -= min(mario.y - self.y,2)
            mario.x += min(self.x - mario.x , 2)
        else :
            if mario.y < self.y :
                mario.y += min(self.y - mario.y,2)
            else :
                mario.y -= min(mario.y - self.y,2)
            mario.x -= min (mario.x - self.x,2)

class firebeams(Item):
    def __init__(self,x,y,height,width,board):
        super().__init__(x,y,height,width,board)
        self.__height = 4
        self.__width = 4
        self.__matrix = [
            [' ',' ',' ','H'],
            [' ',' ','H',' '],
            [' ','H',' ',' '],
            ['H',' ',' ',' ']
        ]
        for i in range (4):
            for j in range(4):
                if self.matrix[i][j] == 'H':
                    self.matrix[i][j] = Fore.YELLOW +Back.BLACK + Style.BRIGHT +  self.matrix[i][j] + Style.RESET_ALL +  Back.RESET + Fore.RESET
                else :
                    self.matrix[i][j] = Back.BLACK + self.matrix[i][j] + Back.RESET

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
class firebeams2(Item):
    def __init__(self,x,y,height,width,board):
        super().__init__(x,y,height,width,board)
        self.__height = 4
        self.__width = 4
        self.__matrix = [
            ['H',' ',' ',' '],
            [' ','H',' ',' '],
            [' ',' ','H',' '],
            [' ',' ',' ','H']
        ]
        for i in range (4):
            for j in range(4):
                if self.matrix[i][j] == 'H':
                    self.matrix[i][j] = Fore.YELLOW +Back.BLACK + Style.BRIGHT +  self.matrix[i][j] + Style.RESET_ALL +  Back.RESET + Fore.RESET
                else :
                    self.matrix[i][j] = Back.BLACK + self.matrix[i][j] + Back.RESET

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
