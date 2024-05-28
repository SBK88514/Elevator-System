import Elevator
from settings import *
from Floor import *


class Building(pygame.sprite.Group):
    def __init__(self, x_position):
        super().__init__()
        self.floors = []
        self.elevators = []

        self.position = (x_position, SCREEN_HEIGHT)

        for floor_num in range(NUMBER_OF_FLOORS):
            floor = Floor(position=(self.position[0], self.position[1] - floor_num * FLOOR_HEIGHT),floor_number=floor_num + 1)
            self.floors.append(floor)
            self.add(floor)

        for elevator_num in range(NUMBER_OF_ELEVATORS):
            elevator_position = (
                self.position[0] + FLOOR_WIDTH // 1.5 + elevator_num * ELEVATOR_WIDTH, self.position[1])
            elevator = Elevator.Elevator(position=elevator_position)
            elevator.building = self
            self.elevators.append(elevator)
            self.add(elevator)

    def update(self):
        for floor in self.floors:
            floor.update(floor.time_remaining)
            floor.draw(SCREEN)

        for elevator in self.elevators:
            elevator.update()
            SCREEN.blit(elevator.image, elevator.rect)

    def check_faster_elevator(self, floor_clicked):
        closest_elevator = None
        min_time = float('inf')

        for elevator in self.elevators:
            time_to_floor = elevator.calculate_time_to_floor(floor_clicked)
            if time_to_floor < min_time:
                min_time = time_to_floor
                closest_elevator = elevator
        if closest_elevator:
            self.request_elevator(floor_clicked, closest_elevator)
            for floor in self.floors:
                if floor.floor_num == floor_clicked:
                    floor.time_remaining = min_time

    def request_elevator(self, floor_clicked, elevator):
        elevator.request(floor_clicked)

    def elevator_arrived(self, floor_number):
        for floor in self.floors:
            if floor.floor_num == floor_number:
                floor.time_remaining = 0