import numpy as np


def div(a, b):
    if b == 0:
        return np.nan
    else:
        arr_a = np.array(a)
        arr_b = np.array(b)
        return arr_a / arr_b
    
    
def gen_array():
    vals = list(range(1, 101))
    val_list = []
    for el in vals:
        if el % 3 == 0:
            val_list.append(0)
        else:
            val_list.append(el)
    arr = np.array(val_list)
    fin_arr = arr.reshape((10, 10))
    return fin_arr


def dot(arr1, arr2):
    try:
        arr1.reshape((3, 3))
        arr2.reshape((3, 3))
        return np.dot(arr1, arr2)
    except Exception:
        raise ValueError()
        
        
def mult3d(a, b):
    return np.einsum("ijk,ij->ijk", a, b)


class ABM:
    def __init__(self):
        self.timestep = 0

    def step(self):
        self.timestep += 1

    def status(self):
        return 'step'


def step_model(model, steps):
    statuses = []
    for _ in range(steps):
        statuses.append(model.status())
        model.step()
    return statuses


class ABMWithStep(ABM):
    def status(self):
        return f'step {self.timestep}'
    
    
class Tracker:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    def get_position(self):
        return (self.lon, self.lat)
    

class FlightTracker(Tracker):
    def __init__(self, lon, lat, height):
        self.lon = lon
        self.lat = lat
        self.height = height

    def get_height(self):
        return self.height
    
    
class Polygon:
    def __init__(self, *sides):
        self.sides = sides

    def compute_perimeter(self):
        return sum(self.sides)
    
class Rectangle(Polygon):
    def __init__(self, length=0, width=0):
        super().__init__()
        self.sides = length * 2, width * 2


class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__()
        self.sides = side * 2, side * 2
        
        
def zero_crossings(readings):
    arr = np.array(readings)
    return (np.diff(np.sign(arr)) != 0).sum()


def outer_sum(x, y):
    arr_x = np.array(x)
    arr_y = np.array(y)
    return list(arr_y + arr_x[:, None])

