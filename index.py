from browser import window
import javascript
from linked_list import LinkedList


Phaser = window.Phaser


class Game(object):
    def __init__(self):

        config = {
            "type": Phaser.AUTO,
            "width": 800,
            "height": 600,
            "backgroundColor": "#efefef",
            "scene": {
                "preload": self.preload,
                "create": self.create,
                "update": self.update,
            },
        }

        self.game = window.Phaser.Game.new(config)

        self.linked_list = LinkedList()
        self.linked_list.insert("D")
        self.linked_list.insert("C")
        self.linked_list.insert("B")
        self.linked_list.insert("A")

        self.head_display_node = None

    def preload(self, *args):
        this = javascript.this()
        this.load.image("sky", "assets/sky.png")
        this.load.image("arrow", "assets/arrow.png")
        this.load.image("note", "assets/sticky-purple.png")
        this.load.image("note2", "assets/sticky-red.png")
        this.load.image("current-note", "assets/sticky-yellow.png")
        this.load.image("crown", "assets/crown.png")

    def create(self, *args):
        this = javascript.this()
        this.add.image(400, 300, "sky")

        self.head_display_node = DisplayNode(
            this, self.linked_list.head, parent=self
        )

        self.crown = this.add.sprite(200, 200, "crown").setInteractive()
        self.crown.setScale(0.5)

        self.crown.setX(self.head_display_node.group.x)
        self.crown.setY(self.head_display_node.group.y - 80)

        def drag(pointer, gameObject, dragX, dragY):
            gameObject.x = dragX
            gameObject.y = dragY

        this.input.setDraggable(self.crown)
        this.input.on("drag", drag)

        self.note = this.add.sprite(100, 500, "note")
        self.note.setScale(0.15)
        self.note.setInteractive()
        this.input.setDraggable(self.note)

        self.note2 = this.add.sprite(150, 500, "note2")
        self.note2.setScale(0.15)
        self.note2.setInteractive()
        this.input.setDraggable(self.note2)

        self.current_note = this.add.sprite(200, 500, "current-note")
        self.current_note.setScale(0.1)
        self.current_note.setInteractive()
        this.input.setDraggable(self.current_note)

    def update(self, *args):
        this = javascript.this()
        # self.arrow.rotation += 0.1


class DisplayNode:
    def __init__(self, this, node, x=150, y=150, parent=None):

        print(parent and parent.linked_list)

        def point_left(pointer, *args):
            this = javascript.this()

            if this.rotation == 0.5:
                this.rotation = -2.5
                this.setX(this.x - 170)
                this.setY(this.y - 70)
            else:
                this.rotation = 0.5
                this.setX(this.x + 170)
                this.setY(this.y + 70)

                pass

        self.group = this.add.container()

        self.arrow = this.add.sprite(90, 30, "arrow").setInteractive()
        self.arrow.on("pointerup", point_left)
        self.arrow.rotation = 0.5

        self.group.add(self.arrow)

        self.circle = this.add.circle(0, 0, 50, 0x9966FF).setInteractive()
        self.circle.setStrokeStyle(8, 0xEFC53F)

        self.text = this.add.text(-5, -5, node.value)

        self.group.add(self.circle)
        self.group.add(self.text)

        # self.group.setAlpha(0.1)
        self.group.setY(y)
        self.group.setX(x)

        if node.next:
            DisplayNode(this, node.next, x + 150, y + 100, parent=parent)


GAME = Game()
