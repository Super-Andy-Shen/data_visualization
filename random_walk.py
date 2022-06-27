from random import choice

class Randomwalk:
    def __init__(self,num_points=5000):
        self.num_points = num_points

        self.x_val = [0]
        self.y_val = [0]
        self.steps = 0
    def fill_walk(self):
        while len(self.x_val) < self.num_points:

            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance


            if x_step == 0 and y_step == 0:
                continue
            
            x = self.x_val[-1] + x_step
            y = self.y_val[-1] + y_step
            self.x_val.append(x)
            self.y_val.append(y)
            

        

    
