import time


class MicrowaveOven:
    door_open = False
    food = False
    clock_time = None
    start_time = None
    curr_time = None

    def __init__(self):
        pass

    def open_door(self):
        self.door_open = True

    def close_door(self):
        self.door_open = False

    def is_door_open(self):
        return self.door_open

    def insert_food(self):
        if self.door_open and not self.has_food():
            self.food = True
            return True
        return False

    def remove_food(self):
        if self.door_open and self.has_food():
            self.food = False
            return True
        return False

    def has_food(self):
        return self.food

    def cook_food(self, t):
        self.clock_time = t
        self.start_time = time.time()
        return

    def how_long_has_current_food_cooked(self):
        self.curr_time = time.time()
        if not self.food:
            return -1
        else:
            return int(self.curr_time - self.start_time)
# pass_all_tests("asdfasdf")

m = MicrowaveOven()
m.open_door()
m.insert_food()
m.cook_food(50)
time.sleep(100)
how_long = m.how_long_has_current_food_cooked()
print(how_long)