import math

# User inputs Given Variables

NP = float(input("What is the number of teeth for the pinion? "))
NG = float(input("What is the number of teeth for the gear? "))
PHI = float(input("What is the pressure angle? "))
np = float(input("What speed does the pinion rotate at in rev/min? "))
H = float(input("What is the value of power in hp? "))
P = float(input("What is the diametral pitch in teeth/in? "))
F = float(input("What is the face width in inches? "))
Qv = float(input("What is the quality standard? "))
HBp = float(input("What is the hardness of the pinion? "))
HBg = float(input("What is the hardness of the gear? "))
N = float(input("What is the value of pinion life in cycles "))
R = float(input("What is the value of reliability? "))

# Calculate the AGMA Bending Stress for Pinion

# Calculate Pinion Diameter

dp = (NP / P)
print(f'The value of pinion diameter is: {dp}')

# Calculate Velocity Pitchline 

V = ( math.pi * dp * np) / 12
print(f'The value of velocity pitchline is: {V}')

# Calculate Transmitted Load

Wt = (33000 * ( H / V))
print(f'The value of transmitted load is: {Wt}')

# The overload factor according to table

Ko = 1
print(f'The value of overload factor is: {Ko}')

# Calculate the dynamic factor

B = (0.25*(12 - Qv)** (2/3))

A = (50 + 56*(1-B))

Kv = ((A + math.sqrt(V)) / (A))** (B)
print(f'The value of dynamic factor is: {Kv}')

# Calculate the size factor

Y = 0.245 # According to table 14-2

Ks = (1.192*((F* math.sqrt (Y)) / P)** 0.0535)
print(f'The value of size factor: {Ks}')

# Calculate Load Distribution Factor

Cmc = 1 # Uncrowned teeth value

Cpf = ((F / (10 * dp)) - 0.0375 + (0.01258 * F))

Ce = 1

Cma = 0.17 # From Figure 14-11

Cpm = 1 

Km = 1 + Cmc*((Cpf * Cpm) + (Cma * Ce))
print(f'The value of the load distribution factor is: {Km}')

# The Rim thickness factor

Kb = 1 # Assuming constant thickness in gears
print(f'The value of rim thickness factor is: {Kb}')

# Spur gear bending geometry factor

J = 0.21 # From Figure 14-6
print(f'The value of spur gear bending geometry factor: {J}')

# Calculate AGMA Bending Stress

sigma = (Wt * Ko * Kv * Ks * (P / F) * (Km * Kb)/J)
print(f'The value of AGMA bending stress is: {sigma}')

# Calculate the Factor of Safety Due to Bending

St = 77.3 * (HBp) + 12800
print(f'The value of gear bending strength is: {St}')

YN = 1.3558 * (N)** -0.0178
print(f'The value of stress cycle factor for bending stress is: {YN}')

Kt = 1
print(f'The value of temperature factor is: {Kt}')

Kr = 1.25 # From Table 14-10
print(f'The value of reliability factor is: {Kr}')

SF = ((St * YN)/(Kt * Kr)) / sigma
print(f'The value of the factor of safety due to bending is: {SF}')

# Calculate AGMA Contact Stress (Wear) for pinion

Cp = 2300 # From Table 14-8
print(f'The value of elastic coefficient is: {Cp}')

Cf = 1 
print(f'The value of surface condition factor is: {Cf}')

MN = 1 # For Spur Gears

MG = (NG / NP)

# Convert PHI from degrees to Radians
PHIr = math.radians (PHI)

I = ((math.cos(PHIr))* (math.sin(PHIr)) / (2*MN)) * (MG / (MG + 1))
print(f'The value of geometry factor of pitting resistance is: {I}')

sigmaC = Cp * math.sqrt(Wt * Ko * Kv * Ks * (Km / (dp * F)) * (Cf / I ))
print(f'The value of AGMA contact stress is: {sigmaC}')

# Calculate Factor Of Safety due to wear (Contact)

Sc = 322 * (HBp) + 29100
print(f'The value of gear contact strength is: {Sc}')

ZN = 1.4488 * (N)** -0.023
print(f'The value of stress cycle factor is: {ZN}')

CH = 1
print(f'The value of hardness ratio factor is: {CH}')

SH = ((Sc * ZN * CH) / (Kt * Kr)) / (sigmaC)
print(f'The value of AGMA factor of safety due to wear (contact) is: {SH}')

if SF > SH**2:
    print('The critical failure mode for the pinion is from wear(contact)')
else:
    print('The critical failure mode for the pinion is from bending stress')
    