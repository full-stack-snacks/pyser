from browser import window
import javascript

Phaser = window.Phaser

class Game(object):
    def __init__(self):

        config = {
            'type': Phaser.AUTO,
            'width': 800,
            'height': 600,
            'backgroundColor': '#2d2d2d',
            'scene': {
                'preload': self.preload,
                'create': self.create,
            }
        };

        self.game = window.Phaser.Game.new(config)

    def preload(self, *args):
        this = javascript.this()

        this.load.setBaseURL('https://labs.phaser.io')
        this.load.image('logo', 'assets/sprites/phaser3-logo.png')


    def create(self, *args):
        this = javascript.this()
        this.add.image(400, 300, 'logo')



GAME = Game()
