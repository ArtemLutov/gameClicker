from random import *    # достаем вообще всё из random
from pygame import *    # достаем вообще всё из pygame
from ctypes import *
from tkinter import *

import random   # импорт библиотеки рандом
import pygame   # импорт библиотеки пайгейм

def respawn_target1():  # DEFine - определить. Указываем функцию которая "телепортирует" в случайном месте наш объект
    target_rect1.x = (random.randint(0, W - target_rect1.w)) #обращаемся к прямоугольной области нашей цели в позиции Х (левую точку экрана, ширина минус ширина нашего объекта)
    target_rect1.y = (random.randint(0, H - target_rect1.h)) #так же, высота

def respawn_target2():

    target_rect2.x = (random.randint(0, W - target_rect2.w))
    target_rect2.y = (random.randint(0, H - target_rect2.h))

def respawn_target3():

    target_rect3.x = (random.randint(0, W - target_rect3.w))
    target_rect3.y = (random.randint(0, H - target_rect3.h))

def exitimage0():

    exitimage_rect0.x = (0, W / 2)
    exitimage_rect0.y = (0, H / 2)

def spawn_start0():
    start_rect0.x = (windll.user32.GetSystemMetrics(0) / 2 - exit_rect4.w)
    start_rect0.y = (windll.user32.GetSystemMetrics(1) / 2 - exit_rect4.h)

pygame.init ()  # инициализируем сам пайгейм
pygame.font.init ()     # инициализируем шрифты в функции инит для вывода очков

W = windll.user32.GetSystemMetrics(0) - 10    # ширина
H = windll.user32.GetSystemMetrics(1) - 80     # высота

