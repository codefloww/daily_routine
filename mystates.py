# states need to change energy, place, routine
class States:
    def initial_state(self, hour, energy, place, routine):
        if hour <= 6 or hour >=23:
            routine.add_routine(self.sleep_state)
            return 35, "home", routine
        else:
            routine.add_routine(self.work_state)
            return energy, "home", routine
        

    def sleep_state(self, hour, energy, place, routine):
        energy += 12 if place == "home" else 7
        if (hour > 8 and hour < 24) or energy > 130:
            routine.add_routine(self.eat_state)
            return energy, place, routine
        else:
            routine.add_routine(self.sleep_state)
            return energy, place, routine

    def eat_state(self, hour, energy, place, routine):
        energy += 10
        if place == "home":
            if 8<hour<11: 
                routine.add_routine(self.route_state)
                return energy, 'street', routine
            elif 12<hour<20:
                routine.add_routine(self.work_state)
                return energy, place, routine
            elif 19<hour<24:
                routine.add_routine(self.rest_state)
                return energy, place, routine
            else:
                routine.add_routine(self.sleep_state)
                return energy, place, routine
        elif place == "university":
            if 8<hour<20:
                routine.add_routine(self.work_state)
                return energy, place, routine
            elif 19<hour<24:
                routine.add_routine(self.route_state)
                return energy, 'street', routine
        else:
            if 14<hour<18: 
                routine.add_routine(self.rest_state)
                return energy, place, routine
            else:
                routine.add_routine(self.route_state)
                return energy, 'street', routine

    def work_state(self, hour, energy, place, routine):
        if place == "home":
            energy -= 5
            if (10<hour<13 or 15<hour<22) and energy > 30:
                routine.add_routine(self.work_state)
                return energy, place, routine
            elif (22<hour<24) and energy > 30:
                routine.add_routine(self.rest_state)
                return energy, place, routine
            elif energy <=30 and (23<hour or hour<9):
                routine.add_routine(self.sleep_state)
            else:
                routine.add_routine(self.eat_state)
            return energy, place, routine
        elif place == "university":
            energy -= 7
            if  19<hour<24:
                routine.add_routine(self.route_state)
                return energy, 'street', routine
            elif 14<hour<16 and energy < 30:
                routine.add_routine(self.eat_state)
                return energy, place, routine
            elif 16<hour<19 and energy < 40:
                routine.add_routine(self.rest_state)
                return energy, place, routine
            else:
                routine.add_routine(self.work_state)
                return energy, place, routine
        else:
            energy -= 7
            routine.add_routine(self.route_state)
            return energy, 'street', routine
    def route_state(self, hour, energy, place, routine):
        if (16<hour or hour <10):
            routine.add_routine(self.rest_state)
            return energy, 'home', routine
        else:
            routine.add_routine(self.work_state)
            return energy, 'university', routine
    def rest_state(self, hour, energy, place, routine):
        energy +=5
        if place == "home":
            if energy < 30 and 22<hour or hour<10:
                routine.add_routine(self.sleep_state)
                return energy, place, routine
            elif energy < 30 and 14<hour<16:
                routine.add_routine(self.eat_state)
                return energy, place, routine
            elif energy< 30 and 18<hour<21:
                routine.add_routine(self.rest_state)
                return energy, place, routine
            else:
                routine.add_routine(self.work_state)
                return energy, place, routine
        elif place == "university":
            if energy < 30 and 20<hour<24:
                routine.add_routine(self.route_state)
                return energy, 'street', routine
            elif energy < 30 and 14<hour<16:
                routine.add_routine(self.eat_state)
                return energy, place, routine
            elif energy< 30 and 16<hour<18:
                routine.add_routine(self.rest_state)
                return energy, place, routine
            elif energy > 30 and (23>hour or hour>9):
                routine.add_routine(self.work_state)
                return energy, place, routine
            else:
                routine.add_routine(self.sleep_state)
                return energy, place, routine
    # states = {
    #     "initial": initial_state,
    #     "sleep": sleep_state,
    #     "eat": eat_state,
    #     "work": work_state,
    #     "route": route_state,
    #     "rest": rest_state,
    # }
