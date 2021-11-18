import scene
import math
import pygame

#CArga de imagenes
g=pygame.image.load('img/g.jpg')
copernicoimg=pygame.image.load('img/copernico.png')
datasol=pygame.image.load('img/datasol.png')
ptolomeo1=pygame.image.load('img/ptolomeo1.png')
aristoteles1=pygame.image.load('img/aristoteles1.png')
aristarco1=pygame.image.load('img/aristarco1.png')
kepler1=pygame.image.load('img/kepler1.png')
info=pygame.image.load('img/info.png')
stars=pygame.image.load('img/stars.png')
sol=pygame.image.load('img/sol.png')
earth=pygame.image.load('img/earth.png')
notaoff=pygame.image.load('img/not.png')
evo=pygame.image.load('img/evo.png')
infoact=pygame.image.load('img/infoact.png')
nota=pygame.image.load('img/nosound.png')
evolucionon=pygame.image.load('img/evolucion.png')
cross = pygame.image.load('img/cross.png')
nombre = pygame.image.load('img/nombre.png')
relojactivo = pygame.image.load('img/relojactivo.png')

pmercurio = pygame.image.load('img/mercurio.png')
pmercurio = pygame.transform.scale(pmercurio, (600, 600))
pvenus = pygame.image.load('img/venus.jpg')
pvenus = pygame.transform.scale(pvenus, (600, 600))
ptierra = pygame.image.load('img/tierra.jpg')
ptierra = pygame.transform.scale(ptierra, (600, 600))
pmarte = pygame.image.load('img/marte.jpg')
pmarte = pygame.transform.scale(pmarte, (600, 600))
pjupiter = pygame.image.load('img/jupiter.jpg')
pjupiter = pygame.transform.scale(pjupiter, (600, 600))
psaturno = pygame.image.load('img/saturno.jpg')
psaturno = pygame.transform.scale(psaturno, (600, 600))
purano = pygame.image.load('img/urano.jpg')
purano = pygame.transform.scale(purano, (600, 600))
pneptuno = pygame.image.load('img/neptuno.jpg')
pneptuno = pygame.transform.scale(pneptuno, (600, 600))


dmercurio = pygame.image.load('img/dmercurio.png')
dvenus = pygame.image.load('img/dvenus.png')
dmarte = pygame.image.load('img/dmarte.png')
dtierra = pygame.image.load('img/dtierra.png')
djupiter = pygame.image.load('img/djupiter.png')
dsaturno = pygame.image.load('img/dsaturno.png')
dneptuno = pygame.image.load('img/dneptuno.png')
durano = pygame.image.load('img/durano.png')
crossback = pygame.image.load('img/crossback2.png')


#Pantalla de inicio
class SceneHome(scene.Scene):
    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.sistemasolar=False
        self.x=0
        self.y=0
        self.color= (74,73,255)
        self.tetha=0
        self.font2 = pygame.font.Font(None, 26)
        self.font1 = pygame.font.Font(None, 130)
    def on_event(self):
        keys=pygame.key.get_pressed()
        if self.director.click==True:
            self.sistemasolar=True
    def on_update(self):
        self.tetha+=0.04
        h=600
        k=350
        if self.tetha>=6.29:
            self.tetha=0
        self.x, self.y= trayectorias(h,k,400,200,self.tetha)
        


    def on_draw(self, screen):
        screen.fill((20,20,20))
        pygame.draw.ellipse(screen, (120,120,30), (600-1/(1/400**2 )**(1/2),350 - 1/( 1/200**2)**(1/2),2/(1/400**2 )**(1/2),2/( 1/200**2)**(1/2)), 1)       
        pygame.draw.circle(screen, (190,0,10), (int(self.x), int(self.y)), 30, 0)        
        if self.sistemasolar:
            pygame.mixer.music.load("img/solar.mp3")
            pygame.mixer.music.play(-1)
            self.sistemasolar=False
            scene=sistemasolar(self.director)
            self.director.change_scene(scene)
        autores =self.font2.render( "Autores: Navarro Ramon, Teran Molina Cinthia" , True, self.color)
        contacto =self.font2.render( "Contacto: ramon17017@outlook.com" , True, self.color)
        vercion =self.font2.render( "v0.2" , True, self.color)
        screen.blit(autores, [10, 650])
        screen.blit(contacto, [10, 675])
        screen.blit(vercion, [1175, 670])
        screen.blit(nombre, (0,0),(0,0,1000,600))

