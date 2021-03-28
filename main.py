from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

from game import *
from player import *


class BoardButton(Button):
    pass


class BoardLayout(GridLayout):
    def __init__(self, board, **kwargs):
        super(BoardLayout, self).__init__(**kwargs)

        self.rows = len(board)

        for line in board:
            for _ in line:
                self.add_widget(BoardButton())


class BaseLayout(FloatLayout):
    pass


class OXOXApp(App):
    def __init__(self, board, **kwargs):
        super().__init__(**kwargs)
        self.board = board

        self.base_layout = None
        self.board_layout = None

    def build(self):
        Window.maximize()
        Window.clearcolor = (1, 1, 1, 1)

        self.base_layout = BaseLayout()

        self.board_layout = BoardLayout(self.board)

        Window.bind(on_resize=self.on_resize)

        self.on_resize(Window, Window.size[0], Window.size[1])

        self.base_layout.add_widget(self.board_layout)
        return self.base_layout

    def on_resize(self, window, width, height):
        x_pos = (width - (75 * len(self.board))) / 2
        self.board_layout.pos_hint = {"y": -0.3}
        self.board_layout.pos = (x_pos, 0)


if __name__ == '__main__':
    # creating game
    game = Game(6, 6, [Player(1), Player(2)])

    # starting kivy
    OXOXApp(game.board).run()

    """
    # starting new match
    winner = game.play()

    # printing winner
    print("Player number " + str(winner) + " won!")

    """
