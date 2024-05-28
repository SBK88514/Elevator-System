from settings import *
import time

class Elevator(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = ELEVATOR_SCALE
        self.rect = self.image.get_rect(midbottom=position)
        self.current_floor = 0
        self.target_floor = None
        self.speed = 1
        self.building = None
        self.arrival_time = None

    def request(self, floor_clicked):
        self.target_floor = floor_clicked

    def update(self):
        if self.target_floor is not None:
            target_y = SCREEN_HEIGHT - (self.target_floor * FLOOR_HEIGHT)
            if self.rect.y > target_y:
                self.rect.y -= 3
            elif self.rect.y < target_y:
                self.rect.y += 3
            else:
                self.current_floor = self.target_floor
                self.target_floor = None
            if self.building:
                self.building.elevator_arrived(self.current_floor)

    def calculate_time_to_floor(self, floor_number):
        if self.target_floor is None:
            return 0
        target_y = SCREEN_HEIGHT - (floor_number * FLOOR_HEIGHT)
        distance = abs(self.rect.y - target_y)
        return distance / self.speed
