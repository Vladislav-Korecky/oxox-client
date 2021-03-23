from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

from game import *
from player import *


class BaseLayout(FloatLayout):
    pass


class OXOXApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        layout = BaseLayout()
        return layout


if __name__ == '__main__':
    # creating game
    game = Game(6, 6, [Player(1), Player(2)])

    # starting kivy
    OXOXApp().run()

    # starting new match
    winner = game.play()

    # printing winner
    print("Player number " + str(winner) + " won!")
