import pygame
import pygame_gui
from settings import Settings
from context import data_ctx, algo_ctx


class Window(Settings):
    def __init__(self, data):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Sorting Algorithms Visualiser')
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)
        self.manager = pygame_gui.UIManager((self.WIDTH, self.HEIGHT))
        self.screen.fill(self.BACKGROUND_COLOR)

        # Algorithms
        self.algo_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(750, 50, 125, 25),
                                                      text='Algorithm', manager=self.manager)
        self.algo_dropdown = pygame_gui.elements.UIDropDownMenu(
            relative_rect=pygame.Rect(750, 75, 125, 30), options_list=[option for option in
                                                                       algo_ctx.keys()],
            manager=self.manager, starting_option='Selection')
        self.run_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(735, 500, 150, 30),
                                                    text='Start/Stop', manager=self.manager)

        # Data
        self.data_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(750, 125, 125, 25),
                                                      text='Data', manager=self.manager)
        self.data_dropdown = pygame_gui.elements.UIDropDownMenu(
            relative_rect=pygame.Rect(750, 150, 125, 30), options_list=[option for option in
                                                                        data_ctx.keys()],
            manager=self.manager, starting_option='Random')
        self.generate_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(735, 450, 150, 30), text='Generate Data',
            manager=self.manager)

        # Data Size
        self.size_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(745, 250, 135, 25),
                                                      text=f'Data Size - {Settings.SIZE}',
                                                      manager=self.manager)
        self.data_size = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(735, 275, 150, 25), start_value=self.SIZE, value_range=(
                self.MIN_SIZE, self.MAX_SIZE), manager=self.manager)

        # Algo Speed
        self.speed_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(750, 325, 125, 25),
                                                       text='Algorithm Speed', manager=self.manager)
        self.algo_speed = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(735, 350, 150, 25), start_value=60, value_range=(
                self.MIN_FPS, self.MAX_FPS), manager=self.manager)



    def draw_bars(self, data, redBar1, redBar2, blueBar1, blueBar2, greenRows={}, **kwargs):
        bar_width = (self.WIDTH - 200) / len(data)
        pygame.draw.rect(self.screen, self.BACKGROUND_COLOR, (0, 0, 700, 600))
        for num in range(len(data)):
            if num in (redBar1, redBar2):
                color = self.RED
            elif num in (blueBar1, blueBar2):
                color = self.BLUE
            elif num in greenRows:
                color = self.GREEN
            else:
                color = self.GRADIENTS[num % 3]
            pygame.draw.rect(self.screen, color,
                             (num * bar_width , self.HEIGHT - data[num], bar_width, data[num]))