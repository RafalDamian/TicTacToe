import pygame
from pygame.constants import BUTTON_X1, BUTTON_X2, MOUSEBUTTONDOWN
#import tictactoe_bot as bot

class TicTacToe():
    '''main class for game management'''

    def __init__(self):
        '''game initialization and resources creation'''
        pygame.init()
        self.running = True
        self.game_running = False
        self.click = False
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.bg_color = (0,0,0)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Tic Tac Toe")

        self.player_1 = 'PLAYER 1'
        self.player_2 = 'PLAYER 2'


    def run_game(self):
        """ main game loop initialization """
        x = self.screen_width / 2
        y = self.screen_height
        while self.running:
            ''' main menu '''
            (mx, my) = pygame.mouse.get_pos()
            self.screen.fill(self.bg_color)
            self.draw_text('Tic Tac Toe', 150, (255,255,255), x, y*0.2)
            button_pvp = pygame.Rect((0.8*x, y*0.3), (0.4*x, 0.1*y))
            button_pvc = pygame.Rect((0.8*x, y*0.5), (0.4*x, 0.1*y))
            button_exit = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            self.draw_button(button_pvp, (255,0,0), 'PLAYER VS PLAYER', 40, (255,255,255))
            self.draw_button(button_pvc, (255,0,0), 'PLAYER VS COMPUTER', 40, (255,255,255))
            self.draw_button(button_exit, (255,0,0), 'EXIT', 40, (255,255,255))

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

            self._check_menu_events()

            pygame.display.flip()
        
        pygame.display.quit()
        pygame.quit()
        exit()


    def draw_text(self, text, font_size, color, x, y):
        font = pygame.font.SysFont(None, font_size)
        gen_text = font.render(text, 1, color)
        rect = gen_text.get_rect()
        rect.center = (x, y)
        self.screen.blit(gen_text, rect)


    def draw_button(self, button, color, text, font_size, text_color):
        pygame.draw.rect(self.screen, color, button)
        (x, y) = button.center
        self.draw_text(text, font_size, text_color, x, y)
       

    def _player_vs_computer(self):
        x = self.screen_width / 2
        y = self.screen_height
        while self.game_running:
            (mx, my) = pygame.mouse.get_pos()

            self.screen.fill(self.bg_color)

            self.draw_text('TYPE YOUR NAME', 60, (255,255,255), x, y*0.15)
            button_p1 = pygame.Rect((0.8*x, y*0.2), (0.4*x, 0.1*y))
            self.draw_button(button_p1, (255,0,0), self.player_1, 40, (255,255,255))

            self.draw_text('SELECT DIFFICULTY', 60, (255,255,255), x, y*0.45)
            button_easy = pygame.Rect((0.8*x, y*0.5), (0.4*x, 0.1*y))
            button_medium = pygame.Rect((0.8*x, y*0.65), (0.4*x, 0.1*y))
            button_imposible = pygame.Rect((0.8*x, y*0.8), (0.4*x, 0.1*y))
            self.draw_button(button_easy, (255,0,0), 'EASY', 40, (255,255,255))
            self.draw_button(button_medium, (255,0,0), 'MEDIUM', 40, (255,255,255))
            self.draw_button(button_imposible, (255,0,0), 'IMPOSIBLE', 40, (255,255,255))

            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            button_play = pygame.Rect((1.5*x, y*0.8), (0.4*x, 0.1*y))

            self.draw_button(button_menu, (255,0,0), 'BACK TO MENU', 40, (255,255,255))
            self.draw_button(button_play, (255,0,0), 'PLAY', 40, (255,255,255))

            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.game_running = False

            if button_play.collidepoint((mx, my)):
                if self.click:
                    self.play_pvp()

            self._check_menu_events()

            pygame.display.flip()

    def play_pvp(self):
        return 'dupa'

    def _player_vs_player(self):
        x = self.screen_width / 2
        y = self.screen_height
        while self.game_running:
            (mx, my) = pygame.mouse.get_pos()

            self.screen.fill(self.bg_color)

            self.draw_text('TYPE YOUR NAMES', 60, (255,255,255), x, y*0.2)
            button_p1 = pygame.Rect((0.8*x, y*0.3), (0.4*x, 0.1*y))
            button_p2 = pygame.Rect((0.8*x, y*0.5), (0.4*x, 0.1*y))
            self.draw_button(button_p1, (255,0,0), self.player_1, 40, (255,255,255))
            self.draw_button(button_p2, (255,0,0), self.player_2, 40, (255,255,255))

            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            button_play = pygame.Rect((1.5*x, y*0.8), (0.4*x, 0.1*y))

            self.draw_button(button_menu, (255,0,0), 'BACK TO MENU', 40, (255,255,255))
            self.draw_button(button_play, (255,0,0), 'PLAY', 40, (255,255,255))

            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.game_running = False

            if button_play.collidepoint((mx, my)):
                if self.click:
                    self.play_pvp()

            self._check_menu_events()

            pygame.display.flip()

    def _check_menu_events(self):
        '''reaction to events generated by the keyboard and mouse inside menu'''
        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button:
                    self.click = True



if __name__ == "__main__":
    game = TicTacToe()
    game.run_game()

