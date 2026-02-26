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
        self.keys_pressed = set()

        self.tile_map = arcade.load_tilemap("lesson.tmx",
                                            scaling=0.5)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Физический движок
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.player,
            gravity_constant=GRAVITY,
            walls=self.scene['collision'],
            ladders=self.scene['ladders']
        )

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.player_spritelist.draw()

    def on_update(self, delta_time):
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        if key == arcade.key.UP:
            on_ladder = arcade.check_for_collision_with_list(self.player, self.scene['ladders'])
            if on_ladder:
                self.player.change_y = LADDER_SPEED
        elif key == arcade.key.DOWN:
            on_ladder = arcade.check_for_collision_with_list(self.player, self.scene['ladders'])
            if on_ladder:
                self.player.change_y = -LADDER_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)
        if key == arcade.key.LEFT and self.player.change_x < 0:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT and self.player.change_x > 0:
            self.player.change_x = 0
        elif key == arcade.key.UP and self.player.change_y > 0:
            self.player.change_y = 0
        elif key == arcade.key.DOWN and self.player.change_y < 0:
            self.player.change_y = 0


def setup_game(width=768, height=450, title="Ladders Runner"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()