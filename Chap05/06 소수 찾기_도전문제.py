import math

def sphereVolume(radius):
    volume=(4.0/3.0)*math.pi*radius*radius*radius
    return volume

def compare(radius1, radius2):
    print(radius1,"의 부피:", sphereVolume(radius1))
    print(radius2,"의 부피:", sphereVolume(radius2))
    
radius1, radius2=map(float,input().split())
compare(radius1, radius2)
