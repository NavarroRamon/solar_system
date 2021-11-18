import os, sys
with open(os.devnull, 'w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    import pygame
    sys.stdout = oldstdout
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)
import director
import scene_home

print("=====================================================================================")
print("SALUDOS TERRICOLA!===================================================================")
print("=====================================================================================")
print("=                                   SISTEMA SOLAR                                   =")
print("=====================================================================================")
print("=====================================================================================")
print("= Con esta aplicación es posible visualizar algunos de los modelos de sistema solar =")
print("= que han sido elaborados a través de la historia.                                  =")
print("= Además de eso presenta información básica y curiosidades acerca de los planetas   =")
print("= que componen nuestro sistema solar.                                               =")
print("=====================================================================================")
print("")
print("=====================================================================================")
print("= Todas imagenes utilizadas son de uso libre, los iconos y sonidos que se muestran  =")
print("= en el programa han sido elaborados desde cero.                                    =")
print("= La elaboración de este programa ha sido realizada en el lenguaje python           =")
print("= utilizando las paqueterias 'pygame' y 'math'.                                     =")
print("= Puedes enviar tus dudas o sugerencias al correo que aparece en la parte inferior. =")
print("=====================================================================================")
print("")
print("=====================================================================================")
print("= Contacto: ramon17017@outlook.com                                 v0.2, 12/12/2019 =")
print("=====================================================================================")


def main():    
    dir = director.Director()
    scene = scene_home.SceneHome(dir)
    dir.change_scene(scene)
    dir.loop()    
    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    main()