class sistemasolar(scene.Scene):
    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.showinfo=False
        self.font2 = pygame.font.Font(None, 26)
        self.info = pygame.Rect(1175,30,12,30)
        self.relojact=False
        self.evolucion=False
        self.solbox=pygame.Rect(630,330,80,80)
        self.copernicobox=pygame.Rect(1,1,1,1)
        self.keplerbox=pygame.Rect(1,1,1,1)
        self.sound=True
        self.one=False
        self.aristotelesrect = (87, 48, 160, 34)
        self.aristoteles = pygame.Rect(self.aristotelesrect)
        self.two=False
        self.aristarcorect = (270, 48, 275, 34)
        self.aristarco = pygame.Rect(self.aristarcorect)
        self.three=False
        self.ptolomeorect = (566, 48, 254, 34)
        self.ptolomeo = pygame.Rect(self.ptolomeorect)
        self.four=True
        self.keplerrect = (840, 48, 110, 34)
        self.kepler = pygame.Rect(self.keplerrect)

        self.evolucionbox = pygame.Rect(9, 611, 140, 80)
        self.soundbox = pygame.Rect(3, 6, 50, 60)
        self.tiempo = pygame.Rect(521, 632, 500,681)
        self.reloj = pygame.Rect(1047, 618, 498,70)
        self.clickbox=pygame.Rect(4,1,5,5)
        self.crossic=pygame.Rect(1080, 65, 60,60)
        self.d=8
        self.tiempo2=27
        self.cross=True
        self.mercuriox=0
        self.mercurioy=0
        self.mercuriotetha=3.1417
        
        self.mercord=(0,0,10,10)        
        self.vencord=(0,0,10,10)
        self.tiecord=(0,0,10,10)
        self.marcord=(0,0,10,10)
        self.jupcord=(0,0,10,10)
        self.satcord=(0,0,10,10)
        self.uracord=(0,0,10,10)
        self.nepcord=(0,0,10,10)
        
        self.venusx=0
        self.venusy=0
        self.venustetha=0
        
        self.tierrax=0
        self.tierray=0
        self.tierratetha=3.1417
        
        self.martex=0
        self.martey=0
        self.martetetha=3.1417

        self.jupiterx=0
        self.jupitery=0
        self.jupitertetha=3.1417

        self.saturnox=0
        self.saturnoy=0
        self.saturnotetha=3.1417
        
        self.uranox=0
        self.uranoy=0
        self.uranotetha=3.1417
        
        self.neptunox=0
        self.neptunoy=0
        self.neptunotetha=3.1417
        
        self.escala=27
        self.moveticker=0
        self.realod=pygame.Rect(1145,620,70,70)
        self.a=0
        self.b=3
        self.c=5
        self.orbitaexterna1=0
        self.orbitainterna1=0
        self.orbitaexterna2=3
        self.orbitainterna2=1
        self.orbitaexterna3=5
        self.orbitainterna3=3
    def on_event(self):        
        self.aumentos()
        [x,y]=pygame.mouse.get_pos()
        self.clickbox=pygame.Rect(x,y,5,5)
        
        if self.four:
            self.infour()
            
        if self.clickbox.colliderect(self.evolucionbox) and self.director.click:
            if self.evolucion==True:
                self.evolucion=False
            else:
                self.evolucion=True
        elif self.clickbox.colliderect(self.soundbox):
            if self.director.click:
                if self.sound:
                    self.sound=False
                    pygame.mixer.music.stop()
                else:
                    self.sound=True
                    pygame.mixer.music.play(-1)
            
    def on_update(self):
        if self.moveticker>0:
            self.moveticker-=1
        if self.four:
            self.trayectoriaselipticas()        
        elif self.one:
            self.a+=0.02
            if self.a >= 6.2832:
                self.a=0
            self.b+=0.007
            if self.b >= 6.2832:
                self.b=0
            self.c+=0.01
            if self.c >= 6.2832:
                self.c=0
        elif self.two:
            self.a+=0.02
            if self.a >= 6.2832:
                self.a=0
            self.b+=0.007
            if self.b >= 6.2832:
                self.b=0
            self.c+=0.01
            if self.c >= 6.2832:
                self.c=0
        elif self.three:
            self.orbitaexterna1+=0.05
            if self.orbitaexterna1 >= 6.2832:
                self.c=0
            self.orbitainterna1+=0.005
            if self.orbitainterna1 >= 6.2832:
                self.c=0
            self.orbitaexterna2+=0.05
            if self.orbitaexterna2 >= 6.2832:
                self.c=0
            self.orbitainterna2+=0.005
            if self.orbitainterna2 >= 6.2832:
                self.c=0
            self.orbitaexterna3+=0.05
            if self.orbitaexterna3 >= 6.2832:
                self.c=0
            self.orbitainterna3+=0.007
            if self.orbitainterna3 >= 6.2832:
                self.c=0
            
    def on_draw(self, screen):
        screen.fill((0,0,0))
