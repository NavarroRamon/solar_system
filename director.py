import pygame
import sys



class Director:
    def __init__(self):
        self.screen = pygame.display.set_mode((1224, 700))
        pygame.display.set_caption("SistemaSolar")
        self.scene = None
        self.fullscreen = False
        self.quit_flag = False
        self.clock = pygame.time.Clock()
        self.framerate=30
        self.click=False
        self.down=False
        self.clickbox=pygame.Rect(4,1,5,5)
        self.giro=True
    def loop(self):
        while not self.quit_flag:
            time = self.clock.tick(self.framerate)
            [x,y]=pygame.mouse.get_pos()
            self.clickbox=pygame.Rect(x,y,5,5)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.click=True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.down=True
                else:
                    self.down=False
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        if self.giro:
                            self.giro=False
                        else:
                            self.giro=True



            self.scene.on_event()

            self.scene.on_update()

            self.scene.on_draw(self.screen)

            self.click=False

            pygame.display.flip()




    def change_scene(self, scene):
        self.scene = scene

    def quit(self):
        self.quit_flag = True
