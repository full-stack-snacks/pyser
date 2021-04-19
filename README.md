# pyser

What’s this? The Getting Started Tutorial for the excellent Phaser JavaScript library. But the custom game code is in…. PYTHON thanks to Brython runs Python in the browser.
https://pyser-f4k03uc0q-fullstacksnacks.vercel.app/

E.g. code so you know I mean it :wink:
def addBounce(child, *args):
            child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8))
        self.stars.children.iterate(addBounce)
def collectStar(player, star):
            star.disableBody(True, True)
            self.score += 10
            self.scoreText.setText(“Score:   +str(self.score)) (edited)
