import arcade

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 450
SCREEN_TITLE = "Ladders Runner"
TILE_SCALING = 0.5
GRAVITY = 0.5
PLAYER_SPEED = 6
LADDER_SPEED = 3  # Скорость по лестнице


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SPANISH_SKY_BLUE)

    def setup(self):
        self.player_spritelist = arcade.SpriteList()
        self.player = arcade.Sprite(
            ":resources:/images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player.center_x = 25
        self.player.center_y = 100
        self.player_spritelist.append(self.player)

        self.tile_map = arcade.load_tilemap("lesson.tmx",
                                            scaling=0.5)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.obstackles = arcade.SpriteList()

        for plat in self.scene['platforms']:
            if plat.center_y < SCREEN_HEIGHT // 3:
                plat.boundary_bottom = 32
                plat.boundary_top = 256
                plat.change_y = 2
            else:
                plat.boundary_bottom = 232
                plat.boundary_top = 384
                plat.change_y = 1

                # Физический движок
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.player,
            gravity_constant=GRAVITY,
            walls=self.scene['collision'],
            platforms=self.scene['platforms']
        )

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.player_spritelist.draw()

    def on_update(self, delta_time):
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT and self.player.change_x < 0:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT and self.player.change_x > 0:
            self.player.change_x = 0


def setup_game(width=768, height=450, title="Ladders Runner"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()