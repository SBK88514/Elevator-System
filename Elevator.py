from settings import *
import time


class Elevator(pygame.sprite.Sprite):
    def __init__(self, position, building):
        super().__init__()
        self.image = ELEVATOR_SCALE
        self.rect = self.image.get_rect(midbottom=position)
        self.current_floor = 0
        self.target_floor = []
        self.speed = SPEED
        self.building = building
        self.arrival_time = None
        self.waiting = False

    def request(self, floor_clicked):
        self.target_floor.append(floor_clicked)

    def update(self):
        if len(self.target_floor) > 0:
            target_y = SCREEN_HEIGHT - (self.target_floor[0] * FLOOR_HEIGHT)
            if self.rect.y > target_y:
                self.rect.y -= self.speed
            elif self.rect.y < target_y:
                self.rect.y += self.speed
            else:
                self.current_floor = self.target_floor[0]
                self.target_floor = self.target_floor[1:]
                self.building.elevator_arrived(self.current_floor)
                self.arrival_time = time.time()
                self.waiting = True

        if self.waiting:
            if time.time() - self.arrival_time >= 1:
                self.waiting = False
                self.arrival_time = None

    def calculate_time_to_floor(self, floor_number):
        if len(self.target_floor) == 0:
            target_y = SCREEN_HEIGHT - (floor_number * FLOOR_HEIGHT)
            distance = abs(self.rect.y - target_y)
            return distance / self.speed
        else:
            target_y = SCREEN_HEIGHT - (floor_number * FLOOR_HEIGHT)
            distance = abs(self.target_floor[-1] - target_y)
            return distance / self.speed
