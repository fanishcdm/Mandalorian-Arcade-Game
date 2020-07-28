from colorama import Fore,Back,Style

def superimpose(x,y,height,width,board_matrix,item_matrix):
    ii = 0
    for i in range(y,y+height):
        jj = 0
        for j in range(x,x+width):
            board_matrix[i][j] = item_matrix[ii][jj]
            jj += 1
        ii += 1


class Map:

    def __init__(self,height,width):
        self.__height=height
        self.__width=width
        self.__x_cross = 0
        self.__matrix = [[' ' for x in range(width)] for y in range(height)]

        for i in range(self.height):
            for j in range(self.width):
                self.matrix[i][j] = Back.BLACK + self.matrix[i][j] + Back.RESET

        # bottom
        self.block = [
            ['^', '^', '^', '^', '^', '^', '^', '^', '^'],
            ['^', '^', '^', '^', '^', '^', '^', '^', '^'],
            ['^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ]

        for i in range(3):
            for j in range(9):
                self.block[i][j] = Fore.BLACK + Back.WHITE + self.block[i][j] +Back.RESET  +Fore.RESET
        self.reset_matrix()

    def get_mat(self):
        return self.__matrix
    def set_mat(self,x):
        self.__matrix = x
    matrix = property(get_mat,set_mat)
    def get_x_cross(self):
        return self.__x_cross
    def set_x_cross(self,x):
        self.__x_cross = x
    x_cross = property(get_x_cross,set_x_cross)
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

    def get_matrix(self):
        return self.matrix

    def update_matrix(self,new_matrix):
        self.matrix= new_matrix

    def reset_matrix(self):
        self.matrix = [[' ' for x in range(self.width)] for y in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                self.matrix[i][j] = Back.BLACK + self.matrix[i][j] + Back.RESET

        for i in range(0, self.width , 9):
            superimpose(i, self.height - 3, 3, 9, self.matrix, self.block)


    def print_matrix(self,x):
        string_matrix = ""
        for i in range(self.height):
            for j in range(x,x+120):
                string_matrix += self.matrix[i][j]
            string_matrix += '\n'
        return string_matrix

    def __str__(self):
        string_matrix = ""
        for i in range(self.height):
            for j in range(self.width):
                string_matrix += self.matrix[i][j]
            string_matrix += '\n'
        return string_matrix

if __name__ == '__main__':
    a = Map(32,1404)
    print(a)
