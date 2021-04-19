from browser import window
import javascript

Phaser = window.Phaser


class Game(object):
    def __init__(self):

        config = {
            "type": Phaser.AUTO,
            "width": 800,
            "height": 600,
            "physics": {
                "default": "arcade",
                "arcade": {
                    "gravity": {"y": 300},
                    "debug": False,
                },
            },
            "scene": {
                "preload": self.preload,
                "create": self.create,
                "update": self.update,
            },
        }

        self.game = window.Phaser.Game.new(config)
        self.score = 0

    def preload(self, *args):
        this = javascript.this()

        this.load.image("sky", "assets/sky.png")
        this.load.image("ground", "assets/platform.png")
        this.load.image("star", "assets/star.png")
        this.load.image("bomb", "assets/bomb.png")
        this.load.spritesheet(
            "dude", "assets/dude.png", {"frameWidth": 32, "frameHeight": 48}
        )

    def create(self, *args):
        this = javascript.this()
        this.add.image(400, 300, "sky")

        self.platforms = this.physics.add.staticGroup()

        self.platforms.create(400, 568, "ground").setScale(2).refreshBody()

        self.platforms.create(600, 400, "ground")
        self.platforms.create(50, 250, "ground")
        self.platforms.create(750, 220, "ground")

        self.player = this.physics.add.sprite(100, 450, "dude")

        self.player.setBounce(0.2)
        self.player.setCollideWorldBounds(True)

        this.physics.add.collider(self.player, self.platforms)

        this.anims.create(
            {
                "key": "left",
                "frames": this.anims.generateFrameNumbers(
                    "dude", {"start": 0, "end": 3}
                ),
                "frameRate": 10,
                "repeat": -1,
            }
        )

        this.anims.create(
            {
                "key": "turn",
                "frames": [{"key": "dude", "frame": 4}],
                "frameRate": 20,
            }
        )

        this.anims.create(
            {
                "key": "right",
                "frames": this.anims.generateFrameNumbers(
                    "dude", {"start": 5, "end": 8}
                ),
                "frameRate": 10,
                "repeat": -1,
            }
        )

        self.stars = this.physics.add.group(
            {
                "key": "star",
                "repeat": 11,
                "setXY": {"x": 12, "y": 0, "stepX": 70},
            }
        )

        def addBounce(child, *args):
            child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8))

        self.stars.children.iterate(addBounce)

        def collectStar(player, star):
            star.disableBody(True, True)
            self.score += 10
            self.scoreText.setText("Score: " + str(self.score))

            x = (
                Phaser.Math.Between(400, 800)
                if player.x < 400
                else Phaser.Math.Between(0, 400)
            )

            bomb = bombs.create(x, 16, "bomb")
            bomb.setBounce(1)
            bomb.setCollideWorldBounds(True)
            bomb.setVelocity(Phaser.Math.Between(-200, 200), 20)

        this.physics.add.collider(self.stars, self.platforms)

        this.physics.add.overlap(
            self.player, self.stars, collectStar, None, this
        )

        self.scoreText = this.add.text(
            16, 16, "score: 0", {"fontSize": "32px", "fill": "#000"}
        )

        def hitBomb(player, bomb):
            this.physics.pause()

            player.setTint(0xFF0000)

            player.anims.play("turn")

        bombs = this.physics.add.group()

        this.physics.add.collider(bombs, self.platforms)

        this.physics.add.collider(self.player, bombs, hitBomb, None, this)

    def update(self, *args):

        this = javascript.this()

        self.cursors = this.input.keyboard.createCursorKeys()

        if self.cursors.left.isDown:

            self.player.setVelocityX(-160)

            self.player.anims.play("left", True)

        elif self.cursors.right.isDown:

            self.player.setVelocityX(160)

            self.player.anims.play("right", True)

        else:

            self.player.setVelocityX(0)

            self.player.anims.play("turn")

        if (
            self.cursors.up.isDown or self.cursors.space.isDown
        ) and self.player.body.touching.down:

            self.player.setVelocityY(-330)


GAME = Game()
