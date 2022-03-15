# Lionel Lynch
# mathfun.py
# Calculate the sides of a triangle given the length or angle of a
# right triangle

import math

# Calculate the adj length given the hyp and adj angle 
def adj_len(angle, hyp):
    angle = math.degrees(angle)
    adj_len = (math.cos(angle)*hyp)
    print(f'The length of the Adjacent side is {adj_len}')

# Calcualte the opp length given the hyp and adj angle
def opp_len(angle, hyp):
    angle = math.degrees(angle)
    opp_len = (math.sin(angle)* hyp)
    print(f'The length of the Opposite side is {opp_len}')

# Calcualte the adj angle given the hyp and opp length
def adj_angle(opp, hyp):
    given =  opp/hyp
    angle = math.degrees((math.asin(given)))
    print(f"The angle given the Opposite length and Hypotenuse is:{angle}")
    
# Calcualte the adj angle given the adj and opp length 
def adj_angle_Two(adj, opp):
    given =  opp/adj
    angle = math.degrees((math.atan(given)))
    print(f"The angle given the Adjacent and Opposite length is:{angle}")
    
# User input to determine the given hyp, adj, opp, and angle
hyp = float(input("Enter Hypotenuse: "))
adj = float(input("Enter Adjacent length: "))
opp = float(input("Enter Opposite length: "))
angle = float(input("What is the adjacent angle? Give in Degrees. : "))

#main program test code
adj_len(angle, hyp)
opp_len(angle, hyp)
adj_angle(opp, hyp)
adj_angle_Two(adj, opp)