#                   pygame.image.save(screen, "Dataimage.png")
        if self.four:
            self.drawfour(screen)
        elif self.one:
            self.drawone(screen)
        elif self.two:
            self.drawtwo(screen)
        elif self.three:
            self.drawthree(screen)                        



        if self.sound==False:
            screen.blit(nota, (0,0),(0,0,70,100))
        else:
            screen.blit(notaoff, (0,0),(0,0,70,100))
        self.evolucionfunc(screen)



        
        if self.showinfo==False:
            pygame.draw.rect(screen , (100,0,0), (1080,64,60,60), 0)
            pygame.draw.rect(screen , (125,0,0), (1085,69,50,50), 0)
            pygame.draw.rect(screen , (150,0,0), (1090,74,40,40), 0)            
            pygame.draw.rect(screen , (175,0,0), (1095,79,35,30), 0)
            pygame.draw.rect(screen , (200,0,0), (1100,84,20,20), 0)
            pygame.draw.rect(screen , (255,0,0), (1105,89,10,10), 0)           
        else:
            pygame.draw.rect(screen , (0,100,0), (1080,64,60,60), 0)
            pygame.draw.rect(screen , (0,125,0), (1085,69,50,50), 0)
            pygame.draw.rect(screen , (0,150,0), (1090,74,40,40), 0)            
            pygame.draw.rect(screen , (0,175,0), (1095,79,35,30), 0)
            pygame.draw.rect(screen , (0,200,0), (1100,84,20,20), 0)
            pygame.draw.rect(screen , (0,255,0), (1105,89,10,10), 0) 
            
        if self.clickbox.colliderect(self.crossic) and self.director.click:
            if self.showinfo==True:
                self.showinfo=False
            else:
                self.showinfo=True

