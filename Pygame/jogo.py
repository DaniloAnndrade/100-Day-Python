import pygame

#cores
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)


#inicio
pygame.init()

#janela
fonte = pygame.font.Font(None,48)
janela = pygame.display.set_mode((640,480))
pygame.display.set_caption("I don't need help!!")

# cor da tela
janela.fill(branco)


# Objeto 
pygame.draw.line(janela,preto,(20,410),(420,410),48)
pygame.draw.polygon(janela,preto,((191,206),(236,277),(156,277)),0)
pygame.draw.circle(janela,azul,(100,50),20,0)

# Texto
fonte = pygame.font.Font(None,40)
texto = fonte.render("Oi Meu nome e pregui",True, branco)
janela.blit(texto,[30,400])




pygame.display.update()
cont = True


while cont:
    for evento in pygame.event.get():
        # se aperta no X a tela fecha
        if evento.type==pygame.QUIT:
            cont = False


pygame.quit()