import pygame
#import Main.rsrc.py
import sys
from PythonCard import model
from PythonCard.components import statictext, button, spinner, staticline

# Cuadritos de amonestaciones
def cuadros():
    colorMargen = [0, 0, 0]
    yCuadros = 4 * (alto // 5)
    alturaCuadros = alto - (alto * 0.85)
    amarillo = [255, 255, 0]
    rojo = [220, 0, 0]
    pygame.draw.rect(screen, rojo, (10, yCuadros, ancho // 12, alturaCuadros), 0)
    pygame.draw.rect(screen, amarillo, (ancho // 12 + 20, yCuadros, ancho // 12, alturaCuadros), 0)
    pygame.draw.rect(screen, colorMargen, (10, yCuadros, ancho // 12, alturaCuadros), 5)
    pygame.draw.rect(screen, colorMargen, (ancho // 12 + 20, yCuadros, ancho // 12, alturaCuadros), 5)

    pygame.draw.rect(screen, rojo, (ancho - 10 - ancho // 12, yCuadros, ancho // 12, alturaCuadros), 0)
    pygame.draw.rect(screen, amarillo, (ancho - (ancho // 12 + 20 + ancho // 12), yCuadros, ancho // 12, alturaCuadros), 0)
    pygame.draw.rect(screen, colorMargen, (ancho - 10 - ancho // 12, yCuadros, ancho // 12, alturaCuadros), 5)
    pygame.draw.rect(screen, colorMargen, (ancho - (ancho // 12 + 20 + ancho // 12), yCuadros, ancho // 12, alturaCuadros),
                     5)

    pygame.draw.rect(screen, [230, 230, 230], (ancho // 2 - ancho // 24, alto // 2 - alturaCuadros // 2, ancho // 12, alturaCuadros), 0)
    pygame.draw.rect(screen, colorMargen, (ancho // 2 - ancho // 24, alto // 2 - alturaCuadros // 2, ancho // 12, alturaCuadros), 5)

    pygame.draw.rect(screen, [225, 225, 225], (ancho // 2 - ancho // 24, alto // 2 + alturaCuadros // 2 - alto * 0.02, ancho // 12, alto * 0.03), 0)
    pygame.draw.rect(screen, [15, 15, 15], (ancho // 2 - ancho // 24, alto // 2 + alturaCuadros // 2 - alto * 0.02, ancho // 12, alto * 0.03), 5)

# Copia al lienzo las amonestaciones y el numero de round
def amonestaciones():
    global kAzul
    global kRojo
    global gAzul
    global gRojo
    global numeroRound

    cuadros()

    textoRound = pygame.font.Font.render(TextoGamjeom, str(numeroRound), 1, (10, 10, 10))
    anchoMarcador = textoRound.get_width()
    screen.blit(textoRound, (ancho // 2 - anchoMarcador // 2, alto // 2 - textoRound.get_height() // 2))

    textoKAzul = pygame.font.Font.render(TextoGamjeom, str(kAzul), 1, (10, 10, 10))
    anchoMarcador = textoKAzul.get_width()
    screen.blit(textoKAzul, (ancho - (20 + 3 * ancho // 24 + anchoMarcador//2), 95 * alto // 120))

    textoKRojo = pygame.font.Font.render(TextoGamjeom, str(kRojo), 1, (10, 10, 10))
    anchoMarcador = textoKRojo.get_width()
    screen.blit(textoKRojo, (20 + 3 * ancho // 24 - anchoMarcador//2, 95 * alto // 120))

    textoGAzul = pygame.font.Font.render(TextoGamjeom, str(gAzul), 1, (10, 10, 10))
    anchoMarcador = textoGAzul.get_width()
    screen.blit(textoGAzul, (ancho - ( 10 + ancho // 24 + anchoMarcador // 2 ), 95 * alto // 120))

    textoGRojo = pygame.font.Font.render(TextoGamjeom, str(gRojo), 1, (10, 10, 10))
    anchoMarcador = textoGRojo.get_width()
    screen.blit(textoGRojo, (10 + ancho // 24 - anchoMarcador // 2, 95 * alto // 120))

    textoBotonSigRound = pygame.font.Font.render(TextoLetrero, "Sig. Round", 1, (15, 15, 15))
    anchoMarcador = textoBotonSigRound.get_width()
    screen.blit(textoBotonSigRound, (ancho // 2 - anchoMarcador // 2, alto // 2 + (alto - (alto * 0.85)) // 2 - alto * 0.02 + 3))

# Aumenta puntos al marcador rojo
def puntoRojo(punto):
    global puntajeRojo, alto, ancho, TextoGrande
    textoRojo = pygame.font.Font.render(TextoGrande, str(puntajeRojo), 1, (10, 10, 10))
    anchoMarcador = textoRojo.get_width()
    altoMarcador = textoRojo.get_height()
    pygame.draw.rect(screen, (255, 0, 0), ([ancho // 3 - 2 * anchoMarcador // 3, alto // 7], (anchoMarcador, altoMarcador)))
    puntajeRojo += punto
    textoRojo = pygame.font.Font.render(TextoGrande, str(puntajeRojo), 1, (10, 10, 10))
    anchoMarcador = textoRojo.get_width()
    screen.blit(textoRojo, [ancho // 3 - 2 * anchoMarcador // 3, alto // 7])

# Aumenta puntos al marcador rojo
def puntoAzul(punto):
    global puntajeAzul, alto, ancho, TextoGrande
    textoAzul = pygame.font.Font.render(TextoGrande, str(puntajeAzul), 1, (10, 10, 10))
    anchoMarcador = textoAzul.get_width()
    altoMarcador = textoAzul.get_height()
    pygame.draw.rect(screen, (0, 0, 255), ([2 * ancho // 3 - anchoMarcador // 3, alto // 7], (anchoMarcador, altoMarcador)))
    puntajeAzul += punto
    textoAzul = pygame.font.Font.render(TextoGrande, str(puntajeAzul), 1, (10, 10, 10))
    anchoMarcador = textoAzul.get_width()
    screen.blit(textoAzul, (2 * ancho // 3 - anchoMarcador // 3, alto // 7))

# Verifica cuantos botones de rojo han sido presionados
def presionadosRojo():
    global play
    cuenta = 0

    if JR1_1[1]:
        if pygame.time.get_ticks() - JR1_1[0] <= 2000:
            cuenta += 1
        else:
            JR1_1[1] = False
            pygame.draw.rect(screen, (255, 0, 0), ((1 * ancho // 12, 2 * alto // 12), tamanoDeControles))
    if JR1_2[1]:
        if pygame.time.get_ticks() - JR1_2[0] <= 2000:
            cuenta += 1
        else:
            JR1_2[1] = False
            pygame.draw.rect(screen, (255, 0, 0), ((2 * ancho // 12, 2 * alto // 12), tamanoDeControles))
    if JR1_3[1]:
        if pygame.time.get_ticks() - JR1_3[0] <= 2000:
            cuenta += 1
        else:
            JR1_3[1] = False
            pygame.draw.rect(screen, (255, 0, 0), ((3 * ancho // 12, 2 * alto // 12), tamanoDeControles))
    if JR1_4[1]:
        if pygame.time.get_ticks() - JR1_4[0] <= 2000:
            cuenta += 1
        else:
            JR1_4[1] = False
            pygame.draw.rect(screen, (255, 0, 0), ((4 * ancho // 12, 2 * alto // 12), tamanoDeControles))

    if cuenta > numeroControles:
        if play:
            puntoRojo(1)
        JR1_1[1] = False
        JR1_2[1] = False
        JR1_3[1] = False
        JR1_4[1] = False
        pygame.draw.rect(screen, (255, 0, 0), ((1 * ancho // 12, 2 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (255, 0, 0), ((2 * ancho // 12, 2 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (255, 0, 0), ((3 * ancho // 12, 2 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (255, 0, 0), ((4 * ancho // 12, 2 * alto // 12), tamanoDeControles))

# Verifica cuantos botones de rojo han sido presionados
def presionadosRojo3():
    global play
    cuenta = 0

    if JR3_1[1]:
        if pygame.time.get_ticks() - JR3_1[0] <= 2000:
            cuenta += 1
        else:
            JR3_1[1] = False
            pygame.draw.rect(screen, (255, 0, 0), ((1 * ancho // 12, 1 * alto // 12), tamanoDeControles))
    if JR3_2[1]:
        if pygame.time.get_ticks() - JR3_2[0] <= 2000:
            cuenta += 1
        else:
            JR3_2[1] = False
            pygame.draw.rect(screen, (255, 0, 0), ((2 * ancho // 12, 1 * alto // 12), tamanoDeControles))
    if JR3_3[1]:
        if pygame.time.get_ticks() - JR3_3[0] <= 2000:
            cuenta += 1
        else:
            JR3_3[1] = False
            pygame.draw.rect(screen, (255, 0, 0), ((3 * ancho // 12, 1 * alto // 12), tamanoDeControles))
    if JR3_4[1]:
        if pygame.time.get_ticks() - JR3_4[0] <= 2000:
            cuenta += 1
        else:
            JR3_4[1] = False
            pygame.draw.rect(screen, (255, 0, 0), ((4 * ancho // 12, 1 * alto // 12), tamanoDeControles))

    if cuenta > numeroControles:
        if play:
            puntoRojo(3)
        JR3_1[1] = False
        JR3_2[1] = False
        JR3_3[1] = False
        JR3_4[1] = False
        pygame.draw.rect(screen, (255, 0, 0), ((1 * ancho // 12, 1 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (255, 0, 0), ((2 * ancho // 12, 1 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (255, 0, 0), ((3 * ancho // 12, 1 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (255, 0, 0), ((4 * ancho // 12, 1 * alto // 12), tamanoDeControles))

# Verifica cuantos botones de Azul han sido presionados
def presionadosAzul():
    global play
    cuenta = 0

    if JA1_1[1]:
        if pygame.time.get_ticks() - JA1_1[0] <= 2000:
            cuenta += 1
        else:
            JA1_1[1] = False
            pygame.draw.rect(screen, (0, 0, 255), ((ancho - 4 * ancho // 12, 2 * alto // 12), tamanoDeControles))
    if JA1_2[1]:
        if pygame.time.get_ticks() - JA1_2[0] <= 2000:
            cuenta += 1
        else:
            JA1_2[1] = False
            pygame.draw.rect(screen, (0, 0, 255), ((ancho - 3 * ancho // 12, 2 * alto // 12), tamanoDeControles))
    if JA1_3[1]:
        if pygame.time.get_ticks() - JA1_3[0] <= 2000:
            cuenta += 1
        else:
            JA1_3[1] = False
            pygame.draw.rect(screen, (0, 0, 255), ((ancho - 2 * ancho // 12, 2 * alto // 12), tamanoDeControles))
    if JA1_4[1]:
        if pygame.time.get_ticks() - JA1_4[0] <= 2000:
            cuenta += 1
        else:
            JA1_4[1] = False
            pygame.draw.rect(screen, (0, 0, 255), ((ancho - 1 * ancho // 12, 2 * alto // 12), tamanoDeControles))

    if cuenta > numeroControles:
        if play:
            puntoAzul(1)
        JA1_1[1] = False
        JA1_2[1] = False
        JA1_3[1] = False
        JA1_4[1] = False
        pygame.draw.rect(screen, (0, 0, 255), ((ancho - 1 * ancho // 12, 2 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (0, 0, 255), ((ancho - 2 * ancho // 12, 2 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (0, 0, 255), ((ancho - 3 * ancho // 12, 2 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (0, 0, 255), ((ancho - 4 * ancho // 12, 2 * alto // 12), tamanoDeControles))

# Verifica cuantos botones de Azul han sido presionados
def presionadosAzul3():
    global play
    cuenta = 0

    if JA3_1[1]:
        if pygame.time.get_ticks() - JA3_1[0] <= 2000:
            cuenta += 1
        else:
            JA3_1[1] = False
            pygame.draw.rect(screen, (0, 0, 255), ((ancho - 4 * ancho // 12, 1 * alto // 12), tamanoDeControles))
    if JA3_2[1]:
        if pygame.time.get_ticks() - JA3_2[0] <= 2000:
            cuenta += 1
        else:
            JA3_2[1] = False
            pygame.draw.rect(screen, (0, 0, 255), ((ancho - 3 * ancho // 12, 1 * alto // 12), tamanoDeControles))
    if JA3_3[1]:
        if pygame.time.get_ticks() - JA3_3[0] <= 2000:
            cuenta += 1
        else:
            JA3_3[1] = False
            pygame.draw.rect(screen, (0, 0, 255), ((ancho - 2 * ancho // 12, 1 * alto // 12), tamanoDeControles))
    if JA3_4[1]:
        if pygame.time.get_ticks() - JA3_4[0] <= 2000:
            cuenta += 1
        else:
            JA3_4[1] = False
            pygame.draw.rect(screen, (0, 0, 255), ((ancho - 1 * ancho // 12, 1 * alto // 12), tamanoDeControles))

    if cuenta > numeroControles:
        if play:
            puntoAzul(3)
        JA3_1[1] = False
        JA3_2[1] = False
        JA3_3[1] = False
        JA3_4[1] = False
        pygame.draw.rect(screen, (0, 0, 255), ((ancho - 1 * ancho // 12, 1 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (0, 0, 255), ((ancho - 2 * ancho // 12, 1 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (0, 0, 255), ((ancho - 3 * ancho // 12, 1 * alto // 12), tamanoDeControles))
        pygame.draw.rect(screen, (0, 0, 255), ((ancho - 4 * ancho // 12, 1 * alto // 12), tamanoDeControles))

def dibujarReloj():
    global TextoReloj
    global TextoBoton
    global play
    global pausaReloj
    global segundos
    global roundMin
    global roundSeg
    global numeroRound
    global descansoMin
    global descansoSeg
    global descanso
    if play:
        segundos = pygame.time.get_ticks() - pausaReloj
        if descanso == False:
            aux = int(roundMin * 60) + roundSeg
            aux2 = int(segundos // 1000)
            if aux2 >= aux:
                pausaReloj = pygame.time.get_ticks()
                if numeroRound < totaRound:
                    descanso = True
                else:
                    play = False
        else:
            aux = int(descansoMin * 60) + descansoSeg
            aux2 = int(segundos // 1000)
            textoDescanso = pygame.font.Font.render(TextoDescanso, "Descanso", 1, (210, 110, 0))
            screen.blit(textoDescanso, (ancho // 2 - textoDescanso.get_width() // 2, alto // 2))
            if aux2 >= aux:
                pausaReloj = pygame.time.get_ticks()
                # Estoy haciendo pruebas para iniciar el siguiente round
                # hasta que el juez lo indique
                descanso = False
                play = False
                print pausa
                # numeroRound = numeroRound + 1
                pygame.draw.rect(screen, [255, 0, 0], (0, 0, ancho // 2, alto - alto * 0.03))
                pygame.draw.rect(screen, [0, 0, 255], (ancho // 2, 0, ancho, alto - alto * 0.03))
                textoRojo = pygame.font.Font.render(TextoGrande, str(puntajeRojo), 1, (10, 10, 10))
                screen.blit(textoRojo, [ancho // 3 - 2 * textoRojo.get_width() // 3, alto // 7])
                textoAzul = pygame.font.Font.render(TextoGrande, str(puntajeAzul), 1, (10, 10, 10))
                screen.blit(textoAzul, (2 * ancho // 3 - textoAzul.get_width() // 3, alto // 7))
    elif pausa:
        segundosPausa = pygame.time.get_ticks() - segundos - pausaReloj
        segundosPausaPantalla = int(segundosPausa // 1000)
        segundosPausaUnidadPantalla = (segundosPausaPantalla % 60) % 10
        segundosPausaDecenaPantalla = (segundosPausaPantalla % 60) // 10
        minutosPausa = segundosPausaPantalla // 60
        stringPausa = str(minutosPausa) + ":" + str(segundosPausaDecenaPantalla) + str(segundosPausaUnidadPantalla)
        textoPausa = pygame.font.Font.render(TextoDescanso, stringPausa, 1, (210, 110, 0))
        pygame.draw.rect(screen, [255, 0, 0], (0, 0, ancho // 2, alto - alto * 0.03))
        pygame.draw.rect(screen, [0, 0, 255], (ancho // 2, 0, ancho, alto - alto * 0.03))
        textoRojo = pygame.font.Font.render(TextoGrande, str(puntajeRojo), 1, (10, 10, 10))
        screen.blit(textoRojo, [ancho // 3 - 2 * textoRojo.get_width() // 3, alto // 7])
        textoAzul = pygame.font.Font.render(TextoGrande, str(puntajeAzul), 1, (10, 10, 10))
        screen.blit(textoAzul, (2 * ancho // 3 - textoAzul.get_width() // 3, alto // 7))
        screen.blit(textoPausa, (ancho // 2 - textoPausa.get_width() // 2, alto // 2))

    pygame.draw.rect(screen, [100, 100, 100], ((ancho // 3, alto - 1.2 * (alto // 6)), (ancho // 3, alto // 7)))
    pygame.draw.rect(screen, [0, 0, 0], ((ancho // 3, alto - 1.2 * (alto // 6)), (ancho // 3, alto // 7)), 5)

    # Boton play//pausa
    pygame.draw.circle(screen, [50, 10, 10], (9 * ancho // 24, int((alto - 1.2 * (alto // 6)) + alto // 28)), alto // 36)
    pygame.draw.circle(screen, [150, 0, 0], (9 * ancho // 24, int((alto - 1.2 * (alto // 6)) + alto // 28)), alto // 36, alto // 200)
    if play:
        pygame.draw.rect(screen, [150, 0, 0], ([9 * ancho // 24 - alto // 72, int((alto - 1.2 * (alto // 6)) - alto // 72 + alto // 28)], (alto // 144, alto // 36)))
        pygame.draw.rect(screen, [150, 0, 0], ([9 * ancho // 24 + alto // 144, int((alto - 1.2 * (alto // 6)) - alto // 72 + alto // 28)], (alto // 144, alto // 36)))
    else:
        pygame.draw.polygon(screen, [150, 0, 0], [[9 * ancho // 24 - alto // 72, int((alto - 1.2 * (alto // 6)) + alto // 72 + alto // 28)], [9 * ancho // 24 - alto // 72, int((alto - 1.2 * (alto // 6)) - alto // 72 + alto // 28)], [9 * ancho // 24 + alto // 72, int((alto - 1.2 * (alto // 6) + alto // 28))]])


    # Boton stop
    pygame.draw.circle(screen, [50, 10, 11], (9 * ancho // 24, int((alto - 1.2 * (alto // 6)) - alto // 28 + alto // 7)), alto // 36)
    pygame.draw.circle(screen, [150, 0, 1], (9 * ancho // 24, int((alto - 1.2 * (alto // 6)) - alto // 28 + alto // 7)), alto // 36, alto // 200)
    pygame.draw.rect(screen, [150, 0, 1], ([9 * ancho // 24 - alto // 72, int((alto - 1.2 * (alto // 6)) - alto // 28 + alto // 7 - alto // 72)], (alto // 36, alto // 36)))

    if descanso:
        segundosPantalla = descansoMin * 60 + descansoSeg -int(segundos // 1000)
    else:
        segundosPantalla = roundMin * 60 + roundSeg - int(segundos // 1000)
    segundosUnidadPantalla = (segundosPantalla % 60) % 10
    segundosDecenaPantalla = (segundosPantalla % 60) // 10
    minutos = segundosPantalla // 60
    stringReloj = str(minutos) + ":" + str(segundosDecenaPantalla) + str(segundosUnidadPantalla)
    if descanso:
        textoReloj = pygame.font.Font.render(TextoReloj, stringReloj, 1, (10, 10, 250))
    else:
        textoReloj = pygame.font.Font.render(TextoReloj, stringReloj, 1, (10, 10, 10))

    screen.blit(textoReloj, (ancho // 2 - textoReloj.get_width() // 2, alto - alto // 5))

# Carga la pantalla al inicio
def pantalla():
    global TamanoGrande
    global TextoGrande
    global anchoMarcador
    global TamanoGajeom
    global TextoGamjeom
    global TextoControles
    global TamanoControles
    global tamanoDeControles
    global TamanoReloj
    global TextoReloj
    global TamanoBoton
    global TextoBoton
    global TamanoLetrero
    global TextoLetrero
    global TamanoDescanso
    global TextoDescanso
    global letraUniversal

    TamanoGrande = 0
    TextoGrande = pygame.font.SysFont(letraUniversal, TamanoGrande)
    TamanoGajeom = 0
    TextoGamjeom = pygame.font.SysFont(letraUniversal, TamanoGajeom)
    TamanoControles = 0
    TextoControles = pygame.font.SysFont(letraUniversal, TamanoControles)
    TamanoReloj = 0
    TextoReloj = pygame.font.SysFont(letraUniversal, TamanoReloj)
    TamanoBoton = 0
    TextoBoton = pygame.font.SysFont(letraUniversal, TamanoBoton)
    TamanoLetrero = 0
    TextoLetrero = pygame.font.SysFont(letraUniversal, TamanoLetrero)
    TamanoDescanso = 0
    TextoDescanso = pygame.font.SysFont(letraUniversal, TamanoDescanso)

    ancho = int(pygame.Surface.get_width(screen))
    alto = int(pygame.Surface.get_height(screen))
    # Fondo
    pygame.draw.rect(screen, [255, 0, 0], (0, 0, ancho // 2, alto))
    pygame.draw.rect(screen, [0, 0, 255], (ancho // 2, 0, ancho, alto))
    pygame.draw.rect(screen, [255, 255, 255], (0, alto - (alto * 0.03), ancho, alto * 0.03), 0)
    screen.blit(logo, [((ancho // 2) - 302 // 4), 10])

    # Kyong-go y Gam-jeom
    cuadros()

    # Alto de texto grande
    textoRojo = pygame.font.Font.render(TextoGrande, str(puntajeRojo), 1, (10, 10, 10))
    textPos = textoRojo.get_rect()
    altoMarcador = textPos.height

    while altoMarcador < 2 * alto // 3:
        TamanoGrande += 10
        TextoGrande = pygame.font.SysFont(letraUniversal, TamanoGrande)
        textoRojo = pygame.font.Font.render(TextoGrande, str(0), 1, (10, 10, 10))
        altoMarcador = textoRojo.get_height()

    textoRojo = pygame.font.Font.render(TextoGrande, str(puntajeRojo), 1, (10, 10, 10))
    textoAzul = pygame.font.Font.render(TextoGrande, str(puntajeAzul), 1, (10, 10, 10))
    screen.blit(textoAzul, (2 * ancho // 3 - textoAzul.get_width() // 3, alto // 7))
    screen.blit(textoRojo, (ancho // 3 - 2 * textoRojo.get_width() // 3, alto // 7))

    #Alto de amonestaciones
    textoKRojo = pygame.font.Font.render(TextoGamjeom, str(kRojo), 1, (10, 10, 10))
    textPos = textoKRojo.get_rect()
    anchoMarcador = textPos.width

    while anchoMarcador * 2 < ancho // 13:
        TamanoGajeom += 10
        TextoGamjeom = pygame.font.SysFont(letraUniversal, TamanoGajeom)
        textoKRojo = pygame.font.Font.render(TextoGamjeom, str(kRojo), 1, (10, 10, 10))
        textPos = textoKRojo.get_rect()
        anchoMarcador = textPos.width

    amonestaciones()

    # Alto de controles
    textoControl = pygame.font.Font.render(TextoControles, str(1), 1, (10, 10, 10))
    textPos = textoControl.get_rect()
    altoMarcador = textPos.height

    while altoMarcador < alto // 20:
        TamanoControles += 10
        TextoControles = pygame.font.SysFont(letraUniversal, TamanoControles)
        textoControl = pygame.font.Font.render(TextoControles, str(1), 1, (10, 10, 10))
        textPos = textoControl.get_rect()
        altoMarcador = textPos.height
        anchoMarcador = textPos.width

    tamanoDeControles = (anchoMarcador, altoMarcador)

    # Reloj de rounds
    textoReloj = pygame.font.Font.render(TextoReloj, "5:59", 1, (10, 10, 10))
    textPos = textoReloj.get_rect()
    altoMarcador = textPos.height

    while altoMarcador < alto // 7:
        TamanoReloj += 10
        TextoReloj = pygame.font.SysFont(letraUniversal, TamanoReloj)
        textoReloj = pygame.font.Font.render(TextoReloj, "5:59", 1, (10, 10, 10))
        textPos = textoReloj.get_rect()
        altoMarcador = textPos.height
        anchoMarcador = textPos.width

    dibujarReloj()

    # Alto letrero al fondo de la pantalla
    textoLetrero = pygame.font.Font.render(TextoLetrero, "Ganjeom: +A  -Z     Kyongo: +S  -X                Puntaje Rojo: +D  -C", 1, (10, 10, 10))
    anchoMarcador = textoLetrero.get_width()
    altoMarcador = textoLetrero.get_height()

    while anchoMarcador < ancho / 3 and altoMarcador < alto * 0.02:
        TamanoLetrero += 1
        TextoLetrero = pygame.font.SysFont(letraUniversal, TamanoLetrero)
        textoLetrero = pygame.font.Font.render(TextoLetrero, "Ganjeom: +A  -Z     Kyongo: +S  -X                Puntaje Rojo: +D  -C", 1, (10, 10, 10))
        anchoMarcador = textoLetrero.get_width()
        altoMarcador = textoLetrero.get_height()


    textoLetrero = pygame.font.Font.render(TextoLetrero, "Ganjeom: +A  -Z     Kyongo: +S  -X                Puntaje Rojo: +D  -C", 1, (10, 10, 10))
    screen.blit(textoLetrero, (ancho * 0.01, alto - alto * 0.03))
    textoLetrero = pygame.font.Font.render(TextoLetrero, "Puntaje Azul: +H  -B                Kyongo: +J  -N     Ganjeom: +K  -M", 1, (10, 10, 10))
    screen.blit(textoLetrero, (ancho - textoLetrero.get_width() - ancho * 0.01, alto - alto * 0.03))
    textoLetrero = pygame.font.Font.render(TextoLetrero, "Play / Pausa: Espacio    Stop: V    Sig.Round: F", 1, (10, 10, 10))
    screen.blit(textoLetrero, (ancho / 2 - textoLetrero.get_width() / 2 - ancho * 0.01, alto - alto * 0.03))

    # Aqui esta el codigo del letrero de configurar
    # Aun no funciona porque da error con SIGABRT

    # textoLetrero = pygame.font.Font.render(TextoLetrero, "Configurar", 1, (249, 180, 61))
    # pygame.draw.rect(screen, [231, 231, 231],(ancho // 2 - textoLetrero.get_width() // 2 - 5, alto - alto * 0.03, textoLetrero.get_width() + 10, alto * 0.03))
    # pygame.draw.rect(screen, [0, 0, 0],(ancho // 2 - textoLetrero.get_width() // 2 - 5, alto - alto * 0.03, textoLetrero.get_width() +  10, alto * 0.03), 2)
    # screen.blit(textoLetrero, (ancho // 2 - textoLetrero.get_width() // 2, alto - alto * 0.03))

    # Ancho Descanso
    textoDescanso = pygame.font.Font.render(TextoDescanso, "Descanso", 1, (210, 110, 0))
    textPos = textoDescanso.get_rect()
    anchoMarcador = textPos.width

    while anchoMarcador < 2 * ancho // 3:
        TamanoDescanso += 10
        TextoDescanso = pygame.font.SysFont(letraUniversal, TamanoDescanso)
        textoDescanso = pygame.font.Font.render(TextoDescanso, "Descanso", 1, (210, 110, 0))
        anchoMarcador = textoDescanso.get_width()

def ventana():
    class MainWindow(model.Background):
        def on_initialize(self, event):
            self.components.Rounds.value = int(totaRound)
            self.components.DescansoSegundos.value = int(descansoSeg)
            self.components.DescansoMinutos.value = int(descansoMin)
            self.components.CombateMinutos.value = int(roundMin)
            self.components.CombateSegundos.value = int(roundSeg)
            self.components.Controles.value = 2

        def on_btnOK_mouseClick(self, event):
            global totaRound
            global descansoMin
            global descansoSeg
            global roundMin
            global roundSeg
            global numeroControles
            # print self.components.Rounds.value
            totaRound = self.components.Rounds.value
            descansoSeg = self.components.DescansoSegundos.value
            descansoMin = self.components.DescansoMinutos.value
            roundMin = self.components.CombateMinutos.value
            roundSeg = self.components.CombateSegundos.value
            numeroControles = self.components.Controles.value
            if (numeroControles == 2):
                numeroControles = 1
            else:
                numeroControles = 2
            self.close()

    app = model.Application(MainWindow)
#    app = model.Application(MainWindow, None, "Main.rsrc.py data")
    app.MainLoop()
rsrc = "Main.rsrc.py data"
# Variables de los marcadores
puntajeAzul = 0
puntajeRojo = 0
kRojo = 0
kAzul = 0
gRojo = 0
gAzul = 0
numeroRound = 0
totaRound = 3
numeroControles = 2

# Variable para el contador de tiempo
play = False
descanso = False
pausa = False
pausaReloj = 0
segundos = 0
roundMin = 1
roundSeg = 30
descansoMin = 0
descansoSeg = 30

# Reloj para contar los segundos entre cada punto marcado por cada juez
# Usare pygame.time.get_ticks() como reloj

#  Variables de cada boton usado por cada juez

# Juez Rojo 1 Punto
JR1_1 = [0, False]
JR1_2 = [0, False]
JR1_3 = [0, False]
JR1_4 = [0, False]

# Juez Rojo 3 Puntos
JR3_1 = [0, False]
JR3_2 = [0, False]
JR3_3 = [0, False]
JR3_4 = [0, False]

# Juez Azul 1 Punto
JA1_1 = [0, False]
JA1_2 = [0, False]
JA1_3 = [0, False]
JA1_4 = [0, False]

# Juez Azul 3 Puntos
JA3_1 = [0, False]
JA3_2 = [0, False]
JA3_3 = [0, False]
JA3_4 = [0, False]

ventana()

pygame.init()
ancho = int(pygame.display.list_modes()[0][0])
alto = int(pygame.display.list_modes()[0][1])
screen = pygame.display.set_mode((ancho,alto), pygame.FULLSCREEN)
#pygame.display.toggle_fullscreen()

logo = pygame.image.load("Imagenes/Logo2.png")
logo = pygame.transform.scale(logo, (int(ancho / 9.04), int(alto / 4.65)))

# Tamano de las letras
letraUniversal = pygame.font.get_default_font()
TamanoGrande = 0
TextoGrande = pygame.font.SysFont(letraUniversal, TamanoGrande)
TamanoGajeom = 0
TextoGamjeom = pygame.font.SysFont(letraUniversal, TamanoGajeom)
TamanoControles = 0
TextoControles = pygame.font.SysFont(letraUniversal, TamanoControles)
TamanoReloj = 0
TextoReloj = pygame.font.SysFont(letraUniversal, TamanoReloj)
TamanoBoton = 0
TextoBoton = pygame.font.SysFont(letraUniversal, TamanoBoton)
TamanoLetrero = 0
TextoLetrero = pygame.font.SysFont(letraUniversal, TamanoLetrero)
TamanoDescanso = 0
TextoDescanso = pygame.font.SysFont(letraUniversal, TamanoDescanso)

pantalla()

# Controla la velocidad (FPS) del sistema
reloj = pygame.time.Clock()


while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # print JR1_1[0], JR1_1[1]
            # print JR1_2[0], JR1_2[1]
            # print JR1_3[0], JR1_3[1]
            # print JR1_4[0], JR1_4[1]
            # print reloj.get_fps()
            sys.exit()
        if (play and not (descanso)):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                JR1_1 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(1), 1, (10, 10, 10)), (1 * ancho // 12, 2 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                JR1_2 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(2), 1, (10, 10, 10)), (2 * ancho // 12, 2 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                JR1_3 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(3), 1, (10, 10, 10)), (3 * ancho // 12, 2 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                JR1_4 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(4), 1, (10, 10, 10)), (4 * ancho // 12, 2 * alto // 12))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                JR3_1 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(1), 1, (10, 10, 10)), (1 * ancho // 12, 1 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                JR3_2 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(2), 1, (10, 10, 10)), (2 * ancho // 12, 1 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                JR3_3 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(3), 1, (10, 10, 10)), (3 * ancho // 12, 1 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                JR3_4 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(4), 1, (10, 10, 10)), (4 * ancho // 12, 1 * alto // 12))


            if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                JA1_1 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(1), 1, (10, 10, 10)), (ancho - 4 * ancho // 12, 2 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                JA1_2 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(2), 1, (10, 10, 10)), (ancho - 3 * ancho // 12, 2 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                JA1_3 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(3), 1, (10, 10, 10)), (ancho - 2 * ancho // 12, 2 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                JA1_4 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(4), 1, (10, 10, 10)), (ancho - 1 * ancho // 12, 2 * alto // 12))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_7:
                JA3_1 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(1), 1, (10, 10, 10)), (ancho - 4 * ancho // 12, 1 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
                JA3_2 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(2), 1, (10, 10, 10)), (ancho - 3 * ancho // 12, 1 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
                JA3_3 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(3), 1, (10, 10, 10)), (ancho - 2 * ancho // 12, 1 * alto // 12))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                JA3_4 = [pygame.time.get_ticks(), True]
                screen.blit(pygame.font.Font.render(TextoControles, str(4), 1, (10, 10, 10)), (ancho - 1 * ancho // 12, 1 * alto // 12))

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            gRojo += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            kRojo += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
            kAzul += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            gAzul += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            if gRojo > 0:
                gRojo -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            if kRojo > 0:
                kRojo -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            if kAzul > 0:
                kAzul -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            if gAzul > 0:
                gAzul -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            puntoRojo(1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            if puntajeRojo > 0:
                puntoRojo(-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            puntoAzul(1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            if puntajeAzul > 0:
                puntoAzul(-1)
        # Usare la tecla espacio para cambiar play/pausa
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if play:
                play = False
                pausa = True
            elif pausa == False:
                if numeroRound < totaRound:
                    descanso = False
                    play = True
                    pausaReloj = pygame.time.get_ticks()
                    numeroRound = numeroRound + 1
            else:
                play = True
                pausa = False
                pausaReloj = pygame.time.get_ticks() - segundos
                pygame.draw.rect(screen, [255, 0, 0], (0, 0, ancho // 2, alto - alto * 0.03))
                pygame.draw.rect(screen, [0, 0, 255], (ancho // 2, 0, ancho, alto - alto * 0.03))
                textoRojo = pygame.font.Font.render(TextoGrande, str(puntajeRojo), 1, (10, 10, 10))
                screen.blit(textoRojo, [ancho // 3 - 2 * textoRojo.get_width() // 3, alto // 7])
                textoAzul = pygame.font.Font.render(TextoGrande, str(puntajeAzul), 1, (10, 10, 10))
                screen.blit(textoAzul, (2 * ancho // 3 - textoAzul.get_width() // 3, alto // 7))
        # Boton Stop
        if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
            play = False
            pausa = False
            segundos = 0
            puntajeAzul = 0
            puntajeRojo = 0
            kRojo = 0
            kAzul = 0
            gRojo = 0
            gAzul = 0
            numeroRound = 0
            pygame.draw.rect(screen, [255, 0, 0], (0, 0, ancho // 2, alto - alto * 0.03))
            pygame.draw.rect(screen, [0, 0, 255], (ancho // 2, 0, ancho, alto - alto * 0.03))
            textoAzul = pygame.font.Font.render(TextoGrande, "0", 1, (10, 10, 10))
            anchoMarcador = textoAzul.get_width()
            screen.blit(textoAzul, (2 * ancho // 3 - anchoMarcador // 3, alto // 7))
            screen.blit(textoAzul, (ancho // 3 - 2 * anchoMarcador // 3, alto // 7))

        # Boton Sig. Round
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            pausa = False
            play = False
            descanso = False
            if numeroRound < totaRound:
                #descanso = False
                #play = True
                pausaReloj = pygame.time.get_ticks()
                #numeroRound = numeroRound + 1
            pygame.draw.rect(screen, [255, 0, 0], (0, 0, ancho // 2, alto - alto * 0.03))
            pygame.draw.rect(screen, [0, 0, 255], (ancho // 2, 0, ancho, alto - alto * 0.03))
            textoRojo = pygame.font.Font.render(TextoGrande, str(puntajeRojo), 1, (10, 10, 10))
            screen.blit(textoRojo, [ancho // 3 - 2 * textoRojo.get_width() // 3, alto // 7])
            textoAzul = pygame.font.Font.render(TextoGrande, str(puntajeAzul), 1, (10, 10, 10))
            screen.blit(textoAzul, (2 * ancho // 3 - textoAzul.get_width() // 3, alto // 7))
        if event.type == pygame.MOUSEBUTTONDOWN:
            # # print screen.get_at(event.pos)
            # Boton Play//Pausa
            if screen.get_at(event.pos) == (150, 0, 0) or screen.get_at(event.pos) == (50, 10, 10):
                if play:
                    play = False
                    pausa = True
                elif pausa == False:
                    if numeroRound < totaRound:
                        descanso = False
                        play = True
                        pausaReloj = pygame.time.get_ticks()
                        numeroRound = numeroRound + 1
                else:
                    play = True
                    pausa = False
                    pausaReloj = pygame.time.get_ticks() - segundos
                    pygame.draw.rect(screen, [255, 0, 0], (0, 0, ancho // 2, alto - alto * 0.03))
                    pygame.draw.rect(screen, [0, 0, 255], (ancho // 2, 0, ancho, alto - alto * 0.03))
                    textoRojo = pygame.font.Font.render(TextoGrande, str(puntajeRojo), 1, (10, 10, 10))
                    screen.blit(textoRojo, [ancho // 3 - 2 * textoRojo.get_width() // 3, alto // 7])
                    textoAzul = pygame.font.Font.render(TextoGrande, str(puntajeAzul), 1, (10, 10, 10))
                    screen.blit(textoAzul, (2 * ancho // 3 - textoAzul.get_width() // 3, alto // 7))
            # Boton Stop
            if screen.get_at(event.pos) == (150, 0, 1) or screen.get_at(event.pos) == (50, 10, 11):
                play = False
                pausa = False
                segundos = 0
                puntajeAzul = 0
                puntajeRojo = 0
                kRojo = 0
                kAzul = 0
                gRojo = 0
                gAzul = 0
                numeroRound = 0
                pygame.draw.rect(screen, [255, 0, 0], (0, 0, ancho // 2, alto - alto * 0.03))
                pygame.draw.rect(screen, [0, 0, 255], (ancho // 2, 0, ancho, alto - alto * 0.03))
                textoAzul = pygame.font.Font.render(TextoGrande, "0", 1, (10, 10, 10))
                anchoMarcador = textoAzul.get_width()
                screen.blit(textoAzul, (2 * ancho // 3 - anchoMarcador // 3, alto // 7))
                screen.blit(textoAzul, (ancho // 3 - 2 * anchoMarcador // 3, alto // 7))
            # Boton Configurar
            if screen.get_at(event.pos) == (231, 231, 231) or screen.get_at(event.pos) == (249, 180, 61):
                pygame.quit()
                ventana()
                puntajeAzul = 0
                puntajeRojo = 0
                kRojo = 0
                kAzul = 0
                gRojo = 0
                gAzul = 0
                numeroRound = 1
                play = False
                descanso = False
                pausa = False
                pausaReloj = 0
                segundos = 0
                pygame.init()
                screen = pygame.display.set_mode()
                pygame.display.toggle_fullscreen()
                ancho = int(pygame.Surface.get_width(screen))
                alto = int(pygame.Surface.get_height(screen))
                pantalla()
                pygame.display.flip()

            # Boton Sig. Round
            if screen.get_at(event.pos) == (225, 225, 225) or screen.get_at(event.pos) == (15, 15, 15):
                pausa = False
                play = False
                descanso = False
                if numeroRound < totaRound:
                    #descanso = False
                    #play = True
                    pausaReloj = pygame.time.get_ticks()
                    #numeroRound = numeroRound + 1
                pygame.draw.rect(screen, [255, 0, 0], (0, 0, ancho // 2, alto - alto * 0.03))
                pygame.draw.rect(screen, [0, 0, 255], (ancho // 2, 0, ancho, alto - alto * 0.03))
                textoRojo = pygame.font.Font.render(TextoGrande, str(puntajeRojo), 1, (10, 10, 10))
                screen.blit(textoRojo, [ancho // 3 - 2 * textoRojo.get_width() // 3, alto // 7])
                textoAzul = pygame.font.Font.render(TextoGrande, str(puntajeAzul), 1, (10, 10, 10))
                screen.blit(textoAzul, (2 * ancho // 3 - textoAzul.get_width() // 3, alto // 7))
    presionadosRojo()
    presionadosRojo3()
    presionadosAzul()
    presionadosAzul3()
    dibujarReloj()
    amonestaciones()
    screen.blit(logo, [((ancho // 2) - logo.get_width() // 2), 10])
    # pygame.image.save(screen, "Capture.jpg")
    # Controla los FPS
    reloj.tick(15)