#==============================================================================
#________CUATRO_MODELOS________________________________________________________
#==============================================================================
    def drawthree(self, screen):
        screen.blit(stars, (0,0),(0,0,1224,700))            
        pygame.draw.circle(screen, (120,120,120), (398,375), 100, 1)
        pygame.draw.circle(screen, (120,120,120), (398,375), 160, 1)
        pygame.draw.circle(screen, (120,120,120), (398,375), 230, 1)
        screen.blit(earth, (0,0),(0,0,500,500))  
        pygame.draw.circle(screen, (120,60,60), (400+ int(160*math.cos(self.orbitainterna1))+ int(30*math.cos(self.orbitaexterna1)),375+ int(160*math.sin(self.orbitainterna1))+ int(30*math.sin(self.orbitaexterna1))), 12, 0) 
        pygame.draw.circle(screen, (160,160,60), (400+ int(100*math.cos(self.orbitainterna2))+ int(20*math.cos(self.orbitaexterna2)),375+ int(100*math.sin(self.orbitainterna2))+ int(20*math.sin(self.orbitaexterna2))), 13, 0)            
        pygame.draw.circle(screen, (220,220,0), (400+ int(230*math.cos(self.orbitainterna3))+ int(20*math.cos(self.orbitaexterna3)),375+ int(230*math.sin(self.orbitainterna3))+ int(20*math.sin(self.orbitaexterna3))), 16, 0)            
        if self.showinfo:
            screen.blit(ptolomeo1, (780,150))      

    def drawtwo(self,screen):
        pygame.draw.circle(screen, (120,120,120), (398,375), 100, 1)
        pygame.draw.circle(screen, (120,120,120), (398,375), 160, 1)
        pygame.draw.circle(screen, (120,120,120), (398,375), 230, 1)
        screen.blit(stars, (0,0),(0,0,1224,700))            
        screen.blit(sol, (0,0),(0,0,500,500))  
        pygame.draw.circle(screen, (140,60,50), (400+ int(100*math.cos(self.a)),375+ int(100*math.sin(self.a))), 13, 0)
        pygame.draw.circle(screen, (160,160,160), (400+ int(160*math.cos(self.c))+ int(30*math.cos(self.a)),375+ int(160*math.sin(self.c))+ int(30*math.sin(self.a))), 8, 0)      
        pygame.draw.circle(screen, (0,0,250), (400+ int(160*math.cos(self.c)),375+ int(160*math.sin(self.c))), 15, 0)         
        pygame.draw.circle(screen, (130,130,0), (400+ int(230*math.cos(self.b)),375+ int(230*math.sin(self.b))), 18, 0)
        if self.showinfo:
            screen.blit(aristarco1, (780,150))    
    def drawone(self,screen):
        pygame.draw.circle(screen, (120,120,120), (398,375), 100, 1)
        pygame.draw.circle(screen, (120,120,120), (398,375), 160, 1)
        pygame.draw.circle(screen, (120,120,120), (398,375), 230, 1)
        screen.blit(stars, (0,0),(0,0,1224,700))            
        screen.blit(earth, (0,0),(0,0,500,500))  
        pygame.draw.circle(screen, (160,160,160), (400+ int(100*math.cos(self.a)),375+ int(100*math.sin(self.a))), 10, 0)
        pygame.draw.circle(screen, (30,60,10), (400+ int(160*math.cos(self.c)),375+ int(160*math.sin(self.c))), 14, 0)
        pygame.draw.circle(screen, (230,230,0), (400+ int(230*math.cos(self.b)),375+ int(230*math.sin(self.b))), 18, 0)
        if self.showinfo:
            screen.blit(aristoteles1, (780,150))    
    def allfalse(self):
        self.one=False
        self.two=False
        self.three=False
        self.four=False
    def infour(self):
        [x,y]=pygame.mouse.get_pos()
        if self.clickbox.colliderect(self.realod):
            if self.director.down:
                self.mercuriotetha=3.1417
                self.venustetha=3.1417
                self.tierratetha=3.1417
                self.martetetha=3.1417
                self.jupitertetha=3.1417
                self.saturnotetha=3.1417
                self.uranotetha=3.1417
                self.neptunotetha=3.1417
        elif self.clickbox.colliderect(self.reloj) and self.director.click:
            if self.relojact==True:
                self.relojact=False
            else:
                self.relojact=True
        elif self.clickbox.colliderect(self.tiempo) and self.relojact==True:
            self.tiempo2=x-520
            if self.director.click:
                self.escala=self.tiempo2
    def drawfour(self, screen):
        pygame.draw.circle(screen, (255,180,0), (670,375), 70, 0)
        pygame.draw.circle(screen, (240,100,250),    (int(self.neptunox),int(self.neptunoy)), 10, 0)                
        pygame.draw.circle(screen, (0,40,80),    (int(self.uranox),int(self.uranoy)), 12, 0)        
        pygame.draw.circle(screen, (240,100,200),    (int(self.saturnox),int(self.saturnoy)), 22, 0)        
        pygame.draw.circle(screen, (140,100,150),    (int(self.jupiterx),int(self.jupitery)), 30, 0)        
        pygame.draw.circle(screen, (140,0,0),    (int(self.martex),int(self.martey)), 3, 0) 
        pygame.draw.circle(screen, (0,0,190),    (int(self.tierrax),int(self.tierray)), 3, 0)        
        pygame.draw.circle(screen, (40,200,120),   (int(self.venusx)   ,int(self.venusy)), 6, 0)     
        pygame.draw.circle(screen, (140,100,0),    (int(self.mercuriox),int(self.mercurioy)), 2, 0)

        pygame.draw.circle(screen, (240,240,140),    (int(self.neptunox),int(self.neptunoy)), 10, 1)                
        pygame.draw.circle(screen, (240,240,140),    (int(self.uranox),int(self.uranoy)), 12, 1)        
        pygame.draw.circle(screen, (240,240,140),    (int(self.saturnox),int(self.saturnoy)), 22, 1)        
        pygame.draw.circle(screen, (240,240,140),    (int(self.jupiterx),int(self.jupitery)), 30, 1)        
        pygame.draw.circle(screen, (240,240,140),    (int(self.martex),int(self.martey)), 3, 1) 
        pygame.draw.circle(screen, (240,240,140),    (int(self.tierrax),int(self.tierray)), 3, 1)        
        pygame.draw.circle(screen, (240,240,140),   (int(self.venusx)   ,int(self.venusy)), 6, 1)     
        pygame.draw.circle(screen, (240,240,140),    (int(self.mercuriox),int(self.mercurioy)), 2, 1)

        if self.showinfo==False:
            screen.blit(cross,     (0,0),(0,0,1224,700))   
        else:
            screen.blit(crossback, (0,0),(0,0,1224,700))
        if self.showinfo:
            self.letrasplanetas(screen)
        if self.relojact:
            screen.blit(relojactivo, (0,0),(0,0,1224,700))
            pygame.draw.rect(screen , (80,130,205), (522, 633, self.tiempo2,50), 0)
            level = self.font2.render( str(self.escala) + "Días" , True, (204,223,255))
            screen.blit(level, [733, 646])
        self.keplerbox=pygame.Rect(self.neptunox-5,self.neptunoy-5,10,10)
        self.copernicobox=pygame.Rect(self.jupiterx-10,self.jupitery-10,20,20)
        if self.clickbox.colliderect(self.solbox) and self.director.click:
            scene=solfun(self.director)
            self.director.change_scene(scene)            
        elif self.clickbox.colliderect(self.keplerbox) and self.director.click:
            scene=keplerfun(self.director)
            self.director.change_scene(scene)            
        elif self.clickbox.colliderect(self.copernicobox) and self.director.click:
            scene=copernico(self.director)
            self.director.change_scene(scene)            
