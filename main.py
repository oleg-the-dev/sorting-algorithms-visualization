import pygame
from sys import exit
from display import Window
from data import Data
from settings import Settings
import pygame_gui
from context import data_ctx, algo_ctx

def main():
    data_type = 'Random'
    algo_type = 'Selection'

    data = data_ctx[data_type]()
    algorithm = algo_ctx[algo_type]

    display = Window(data)
    manager = display.manager

    sorting = False
    algo_generator = None

    clock = pygame.time.Clock()

    while True:
        clock.tick(display.FPS)

        if sorting:
            try:
                generator, red_1, red_2, blue_1, blue_2 = next(algo_generator)
                display.draw_bars(generator, red_1, red_2, blue_1, blue_2)
            except StopIteration:
                sorting = False
        else:
            display.draw_bars(data, -1, -1, -1, -1)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    data = data_ctx[data_type]()
                    sorting = False

            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == display.algo_dropdown:
                    algo_type = event.text
                if event.ui_element == display.data_dropdown:
                    data_type = event.text

            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == display.data_size:
                    Settings.SIZE = event.value
                    display.size_label.set_text(f'Data Size - {Settings.SIZE}')
                if event.ui_element == display.algo_speed:
                    Settings.FPS = event.value

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == display.generate_btn:
                    data = data_ctx[data_type]()
                if event.ui_element == display.run_btn:
                    if not sorting:
                        sorting = True
                        algo_generator = algo_ctx[algo_type](data, 0, len(data) - 1)
                    else:
                        sorting = False

            manager.process_events(event)

        pygame.draw.rect(display.screen, display.BACKGROUND_COLOR, (700, 0, 200, 600))
        manager.update(clock.tick(60)/1000)
        manager.draw_ui(display.screen)
        pygame.display.update()

if __name__ == '__main__':
    main()
