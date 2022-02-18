import pygame
import pygame_gui
from application.context import data_ctx, algo_ctx
from application.display import Window
from settings import Settings
from sys import exit


def main():
    data_type = 'Random'
    algo_type = 'Selection'

    data = data_ctx[data_type]()

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
                display.run_btn.set_text('Start')
        else:
            display.draw_bars(data, -1, -1, -1, -1)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Keyboard Controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    data = data_ctx[data_type]()
                    sorting = False
                if event.key == pygame.K_SPACE:
                    if not sorting:
                        sorting = True
                        display.run_btn.set_text('Stop')
                        algo_generator = algo_ctx[algo_type](data, 0,
                                                             len(data) - 1)
                    else:
                        sorting = False
                        display.run_btn.set_text('Start')

            # GUI Events
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
                        display.run_btn.set_text('Stop')
                        algo_generator = algo_ctx[algo_type](data, 0,
                                                             len(data) - 1)
                    else:
                        sorting = False
                        display.run_btn.set_text('Start')

            manager.process_events(event)

        pygame.draw.rect(display.screen, display.BACKGROUND_COLOR,
                         (700, 0, 200, 600))
        manager.update(clock.tick(60) / 1000)
        manager.draw_ui(display.screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