#==============================================================================
#________FUNCIONES_UTILIZADAS__________________________________________________
#==============================================================================
    def evolucionfunc(self,screen):
        if self.evolucion:
            screen.blit(evolucionon, (0,0),(0,0,1000,700))
            if self.one:
                pygame.draw.rect(screen , (150,150,150), (self.aristotelesrect), 2)   
            elif self.two:
                pygame.draw.rect(screen , (150,150,150), (self.aristarcorect), 2) 
            elif self.three:
                pygame.draw.rect(screen , (150,150,150), (self.ptolomeorect), 2)
            elif self.four:
                pygame.draw.rect(screen , (150,150,150), (self.keplerrect), 2)
            if self.clickbox.colliderect(self.aristoteles):
                pygame.draw.rect(screen , (150,150,0), (self.aristotelesrect), 1) 
                if self.director.click:
                    self.allfalse()
                    self.one=True
            elif self.clickbox.colliderect(self.aristarco):
                pygame.draw.rect(screen , (150,150,0), (self.aristarcorect), 1)
                if self.director.click:
                    self.allfalse()
                    self.two=True
            elif self.clickbox.colliderect(self.ptolomeo):
                pygame.draw.rect(screen , (150,150,0), (self.ptolomeorect), 1)
                if self.director.click: 
                    self.allfalse()
                    self.three=True
            elif self.clickbox.colliderect(self.kepler):
                if self.director.click:
                    self.allfalse()
                    self.four=True
                pygame.draw.rect(screen , (150,150,0), (self.keplerrect), 1)
        else:
            screen.blit(evo, (0,0),(0,0,1000,700)) 
    def trayectoriaselipticas(self):
        mercuriodx=70+self.d
        mercuriody=68+self.d
        self.mercuriox, self.mercurioy= trayectorias(670,375,mercuriodx,mercuriody,self.mercuriotetha)
        self.mercord=(670-mercuriodx, 375-mercuriody, 2*mercuriodx,2*mercuriody )

        venusdx=70+self.d*2
        venusdy=68+int(self.d*1.7)
        self.venusx, self.venusy= trayectorias(665,375,venusdx,venusdy,self.venustetha)
        self.vencord=(665-venusdx, 375-venusdy, 2*venusdx,2*venusdy )

        tierradx=70+self.d*3
        tierrady=68+int(self.d*2.5)
        self.tierrax, self.tierray= trayectorias(668,375,tierradx,tierrady,self.tierratetha)
        self.tiecord=(668-tierradx, 375-tierrady, 2*tierradx,2*tierrady )

        martedx=70+self.d*6
        martedy=68+self.d*5
        self.martex, self.martey= trayectorias(660,375,martedx,martedy,self.martetetha)
        self.marcord=(660-martedx, 375-martedy, 2*martedx,2*martedy )

        jupiterdx=70+self.d*11
        jupiterdy=68+self.d*8
        self.jupiterx, self.jupitery= trayectorias(650,375,jupiterdx,jupiterdy,self.jupitertetha)
        self.jupcord=(650-jupiterdx, 375-jupiterdy, 2*jupiterdx,2*jupiterdy )

        saturnodx=70+self.d*20
        saturnody=68+self.d*16
        self.saturnox, self.saturnoy= trayectorias(620,375,saturnodx,saturnody,self.saturnotetha)
        self.satcord=(620-saturnodx, 375-saturnody, 2*saturnodx,2*saturnody )

        uranodx=70+self.d*40
        uranody=68+self.d*33
        self.uranox, self.uranoy= trayectorias(600,375,uranodx,uranody,self.uranotetha)
        self.uracord=(600-uranodx, 375-uranody, 2*uranodx,2*uranody )

        neptunodx=70+self.d*57
        neptunody=68+self.d*47
        self.neptunox, self.neptunoy= trayectorias(550,385,neptunodx,neptunody,self.neptunotetha)
        self.nepcord=(550-neptunodx, 385-neptunody, 2*neptunodx,2*neptunody )


    def letrasplanetas(self,screen):

        neptunotx=pygame.Rect(1020,500+35,190,50)
        uranotx=pygame.Rect(1020,450+30,190,50)
        saturnotx=pygame.Rect(1020,400+25,190,50)
        jupitertx=pygame.Rect(1020,350+20,190,50)
        martetx=pygame.Rect(1020,300+15,190,50)
        tierratx=pygame.Rect(1020,250+10,190,50)
        venustx=pygame.Rect(1020,200+5,190,50)
        mercuriotx=pygame.Rect(1020,150,190,50)
        if self.clickbox.colliderect(mercuriotx):
            pygame.draw.ellipse(screen, (120,120,120), (self.mercord), 1)

            pygame.draw.rect(screen , (130,130,0), (1020,150,190,50), 1)
            pygame.draw.circle(screen, (255,255,0),    (int(self.mercuriox),int(self.mercurioy)), 2+1, 1)

            level = self.font2.render( "Mercurio" , True, (204,223,255))
            screen.blit(level, [self.mercuriox, self.mercurioy -20])
            if self.director.click==True:
                self.director.change_scene(planetasf(self.director,pmercurio))
        elif self.clickbox.colliderect(venustx):
            pygame.draw.ellipse(screen, (120,120,120), (self.vencord), 1)   

            pygame.draw.rect(screen , (130,130,0), (1020,200+5,190,50), 1)
            pygame.draw.circle(screen, (255,255,0),   (int(self.venusx)   ,int(self.venusy)), 6+1, 1)     

            level = self.font2.render( "Venus" , True, (204,223,255))
            screen.blit(level, [self.venusx, self.venusy -20])
            if self.director.click==True:
                self.director.change_scene(planetasf(self.director,pvenus))
        elif self.clickbox.colliderect(tierratx):
            pygame.draw.ellipse(screen, (120,120,120), (self.tiecord), 1)       

            pygame.draw.rect(screen , (130,130,0), (1020,250+10,190,50), 1)
            pygame.draw.circle(screen, (255,255,0),    (int(self.tierrax),int(self.tierray)), 3+1, 1)        
            level = self.font2.render( "Tierra" , True, (204,223,255))
            screen.blit(level, [self.tierrax, self.tierray -20])
            if self.director.click==True:
                scene=planetasf(self.director,ptierra)
                self.director.change_scene(scene)
        elif self.clickbox.colliderect(martetx):
            pygame.draw.ellipse(screen, (120,120,120), (self.marcord), 1)

            pygame.draw.rect(screen , (130,130,0), (1020,300+15,190,50), 1)
            pygame.draw.circle(screen, (255,255,0),    (int(self.martex),int(self.martey)), 3+1, 2) 
            level = self.font2.render( "Marte" , True, (204,223,255))
            screen.blit(level, [self.martex, self.martey -22])
            if self.director.click==True:
                self.director.change_scene(planetasf(self.director,pmarte))
        elif self.clickbox.colliderect(jupitertx):
            pygame.draw.ellipse(screen, (120,120,120), (self.jupcord), 1)

            pygame.draw.rect(screen , (130,130,0), (1020,350+20,190,50), 1)
            pygame.draw.circle(screen, (255,255,0),    (int(self.jupiterx),int(self.jupitery)), 30+1, 2)  
            level = self.font2.render( "Jupiter" , True, (204,223,255))
            screen.blit(level, [self.jupiterx -30 , self.jupitery -50]) 
            if self.director.click==True: 
                self.director.change_scene(planetasf(self.director,pjupiter))
        elif self.clickbox.colliderect(saturnotx):
            pygame.draw.ellipse(screen, (120,120,120), (self.satcord), 1)       

            pygame.draw.rect(screen , (130,130,0), (1020,400+25,190,50), 1)
            pygame.draw.circle(screen, (255,255,0),    (int(self.saturnox),int(self.saturnoy)), 22+1, 2)
            level = self.font2.render( "Saturno" , True, (204,223,255))
            screen.blit(level, [self.saturnox -10, self.saturnoy -40])
            if self.director.click==True:
                self.director.change_scene(planetasf(self.director,psaturno))
        elif self.clickbox.colliderect(uranotx):
            pygame.draw.ellipse(screen, (120,120,120), (self.uracord), 1)       
            
            pygame.draw.rect(screen , (130,130,0), (1020,450+30,190,50), 1)
            pygame.draw.circle(screen, (255,255,0),    (int(self.uranox),int(self.uranoy)), 12+1, 2)
            level = self.font2.render( "Urano" , True, (204,223,255))
            screen.blit(level, [self.uranox, self.uranoy -30])
            if self.director.click==True:
                self.director.change_scene(planetasf(self.director, purano))
        elif self.clickbox.colliderect(neptunotx):
            pygame.draw.ellipse(screen, (120,120,120), (self.nepcord), 1)       

            pygame.draw.rect(screen , (130,130,0), (1020,500+35,190,50), 1)
            pygame.draw.circle(screen, (255,255,0),    (int(self.neptunox),int(self.neptunoy)), 10+1, 2)
            level = self.font2.render( "Neptuno" , True, (204,223,255))
            screen.blit(level, [self.neptunox, self.neptunoy -30])
            if self.director.click==True:
                self.director.change_scene(planetasf(self.director, pneptuno))
    
    def aumentos(self):
        self.mercuriotetha+=self.escala*6.2832/(88*30)
        self.venustetha+=self.escala*6.2832/(224*30)
        self.tierratetha+=self.escala*6.2832/(365*30)
        self.martetetha+= self.escala*6.2832/(687*30)       
        self.jupitertetha+=self.escala*6.2832/(4380*30)
        self.saturnotetha+=self.escala*6.2832/(108405*30)
        self.uranotetha+=self.escala*6.2832/(30769.5*30)
        self.neptunotetha+=self.escala*6.2832/(60152*30)



