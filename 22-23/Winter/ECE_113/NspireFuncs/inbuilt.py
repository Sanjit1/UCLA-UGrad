import math
import random

def fabs(x):
    return abs(x)

def sqrt(x):
    return x**0.5

def exp(x):
    return math.e**x

def pow(x, y):
    return x**y

def log(x, base):
    return math.log(x, base)

def fmod(x, y):
    return x % y

def ceil(x):
    return math.ceil(x)

def floor(x):
    return math.floor(x)

def trunc(x):
    return math.trunc(x)

# define constants
pi = math.pi
e = math.e

def radians(x):
    return x * pi / 180

def degrees(x):
    return x * 180 / pi

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def asin(x):
    return math.asin(x)

def acos(x):
    return math.acos(x)

def atan(x):
    return math.atan(x)

def atan2(y, x):
    return math.atan2(y, x)

def random():
    return random.random()

def uniform(a, b):
    return random.uniform(a, b)

def randint(a, b):
    return random.randint(a, b)

def choice(seq):
    return random.choice(seq)

def randrange(start, stop=None, step=1):
    return random.randrange(start, stop, step)

def seed(x=None):
    random.seed(x)

