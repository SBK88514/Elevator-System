import pygame

import Elevator
from settings import *
from Floor import *


class Building(pygame.sprite.Group):
    def __init__(self, x_position):
        super().__init__()
        self.floors = []
        self.elevators = []

        self.position = (x_position, SCREEN_HEIGHT)

        self.create_floors()
        self.create_elevators()

    def create_floors(self):
        for floor_num in range(NUMBER_OF_FLOORS):
            floor = Floor(position=(self.position[0], self.position[1] - floor_num * FLOOR_HEIGHT))
            floor_id = floor_num
            self.floors.append(floor)
            self.add(floor)

    def create_elevators(self):
        for elevator_num in range(NUMBER_OF_ELEVATORS):
            elevator_position = (self.position[0] + FLOOR_WIDTH // 1.5 + elevator_num * ELEVATOR_WIDTH, self.position[1])
            elevator = Elevator.Elevator(position=elevator_position)
            elevator_id = elevator_num
            self.elevators.append(elevator)
            self.add(elevator)

    def update(self):
        for floor in self.floors:
            floor.update()

        for elevator in self.elevators:
            elevator.update()

        for floor in self.floors:
            SCREEN.blit(floor.image, floor.rect)

        for elevator in self.elevators:
            SCREEN.blit(elevator.image, elevator.rect)

        # self.floors.draw(SCREEN)
        # self.elevators.draw(SCREEN)
