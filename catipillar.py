import arcade

class player(arcade.Sprite):
    def __init__(self):
        super().__innit__(':resources:images/animated_characters/robot/robot_idle.png')
        self.center_x = 400
        self.center_y = 400

class bullet(arcade.Sprite):
        def __init__(self, x, y, change_x, change_y):
            super().__init__(':resources:images/space_shooter/lazer01.png')

class game(arcade.Window):
    def __init__(self): 
        super().__init__(800, 800, 'pilla')
        self.pilla = arcade.sprite(':resources:images/enemies/wormgreen_dead.png')
        self.pilla.center_x = 400
        self.pilla.change_y = 3
        self.scene = arcade.Scene()
        self.scene.add_sprite_list('players')
        self.scene['players'].append("pilla")


arcade.run()

