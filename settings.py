import pygame

class Settings:

    def __init__(self, screen):
        self.bg_color = (0,0,0)
        self.button_color = (255,0,0)
        self.text_color = (255,255,255)
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.positions = {
            1: (0.383*self.screen_width, 0.2*self.screen_height+0.058*self.screen_width),
            2: (0.5*self.screen_width, 0.2*self.screen_height+0.058*self.screen_width),
            3: (0.616*self.screen_width, 0.2*self.screen_height+0.058*self.screen_width),
            4: (0.383*self.screen_width, 0.2*self.screen_height+0.175*self.screen_width),
            5: (0.5*self.screen_width, 0.2*self.screen_height+0.175*self.screen_width),
            6: (0.616*self.screen_width, 0.2*self.screen_height+0.175*self.screen_width),
            7: (0.383*self.screen_width, 0.2*self.screen_height+0.293*self.screen_width),
            8: (0.5*self.screen_width, 0.2*self.screen_height+0.293*self.screen_width),
            9: (0.616*self.screen_width, 0.2*self.screen_height+0.293*self.screen_width),
        } # center of game field square

        x = 0.5 * self.screen_width
        y = self.screen_height
        board = pygame.Rect((0.65*x, 0.2*y), (0.7*x,0.7*x))
        a = 0.7/3*x #single position square side len
        pos_hw = (a, a)
        self.positions_buttons = {
            1:  pygame.Rect(board.topleft,pos_hw),
            2:  pygame.Rect((board.left+a,board.top),pos_hw),
            3:  pygame.Rect((board.left+2*a,board.top),pos_hw),
            4:  pygame.Rect((board.left,board.top+a),pos_hw),
            5:  pygame.Rect((board.left+a,board.top+a),pos_hw),
            6:  pygame.Rect((board.left+2*a,board.top+a),pos_hw),
            7:  pygame.Rect((board.left,board.top+2*a),pos_hw),
            8:  pygame.Rect((board.left+a,board.top+2*a),pos_hw),
            9:  pygame.Rect((board.left+2*a,board.top+2*a),pos_hw),
        }