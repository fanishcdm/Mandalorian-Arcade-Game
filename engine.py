from colorama import Fore,Back,Style
import os
import sys
import subprocess
import time
from generate_map import Map
import config
from input import Get, input_to
from person import Mario,Boss
from items import Coin,firebeams,bullet,magnet,firebeams2
from utilities import superimpose, clear_sprite
class Engine:


    def __init__(self):
        self.__screen = Map(35,1404)
        self.__firebeams = [] # enemies
        self.__firebeams2 = [] # enemies
        self.__coins = []
        self.__mario = Mario(0, self.__screen.height - 10,
                           1, 1, 1, 1, 1, self.__screen)
        self.__boss = Boss(1350, self.__screen.height - 7,
                           1, 1, 1, 1, 1, self.__screen)
        self.__bullets = []
        self.__magnets = []
        self.__shield = 0
        self.__start_time = -1
        self.__bossbulltime = -1
        self.__time = 0
        self.__accn = 0.1
        self.__magnetpresent = 0
    def initialize_items(self):
        '''Function to initialize various objects on the
        game's map.
        '''
        coins_pos = config.coins_pos
        firebeams_pos = config.firebeams_pos
        firebeams2_pos = config.firebeams2_pos
        magnets_pos = config.magnets_pos
        for coin in coins_pos:
            self.__coins.append(Coin(coin[0], coin[1], None, None, self.__screen))
        for magne in magnets_pos:
            self.__magnets.append(magnet(magne[0], magne[1], None, None, self.__screen))
        for firebeam in firebeams_pos:
            self.__firebeams.append(firebeams(firebeam[0], firebeam[1], None, None, self.__screen))
        for firebeam2 in firebeams2_pos:
            self.__firebeams2.append(firebeams2(firebeam2[0], firebeam2[1], None, None, self.__screen))
        self.__start_time = time.time()
    def initialize(self):
        os.system('clear')
        print(
            Style.BRIGHT +
            Fore.YELLOW +
            'Setting up the MAP ...' +
            Style.RESET_ALL)
        self.initialize_items()
        time.sleep(0.5)

    def quit(self):
        '''Function to quit the game
        '''
        os.system('clear')
        sys.exit()
    def won(self):
        '''Function to quit the game
        '''
        os.system('clear')
        print ("\n\nYOU WONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
        sys.exit()

    def update(self):
        '''Function to update the status and the position
        of the objects, enemies and player
        '''
        if self.__mario.y > self.__screen.height - 6 :
            self.__mario.y = self.__screen.height - 6
        if self.__mario.x < self.__screen.x_cross:
            self.__mario.x = self.__screen.x_cross

        if time.time() - self.__start_time > 60.0 :
            self.__start_time = time.time()
            self.__shield = 1

        if time.time() - self.__start_time > 10.0 :
            self.__shield = 0

        if self.__mario.lives <= 0 or self.__mario.mario_boss_life <= 0:
            self.quit()

        if self.__boss.life <= 0:
            self.won()

        for bullet in self.__bullets:
            bullet.move_bullet()

        for bullet in self.__bullets:
            if self.__boss.check_overlap_with_item(bullet) or self.__boss.check_complete_collision_with_item(bullet):
                self.__bullets.remove(bullet)
                self.__boss.life -= 1
        for bullet in self.__bullets:
            if bullet.x - self.__screen.x_cross + bullet.width > 118 :
                self.__bullets.remove(bullet)
        for bullet in self.__bullets:
            for firebeam in self.__firebeams:
                if bullet.check_overlap(firebeam):
                    self.__bullets.remove(bullet)
                    self.__firebeams.remove(firebeam)
                    self.__mario.killed += 1
                    self.__mario.score += 100
                    break
        for bullet in self.__bullets:
            if bullet.x - self.__screen.x_cross + bullet.width > 118 :
                self.__bullets.remove(bullet)
            for firebeam2 in self.__firebeams2:
                if  bullet.check_overlap(firebeam2) :
                    self.__bullets.remove(bullet)
                    self.__firebeams2.remove(firebeam2)
                    self.__mario.killed += 1
                    self.__mario.score += 100
                    break

        for coin in self.__coins:
            if coin.check_collected(self.__mario):
                self.__mario.coins += 1
                self.__mario.score += 150
                self.__coins.remove(coin)
        if self.__shield == 0:
            for firebeam in self.__firebeams:
                if firebeam.check_overlap(self.__mario):
                    self.__firebeams.remove(firebeam)
                    self.__mario.lives -= 1
                    self.restart()
            for firebeam2 in self.__firebeams2:
                if firebeam2.check_overlap(self.__mario):
                    self.__firebeams2.remove(firebeam2)
                    self.__mario.lives -= 1
                    self.restart()
        self.__magnetpresent = 0
        for magnet in self.__magnets :
            if self.__screen.x_cross < magnet.x and magnet.x < self.__screen.x_cross + 110:
                magnet.attract(self.__mario)
                self.__magnetpresent = 1

        for bossbull in self.__boss.bullet:
            if self.__shield == 0 and(self.__mario.check_overlap_with_item(bossbull) or self.__mario.check_complete_collision_with_item(bossbull)):
                self.__boss.bullet.remove(bossbull)
                self.__mario.mario_boss_life -= 5
        for bossbull in self.__boss.bullet:
            if bossbull.x < 1245 :
                self.__boss.bullet.remove(bossbull)

    def render(self):
        '''Function to draw all the objects,
        players and enemies onto the screen'''
        life_string = ""
        for i in range(self.__mario.lives):
            life_string += Fore.WHITE + "❤️  " + Fore.RESET
        print ("\033[0;0f",end="")
        if self.__screen.x_cross < 1252:
            print(
                Fore.WHITE + "💵 :",
                self.__mario.coins,
                " \t\t\t\t\t\t   ",
                life_string + Fore.RESET)
            print(Fore.WHITE + "Score :" , str(self.__mario.score) + Fore.RESET)
        else :
            print(
                "Mario Life: ",self.__mario.mario_boss_life,"\t\t\t\t\t\t\t Boss Life: ",self.__boss.life
            )
        self.__screen.reset_matrix()
        if self.__shield == 1 :
            self.__mario.shield(self.__screen)
        for coin in self.__coins:
            superimpose(coin, self.__screen)
        for magne in self.__magnets:
            superimpose(magne, self.__screen)
        for bullet in self.__bullets:
            superimpose(bullet, self.__screen)
        for firebeam in self.__firebeams:
            superimpose(firebeam, self.__screen)
        for firebeam2 in self.__firebeams2:
            superimpose(firebeam2, self.__screen)
        superimpose(self.__mario, self.__screen)
        self.__boss.update(self.__mario,self.__screen)
        if time.time() - self.__bossbulltime > 1.0 :
            self.__boss.bossshoot()
            self.__bossbulltime = time.time()
        superimpose(self.__boss, self.__screen)
        print(self.__screen.print_matrix(self.__screen.x_cross))
        if self.__screen.x_cross > 1252 :
            self.__screen.x_cross -= 1
        self.__screen.x_cross += 1
        print("🤖 :", self.__mario.killed)

    def right(self):
                    if(self.__mario.y < self.__screen.height - 6):
                        self.__mario.y += 1
                    if self.__mario.x + self.__mario.width < self.__screen.x_cross + 120 :
                        clear_sprite(self.__mario, self.__screen)
                        if not self.__mario.check_right_collision_with_map(
                                self.__screen):
                            self.__mario.x += self.__mario.dx
                    elif self.__screen.x_cross >= 864:
                        clear_sprite(self.__mario, self.__screen)
                        if not self.__mario.check_right_collision_with_map(
                                self.__screen):
                            self.__mario.x += self.__mario.dx
                    else:
                        if not self.__mario.check_right_collision_with_map(
                                self.__screen):
                            self.__screen.x_cross += self.__mario.dx
                            clear_sprite(self.__mario, self.__screen)
                            self.__mario.x += self.__mario.dx

    def left(self):
                    if(self.__mario.y < self.__screen.height - 6):
                        self.__mario.y += 1
                    clear_sprite(self.__mario, self.__screen)
                    if not self.__mario.check_left_collision_with_map(
                            self.__screen):
                        self.__mario.x -= self.__mario.dx

    def up(self):
        if(self.__mario.y > 6):
                        clear_sprite(self.__mario, self.__screen)
                        self.__mario.y -= 3
                        self.__mario.dy = 1
                        self.__time = 0
    def down(self):
                    if(self.__mario.y < self.__screen.height - 6):
                        self.__mario.y += 3

    def degravity(self):
                    if(self.__mario.y < self.__screen.height - 6):
                        self.__mario.y += 1
                        self.__mario.dy = 1
                        self.__time = 0
    def gravity(self):
                    if(self.__mario.y < self.__screen.height - 6):
                        self.__mario.y += int(self.__time * (self.__mario.dy + self.__time*self.__accn/2))
                        self.__mario.dy += int(self.__time*self.__accn)
                        self.__time += 0.5

    def restart(self):
        '''Function to reset the player's and enemies positions
        if the player loses a life.
        '''
        self.render()
        time.sleep(3)
        os.system("clear")
        # self.__mario.x = 0
        self.__mario.y = self.__screen.height - 10
        # self.__screen.x_cross = 0
        self.__bullets = []
        self.__shield = 0
        self.__start_time = -1
        self.__bossbulltime = -1

    def space(self):
        self.__bullets.append(bullet(self.__mario.x + self.__mario.width +1,self.__mario.y + 2,None,None,self.__screen))
        self.gravity()
    def run(self):
        '''Function to run the main game loop
        '''
        getch = Get()
        while True:
            input = input_to(getch)

            if input is not None:
                if input is 'd':
                    self.right()
                elif input is 'a':
                    self.left()
                elif input is 'w':
                    self.up()
                elif input is 's':
                    self.down()
                elif input is 'q':
                    self.quit()
                elif input is ' ':
                    self.space()
            else :
                if self.__screen.x_cross > 1245 or self.__magnetpresent :
                    self.degravity()
                else :
                    self.gravity()
            # os.system('clear')
            self.update()
            self.render()
            time.sleep(0.02)
