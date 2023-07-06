'''
Clone do Jogo Tetris em Python
Utilizando a biblioteca: PyGame
-------
Criado por: Carlos Alberto Morais Moura Filho
Versão: 1.0
Atualizado em: 17/03/2022
'''
# pylint: disable=no-member
# pylint: disable=too-many-locals
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
# pylint: disable=c-extension-no-member
# pylint: disable=no-name-in-module



# Bibliotecas
import os, sys, pygame
from Constants.config import *
from Constants.texts import *
from Classes.colors import Colors
from Classes.game import Game

def close_game():
    '''Função que encerra todas os módulos e bibliotecas utilizados e fecha a janela do jogo'''
    pygame.display.quit()
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()

def main():
    '''Função principal que trata de toda a execução do jogo'''
    # Centraliza a janela do jogo no monitor
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    # Inicia o módulo PyGame
    pygame.init()
    # Inicia o mixer de áudio
    pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
    # Criação da janela
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Seta o ícone e o título do jogo na janela
    pygame.display.set_icon(pygame.image.load(os.path.join(os.getcwd(), 'Assets/images/icon.png')).convert_alpha())
    pygame.display.set_caption(TITLE)
    # 
    clock = pygame.time.Clock()
    #
    leftPressed = False
    rightPressed = False
    downPressed = False
    game = Game()
    # 
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 350)
    # 
    while True:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()
            if event.type == pygame.KEYDOWN:
                if game.game_over == True:
                    game.game_over = False
                    game.reset()
                if event.key == pygame.K_ESCAPE:
                    close_game()
                if event.key in (pygame.K_UP, pygame.K_w, pygame.K_SPACE) and game.game_over == False:
                    game.rotate()
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    leftPressed = True
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    downPressed = True
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    rightPressed = True
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    leftPressed = False
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    downPressed = False
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    rightPressed = False
            if leftPressed and game.game_over == False:
                game.move_left()
            if rightPressed and game.game_over == False:
                game.move_right()
            if downPressed and game.game_over == False:
                game.move_down()
        # Atualiza as posições das peças no jogo
        # Desenha os objectos na tela
        screen.fill(Colors.dark_blue)
        game.draw(screen)
        pygame.display.update()
        # 
        clock.tick(FPS)

try:
    if __name__ == "__main__":
         main()
except SyntaxError as syntax_exception:
    print(f'Oops! Ocorreu um erro de sintaxe no código.\n\
        __class__ = {syntax_exception.__class__}\n\
        __doc__ = {syntax_exception.__doc__}\n\
        args = {syntax_exception.args}')
except (ValueError, ZeroDivisionError) as value_exception:
    print(f'Oops! Ocorreu um erro de valores.\n\
        __class__ = {value_exception.__class__}\n\
        __doc__ = {value_exception.__doc__}\n\
        args = {value_exception.args}')
except TypeError as type_exception:
    print(f'Oops! Ocorreu um erro de conversão de tipo de dados.\n\
        __class__ = {type_exception.__class__}\n\
        __doc__ = {type_exception.__doc__}\n\
        args = {type_exception.args}')
except Exception as general_exception:
    print(f'Oops! Ocorreu um erro não identificado.\n\
        __class__ = {general_exception.__class__}\n\
        __doc__ = {general_exception.__doc__}\n\
        args = {general_exception.args}')
finally:
    close_game()