#==============================================================================
#Cambios_de_pantalla_Planetas__________________________________________________
#==============================================================================

class planetasf(scene.Scene):
    def __init__(self, director,imagen):
        scene.Scene.__init__(self, director)
        self.data=False        
        self.infobox = pygame.Rect(3, 623, 70, 70)
        self.angulo=0
        self.imagen= imagen
    def on_event(self):
        keys=pygame.key.get_pressed()
        if self.director.clickbox.colliderect(self.infobox):
            if self.director.click:
                if self.data==False:
                    self.data=True
                else:
                    self.data=False

        elif keys[pygame.K_a] or self.director.click==True:
            scene=sistemasolar(self.director)
            self.director.change_scene(scene)
    def on_update(self):
        if self.director.giro:
            if self.angulo <360:
                self.angulo+=1
            else:
                self.angulo=0
        else:
            self.angulo=0
    def on_draw(self, screen):
        screen.fill((0,0,0))
        imagen = pygame.transform.rotate(self.imagen, self.angulo)
        a,b,x,y = imagen.get_rect()
        screen.blit(imagen, (50-(x-600)//2,50-(y-600)//2))
#        pygame.draw.circle(screen, (250,250,250), (350, 350), 250, 0)
        pygame.draw.circle(screen, (0,0,0), (350, 350), 330, 80)


class solfun(scene.Scene):
    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.data=False        

    def on_event(self):
        if self.director.click==True:
            scene=sistemasolar(self.director)
            self.director.change_scene(scene)
    def on_update(self):
        pass
    def on_draw(self, screen):
        screen.blit(datasol, (0,0),(0,0,1224,700))            
        
class copernico(scene.Scene):
    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.data=False        

    def on_event(self):
        if self.director.click==True:
            scene=sistemasolar(self.director)
            self.director.change_scene(scene)
    def on_update(self):
        pass
    def on_draw(self, screen):
        screen.blit(copernicoimg, (0,0),(0,0,1224,700))            

class keplerfun(scene.Scene):
    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.data=False        

    def on_event(self):
        if self.director.click==True:
            scene=sistemasolar(self.director)
            self.director.change_scene(scene)
    def on_update(self):
        pass
    def on_draw(self, screen):
        screen.blit(kepler1, (0,0),(0,0,1224,700))            


# Funciones
# ---------------------------------------------------------------------
def trayectorias(h,k,dx,dy,ang):
    x= h + math.cos(ang)/(math.cos(ang)**2/(dx)**2 +math.sin(ang)**2/(dy)**2)**(1/2)
    y= k + math.sin(ang)/(math.cos(ang)**2/(dx)**2 +math.sin(ang)**2/(dy)**2)**(1/2)
    return x,y
# ---------------------------------------------------------------------

def main():
	print("Main")

if __name__ == '__main__':
	main()