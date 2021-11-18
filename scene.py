# -*- encoding: utf-8 -*-

#print("scene")
class Scene:

    def __init__(self, director):
        self.director = director

    def on_update(self):
        raise NotImplemented("Tiene que implementar el método on_update.")

    def on_event(self, event):
        raise NotImplemented("Tiene que implementar el método on_event.")

    def on_draw(self, screen):
        raise NotImplemented("Tiene que implementar el método on_draw.")