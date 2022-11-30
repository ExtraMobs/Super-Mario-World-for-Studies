import pygame
from .animations import Animations


class Resources:
    class Scenes:
        scenes = {}

        @classmethod
        def add_scene(cls, name, pygame_group, *args, **kwargs):
            def call_scene():
                return pygame_group(*args, **kwargs)

            cls.scenes[name] = call_scene

        @classmethod
        def get_scene(cls, name):
            return cls.scenes[name]()

    class Animation:
        cached = {}

        @classmethod
        def add_cache_animation(cls, name, fps, frame_copy=True):
            cls.cached[name] = Animations.get_animation(name, fps, frame_copy)

        @classmethod
        def get_cache_animation(cls, name):
            return_data = cls.cached[name]
            return return_data.copy()

    class Surface:
        surfaces = {}

        @staticmethod
        def load_from_file(path, alpha=True):
            surface = pygame.image.load(path)
            try:
                if alpha:
                    surface = surface.convert_alpha()
                else:
                    surface = surface.convert()
                return surface
            except pygame.error:
                return surface

        @classmethod
        def add_from_file(cls, name, path, alpha=True):
            cls.add_surface(name, cls.load_from_file(path, alpha))

        @classmethod
        def add_surface(cls, name, surface, copy=False):
            if copy:
                surface = surface.copy()
            cls.surfaces[name] = surface

        @classmethod
        def get_surface(cls, name, copy=False) -> pygame.Surface:
            surface = cls.surfaces[name]
            if copy:
                return surface.copy()
            else:
                return surface

        @staticmethod
        def get_new_surface(size, *flags, alpha=True):
            flag = 0
            for f in flags:
                if f != pygame.SRCALPHA:
                    flag |= f
            if alpha:
                flag |= pygame.SRCALPHA
            return pygame.Surface(size, flag)
