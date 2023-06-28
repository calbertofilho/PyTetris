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
import pygame, sys, os
import constants
from Classes.grid import Grid
from Classes.colors import Colors



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
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    # Seta o título do jogo na janela
    pygame.display.set_caption(constants.TITLE)
    # 
    clock = pygame.time.Clock()
    # 
    game_grid = Grid()
    game_grid.print_grid()
    # 
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 200)
    # 
    while True:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
        # Atuliza as posições das peças no jogo
        # Desenha os objectos na tela
        screen.fill(Colors.dark_blue)
        game_grid.draw(screen)
        pygame.display.update()
        # 
        clock.tick(constants.FPS)

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
