#m20 --mpa=20 psi = mpa*145.035



def mpa_psi(mpa):
    return  145.035*mpa 


def psi_mpa(psi):
    return psi/145.035 


mpa = 30
psi = 4350 

#30 Mpa 
a = mpa_psi(mpa)
b = psi_mpa(psi)

print(a)
print(b)