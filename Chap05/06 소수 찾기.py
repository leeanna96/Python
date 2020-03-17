import math

def sphereVolume(radius):
    volume=(4.0/3.0)*math.pi*radius*radius*radius
    return volume

radius=float(input())
print(sphereVolume(radius))
