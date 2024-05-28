from Building import Building
from settings import *


class Manager(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.clock = pygame.time.Clock()
        self.buildings = []
        self.create_buildings()

    def launch_screen(self):
        pygame.init()
        self.clock.tick(FPS)

    def check_click_building(self, mouse_pos):
        for building in self.buildings:
            for floor in building.floors:
                floor_clicked = floor.handle_click(mouse_pos)
                if floor_clicked is not None:
                    building.check_faster_elevator(floor_clicked)

    def create_buildings(self):
        for building_num in range(NUMBER_OF_BUILDING):
            x_position = FLOOR_WIDTH // 2 + building_num * (FLOOR_WIDTH + BUILDING_SPACING)
            building = Building(x_position=x_position)
            self.buildings.append(building)
            self.add(building)

    def update(self):
        for building in self.buildings:
            building.update()
