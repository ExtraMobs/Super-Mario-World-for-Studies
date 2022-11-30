import math
import pygame

import assets
from gameengine import Display, GameEngine, Window, Resources


class Mario(pygame.sprite.DirtySprite):
    def __init__(self) -> None:
        super().__init__()
        self.animation = Resources.Animation.get_cache_animation("mario_small_walk")

        self.pos = pygame.Vector2(0)
        self.offset = pygame.Vector2(0)

        self.image = self.animation.get_current_frame()
        self.rect = self.image.get_rect()
        self.dirty = 2

    def update(self):
        super().update()
        self.animation.update(GameEngine.deltatime)

        self.image = self.animation.get_current_frame()

        if self.animation.current_frame == 1:
            self.offset.y = -1
        else:
            self.offset.y = 0

        pos = self.pos + self.offset
        self.rect.topleft = (math.ceil(pos.x), math.ceil(pos.y))


class GameManager(pygame.sprite.LayeredDirty):
    def __init__(self) -> None:
        self.mario = Mario()
        super().__init__(self.mario)

    def update(self) -> None:
        super().update()
        if GameEngine.request_quit:
            GameEngine.quit()


class Game:
    def __init__(self):

        Window.set_title("Super Mario World [Python]")
        Display.set_scale(4)

        Window.set_size((720, 405))
        Display.update_display_from_window()
        Display.background = Window.window_surface.copy()

        assets.load_assets()

        GameEngine.set_framerate(60)
        GameEngine.set_scene(GameManager())

    def run(self):
        GameEngine.start_loop()


if __name__ == "__main__":
    Game().run()
