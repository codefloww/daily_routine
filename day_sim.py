import random
from mystates import States
import time

# place: home, university, street
class Simulation:
    def __init__(self) -> None:
        # self.start = States().initial_state
        # self.sleep = States().sleep_state
        # self.eat = States().eat_state
        # self.work = States().work_state
        # self.route = States().route_state
        # self.rest = States().rest_state

        self.energy = 40
        self.place = "home"
        self.stopped = False
        self.hour = 0
        self.events = [
            Events().air_alert,
            Events().forgot_deadline,
            Events().broken_bus,
        ]
        self.routine = RoutineQueue([States().initial_state])

    def run(self) -> None:
        # Event loop
        count = 0
        while not self.stopped and count < 100:
            self.run_hour()
            self.decide_event()
            self.print_status()
            if self.energy < 0:
                self.stopped = True
                print("I died(((")
            if self.hour == 24:
                self.hour = 0
                print("New Day!")
            count += 1
            time.sleep(1)

    def run_hour(self):
        state = self.routine.get_next_routine()
        self.energy, self.place, self.routine = state(
            self.hour, self.energy, self.place, self.routine
        )
        self.hour += 1
        self.energy -= 2  # hourly functioning of organism

    def decide_event(self):
        event = random.choice(self.events)
        self.energy, self.place, self.routine = event(
            self.hour, self.energy, self.place, self.routine
        )
        
    def print_status(self):
        print(
            "status: hour: {}, energy: {}, place: {}, routine: {}".format(
                self.hour, self.energy, self.place, self.routine
            )
        )


class Events:
    def air_alert(self, hour, energy, place, routine):
        if random.random() < 0.5:
            energy -= 3
            print("Air alert!")
            current_state = routine.see_current_routine().__name__.split("_")[0]
            if current_state == "sleep" or current_state == "work":
                routine.remove_routine()
                routine.add_routine(States().rest_state)
        return energy, place, routine

    def forgot_deadline(self, hour, energy, place, routine):
        current_state = routine.see_current_routine().__name__.split("_")[0]
        if random.random() < 0.4 and current_state != "sleep":
            print("F***, I forgot about deadline!")
            energy -= 5
            routine.remove_routine()
            routine.add_routine(States().work_state)
        return energy, place, routine

    def broken_bus(self, hour, energy, place, routine):
        current_state = routine.see_current_routine().__name__.split("_")[0]
        if current_state == "route":
            energy -= 5
            print("Bus is broken!")
        return energy, place, routine

class RoutineQueue:
    def __init__(self, routine=None) -> None:
        self.routine = routine or []

    def add_routine(self, routine):
        self.routine.append(routine)

    def get_next_routine(self):
        if self.routine:
            self.current_routine = self.routine.pop(0)
            return self.current_routine

    def see_current_routine(self):
        if self.routine:
            return self.routine[0]

    def remove_routine(self):
        if self.routine:
            self.routine.pop(0)

    def __str__(self) -> str:
        return str(self.routine[0].__name__.split("_")[0])


if __name__ == "__main__":
    sim = Simulation()
    sim.run()
