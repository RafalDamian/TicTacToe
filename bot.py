import random
import unittest

class Bot():

    def __init__(self):
        pass

    def pick_position(self, game_status):
        available_positions = []
        for position in [x for x in range(1,10)]:
            if not game_status[position]: available_positions.append(position)
        return random.choice(available_positions) 
    
    def pick_corner(self, game_status):
        available_corners = []
        for corner in [1,3,7,9]:
            if not game_status[corner]: available_corners.append(corner)
        if not available_corners: return 0
        return random.choice(available_corners)        

    def check_threats(self, game_status, who_is_threating):
        '''checks every field in case of being a threat
        [1][2][3]
        [4][5][6]
        [7][8][9]
        '''
        x = who_is_threating
        gs = game_status
        if ( ( gs[2] == x and gs[3] == x ) or ( gs[4] == x and gs[7] == x ) or ( gs[5] == x and gs[9] == x ) ) and not gs[1]:
            return 1
        elif ( ( gs[1] == x and gs[2] == x ) or ( gs[6] == x and gs[9] == x ) or ( gs[5] == x and gs[7] == x ) ) and not gs[3]:
            return 3
        elif ( ( gs[8] == x and gs[9] == x ) or ( gs[1] == x and gs[4] == x ) or ( gs[5] == x and gs[3] == x ) ) and not gs[7]:
            return 7
        elif ( ( gs[7] == x and gs[8] == x ) or ( gs[3] == x and gs[6] == x ) or ( gs[5] == x and gs[1] == x ) ) and not gs[9]:
            return 9
        elif ( ( gs[1] == x and gs[3] == x ) or ( gs[5] == x and gs[8] == x ) ) and not gs[2]:
            return 2
        elif ( ( gs[5] == x and gs[6] == x ) or ( gs[1] == x and gs[7] == x ) ) and not gs[4]:
            return 4
        elif ( ( gs[4] == x and gs[5] == x ) or ( gs[3] == x and gs[9] == x ) ) and not gs[6]:
            return 6
        elif ( ( gs[2] == x and gs[5] == x ) or ( gs[7] == x and gs[9] == x ) ) and not gs[8]:
            return 8
        elif ( ( gs[2] == x and gs[8] == x ) or ( gs[4] == x and gs[6] == x ) or ( gs[1] == x and gs[9] == x ) or ( gs[3] == x and gs[7] == x ) ) and not gs[5]:
            return 5
        else:
            return 0

    def easy(self, game_status):
        return self.pick_position(game_status)

    def medium(self, game_status, who_to_move):
        '''first checking threats. if no threats in the position making a random move'''
        if move := self.check_threats(game_status, who_to_move): return move
        opponent = {'X': 'O', 'O': 'X'}
        if move := self.check_threats(game_status, opponent[who_to_move]): return move
        return self.pick_position(game_status)
        
    def impossible(self, game_status, who_to_move):
        '''threats  > corners > band - imposible to defeat'''
        if move := self.check_threats(game_status, who_to_move): return move
        opponent = {'X': 'O', 'O': 'X'}
        if move := self.check_threats(game_status, opponent[who_to_move]): return move
        if move := self.pick_corner(game_status): return move 
        return self.pick_position(game_status)


class Test_Bot(unittest.TestCase):

    def setUp(self):
        self.Bot = Bot()
        self.game_status_1 = {1: 'X', 2: 'X', 3: '',
                              4: '', 5: 'O', 6: '',
                              7: 'O', 8: '', 9: ''}
        self.game_status_2 = {1: 'X', 2: 'O', 3: 'X',
                              4: '', 5: 'O', 6: '',
                              7: '', 8: '', 9: ''}
        self.game_status_3 = {1: 'X', 2: 'X', 3: 'O',
                              4: 'O', 5: 'O', 6: 'X',
                              7: 'X', 8: 'X', 9: ''}
        self.game_status_4 = {1: 'X', 2: 'X', 3: '',
                              4: 'O', 5: 'O', 6: '',
                              7: 'X', 8: 'X', 9: 'O'}
        self.game_status_5 = {1: '', 2: '', 3: '',
                              4: '', 5: '', 6: '',
                              7: '', 8: '', 9: ''}
        self.game_status_6 = {1: '', 2: '', 3: '',
                              4: '', 5: 'O', 6: '',
                              7: '', 8: '', 9: ''}
        self.game_status_7 = {1: 'b', 2: '', 3: 'd',
                              4: '', 5: 'O', 6: '',
                              7: 'a', 8: '', 9: 'c'}
        self.game_status_8 = {
                              1: '', 2: '', 3: 'O',
                              4: 'O', 5: 'X', 6: 'X',
                              7: '', 8: 'X', 9: 'O'}
    
    
    def test_easy_bot_1(self):
        self.assertEqual(self.Bot.easy(self.game_status_3), 9)
    
    def test_easy_bot_2(self):
        self.assertIn(self.Bot.easy(self.game_status_5), [x for x in range(1,10)])
    
    def test_easy_bot_3(self):
        self.assertIn(self.Bot.easy(self.game_status_1), [3, 4, 6, 8, 9])

    def test_medium_bot_1(self):
        self.assertEqual(self.Bot.medium(self.game_status_1, 'X'), 3)
        self.assertEqual(self.Bot.medium(self.game_status_1, 'O'), 3)

    def test_medium_bot_2(self):
        self.assertEqual(self.Bot.medium(self.game_status_2, 'X'), 8)
        self.assertEqual(self.Bot.medium(self.game_status_2, 'O'), 8)

    def test_medium_bot_3(self):
        self.assertEqual(self.Bot.medium(self.game_status_3, 'X'), 9)
        self.assertEqual(self.Bot.medium(self.game_status_3, 'O'), 9)
    
    def test_medium_bot_4(self):
        self.assertEqual(self.Bot.medium(self.game_status_4, 'X'), 3)
        self.assertEqual(self.Bot.medium(self.game_status_4, 'O'), 6)

    def test_medium_bot_5(self):
        self.assertIn(self.Bot.medium(self.game_status_5, 'X'), [x for x in range(1,10)])

    def test_medium_bot_6(self):
        self.assertEqual(self.Bot.medium(self.game_status_8, 'O'), 2)

    def test_impossible_bot_1(self):
        self.assertEqual(self.Bot.impossible(self.game_status_1, 'X'), 3)
        self.assertEqual(self.Bot.impossible(self.game_status_1, 'O'), 3)

    def test_impossible_bot_2(self):
        self.assertEqual(self.Bot.impossible(self.game_status_2, 'X'), 8)
        self.assertEqual(self.Bot.impossible(self.game_status_2, 'O'), 8)

    def test_impossible_bot_3(self):
        self.assertEqual(self.Bot.impossible(self.game_status_3, 'X'), 9)
        self.assertEqual(self.Bot.impossible(self.game_status_3, 'O'), 9)
    
    def test_impossible_bot_4(self):
        self.assertEqual(self.Bot.impossible(self.game_status_4, 'X'), 3)
        self.assertEqual(self.Bot.impossible(self.game_status_4, 'O'), 6)

    def test_impossible_bot_5(self):
        self.assertIn(self.Bot.impossible(self.game_status_5, 'X'), [1, 3, 7, 9])

    def test_impossible_bot_6(self):
        self.assertIn(self.Bot.impossible(self.game_status_6, 'X'), [1, 3, 7, 9])

    def test_impossible_bot_7(self):
        self.assertIn(self.Bot.impossible(self.game_status_7, 'X'), [2,4,6,8])


if __name__ == '__main__':
    unittest.main()