SCREEN_SIZE = (W, H)    # Кортеж с хранением двух значений X и Y, а большими буквами т.к. это константа, такое правило
SCREEN_CENTER = (W // 2, H // 2)    # // это целое деление, делим ширину и высоту на 2 для определения центра, пригодится
SCREEN_TOP = (W // 2, 0)    # создаем переменную для верхней центральной части
SCREEN_TOP1 = (W // 2 - 64, 0)
SCREEN_TOP2 = (W // 2 - 128, 0)
SCREEN_TOP3 = (W // 2 - 192, 0)
screen = pygame.display.set_mode((SCREEN_SIZE), RESIZABLE)   # создаем само окно
current_size = screen.get_size()

virtual_surface = Surface((SCREEN_SIZE))

FPS = 60    # создаем частоту обновления экрана чтобы тянуло и на слабых компах
clock = pygame.time.Clock()     # создаем объект часы

ARIAL_FONT_PATH = pygame.font.match_font('arial')   # через функцию match.font мы можем найти любой шрифт любой операционки
ARIAL_64 = pygame.font.Font (ARIAL_FONT_PATH, 64)   #устанавливаем шрифт 64 размера и 36 соответственно
ARIAL_36 = pygame.font.Font (ARIAL_FONT_PATH, 36)

                        # Тут объявляются все данные для нашей игры, а потом уже логика

INIT_DELAY = 2000   # переменная, задержка времени в милисекундах
finish_delay = INIT_DELAY   # создаем переменную которая хранит "сколько нам осталось" до конца игры
DECREASE_BASE = 1.005   # Переменная отвечающая за то, насколько быстро уменьшается наше время
last_respawn_time = 2000    # Переменная запоминает когда мы кликнули по объекту последний раз ИЛИ время последнего "спавна" нашего объекта

game_over = False   # Основное игровое поле False - т.к. мы заранее не проиграли ещё

RETRY_SURFACE = ARIAL_36.render('Нажмите любую кнопку чтобы начать сначала', True, (0, 0, 0))     # Выводящийся текст после окончания игры. Surface - это поверхность
                                                                                    # у шрифтов есть функция Render позволяющий рендерить поверхности с текстом
                                                                                    # True - сглаживать текст или нет и в скобках (цвет)
RETRY_RECT = RETRY_SURFACE.get_rect()   # создаем прямоугольник - Rect область, которая хранит позицию и размер фразы выше
RETRY_RECT.midtop = (SCREEN_CENTER) # создаем позицию/поверхность, где указываем, что её позиция должна быть в центре экрана

score = 0   # создаем переменную общих нажатий объектов
score1 = 0     # очки нажатий на первый объект и т.д.
score2 = 0
score3 = 0

start_IMAGE0 = pygame.image.load(r'resources\0StartTheGame.jpg') # Стрелка для начала игры
TARGET_IMAGE1 = pygame.image.load(r'resources\1RedSquare.jpg')  # загружаем 1 картинку прописав функцию load у модуля image в pygame.
                                                        # Можно прописать точный адрес до картинки, либо можно просто написать название картинки, если она лежит в той же папке, что и наш проект
                                                        # создаем поверхность с нашей картинкой
TARGET_IMAGE2 = pygame.image.load(r'resources\2GreenSquare.jpg') # загружаем остальные
TARGET_IMAGE3 = pygame.image.load(r'venv\resources\3YellowSquare.jpg')
exit_IMAGE4 = pygame.image.load(r'resources\4exit.jpg')

start_IMAGE0 = pygame.transform.scale(start_IMAGE0, (120, 120))
TARGET_IMAGE1 = pygame.transform.scale(TARGET_IMAGE1, (120, 120))     # выставляем размеры картинки
TARGET_IMAGE2 = pygame.transform.scale(TARGET_IMAGE2, (120, 120))
TARGET_IMAGE3 = pygame.transform.scale(TARGET_IMAGE3, (120, 120))
exit_IMAGE4 = pygame.transform.scale(exit_IMAGE4, (100, 50))

start_rect0 = start_IMAGE0.get_rect()
target_rect1 = TARGET_IMAGE1.get_rect()   # создаем переменную с размером и позицией на экране и благодаря области get.rect мы узнаем кликнула ли мышь по ней
target_rect2 = TARGET_IMAGE2.get_rect()
target_rect3 = TARGET_IMAGE3.get_rect()
exitimage_rect0 = exit_IMAGE4.get_rect()



respawn_target1()     # Указывем, чтобы объект в начале появлялся в случайной точке(она определена через def и random (а потом уже идет цикл игры)
respawn_target2()
respawn_target3()

                        #создаем игровой цикл
#start_running = True
 #while start_running:
  #   for e in pygame.event.get():
   #      if e.type == pygame.QUIT:
    #         running = False
     #    elif e.type == pygame.MOUSEBUTTONDOWN:  # Если было нажатие мышью
      #       if e.button == pygame.BUTTON_LEFT:
       #          if start_rect0.collidepoint(e.pos):
        #         start_running = False


running = True  # указываем запущен ли наш цикл, в нашем случае он сразу запущен
while running:  #while работает только пока цикл True, как только он False он заканчивается
    for e in pygame.event.get():    # для этого перебираем все функции, для получения всех событий происходящих внутри
        if e.type == pygame.QUIT:   # Если ивент quit т.е. выход из игры, то мы остановим цикл
            running = False
        elif e.type == VIDEORESIZE:
            current_size = e.size


        elif e.type == pygame.KEYDOWN:  # Если нажимается любая клавиша, то игра перезапустится
            if game_over:   # Но это событие должно отслеживаться только в том случае, когда мы проиграли чтобы перезапустить игру
                score = 0   # А для перезапуска нам нужно обнулить очки
                score1 = 0
                score2 = 0
                score3 = 0
                finish_delay = INIT_DELAY   # Обнулить финиш делэй (это наша задержка для перезапуска) и устанавливаем её на начальную задержку
                game_over = False   # так же возвращаем состояние проигрыша в False т.к. изначально мы НЕ проиграли
                last_respawn_time = pygame.time.get_ticks()     # Обнулить последний клик в игровом времени, чтобы задержка началась с текущего времени

                            # Создаем ивент нажатия мышью для этого создаем блок elif ИНАЧЕЕСЛИ
        elif e.type == pygame.MOUSEBUTTONDOWN:  # Если было нажатие мышью
            if e.button == pygame.BUTTON_LEFT:  # берём левую клавишу мыши (обращение к button) если к клавиатуре то (key)
                if not game_over and target_rect1.collidepoint(e.pos):   # проверяем ДВА условия (если мы не проиграли И если мы попали по объекту)
                    score1 += 1 # прибавляем сразу и в первый и в общий очко
                    score += 1  # если выполняются два условия, то очки прибавляются
                    respawn_target1() # Так же вызывается новый респавн объекта
                    last_respawn_time = pygame.time.get_ticks() # так же наше время последнего респавна меняется
                    finish_delay = INIT_DELAY / (DECREASE_BASE ** score) # интересное условие, меняем задержку нашей игры (рассчитываем из изначальной задержки поделенной на базовое
                                                                         # уменьшение и возводим в степень очков

                if not game_over and target_rect2.collidepoint(e.pos):
                    score2 += 1
                    score += 1
                    respawn_target2()
                    last_respawn_time = pygame.time.get_ticks()
                    finish_delay = INIT_DELAY / (DECREASE_BASE ** score)

                if not game_over and target_rect3.collidepoint(e.pos):
                    score3 += 1
                    score += 1
                    respawn_target3()
                    last_respawn_time = pygame.time.get_ticks()
                    finish_delay = INIT_DELAY / (DECREASE_BASE ** score)

                if exitimage_rect0.collidepoint(e.pos):
                    running = False


                                # Переходим к блоку визуала игры

    clock.tick (FPS) # передаем обновление экрана заданное количество выше

    virtual_surface.fill ((255, 208, 202))   # Заливаем экран фон цветом светлозелёным

                                # Отрисовываем очки в процессе игры в цикле while

    score_surface = ARIAL_64.render(str(score), True, (0, 0, 0))    # рисуем поверхность с очками и передаем туда очки в нужном шрифте
    score_rect = score_surface.get_rect()   # создаем прямоугольник очков и передаем туда данные из строки выше
    score1_surface = ARIAL_64.render(str(score1), True, (255, 0, 0))
    score1_rect = score1_surface.get_rect()
    score2_surface = ARIAL_64.render(str(score2), True, (0, 255, 0))
    score2_rect = score2_surface.get_rect()
    score3_surface = ARIAL_64.render(str(score3), True, (255, 245, 0))
    score3_rect = score3_surface.get_rect()

    clock_surface = ARIAL_64.render(str(clock), True, (255, 0, 0))                                                      #ДОПИЛИТЬ ВРЕМЯ, но CLOCK занято под FPS
    clock_rect = clock_surface.get_rect()

                                # Игровая логика

    now = pygame.time.get_ticks()   # получаем текущее игровое время
    elapsed = now - last_respawn_time   # Рассчитываем время между последним временем респавна и текущим временем
    if elapsed > finish_delay:  # если времени прошло больше, чем времени для конца игры, значит мы проиграли
        game_over = True    # игра закончена
        score_rect.midbottom = (W // 2 + 128, 500)   # выводит очки по центру экрана по завершению игры
        score1_rect.midbottom = (W // 2 - 64, 500)                                                                              # минимизировать вставки по координатам. настроить подстройку под экран
        score2_rect.midbottom = (W // 2 , 500)
        score3_rect.midbottom = (W // 2 + 64, 500)
        exitimage_rect0.midtop = (SCREEN_TOP)

        virtual_surface.blit (RETRY_SURFACE, RETRY_RECT) # выводит текст проигрыша в определенном шрифте и размере
        virtual_surface.blit(exit_IMAGE4, exitimage_rect0)

    else:   # блок ИНАЧЕ, в этом случае игра продолжает цикл

                        # Для рисовки заднего фона

        h = H - H * elapsed / finish_delay  # рассчитаем высоту ( берем высоту, вычитаем высоту помноженную на прошедшее время и делим на задержку игры
        time_rect = pygame.Rect ((0, 0), (W, h))    # создаем прямоугольную область для нашей области которая уменьшается, передаем координаты и размеры
        time_rect.bottomleft = (0, H)   # указываем направление прямоугольника вниз, то есть уменьшается сверху вниз
        pygame.draw.rect(virtual_surface, (232, 255, 208), time_rect) # рисуем поверхность через функцию pygame модуль draw, функцию rect. Передаем поверхность где мы рисуем и пишем текст

#        virtual_surface.fill((0, 0, 0))



        virtual_surface.blit(TARGET_IMAGE1, target_rect1)  # указываем ЧТО мы хотим нарисовать и ГДЕ
        virtual_surface.blit(TARGET_IMAGE2, target_rect2)
        virtual_surface.blit(TARGET_IMAGE3, target_rect3)
        virtual_surface.blit(exit_IMAGE4, exitimage_rect0)
        virtual_surface.blit(start_IMAGE0, start_rect0)


        score_rect.topleft = (15, 0)  # указываем где должны рисоваться очки в игре очки ТОП либо координаты либо = SCREEN_TOP например ссылка на готовые
        score1_rect.topleft = (15, 64)
        score2_rect.topleft = (15, 128)
        score3_rect.topleft = (15, 192)
        exitimage_rect0.midtop = (SCREEN_TOP)
        start_rect0.topright = (0, H // 3)

        clock_rect.midtop = (SCREEN_TOP)

    # Выходим из блоков IF и ELSE (если и иначе) и рисуем сначала поверхность, потом окно:
    virtual_surface.blit(score_surface, score_rect)     # Что и где хотим нарисовать (Очки по центру прям)
    virtual_surface.blit(score1_surface, score1_rect)
    virtual_surface.blit(score2_surface, score2_rect)
    virtual_surface.blit(score3_surface, score3_rect)

#   virtual_surface.blit(clock_surface, clock_rect)

    scaled_surface = transform.scale(virtual_surface, current_size)
    screen.blit(scaled_surface, (0, 0))

    pygame.display.flip()   # чтобы увидеть какие-либо изменения обращаемся  pygame.display и к функции flip которая переворачивает наш дисплей
pygame.quit()   #Выходим из игры если наш цикл прекратил работу и окно закрывалось
