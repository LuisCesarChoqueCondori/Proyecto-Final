import pygame, sys
from Medico import Medico
from Medicamento import Medicamento
from Virus import Virus


def crear_virus():  # funcion para crear una lista de virus
    distancia = 100
    height = 100
    for x in range(6):
        virus = Virus(distancia, height, window_width, window_height)
        lista_virus.append(virus)
        distancia = distancia + height


def mov_virus():  # funcion para el movimiento de la lista de virus
    for x in lista_virus:
        x.mov_virus()


pygame.init()
window_width = 800
window_height = 600
speed = 20
contador_virus = 6
running_game = True
end_game = False

window_size = (window_width, window_height)
main_window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Project")
medico = Medico(window_width, window_height)
medicamento = Medicamento(window_width / 2, window_height - 30)
lista_virus = []
crear_virus()

# titulos y fuentes
background_image = pygame.image.load('Imagenes/fondo.jpg')
fuente = pygame.font.Font(None, 30)
fuente_contador = pygame.font.SysFont("Arial", 25)
title_game = fuente.render("         #QUEDATE EN CASA", 0, (200, 60, 80))
title_game_end = fuente.render("ERES DADO DE ALTA  ", 0, (200, 100, 130))
title_game_over = fuente.render("ENTRAS EN CUARENTENA  ", 0, (200, 100, 130))

while True:
    tiempo = pygame.time.get_ticks() / 1000
    medico.mov_medico()
    mov_virus()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if running_game:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                medico.rect.left -= medico.medical_speed
            if keys[pygame.K_RIGHT]:
                medico.rect.right += medico.medical_speed
            if keys[pygame.K_SPACE]:
                x, y = medico.rect.center
                medico.disparar_cura(x, y)

    contador = fuente_contador.render("Virus : " + str(contador_virus), 0, (120, 70, 0))
    main_window.blit(background_image, (0, 0))
    main_window.blit(title_game, (240, 7))
    main_window.blit(contador, (650, 15))
    medico.draw_medico(main_window)
    if contador_virus == 0:
        main_window.blit(title_game_end, (300, 200))
        running_game = False
    if end_game:
        main_window.blit(title_game_over, (274, 200))
        running_game = False

    if len(medico.list_curas) > 0:
        for x in medico.list_curas:
            x.draw_medicamento(main_window)
            x.mov_medicamento()
            if x.rect.top < (window_height - window_height):
                medico.list_curas.remove(x)
            else:
                for virus in lista_virus:
                    if x.rect.colliderect(virus.rect):
                        lista_virus.remove(virus)
                        medico.list_curas.remove(x)
                        contador_virus = contador_virus - 1
                        break

    if len(lista_virus) > 0:
        for virus in lista_virus:
            virus.draw_virus(main_window)
            virus.comportamiento(tiempo)
            if len(virus.list_virus) > 0:
                for x in virus.list_virus:
                    x.draw_covid(main_window)
                    x.mov_covid()
                    if x.rect.colliderect(medico.rect):
                        running_game = False
                        end_game = True
                        break
                    if x.rect.top > window_width - 20:
                        virus.list_virus.remove(x)
                    else:
                        for y in medico.list_curas:
                            if x.rect.colliderect(y.rect):
                                medico.list_curas.remove(y)
                                virus.list_virus.remove(x)

    pygame.display.update()
