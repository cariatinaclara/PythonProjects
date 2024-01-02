import math

# Asking user for variable inputs

sd =float(input("What is the shaft diameter? "))
sl = float(input("What is the shaft length? "))  
dr = float(input("What is the disc radius? "))  
sy = float(input("What is the yield strength? "))
sut = float(input("What is the ultimate tensile strength? "))
se = float(input("What is the endurance limit? "))
Fmax = float(input("What is the maximum force? "))
Fmin = float(input("What is the minimum force? "))



# To calculate alternating and mean stresses

Fm = (Fmax + Fmin) / 2
print(f'The Fm value is: {Fm}')
Fa = (Fmax - Fmin) / 2
print(f'The Fa value is: {Fa}')

# Calculate values for alternating and mean stresses

sigmaM = (32*Fm*sl) / (math.pi * sd**3)
print(f'The sigmaM value is: {sigmaM}')
sigmaA = (32*Fa*sl) / (math.pi * sd**3)
print(f'The sigmaA value is: {sigmaA}')

# Calculate Fatigue Factor of Safety With Goodman Criteria

nf = ((sigmaA / se) + (sigmaM / sut))** -1
print(f'The nf value is: {nf}')

# Calculate Langer Factor of Safety

ny = sy / (sigmaA + sigmaM)
print(f'The ny value is: {ny}')

# Calculate Fatigue Factor of Safety With Gerber's Criteria

n = 0.5 * (( sut / sigmaM)** 2) * ( sigmaA / se ) * (-1 + (math.sqrt (1 + ((2* sigmaM * se) / (sut * sigmaA))** 2)))
print(f'The n value is: {n}') 

# Calculate the Maximum Tensile Constant Axial Load

sa = sigmaA

sm = sy * ( 1- (sa / sut))
print(f'The sm value is: {sm}')