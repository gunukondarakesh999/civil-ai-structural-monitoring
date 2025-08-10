#caluclating beam bending stress 
#formula ----> [E/R][M/I][F(stress)/Y]



def bending_stress(M,y,I):
    return (M * y) / I 

M = 50000 #Nm
y = 0.05 #m
I = 1.2e-5 
stress = bending_stress(M,y,I)

print(f"Bending Stress: {stress: .2f} Mpa")