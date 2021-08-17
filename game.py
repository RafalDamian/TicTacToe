import pygame
from pygame.constants import MOUSEBUTTONDOWN
import time
import math

from bot import Bot
from settings import Settings


class TicTacToe():
    '''main class for game management'''

    def __init__(self):
        '''game initialization and resources creation'''
        pygame.init()
        self.running = True
        self.game_running = False
        self.pgl_running = False #pgl = post game lobby
        self.typing = False
        self.click = False
        self.action = False
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption("Tic Tac Toe")

        self.settings = Settings(screen=self.screen)
        self.bg_color = self.settings.bg_color
        self.button_color = self.settings.button_color
        self.text_color = self.settings.text_color
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height
        
        self.player_1 = 'PLAYER 1'
        self.player_2 = 'PLAYER 2'
        self.difficulty = 'medium'

        self.bot = Bot()
        
        self.game_status = {1: '', 2: '', 3: '',
                            4: '', 5: '', 6: '',
                            7: '', 8: '', 9: ''}

        self.positions = self.settings.positions
        self.positions_buttons = self.settings.positions_buttons


    def run_game(self):
        """ main game loop initialization (opens main manu)"""
        x = self.screen_width / 2
        y = self.screen_height
        while self.running:
            (mx, my) = pygame.mouse.get_pos()
            self.screen.fill(self.bg_color)
            self._draw_text('Tic Tac Toe', 150, self.text_color, x, y*0.2)
            button_pvp = pygame.Rect((0.8*x, y*0.3), (0.4*x, 0.1*y))
            button_pvc = pygame.Rect((0.8*x, y*0.5), (0.4*x, 0.1*y))
            button_exit = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_pvp, self.button_color, 'PLAYER VS PLAYER', 40, self.text_color)
            self._draw_button(button_pvc, self.button_color, 'PLAYER VS COMPUTER', 40, self.text_color)
            self._draw_button(button_exit, self.button_color, 'EXIT', 40, self.text_color)

            if button_pvp.collidepoint((mx, my)):
                if self.click:
                    self.game_running = True
                    self._player_vs_player()
            
            if button_pvc.collidepoint((mx, my)):
                if self.click:
                    self.game_running = True
                    self._player_vs_computer()

            if button_exit.collidepoint((mx, my)):
                if self.click:
                    self.running = False

            self._check_events()

            pygame.display.update()
        
        pygame.display.quit()
        pygame.quit()
        exit()

    
    def _player_vs_player(self):
        '''settings menu fo pvp'''
        x = self.screen_width / 2
        y = self.screen_height
        player = 0
        while self.game_running:
            (mx, my) = pygame.mouse.get_pos()

            self.screen.fill(self.bg_color)

            self._draw_text('TYPE YOUR NAMES', 60, self.text_color, x, y*0.2)

            if self.typing:
                self._change_name(player)
                self.action = False

            button_p1 = pygame.Rect((0.8*x, y*0.3), (0.4*x, 0.1*y))
            button_p2 = pygame.Rect((0.8*x, y*0.5), (0.4*x, 0.1*y))
            self._draw_button(button_p1, self.button_color, self.player_1, 40, self.text_color)
            self._draw_button(button_p2, self.button_color, self.player_2, 40, self.text_color)
            players_buttons = {1: button_p1, 2: button_p2}

            if self.typing:
                self._draw_button_circuit(players_buttons[player], self.text_color)

            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            button_play = pygame.Rect((1.5*x, y*0.8), (0.4*x, 0.1*y))
            self._check_events()

            if button_p1.collidepoint((mx, my)):
                if self.click:
                    self.typing = True
                    player = 1
                    self._draw_button_circuit(players_buttons[player], self.text_color)

            if button_p2.collidepoint((mx, my)):
                if self.click:
                    self.typing = True
                    player = 2
                    self._draw_button_circuit(players_buttons[player], self.text_color)

            self._draw_button(button_menu, self.button_color, 'BACK TO MENU', 40, self.text_color)
            self._draw_button(button_play, self.button_color, 'PLAY', 40, self.text_color)

            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.game_running = False

            if button_play.collidepoint((mx, my)):
                if self.click:
                    self._play_pvp()

            pygame.display.update()

    def _player_vs_computer(self):
        '''settings menu fo pvc'''
        x = self.screen_width / 2
        y = self.screen_height
        while self.game_running:
            (mx, my) = pygame.mouse.get_pos()

            self.screen.fill(self.bg_color)

            self._draw_text('TYPE YOUR NAME', 60, self.text_color, x, y*0.15)

            if self.typing:
                self._change_name(1)
                self.action = False

            button_p1 = pygame.Rect((0.8*x, y*0.2), (0.4*x, 0.1*y))
            self._draw_button(button_p1, self.button_color, self.player_1, 40, self.text_color)

            if self.typing:
                self._draw_button_circuit(button_p1, self.text_color)

            if button_p1.collidepoint((mx, my)):
                if self.click:
                    self.typing = True
                    self._draw_button_circuit(button_p1, self.text_color)
            
            self._draw_text('SELECT DIFFICULTY', 60, self.text_color, x, y*0.45)
            button_easy = pygame.Rect((0.8*x, y*0.5), (0.4*x, 0.1*y))
            button_medium = pygame.Rect((0.8*x, y*0.65), (0.4*x, 0.1*y))
            button_impossible = pygame.Rect((0.8*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_easy, self.button_color, 'EASY', 40, self.text_color)
            self._draw_button(button_medium, self.button_color, 'MEDIUM', 40, self.text_color)
            self._draw_button(button_impossible, self.button_color, 'IMPOSSIBLE', 40, self.text_color)

            if button_easy.collidepoint((mx, my)):
                if self.click:
                    self.difficulty = 'easy'
            
            if button_medium.collidepoint((mx, my)):
                if self.click:
                    self.difficulty = 'medium'

            if button_impossible.collidepoint((mx, my)):
                if self.click:
                    self.difficulty = 'impossible'

            if self.difficulty == 'easy':
                self._draw_button_circuit(button_easy, self.text_color)
            elif self.difficulty == 'medium':
                self._draw_button_circuit(button_medium, self.text_color)
            else:
                self._draw_button_circuit(button_impossible, self.text_color)

            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            button_play = pygame.Rect((1.5*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_menu, self.button_color, 'BACK TO MENU', 40, self.text_color)
            self._draw_button(button_play, self.button_color, 'PLAY', 40, self.text_color)

            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.game_running = False

            if button_play.collidepoint((mx, my)):
                if self.click:
                    self._play_pvc()

            self._check_events()

            pygame.display.update()


    def _play_pvp(self):
        '''main pvp game loop'''
        self._reset_game_status()
        x = self.screen_width / 2
        y = self.screen_height
        who_to_move = 'X'
        change_move = {'X': 'O', 'O': 'X'}
        players={
            'X': self.player_1,
            'O': self.player_2
        }
        result = {
            self.player_1: 0,
            self.player_2: 0,
        }
        while self.game_running:
            (mx, my) = pygame.mouse.get_pos()
            self.screen.fill(self.bg_color)
            self._draw_score_board(self.player_1, self.player_2, result)
            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_menu, self.button_color, 'BACK TO MENU', 40, self.text_color)

            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.game_running = False

            self._draw_text(f'{players[who_to_move]} to move', 80, self.text_color, x, y*0.9)
            
            if self._check_game_status() == 'win':
                result[players[change_move[who_to_move]]] += 1
                self.pgl_running = True
                self._post_game_lobby(result, 'win', 'pvp', players[change_move[who_to_move]])
            elif self._check_game_status() == 'draw':
                result[self.player_1] += 0.5
                result[self.player_2] += 0.5
                self.pgl_running = True
                self._post_game_lobby(result, 'draw', 'pvp')

            for position in self.positions_buttons:
                if self.positions_buttons[position].collidepoint((mx,my)):
                    if self.click and not self.game_status[position]:
                        self.game_status[position] = who_to_move
                        who_to_move = change_move[who_to_move]
            
            self._check_events()
            self._draw_tictactoe_board()
            self._draw_game_status()
            pygame.display.update()

    def _play_pvc(self):
        '''main pvc game loop'''
        self._reset_game_status()
        x = self.screen_width / 2
        y = self.screen_height
        who_to_move = 'X'
        change_move = {'X': 'O', 'O': 'X'}
        players={
            'X': self.player_1,
            'O': 'COMPUTER'
        }
        result = {
            self.player_1: 0,
            'COMPUTER': 0,
        }
        while self.game_running:
            (mx, my) = pygame.mouse.get_pos()
            self.screen.fill(self.bg_color)
            self._draw_score_board(self.player_1, 'COMPUTER', result)
            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_menu, self.button_color, 'BACK TO MENU', 40, self.text_color)

            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.game_running = False

            if players[who_to_move] == self.player_1:
                for position in self.positions_buttons:
                    if self.positions_buttons[position].collidepoint((mx,my)):
                        if self.click and not self.game_status[position]:
                            self.game_status[position] = who_to_move
                            who_to_move = change_move[who_to_move]
            elif players[who_to_move] == 'COMPUTER':
                time.sleep(0.5)
                self.game_status[self._get_computer_move(who_to_move)] = who_to_move
                who_to_move = change_move[who_to_move]
            
            if self._check_game_status() == 'win':
                result[players[change_move[who_to_move]]] += 1
                self.pgl_running = True
                self._post_game_lobby(result, 'win', 'pvc', players[change_move[who_to_move]])
            elif self._check_game_status() == 'draw':
                result[self.player_1] += 0.5
                result['COMPUTER'] += 0.5
                self.pgl_running = True
                self._post_game_lobby(result, 'draw', 'pvc')
            
            self._check_events()
            self._draw_tictactoe_board()
            self._draw_game_status()
            pygame.display.update()

    def _post_game_lobby(self, result, win_or_draw, pvp_or_pvc, who_won='no winner'):
        '''post game lobby - play again button'''
        x = self.screen_width / 2
        y = self.screen_height

        while self.pgl_running:
            (mx, my) = pygame.mouse.get_pos()
            self.screen.fill(self.bg_color)

            if pvp_or_pvc == 'pvp':
                self._draw_score_board(self.player_1, self.player_2, result)
            elif pvp_or_pvc == 'pvc':
                self._draw_score_board(self.player_1, 'COMPUTER', result)

            if win_or_draw == 'win':
                self._draw_text(f'{who_won} won!', 80, self.text_color, x, y*0.9)
            elif win_or_draw == 'draw':
                self._draw_text('Draw!', 80, self.text_color, x, y*0.9)

            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_menu, (255,0,0), 'BACK TO MENU', 40, self.text_color)
            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.game_running = False
                    self.pgl_running = False
                    self._reset_game_status()

            button_play_again = pygame.Rect((1.5*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_play_again, self.button_color, 'PLAY AGAIN', 40, self.text_color)
            if button_play_again.collidepoint((mx, my)):
                if self.click:
                    self.pgl_running = False
                    self._reset_game_status()

            self._check_events()
            self._draw_tictactoe_board()
            self._draw_game_status()
            pygame.display.update()

    def _reset_game_status(self):
        '''changes game status to the empty board'''
        self.game_status = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}

    def _get_computer_move(self, who_to_move):
        '''asking computer to find a move in the position'''
        if self.difficulty == 'easy':
            return self.bot.easy(self.game_status)
        elif self.difficulty == 'medium':
            return self.bot.medium(self.game_status, who_to_move)
        elif self.difficulty == 'impossible':
            return self.bot.impossible(self.game_status, who_to_move)

    def _draw_text(self, text, font_size, color, x, y):
        '''draws given text in the given position'''
        font = pygame.font.SysFont(None, font_size)
        gen_text = font.render(text, 1, color)
        rect = gen_text.get_rect()
        rect.center = (x, y)
        self.screen.blit(gen_text, rect)

    def _draw_button(self, button, color, text, font_size, text_color):
        '''draws square with given text in the position of given button'''
        pygame.draw.rect(self.screen, color, button)
        (x, y) = button.center
        self._draw_text(text, font_size, text_color, x, y)

    def _draw_button_circuit(self, button, color):
        '''draws circuit of given button'''
        pygame.draw.rect(self.screen, color, button, 2, 8)

    def _draw_score_board(self, player_1, player_2, result):
        '''draws score board with given result and players on the top of the screen'''
        x = self.screen_width / 2
        y = self.screen_height
        self._draw_text(':', 80, self.text_color, x, y*0.15)
        self._draw_text(f'{result[player_1]}', 80, self.text_color, x*0.9, y*0.15)
        self._draw_text(f'{result[player_2]}', 80, self.text_color, x*1.1, y*0.15)
        self._draw_text(f'{player_1}', 80, self.text_color, x*0.6, y*0.15)
        self._draw_text(f'{player_2}', 80, self.text_color, x*1.4, y*0.15)

    def _draw_tictactoe_board(self):
        '''draws white TicTacToe board like this - # '''
        x = self.screen_width / 2
        y = self.screen_height
        bounds = pygame.Rect((0.65*x, 0.2*y), (0.7*x,0.7*x))
        a1 = (bounds.left, bounds.top + 1/3 * (bounds.bottom - bounds.top) - 0.005*y)
        a2 = (bounds.right - bounds.left, 0.01*y)
        pygame.draw.rect(self.screen, self.text_color, pygame.Rect(a1,a2))
        b1 = (bounds.left, bounds.top + 2/3 * (bounds.bottom - bounds.top) - 0.005*y)
        b2 = (bounds.right - bounds.left, 0.01*y)
        pygame.draw.rect(self.screen, self.text_color, pygame.Rect(b1,b2))
        c1 = (bounds.left + 1/3 * (bounds.right - bounds.left) - 0.005*y, bounds.top)
        c2 = (0.01*y, bounds.bottom - bounds.top)
        pygame.draw.rect(self.screen, self.text_color, pygame.Rect(c1,c2))
        d1 = (bounds.left + 2/3 * (bounds.right - bounds.left) - 0.005*y, bounds.top)
        d2 = (0.01*y, bounds.bottom - bounds.top)
        pygame.draw.rect(self.screen, self.text_color, pygame.Rect(d1,d2))

    def _draw_game_status(self):
        '''draws Xs and Os in the positions provided by game status'''
        for position in range(1,10):
            if symbol := self.game_status[position]:
                if symbol == 'O':
                    self._draw_O(self.positions[position])
                elif symbol == 'X':
                    self._draw_X(self.positions[position])
    
    def _draw_O(self, position):
        '''draws O in the given position'''
        h = self.screen_height
        pygame.draw.circle(self.screen, self.button_color, position, 0.08*h, 8)

    def _draw_X(self, position):
        '''draws X in the given position'''
        h = self.screen_height
        z = 4.5 * math.sqrt(0.25 * h) #pure math
        x = position[0]
        y = position[1]
        a = (x-z, y+z)
        b = (x+z, y-z)
        pygame.draw.line(self.screen, self.button_color, a, b, 12)
        c = (x+z, y+z)
        d = (x-z, y-z)
        pygame.draw.line(self.screen, self.button_color, c, d, 12)

    def _check_game_status(self):
        '''checking win conditions, and draw condition'''
        gs = self.game_status
        if gs[1] == gs[2] and gs[2] == gs[3] and gs[1]: return 'win'
        if gs[4] == gs[5] and gs[5] == gs[6] and gs[4]: return 'win'
        if gs[7] == gs[8] and gs[8] == gs[9] and gs[7]: return 'win'
        if gs[1] == gs[4] and gs[4] == gs[7] and gs[1]: return 'win'
        if gs[2] == gs[5] and gs[5] == gs[8] and gs[2]: return 'win'
        if gs[3] == gs[6] and gs[6] == gs[9] and gs[3]: return 'win'
        if gs[1] == gs[5] and gs[5] == gs[9] and gs[1]: return 'win'
        if gs[3] == gs[5] and gs[5] == gs[7] and gs[3]: return 'win'
        if gs[1] and gs[2] and gs[3] and gs[4] and gs[5] and\
           gs[6] and gs[7] and gs[8] and gs[9]: return 'draw'
        return 0

    def _check_events(self):
        '''reaction to events generated by the keyboard and mouse inside menu'''
        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button:
                    self.click = True

    def _change_name(self, player):
        '''changes name of the player'''
        players = {1: self.player_1, 2: self.player_2}
        while self.action == False:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                            if event.button:
                                self.typing = False
                                self.action = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.typing = False
                        self.action = True
                    elif event.key == pygame.K_BACKSPACE:
                        if len(players[player]) > 0:
                            players[player] = players[player][:-1]
                            self.action = True
                    elif len(players[player]) <= 15: #max 15 char name
                        players[player] += event.unicode
                        self.action = True
        if player == 1:
            self.player_1 = players[player]
        elif player == 2:
            self.player_2 = players[player]


if __name__ == "__main__":
    game = TicTacToe()
    game.run_game()

