import os
import pygame

from gameengine import Display, GameEngine, Window, GameResources, Animations


class SpriteTest(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()
        self.image = GameResources.get_surface("Mario SpriteSheet")
        self.rect = self.image.get_rect()


class GameManager(pygame.sprite.LayeredDirty):
    def __init__(self) -> None:
        super().__init__()

        self.sprite_test = SpriteTest()
        self.add(self.sprite_test)

    def update(self) -> None:
        super().update()
        if GameEngine.request_quit:
            GameEngine.quit()


class Game:
    def __init__(self):

        Window.set_title("Super Mario World [Python]")
        Display.set_scale(4)

        GameEngine.init((720, 405))

        self.load_sprites()

        GameEngine.set_framerate(60)
        GameEngine.set_current_scene(GameManager())

    def load_sprites(self):
        playable_characters = os.path.abspath("assets\Playable Characters")
        GameResources.add_surface_from_file(
            "Mario SpriteSheet",
            os.path.join(playable_characters, "SNES - Super Mario World - Mario.png"),
        )
        GameResources.add_surface_from_file(
            "Luigi SpriteSheet",
            os.path.join(
                playable_characters, "SNES - Super Mario World - Luigi All-Stars.png"
            ),
        )

        mario_spritesheet = GameResources.get_surface("Mario SpriteSheet")

        # Animations.add_animation_data("Mario", Animations.AREA_TYPE, ())

    def run(self):
        GameEngine.start_loop()


if __name__ == "__main__":
    Game().run()
